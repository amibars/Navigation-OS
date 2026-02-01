import base64
import json
import re
import subprocess
import time
import os
import urllib.error
import urllib.request
import html as html_lib
from datetime import datetime, timezone
from pathlib import Path

USER = 'amibars'
README_PATH = Path('README.md')
DETAILS_HEADER = '## 📖 Detailed Descriptions'
HTTP_TIMEOUT = 8
FORCE_NO_API = os.getenv('SYNC_FORCE_NO_API', '1') == '1'
API_AVAILABLE = not FORCE_NO_API


def safe_gh_api(path: str, retries: int = 2):
    global API_AVAILABLE
    if not API_AVAILABLE:
        return None
    for attempt in range(retries + 1):
        try:
            out = subprocess.check_output(
                ['gh', 'api', path],
                text=True, encoding='utf-8', errors='replace',
                timeout=8
            )
            return json.loads(out)
        except subprocess.CalledProcessError:
            if attempt >= retries:
                return None
            time.sleep(1 + attempt)
        except subprocess.TimeoutExpired:
            if attempt >= retries:
                API_AVAILABLE = False
                return None
            time.sleep(1 + attempt)
        except Exception:
            if attempt >= retries:
                API_AVAILABLE = False
                return None
            time.sleep(1 + attempt)
    return None


def fetch_paged(base_path: str, per_page: int = 100):
    page = 1
    results = []
    while True:
        path = f"{base_path}{'&' if '?' in base_path else '?'}per_page={per_page}&page={page}"
        data = safe_gh_api(path)
        if not data:
            break
        results.extend(data)
        page += 1
    return results


def http_get(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception:
        return ''


def fetch_repo_description_html(full_name: str) -> str:
    url = f'https://github.com/{full_name}'
    html = http_get(url)
    if not html:
        return ''
    m = re.search(r'<meta property="og:description" content="([^"]+)"', html)
    if not m:
        m = re.search(r'<meta name="description" content="([^"]+)"', html)
    if not m:
        return ''
    desc = html_lib.unescape(m.group(1)).strip()
    if desc.lower().startswith('github - '):
        desc = desc[9:].strip()
    desc = re.sub(r'\s+-\s+github$', '', desc, flags=re.I)
    desc = re.sub(r'\s+·\s+github$', '', desc, flags=re.I)
    return desc.strip()


def parse_repos_from_html(html: str):
    repos = []
    if not html:
        return repos
    for m in re.finditer(r'href="(/[^/"]+/[^/"]+)"[^>]*itemprop="name codeRepository"', html):
        repos.append(m.group(1).strip('/'))
    if repos:
        return list(dict.fromkeys(repos))
    for m in re.finditer(r'href="(/[^/"]+/[^/"]+)"[^>]*data-hovercard-type="repository"', html):
        repos.append(m.group(1).strip('/'))
    return list(dict.fromkeys(repos))


def fetch_repo_list_html(url: str, max_pages: int = 50):
    repos = []
    seen_urls = set()
    next_url = url
    pages = 0
    while next_url and next_url not in seen_urls and pages < max_pages:
        seen_urls.add(next_url)
        html = http_get(next_url)
        repos.extend(parse_repos_from_html(html))
        m_next = re.search(r'rel="next"[^>]*href="([^"]+)"', html)
        if m_next:
            href = m_next.group(1)
            next_url = 'https://github.com' + href if href.startswith('/') else href
        else:
            next_url = None
        pages += 1
    return list(dict.fromkeys(repos))


def fetch_starred_html(user: str):
    return fetch_repo_list_html(f"https://github.com/{user}?tab=stars")


def fetch_public_html(user: str):
    return fetch_repo_list_html(f"https://github.com/{user}?tab=repositories")


def stub_repo(full: str):
    full = full.strip('/').lower()
    if '/' not in full:
        return None
    owner, name = full.split('/', 1)
    return {
        'full_name': f'{owner}/{name}',
        'name': name,
        'owner': {'login': owner},
        'html_url': f'https://github.com/{owner}/{name}',
        '_stub': True,
    }


def normalize_repo_list(items):
    out = []
    for it in items or []:
        if isinstance(it, str):
            stub = stub_repo(it)
            if stub:
                out.append(stub)
        elif isinstance(it, dict):
            out.append(it)
    return out


print('Fetching GitHub stars/public...')
stars = fetch_paged(f"/users/{USER}/starred")
public_repos = fetch_paged(f"/users/{USER}/repos?type=public")
if not stars:
    stars = fetch_starred_html(USER)
if not public_repos:
    public_repos = fetch_public_html(USER)
stars = normalize_repo_list(stars)
public_repos = normalize_repo_list(public_repos)

star_full = {r['full_name'].lower(): r for r in stars}
public_full = {r['full_name'].lower(): r for r in public_repos}
union_full = {**public_full, **star_full}

repo_cache = {}
readme_cache = {}


def get_repo(full_name: str):
    key = full_name.lower()
    if key in repo_cache:
        return repo_cache[key]
    data = safe_gh_api(f"/repos/{full_name}")
    if data is None:
        # fallback to existing data from stars/public
        data = union_full.get(key)
    repo_cache[key] = data
    return data


branch_cache = {}


def get_default_branch(full_name: str):
    if full_name in branch_cache:
        return branch_cache[full_name]
    branch = None
    try:
        out = subprocess.check_output(
            ['git', 'ls-remote', '--symref', f'https://github.com/{full_name}.git', 'HEAD'],
            text=True, encoding='utf-8', errors='replace',
            timeout=12
        )
        m = re.search(r'ref:\s+refs/heads/([^\s]+)\s+HEAD', out)
        if m:
            branch = m.group(1)
    except Exception:
        branch = None
    if not branch:
        branch = 'main'
    branch_cache[full_name] = branch
    return branch


def fetch_raw_readme(full_name: str):
    branches = ['main', 'master']
    filenames = ['README.md', 'Readme.md', 'README.MD', 'README']
    for br in branches:
        for fname in filenames:
            url = f'https://raw.githubusercontent.com/{full_name}/{br}/{fname}'
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                    return resp.read().decode('utf-8', errors='replace')
            except urllib.error.HTTPError:
                continue
            except Exception:
                continue
    return ''


def get_readme(full_name: str):
    key = full_name.lower()
    if key in readme_cache:
        return readme_cache[key]
    data = safe_gh_api(f"/repos/{full_name}/readme")
    content = ''
    if data and isinstance(data, dict):
        try:
            content = base64.b64decode(data.get('content', '')).decode('utf-8', errors='replace')
        except Exception:
            content = ''
    if not content:
        content = fetch_raw_readme(full_name)
    readme_cache[key] = content
    return content


def owner_of(full_name: str) -> str:
    if not full_name:
        return ''
    return full_name.split('/')[0].lower()


def should_process_full(full_name: str, row_source: str) -> bool:
    # With API disabled we still process via raw/HTML for all repos.
    return True


def extract_summary_from_readme(readme_text: str) -> str:
    if not readme_text:
        return ''
    lines = [l.strip() for l in readme_text.splitlines()]
    buff = []
    for line in lines:
        if not line:
            if buff:
                break
            continue
        low = line.lower()
        if line.startswith('#'):
            continue
        if line.startswith('<'):
            continue
        if line.startswith('[![') or line.startswith('![') or line.startswith('<img'):
            continue
        if low.startswith('https://') or low.startswith('http://'):
            continue
        if low.startswith('!') or low.startswith('```'):
            continue
        if low.startswith('badge') or 'shields.io' in low:
            continue
        buff.append(line)
        if len(' '.join(buff)) > 180:
            break
    summary = ' '.join(buff).strip()
    # remove markdown links
    summary = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', summary)
    summary = re.sub(r'<[^>]+>', '', summary)
    summary = re.sub(r'\s{2,}', ' ', summary)
    return summary.strip()


def is_generic_best(text: str) -> bool:
    t = (text or '').strip().lower()
    if not t:
        return True
    if t in {'see readme', 'readme', 'todo', 'tbd', 'unknown'}:
        return True
    if t.startswith('<') or '<div' in t or '</div>' in t:
        return True
    return False


def is_generic_notfor(text: str) -> bool:
    t = (text or '').strip().lower()
    if not t:
        return True
    if t in {
        'non-matching stack or use case',
        'production',
        'non-telegram',
        'non-osint',
        'non-solana',
        'non-mev',
        'non-n8n',
        'non-js',
        'non-python'
    }:
        return True
    if t.startswith('не подходит, если нужен не '):
        return True
    if t.startswith('non-'):
        return True
    if t.startswith('не подходит для продакшена без'):
        return True
    if t.startswith('не подходит для продакшена без доработки'):
        return True
    if t.startswith('custom design'):
        return True
    return False


def infer_not_for(row, readme_text: str) -> str:
    dtype = row[col_idx['Type']].lower()
    category = row[col_idx['Category']].lower()
    source = row[col_idx['Source']].lower() if col_idx.get('Source') is not None else ''
    inputs = row[col_idx['Inputs']].lower() if col_idx.get('Inputs') is not None else ''
    readme_low = (readme_text or '').lower()

    if 'deprecated' in readme_low or 'no longer maintained' in readme_low:
        return 'Не подходит для новых проектов — репозиторий помечен как deprecated'
    if 'experimental' in readme_low or 'alpha' in readme_low or 'beta' in readme_low or 'wip' in readme_low:
        return 'Не подходит для продакшена без доработки и тестов'
    if source == 'curated' or dtype == 'reference':
        return 'Не подходит, если нужен один готовый продукт без выбора'
    if dtype == 'template':
        return 'Не подходит, если нужен готовый продукт без кастомизации'
    if dtype == 'sdk':
        return 'Не подходит, если нужен готовый сервис, а не библиотека'
    if dtype == 'cli':
        return 'Не подходит, если нужен GUI/веб‑интерфейс'
    if dtype == 'extension':
        return 'Не подходит, если нужен серверный сервис вместо расширения'
    if category == 'educational':
        return 'Не подходит, если нужен production‑ready инструмент'
    if category == 'scraping':
        return 'Не подходит, если нужен официальный API вместо парсинга'
    if category == 'trading':
        return 'Не подходит для реальных денег без длительного тестирования'
    if category == 'osint':
        return 'Не подходит для незаконных/чувствительных сценариев'
    if category in {'solana', 'blockchain'}:
        return 'Не подходит, если не используешь web3/кошельки'
    if category == 'mcp':
        return 'Не подходит, если не используешь MCP‑интеграции'
    if category == 'prompts':
        return 'Не подходит, если нужен готовый сервис, а не набор промптов'
    if category in {'ai', 'ai agent'}:
        return 'Не подходит, если нужен детерминированный pipeline без LLM'
    if category == 'multi-agent':
        return 'Не подходит, если нужен один агент без оркестрации'
    if category == 'rag':
        return 'Не подходит, если нет данных/поиска и нужен только LLM‑ответ'
    if category == 'curated':
        return 'Не подходит, если нужен один готовый продукт без выбора'
    if category == 'browser':
        return 'Не подходит, если браузерная автоматизация запрещена'
    if category == 'infra':
        return 'Не подходит, если нужен простой локальный запуск без инфраструктуры'
    if category == 'devtools':
        return 'Не подходит, если нужен пользовательский продукт, а не dev‑tool'
    if category == 'analytics':
        return 'Не подходит, если не нужна аналитика/метрики'
    if category == 'template':
        return 'Не подходит, если нужен готовый продукт без кастомизации'
    if inputs:
        if 'gpu' in inputs:
            return 'Не подходит, если нет доступа к GPU'
        if 'wallet' in inputs:
            return 'Не подходит, если нет кошелька/он‑чейн доступа'
        if 'browser' in inputs:
            return 'Не подходит, если нельзя запускать браузерную автоматизацию'
        if 'db' in inputs:
            return 'Не подходит, если нельзя поднять БД'
        if 'api key' in inputs:
            return 'Не подходит, если нельзя использовать внешние API‑ключи'
    return 'Не подходит для продакшена без настройки и адаптации'


# --- README parsing ---
readme_text = README_PATH.read_text(encoding='utf-8', errors='replace')
lines = readme_text.splitlines()

header_idx = None
for i, line in enumerate(lines):
    if line.startswith('| # | Repo |'):
        header_idx = i
        break
if header_idx is None:
    raise SystemExit('Catalog table header not found')

end_idx = None
for j in range(header_idx + 1, len(lines)):
    if lines[j].startswith('## '):
        end_idx = j
        break
if end_idx is None:
    end_idx = len(lines)

header_line = lines[header_idx]
columns = [c.strip() for c in header_line.strip().strip('|').split('|')]
col_idx = {c: i for i, c in enumerate(columns)}

row_lines = []
for line in lines[header_idx + 2:end_idx]:
    if re.match(r'^\|\s*\d+\s*\|', line):
        row_lines.append(line)

rows = []
for line in row_lines:
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells) != len(columns):
        continue
    rows.append(cells)


def extract_repo_name(cell: str):
    if cell.startswith('[') and '](' in cell:
        return cell.split('](')[0].lstrip('[').strip()
    return cell.strip()


def anchor_for_name(name: str):
    return re.sub(r'[^a-z0-9-]', '', name.lower().replace(' ', '').replace('/', ''))


def extract_full_from_details(text: str):
    mapping = {}
    if DETAILS_HEADER not in text:
        return mapping
    detail_part = text.split(DETAILS_HEADER, 1)[1]
    sections = re.split(r'(?m)^## ', detail_part)
    for sec in sections[1:]:
        lines_sec = sec.splitlines()
        title = lines_sec[0].strip() if lines_sec else ''
        body = '\n'.join(lines_sec[1:])
        m_repo = re.search(r'^- Repo:\s*(https://github\.com/[^\s]+)', body, flags=re.M)
        if m_repo:
            full = m_repo.group(1).replace('https://github.com/', '').strip('/').lower()
            mapping[title.lower()] = full
    return mapping


full_from_details = extract_full_from_details(readme_text)


basename_map = {}
for full in union_full.keys():
    base = full.split('/')[-1].lower()
    basename_map.setdefault(base, []).append(full)


def select_full_name(display_name: str):
    name_l = display_name.lower()
    if name_l in full_from_details:
        return full_from_details[name_l]
    if '/' in name_l:
        return name_l
    base = name_l
    candidates = basename_map.get(base, [])
    if not candidates:
        return None
    for full in candidates:
        if full in public_full and public_full[full].get('owner', {}).get('login', '').lower() == USER:
            return full
    for full in candidates:
        if full in star_full:
            return full
    return candidates[0]


row_full = {}
used_full = set()
for r in rows:
    name = extract_repo_name(r[col_idx['Repo']])
    full = select_full_name(name)
    if full:
        row_full[name] = full
        used_full.add(full)

missing_full = [full for full in union_full.keys() if full not in used_full]


def classify_type(repo, desc: str):
    name = (repo.get('name') or '').lower() if repo else ''
    desc_l = (desc or '').lower()
    topics = [t.lower() for t in (repo.get('topics') or [])] if repo else []
    if 'awesome' in name or 'awesome' in desc_l or 'list' in desc_l or 'resources' in desc_l:
        return 'reference'
    if any(k in desc_l for k in ['template', 'starter', 'boilerplate', 'landing', 'theme']) or 'template' in name:
        return 'template'
    if 'cli' in name or 'cli' in desc_l or 'command line' in desc_l:
        return 'cli'
    if any(k in desc_l for k in ['sdk', 'client', 'library']) or 'sdk' in topics:
        return 'sdk'
    if any(k in desc_l for k in ['api', 'server', 'gateway', 'backend', 'service']) or 'server' in topics:
        return 'service'
    return 'app'


def classify_category(repo, desc: str):
    name = (repo.get('name') or '').lower() if repo else ''
    desc_l = (desc or '').lower()
    topics = [t.lower() for t in (repo.get('topics') or [])] if repo else []
    def has(k):
        return k in desc_l or k in name or k in topics
    if has('mcp'):
        return 'MCP'
    if has('solana'):
        return 'Solana'
    if has('blockchain') or has('web3') or has('evm') or has('crypto'):
        return 'Blockchain'
    if has('trading') or has('arbitrage') or has('bot') or has('dex') or has('mev'):
        return 'Trading'
    if has('scrap') or has('crawler') or has('scraper'):
        return 'Scraping'
    if has('osint') or has('security'):
        return 'OSINT'
    if has('prompt'):
        return 'Prompts'
    if has('template') or has('dashboard') or has('ui'):
        return 'Template'
    if has('extension'):
        return 'Extension'
    if has('agent') or has('llm') or has('ai'):
        return 'AI'
    if has('education') or has('course'):
        return 'Educational'
    return 'Other'


def classify_maturity(repo, desc: str):
    if repo and repo.get('archived'):
        return 'deprecated'
    desc_l = (desc or '').lower()
    if 'experimental' in desc_l or 'experiment' in desc_l:
        return 'experimental'
    pushed = repo.get('pushed_at') if repo else None
    if pushed:
        try:
            dt = datetime.fromisoformat(pushed.replace('Z', '+00:00'))
            months = (datetime.now(timezone.utc) - dt).days / 30.0
            if months <= 6:
                return 'active'
            if months <= 18:
                return 'maintained'
            return 'stale'
        except Exception:
            pass
    return 'unknown'


def classify_latency(category: str):
    cat = (category or '').lower()
    if cat in {'ml/rl', 'multimodal', 'ai'}:
        return 'quality'
    if cat in {'scraping', 'trading'}:
        return 'fast'
    return 'balanced'


def extract_quickstart(readme_text: str, repo_url: str):
    blocks = re.findall(r'```(?:bash|sh|shell|zsh|powershell|cmd)?\n(.*?)```', readme_text, re.S | re.I)
    patterns = [
        r'^\s*git clone\s+.*',
        r'^\s*pip install\s+.*',
        r'^\s*npm (install|i)\s+.*',
        r'^\s*pnpm (install|i)\s+.*',
        r'^\s*yarn (add|install)\s+.*',
        r'^\s*docker( compose)?\s+.*',
        r'^\s*python\s+.*',
        r'^\s*node\s+.*',
        r'^\s*cargo\s+.*',
        r'^\s*go\s+.*',
    ]
    for block in blocks:
        for line in block.splitlines():
            for pat in patterns:
                if re.match(pat, line.strip(), re.I):
                    return f'`{line.strip()}`'
    for pat in patterns:
        m = re.search(pat, readme_text, re.M | re.I)
        if m:
            return f'`{m.group(0).strip()}`'
    return repo_url


def extract_inputs(text: str):
    t = (text or '').lower()
    found = []
    def add(label):
        if label not in found:
            found.append(label)
    if 'api key' in t or 'apikey' in t or 'api_key' in t or 'token' in t or 'openai' in t or 'gemini' in t or 'anthropic' in t:
        add('API key')
    if 'wallet' in t:
        add('wallet')
    if 'rpc' in t:
        add('RPC')
    if 'gpu' in t or 'cuda' in t:
        add('GPU')
    if 'postgres' in t or 'mysql' in t or 'sqlite' in t or 'database' in t or 'redis' in t:
        add('DB')
    if 'browser' in t or 'chrome' in t or 'playwright' in t:
        add('browser')
    if 'dataset' in t or 'corpus' in t:
        add('dataset')
    if 'telegram' in t:
        add('TG token')
    if not found:
        return 'none'
    return ', '.join(found)


updated_rows = []
for r in rows:
    name = extract_repo_name(r[col_idx['Repo']])
    full = row_full.get(name)
    row_source = r[col_idx['Source']] if col_idx.get('Source') is not None else ''
    if full:
        if not should_process_full(full, row_source):
            updated_rows.append(r)
            continue
        repo = get_repo(full)
        stub = bool(repo and repo.get('_stub'))
        desc = repo.get('description') if repo and not stub else ''
        current_type = r[col_idx['Type']].lower() if r[col_idx['Type']] else ''
        if current_type and current_type != 'unknown':
            rtype = current_type
        else:
            rtype = classify_type(repo, desc) if not stub else 'unknown'
        category = r[col_idx['Category']]
        if (category or '').lower() in {'curated', 'reference'}:
            rtype = 'reference'
        source = r[col_idx['Source']] or 'unknown'
        if source == 'unknown':
            if full in public_full:
                source = 'forked' if public_full[full].get('fork') else 'owned'
            elif full in star_full:
                source = 'starred'
        current_maturity = r[col_idx['Maturity']]
        if current_maturity:
            maturity = current_maturity
        else:
            maturity = classify_maturity(repo, desc) if not stub else 'unknown'
        current_latency = r[col_idx['Latency/Cost']]
        if current_latency:
            latency = current_latency
        else:
            latency = classify_latency(r[col_idx['Category']])
        deploy = r[col_idx['Deployable']]
        if not deploy or deploy == 'unknown':
            if rtype in {'reference', 'template'}:
                deploy = 'no'
            elif rtype in {'app', 'service', 'cli'}:
                deploy = 'yes'
            else:
                deploy = 'unknown'
        readme = ''
        best_for = r[col_idx['Best for']]
        if is_generic_best(best_for):
            readme = get_readme(full)
            summary = extract_summary_from_readme(readme)
            if summary:
                best_for = summary
            else:
                desc_html = fetch_repo_description_html(full)
                if desc_html:
                    best_for = desc_html
        not_for = r[col_idx['Not for']]
        if is_generic_notfor(not_for):
            if readme:
                not_for = infer_not_for(r, readme)
            else:
                not_for = infer_not_for(r, '')
        quick = r[col_idx['Quickstart']]
        if quick.strip().lower() in {'todo', '—', '-', 'see readme', 'reference'}:
            if not readme:
                readme = get_readme(full)
            quick = extract_quickstart(readme, repo.get('html_url', full) if repo else full)
        inputs = r[col_idx['Inputs']]
        if inputs.strip() in {'—', '?', ''}:
            if not readme:
                readme = get_readme(full)
            inputs = extract_inputs(readme or desc)

        r[col_idx['Source']] = source
        r[col_idx['Type']] = rtype
        r[col_idx['Deployable']] = deploy
        r[col_idx['Maturity']] = maturity
        r[col_idx['Latency/Cost']] = latency
        r[col_idx['Quickstart']] = quick
        r[col_idx['Inputs']] = inputs
        r[col_idx['Best for']] = best_for
        r[col_idx['Not for']] = not_for

    updated_rows.append(r)

# add missing
existing_names = {extract_repo_name(r[col_idx['Repo']]).lower() for r in updated_rows}
for full in missing_full:
    if not should_process_full(full, ''):
        continue
    repo = get_repo(full)
    if not repo:
        continue
    stub = bool(repo.get('_stub'))
    desc = repo.get('description') or ''
    category = classify_category(repo, desc)
    rtype = classify_type(repo, desc) if not stub else 'unknown'
    maturity = classify_maturity(repo, desc) if not stub else 'unknown'
    latency = classify_latency(category)
    source = 'forked' if repo.get('fork') and repo.get('owner', {}).get('login', '').lower() == USER else 'owned'
    if full in star_full and source != 'owned':
        source = 'starred'
    deploy = 'no' if rtype in {'reference', 'template'} else 'yes'
    readme = get_readme(full)
    quick = extract_quickstart(readme, repo.get('html_url', full))
    inputs = extract_inputs(readme or desc)

    tmp_row = [''] * len(columns)
    tmp_row[col_idx['Type']] = rtype
    tmp_row[col_idx['Category']] = category

    display = repo.get('full_name') if repo.get('name', '').lower() in existing_names else repo.get('name')
    if repo.get('name', '').lower() in existing_names:
        display = repo.get('full_name')
    anchor = anchor_for_name(display)
    repo_cell = f'[{display}](#{anchor})'

    best_for = desc if desc else extract_summary_from_readme(readme)
    if not best_for:
        best_for = fetch_repo_description_html(full)
    if not best_for:
        best_for = 'See README'
    not_for = infer_not_for(tmp_row, readme)

    row = [''] * len(columns)
    row[col_idx['Repo']] = repo_cell
    row[col_idx['Category']] = category
    row[col_idx['Best for']] = best_for
    row[col_idx['Not for']] = not_for
    row[col_idx['Quickstart']] = quick
    row[col_idx['Maturity']] = maturity
    row[col_idx['Latency/Cost']] = latency
    row[col_idx['Inputs']] = inputs
    row[col_idx['Source']] = source
    row[col_idx['Type']] = rtype
    row[col_idx['Deployable']] = deploy

    updated_rows.append(row)
    existing_names.add(repo.get('name', '').lower())

# re-number rows
new_table_lines = []
for i, row in enumerate(updated_rows, start=1):
    row[col_idx['#']] = str(i)
    new_table_lines.append('| ' + ' | '.join(row) + ' |')

new_lines = lines[:header_idx] + [lines[header_idx], lines[header_idx+1]] + new_table_lines + lines[end_idx:]
readme_text = '\n'.join(new_lines) + '\n'

# Detailed Descriptions
if DETAILS_HEADER not in readme_text:
    raise SystemExit('Details header not found')

pre, detail_part = readme_text.split(DETAILS_HEADER, 1)
sections = re.split(r'(?m)^## ', detail_part)
section_map = {}
section_order = []
for sec in sections[1:]:
    lines_sec = sec.splitlines()
    title = lines_sec[0].strip()
    body = '\n'.join(lines_sec[1:]).rstrip()
    section_map[title] = body
    section_order.append(title)

name_to_full = {}
for r in updated_rows:
    name = extract_repo_name(r[col_idx['Repo']])
    full = select_full_name(name)
    if full:
        name_to_full[name] = full


required_blocks = [
    '**TL;DR:**',
    '### Быстрый выбор',
    '### 🚀 Запуск',
    '### 🧩 Архитектура',
    '### 🧪 Примеры задач',
    '### ⚠️ Ограничения',
    '### 🧭 Fit / Maturity / Ops',
    '### Full links',
]


def generate_section(name: str, row):
    full = name_to_full.get(name)
    repo = get_repo(full) if full else None
    desc = repo.get('description') if repo else ''
    if not desc:
        desc = f'{name} repository.'
    readme = get_readme(full) if full else ''
    quick = row[col_idx['Quickstart']]
    inputs = row[col_idx['Inputs']]
    maturity = row[col_idx['Maturity']]
    latency = row[col_idx['Latency/Cost']]
    category = row[col_idx['Category']]
    rtype = row[col_idx['Type']]

    tldr = f"**TL;DR:** {name} — {desc}. Подходит для задач категории {category.lower()}. Ограничение: зависит от входных данных ({inputs}) или документации." 

    quick_choice = """### Быстрый выбор
- ✅ Используй если: нужен инструмент из категории {cat}, подходит под {best}
- ❌ Не используй если: {notfor}
""".format(cat=category, best=row[col_idx['Best for']], notfor=row[col_idx['Not for']])

    launch = f"""### 🚀 Запуск
{quick if quick else 'См. README'}
"""

    arch = f"""### 🧩 Архитектура
- **Category:** {category}
- **Type:** {rtype}
- **Language:** {repo.get('language') if repo else 'unknown'}
- **Inputs:** {inputs}
"""

    examples = f"""### 🧪 Примеры задач
- {row[col_idx['Best for']]}
- Быстрый прототип/интеграция под {category}
"""

    limits = """### ⚠️ Ограничения
- Качество/полнота зависит от исходного README
- Требуются настройки или ключи, если указано в Inputs
- Может быть экспериментальным или нишевым
"""

    fit = f"""### 🧭 Fit / Maturity / Ops
- **Fit:** {row[col_idx['Best for']]}
- **Maturity:** {maturity}
- **Latency/Cost:** {latency}
- **Ops friction:** {'medium' if inputs not in {'none',''} else 'low'}
"""

    links = """### Full links
- Repo: {url}
""".format(url=repo.get('html_url') if repo else '')

    return '\n'.join([tldr, '', quick_choice, launch, arch, examples, limits, fit, links]).strip() + '\n'


for row in updated_rows:
    name = extract_repo_name(row[col_idx['Repo']])
    body = section_map.get(name)
    if body is None:
        section_map[name] = generate_section(name, row)
        section_order.append(name)
        continue
    missing = [b for b in required_blocks if b not in body]
    if missing:
        extra = generate_section(name, row)
        for block in required_blocks:
            if block in missing:
                m = re.search(re.escape(block) + r'.*?(?=\n### |\Z)', extra, re.S)
                if m:
                    body = body.rstrip() + '\n\n' + m.group(0).strip() + '\n'
        section_map[name] = body

    tldr_match = re.search(r'\*\*TL;DR:\*\*([^\n]+)', section_map[name])
    if tldr_match:
        tldr = tldr_match.group(1).strip()
        sentences = [s for s in re.split(r'[.!?]+', tldr) if s.strip()]
        if len(sentences) < 3:
            extra_sent = f" Полезен для {row[col_idx['Best for']]} и быстрых интеграций.".strip()
            new_tldr = tldr + extra_sent
            section_map[name] = section_map[name].replace(tldr_match.group(0), f"**TL;DR:** {new_tldr}")

new_detail = DETAILS_HEADER + '\n\n'
for name in section_order:
    body = section_map.get(name, '').strip()
    if not body:
        continue
    new_detail += f'## {name}\n\n{body}\n\n'

readme_text = pre + new_detail
README_PATH.write_text(readme_text, encoding='utf-8')

# Update header counts
lines = readme_text.splitlines()
for i, line in enumerate(lines):
    if line.startswith('> **') and 'репозит' in line:
        lines[i] = f"> **{len(updated_rows)} уникальных репозиториев (deduped)**: AI agents, LLM frameworks, Solana/blockchain tools, trading bots, MCP servers, scrapers, DevTools, UI templates."
        break
for i, line in enumerate(lines):
    if 'Catalog Table:' in line:
        lines[i] = f"> Mix of owned/forked/starred repos. **Catalog Table: {len(updated_rows)} indexed entries**."
        break
README_PATH.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print('README updated')
