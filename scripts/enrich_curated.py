import base64
import json
import re
import subprocess
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


def gh_api(path: str):
    try:
        out = subprocess.check_output(['gh', 'api', path], text=True, encoding='utf-8', errors='replace')
        return json.loads(out)
    except Exception:
        return None


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
    readme_cache[full] = content
    return content


STOP_HEADINGS = {
    'license', 'contributing', 'credits', 'acknowledgments', 'acknowledgements',
    'faq', 'changelog', 'release notes', 'code of conduct'
}


def extract_curated_block(readme_text: str) -> str:
    if not readme_text:
        return ''
    lines = readme_text.splitlines()
    start_idx = None
    # Prefer Contents / Table of Contents
    for i, line in enumerate(lines):
        m = re.match(r'^##+\s+(.*)$', line)
        if not m:
            continue
        title = m.group(1).strip().lower()
        if any(k in title for k in ['contents', 'table of contents', 'toc', 'index', 'catalog']):
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

    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        m = re.match(r'^##+\s+(.*)$', lines[i])
        if not m:
            continue
        title = m.group(1).strip().lower()
        if title in STOP_HEADINGS:
            end_idx = i
            break
    block = lines[start_idx:end_idx]

    # Demote headings to fit inside detail section
    def demote(line: str) -> str:
        if line.startswith('#### '):
            return '###### ' + line[5:]
        if line.startswith('### '):
            return '##### ' + line[4:]
        if line.startswith('## '):
            return '#### ' + line[3:]
        return line

    block = [demote(l) for l in block]
    # Trim leading empty lines
    while block and not block[0].strip():
        block.pop(0)
    return '\n'.join(block).strip()


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


# Enrich curated/reference sections
for name in section_order:
    row = row_for(name)
    if not row:
        continue
    source = row[col_idx['Source']].lower()
    dtype = row[col_idx['Type']].lower()
    category = row[col_idx['Category']].lower()
    is_curated = source == 'curated' or dtype in {'reference', 'template'} or category in {'curated', 'reference'}

    body = section_map[name]

    # Fix Latency/Cost in Fit block
    latency = row[col_idx['Latency/Cost']]
    if latency:
        body = re.sub(r'^- \*\*Latency/Cost:\*\*.*$', f"- **Latency/Cost:** {latency}", body, flags=re.M)

    # Clean Quick choice: remove empty lines and duplicates
    if '### Быстрый выбор' in body:
        parts = body.split('### Быстрый выбор')
        head = parts[0]
        rest = '### Быстрый выбор'.join(parts[1:])
        # split block
        lines_rest = rest.splitlines()
        block = []
        i = 0
        while i < len(lines_rest) and not lines_rest[i].startswith('### '):
            line = lines_rest[i].strip()
            if line:
                block.append(line)
            i += 1
        tail = '\n'.join(lines_rest[i:])
        # dedupe
        seen = set()
        cleaned = []
        for line in block:
            if line in seen:
                continue
            seen.add(line)
            cleaned.append(line)
        # keep only bullet lines
        cleaned = [l for l in cleaned if l.startswith('- ')]
        body = head + '### Быстрый выбор\n' + ('\n'.join(cleaned) + '\n' if cleaned else '') + tail

    if is_curated:
        # find repo URL from Full links
        repo_url = None
        m_repo = re.search(r'^- Repo:\s*(https://github\.com/[^\s]+)', body, flags=re.M)
        if m_repo:
            repo_url = m_repo.group(1)
        if repo_url:
            full = repo_url.replace('https://github.com/', '').strip('/')
            readme_text = get_readme(full)
            curated_block = extract_curated_block(readme_text)
            if curated_block:
                section_title = '### 📚 Содержание (из README)'
                # Remove existing block if present
                body = re.sub(r'### 📚 Содержание \(из README\)[\s\S]*?(?=\n### |\Z)', '', body).rstrip()

                # Insert after Architecture block
                if '### 🧩 Архитектура' in body:
                    split = body.split('### 🧩 Архитектура')
                    before = split[0] + '### 🧩 Архитектура'
                    after = '### 🧩 Архитектура'.join(split[1:])
                    # find end of architecture block
                    after_lines = after.splitlines()
                    block_lines = []
                    tail_lines = []
                    idx = 0
                    while idx < len(after_lines) and not after_lines[idx].startswith('### '):
                        block_lines.append(after_lines[idx])
                        idx += 1
                    tail_lines = after_lines[idx:]
                    new_after = '\n'.join(block_lines) + '\n\n' + section_title + '\n' + curated_block + '\n\n' + '\n'.join(tail_lines)
                    body = before + new_after
                else:
                    body = body + '\n\n' + section_title + '\n' + curated_block

    section_map[name] = body.rstrip()

# Rebuild details
new_detail = header + '\n\n'
for name in section_order:
    body = section_map[name].strip()
    new_detail += f'## {name}\n\n{body}\n\n'

text = pre + new_detail
README.write_text(text, encoding='utf-8')
print('curated content injected')
