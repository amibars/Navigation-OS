import base64
import json
import re
import subprocess
import os
import urllib.error
import urllib.request
from pathlib import Path

README = Path('README.md')
text = README.read_text(encoding='utf-8')

# Parse table
lines = text.splitlines()
header_idx = next((i for i,l in enumerate(lines) if l.startswith('| # | Repo |')), None)
if header_idx is None:
    raise SystemExit('Catalog table header not found')
end_idx = next((i for i in range(header_idx+1, len(lines)) if lines[i].startswith('## ')), len(lines))
columns = [c.strip() for c in lines[header_idx].strip().strip('|').split('|')]
col_idx = {c:i for i,c in enumerate(columns)}
rows = []
for line in lines[header_idx+2:end_idx]:
    if re.match(r'^\|\s*\d+\s*\|', line):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == len(columns):
            rows.append(cells)


def name_from_cell(cell: str) -> str:
    if cell.startswith('[') and '](' in cell:
        return cell[1:cell.index('](')].strip()
    return cell.strip()


def row_for(name: str):
    for r in rows:
        if name_from_cell(r[col_idx['Repo']]) == name:
            return r
    return None


FORCE_NO_API = os.getenv('SYNC_FORCE_NO_API', '1') == '1'


def gh_api(path: str):
    if FORCE_NO_API:
        return None
    try:
        out = subprocess.check_output(['gh', 'api', path], text=True, encoding='utf-8', errors='replace')
        return json.loads(out)
    except Exception:
        return None


HTTP_TIMEOUT = 8
branch_cache = {}


def http_get(url: str) -> str:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception:
        return ''


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


readme_cache = {}


def get_readme(full: str) -> str:
    if full in readme_cache:
        return readme_cache[full]
    data = gh_api(f'/repos/{full}/readme')
    content = ''
    if data and isinstance(data, dict):
        try:
            content = base64.b64decode(data.get('content', '')).decode('utf-8', errors='replace')
        except Exception:
            content = ''
    if not content:
        content = fetch_raw_readme(full)
    readme_cache[full] = content
    return content


STOP_HEADINGS = {
    'license', 'contributing', 'credits', 'acknowledgments', 'acknowledgements',
    'faq', 'changelog', 'release notes', 'code of conduct', 'star history', 'support',
    'sponsors', 'thanks', 'thank you', 'community', 'contributions'
}


def clean_line(line: str) -> str:
    # remove HTML img tags
    line = re.sub(r'<img[^>]*>', '', line)
    # remove markdown image ![alt](...)
    line = re.sub(r'!\[[^\]]*\]\([^\)]*\)', '', line)
    # collapse multiple spaces
    line = re.sub(r'\s{2,}', ' ', line).strip()
    return line


def extract_curated_block(readme_text: str) -> str:
    if not readme_text:
        return ''
    lines = readme_text.splitlines()

    # identify start: prefer "Featured" or "AI Projects" or "Contents"
    start_idx = None
    for i, line in enumerate(lines):
        m = re.match(r'^##+\s+(.*)$', line)
        if not m:
            continue
        title = m.group(1).strip().lower()
        if any(k in title for k in ['featured', 'ai projects', 'projects', 'contents', 'table of contents', 'toc', 'index']):
            start_idx = i
            break
    if start_idx is None:
        # fallback to first level-2 heading
        for i, line in enumerate(lines):
            if line.startswith('## '):
                start_idx = i
                break
    if start_idx is None:
        start_idx = 0

    # end at stop heading
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        m = re.match(r'^##+\s+(.*)$', lines[i])
        if not m:
            continue
        title = m.group(1).strip().lower()
        if title in STOP_HEADINGS:
            end_idx = i
            break

    block_lines = []
    for raw in lines[start_idx:end_idx]:
        line = clean_line(raw)
        if not line:
            continue
        # demote headings to keep hierarchy inside section
        if line.startswith('#### '):
            line = '###### ' + line[5:]
        elif line.startswith('### '):
            line = '##### ' + line[4:]
        elif line.startswith('## '):
            line = '#### ' + line[3:]
        # normalize list bullets (keep as-is if already list)
        if re.match(r'^\*\s+', line):
            line = '- ' + line[2:]
        if re.match(r'^\d+\.\s+', line):
            line = '- ' + re.sub(r'^\d+\.\s+', '', line)
        block_lines.append(line)

    return '\n'.join(block_lines).strip()


# Parse details
m = re.search(r'^## .*Detailed Descriptions', text, flags=re.M)
if not m:
    raise SystemExit('Details header not found')
header = m.group(0)
pre, detail_body = text.split(header, 1)
sections = re.split(r'(?m)^## ', detail_body)
section_map = {}
section_order = []
for sec in sections[1:]:
    lines_sec = sec.splitlines()
    title = lines_sec[0].strip() if lines_sec else ''
    body = '\n'.join(lines_sec[1:]).rstrip()
    section_map[title] = body
    section_order.append(title)


def is_curated_row(row):
    source = row[col_idx['Source']].lower()
    dtype = row[col_idx['Type']].lower()
    category = row[col_idx['Category']].lower()
    return source == 'curated' or dtype in {'reference', 'template'} or category in {'curated', 'reference'}


def update_tldr_for_curated(body: str, curated_block: str) -> str:
    # extract top headings for summary
    curated_titles = []
    for line in curated_block.splitlines():
        if line.startswith('#### '):
            title = line.replace('#### ', '').strip()
            if title and title not in curated_titles:
                curated_titles.append(title)
        if len(curated_titles) >= 4:
            break
    tldr_match = re.search(r'\*\*TL;DR:\*\*[^\n]*', body)
    if not tldr_match:
        return body
    tldr = tldr_match.group(0)
    # build enriched tldr
    sentences = []
    sentences.append("curated‑каталог/справочник по теме и набору рабочих AI‑проектов.")
    sentences.append("Полезен, когда нужно быстро увидеть, какие готовые агенты/сценарии можно запустить сразу.")
    if curated_titles:
        sentences.append("Ключевые разделы: " + ", ".join(curated_titles) + ".")
    sentences.append("Большинство пунктов — реальные проекты с собственными README и инструкциями запуска.")
    sentences.append("Ограничение: это список, поэтому выбор и настройка остаются на тебе.")
    new_tldr = "**TL;DR:** " + " ".join(sentences)
    return body.replace(tldr, new_tldr)


# Update curated sections
for name in section_order:
    row = row_for(name)
    if not row or not is_curated_row(row):
        continue
    body = section_map[name]

    # find repo URL
    repo_url = None
    m_repo = re.search(r'^- Repo:\s*(https://github\.com/[^\s]+)', body, flags=re.M)
    if m_repo:
        repo_url = m_repo.group(1)
    if not repo_url:
        continue

    full = repo_url.replace('https://github.com/', '').strip('/')
    readme_text = get_readme(full)
    curated_block = extract_curated_block(readme_text)
    if curated_block:
        # replace existing curated block
        body = re.sub(r'### 📚 Содержание \(из README\)[\s\S]*?(?=\n### |\Z)', '', body).rstrip()
        # insert after Архитектура
        if '### 🧩 Архитектура' in body:
            parts = body.split('### 🧩 Архитектура')
            before = parts[0] + '### 🧩 Архитектура'
            after = '### 🧩 Архитектура'.join(parts[1:])
            after_lines = after.splitlines()
            block_lines = []
            idx = 0
            while idx < len(after_lines) and not after_lines[idx].startswith('### '):
                block_lines.append(after_lines[idx])
                idx += 1
            tail_lines = after_lines[idx:]
            new_after = '\n'.join(block_lines) + '\n\n' + '### 📚 Содержание (из README)\n' + curated_block + '\n\n' + '\n'.join(tail_lines)
            body = before + new_after
        else:
            body = body + '\n\n### 📚 Содержание (из README)\n' + curated_block

        # refresh TL;DR for curated with a clearer message
        body = update_tldr_for_curated(body, curated_block)

    section_map[name] = body.rstrip()

# Rebuild details
new_detail = header + '\n\n'
for name in section_order:
    body = section_map[name].strip()
    new_detail += f'## {name}\n\n{body}\n\n'

text = pre + new_detail
README.write_text(text, encoding='utf-8')
print('curated lists expanded')
