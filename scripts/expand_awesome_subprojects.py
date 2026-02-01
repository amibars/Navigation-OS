import re
from pathlib import Path

README = Path('README.md')
text = README.read_text(encoding='utf-8')

# Parse catalog table
lines = text.splitlines()
header_idx = next((i for i, l in enumerate(lines) if l.startswith('| # | Repo |')), None)
if header_idx is None:
    raise SystemExit('Catalog table header not found')
end_idx = next((i for i in range(header_idx + 1, len(lines)) if lines[i].startswith('## ')), len(lines))

columns = [c.strip() for c in lines[header_idx].strip().strip('|').split('|')]
col_idx = {c: i for i, c in enumerate(columns)}
rows = []
for line in lines[header_idx + 2:end_idx]:
    if re.match(r'^\|\s*\d+\s*\|', line):
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == len(columns):
            rows.append(cells)


def name_from_cell(cell: str) -> str:
    if cell.startswith('[') and '](' in cell:
        return cell[1:cell.index('](')].strip()
    return cell.strip()


def anchor_for_name(name: str) -> str:
    return re.sub(r'[^a-z0-9-]', '', name.lower().replace(' ', '').replace('/', ''))


def make_repo_cell(name: str) -> str:
    return f'[{name}](#{anchor_for_name(name)})'

# Extract awesome-llm-apps section and curated block
m = re.search(r'^## awesome-llm-apps\n([\s\S]*?)(?=\n## |\Z)', text, flags=re.M)
if not m:
    raise SystemExit('awesome-llm-apps section not found')
section_body = m.group(1)

block_match = re.search(r'### 📚 Содержание \(из README\)\n([\s\S]*?)(?=\n### |\Z)', section_body)
if not block_match:
    raise SystemExit('Curated block not found in awesome-llm-apps section')
block = block_match.group(1)

# Parse items from curated block
items = []
current_heading = None
for raw in block.splitlines():
    line = raw.strip()
    if not line:
        continue
    if line.startswith('#### ') or line.startswith('##### ') or line.startswith('###### '):
        current_heading = re.sub(r'^#+\s*', '', line).strip()
        continue
    # extract markdown link
    m_link = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
    if not m_link:
        continue
    title = m_link.group(1).strip()
    path = m_link.group(2).strip()
    # skip external links and star-history
    if path.startswith('http') or path.startswith('https') or path.startswith('#'):
        continue
    # normalize path
    path = path.rstrip('/')
    if not path:
        continue
    # description after dash
    desc = None
    # try to find a dash description after the link
    after = line[m_link.end():].strip()
    if after.startswith('-'):
        desc = after.lstrip('-').strip()
    items.append({
        'title': title,
        'path': path,
        'heading': current_heading or 'Awesome LLM Apps',
        'desc': desc,
    })

# Deduplicate by path
seen = set()
unique_items = []
for it in items:
    key = it['path']
    if key in seen:
        continue
    seen.add(key)
    unique_items.append(it)

# Build mapping for categories

def category_from_heading(heading: str) -> str:
    h = (heading or '').lower()
    if 'mcp' in h:
        return 'MCP'
    if 'rag' in h:
        return 'RAG'
    if 'memory' in h:
        return 'Memory'
    if 'chat with' in h:
        return 'Chat'
    if 'optimization' in h:
        return 'Optimization'
    if 'fine-tuning' in h or 'finetuning' in h:
        return 'Fine-tuning'
    if 'crash course' in h or 'tutorial' in h:
        return 'Educational'
    if 'voice' in h:
        return 'Voice'
    if 'multi-agent' in h or 'multiagent' in h:
        return 'Multi-Agent'
    if 'game' in h:
        return 'Simulation'
    if 'multimodal' in h:
        return 'Multimodal'
    if 'agent' in h:
        return 'AI Agent'
    return 'AI'


def maturity_from_heading(heading: str) -> str:
    h = (heading or '').lower()
    if 'tutorial' in h or 'crash course' in h:
        return 'educational'
    return 'experimental'


def latency_from_category(category: str) -> str:
    c = category.lower()
    if c in {'fine-tuning', 'multimodal'}:
        return 'quality'
    if c in {'optimization'}:
        return 'fast'
    return 'balanced'


def inputs_from_category(category: str) -> str:
    c = category.lower()
    if c in {'rag'}:
        return 'API key, DB, dataset'
    if c in {'memory'}:
        return 'DB'
    if c in {'mcp'}:
        return 'API key'
    if c in {'voice'}:
        return 'API key'
    if c in {'fine-tuning'}:
        return 'GPU, dataset'
    if c in {'multimodal'}:
        return 'API key, GPU'
    if c in {'chat'}:
        return 'API key, browser'
    if c in {'multi-agent', 'ai agent', 'ai'}:
        return 'API key'
    if c in {'simulation'}:
        return 'API key'
    return 'API key'

# Existing names to avoid duplicates
existing_names = {name_from_cell(r[col_idx['Repo']]) for r in rows}

new_rows = []
for it in unique_items:
    repo_name = f"awesome-llm-apps/{it['path']}"
    if repo_name in existing_names:
        continue
    category = category_from_heading(it['heading'])
    best_for = it['desc'] or it['title']
    not_for = f"Не подходит, если нужен не {category}‑сценарий или один стабильный продукт без выбора"
    quick = f"`git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git && cd awesome-llm-apps/{it['path']}`"
    maturity = maturity_from_heading(it['heading'])
    latency = latency_from_category(category)
    inputs = inputs_from_category(category)
    source = 'curated'
    dtype = 'app'
    deployable = 'yes'

    row = [''] * len(columns)
    row[col_idx['Repo']] = make_repo_cell(repo_name)
    row[col_idx['Category']] = category
    row[col_idx['Best for']] = best_for
    row[col_idx['Not for']] = not_for
    row[col_idx['Quickstart']] = quick
    row[col_idx['Maturity']] = maturity
    row[col_idx['Latency/Cost']] = latency
    row[col_idx['Inputs']] = inputs
    row[col_idx['Source']] = source
    row[col_idx['Type']] = dtype
    row[col_idx['Deployable']] = deployable
    new_rows.append(row)
    existing_names.add(repo_name)

# Append new rows to table
updated_rows = rows + new_rows

# Renumber
for i, row in enumerate(updated_rows, start=1):
    row[col_idx['#']] = str(i)

new_table_lines = ['| ' + ' | '.join(row) + ' |' for row in updated_rows]
new_lines = lines[:header_idx] + [lines[header_idx], lines[header_idx+1]] + new_table_lines + lines[end_idx:]
text = '\n'.join(new_lines) + '\n'

# Rebuild details in table order
m2 = re.search(r'^## .*Detailed Descriptions', text, flags=re.M)
header = m2.group(0)
pre, detail_body = text.split(header, 1)
sections = re.split(r'(?m)^## ', detail_body)
section_map = {}
for sec in sections[1:]:
    lines_sec = sec.splitlines()
    title = lines_sec[0].strip() if lines_sec else ''
    body = '\n'.join(lines_sec[1:]).rstrip()
    section_map[title] = body

# Generate new sections for added entries
for row in new_rows:
    name = name_from_cell(row[col_idx['Repo']])
    if name in section_map:
        continue
    category = row[col_idx['Category']]
    best_for = row[col_idx['Best for']]
    not_for = row[col_idx['Not for']]
    quick = row[col_idx['Quickstart']]
    maturity = row[col_idx['Maturity']]
    latency = row[col_idx['Latency/Cost']]
    inputs = row[col_idx['Inputs']]

    tldr = (
        f"**TL;DR:** {name} — подпроект из awesome-llm-apps, который можно запускать отдельно. "
        f"Это {category.lower()}‑сценарий: {best_for}. "
        f"Обычно требует {inputs} и базовой настройки окружения. "
        f"Подходит для быстрых экспериментов и локальных запусков по инструкции в подпроекте. "
        f"Ограничение: стабильность и качество зависят от конкретного подпроекта." 
    )

    quick_choice = "\n".join([
        "### Быстрый выбор",
        f"- ✅ Используй если: нужен {category.lower()}‑пример из awesome-llm-apps",
        f"- ✅ Используй если: хочешь запустить '{best_for}' без самостоятельной сборки",
        f"- ❌ Не используй если: {not_for}",
        f"- ❌ Не используй если: нет доступа к {inputs}",
    ])

    launch = "\n".join([
        "### 🚀 Запуск",
        quick,
        "# Далее см. README внутри подпроекта",
    ])

    arch = "\n".join([
        "### 🧩 Архитектура",
        f"- **Category:** {category}",
        "- **Type:** app",
        "- **Language:** unknown",
        f"- **Inputs:** {inputs}",
        "- **Base repo:** awesome-llm-apps",
    ])

    examples = "\n".join([
        "### 🧪 Примеры задач",
        f"- {best_for}",
        f"- Быстрый прототип/интеграция под {category}",
        "- Проверка идеи/демо без отдельного репозитория",
    ])

    limits = "\n".join([
        "### ⚠️ Ограничения",
        "- Проект может быть экспериментальным",
        "- Требования зависят от подпроекта",
        "- Возможны несовместимости окружения",
    ])

    fit = "\n".join([
        "### 🧭 Fit / Maturity / Ops",
        f"- **Fit:** {best_for}",
        f"- **Maturity:** {maturity}",
        f"- **Latency/Cost:** {latency}",
        f"- **Data constraints:** {inputs}",
        "- **Ops friction:** medium",
    ])

    repo_url = "https://github.com/Shubhamsaboo/awesome-llm-apps"
    subpath = name.replace('awesome-llm-apps/', '')
    sub_url = f"{repo_url}/tree/main/{subpath}"
    links = "\n".join([
        "### Full links",
        f"- Repo: {repo_url}",
        f"- Subpath: {sub_url}",
    ])

    section_map[name] = "\n\n".join([tldr, quick_choice, launch, arch, examples, limits, fit, links]).strip()

# Rebuild detail section in table order
new_detail = header + '\n\n'
for row in updated_rows:
    name = name_from_cell(row[col_idx['Repo']])
    body = section_map.get(name, '').strip()
    new_detail += f'## {name}\n\n{body}\n\n'

text = pre + new_detail

# Update header counts
lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith('> **') and 'deduped' in line:
        lines[i] = re.sub(r'^> \*\*\d+', f"> **{len(updated_rows)}", line)
        break
for i, line in enumerate(lines):
    if 'Catalog Table:' in line:
        lines[i] = f"> Mix of owned/forked/starred repos. **Catalog Table: {len(updated_rows)} indexed entries**."
        break
text = '\n'.join(lines) + '\n'

README.write_text(text, encoding='utf-8')
print(f'Added {len(new_rows)} subprojects from awesome-llm-apps')
