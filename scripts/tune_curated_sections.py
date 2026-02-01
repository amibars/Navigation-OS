import re
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


def is_curated_row(row):
    source = row[col_idx['Source']].lower()
    dtype = row[col_idx['Type']].lower()
    category = row[col_idx['Category']].lower()
    return source == 'curated' or dtype in {'reference', 'template'} or category in {'curated', 'reference'}


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


STOP_TITLES = {
    'featured ai projects', 'featured projects', 'getting started', 'thank you, community, for the support!',
    'thank you, community, for the support', 'sponsors', 'support', 'credits'
}

KEYWORDS = ['agent', 'multi-agent', 'mcp', 'rag', 'voice', 'memory', 'chat', 'optimization', 'fine-tuning', 'tools', 'browser']


def normalize_title(title: str) -> str:
    t = title.strip()
    t = re.sub(r'^#+\s*', '', t)
    t = re.sub(r'^[-–—\s]+', '', t)
    t = t.replace('\uFE0F', '')
    # remove leading emoji or symbols
    t = re.sub(r'^[^A-Za-zА-Яа-я0-9]+\s*', '', t)
    return t.strip()


def extract_curated_titles(body: str):
    block = ''
    m_block = re.search(r'### 📚 Содержание \(из README\)([\s\S]*?)(?=\n### |\Z)', body)
    if m_block:
        block = m_block.group(1)
    titles = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith('#### ') or line.startswith('##### '):
            title = line.replace('#### ', '').replace('##### ', '').strip()
            title = normalize_title(title)
            if not title:
                continue
            low = title.lower()
            if low in STOP_TITLES:
                continue
            if title not in titles:
                titles.append(title)
    # prioritize by keywords
    def score(t):
        low = t.lower()
        s = 0
        for kw in KEYWORDS:
            if kw in low:
                s += 1
        return s
    prioritized = sorted(titles, key=lambda t: (-score(t), titles.index(t)))
    # keep top 5 diverse
    top = []
    for t in prioritized:
        if t not in top:
            top.append(t)
        if len(top) >= 5:
            break
    return top


def replace_block(body: str, heading: str, new_block: str) -> str:
    pattern = re.escape(heading) + r'\n([\s\S]*?)(?=\n### |\Z)'
    if re.search(pattern, body):
        return re.sub(pattern, heading + '\n' + new_block + '\n', body)
    return body


for name in section_order:
    row = row_for(name)
    if not row or not is_curated_row(row):
        continue

    body = section_map[name]

    titles = extract_curated_titles(body)
    if titles:
        tldr_sentences = [
            f"{name} — curated‑каталог/справочник по теме и набору рабочих AI‑проектов.",
            "Полезен, когда нужно быстро увидеть, какие готовые агенты/сценарии можно запустить сразу.",
            "Ключевые разделы: " + ", ".join(titles[:5]) + ".",
            "Большинство пунктов — реальные проекты с собственными README и инструкциями запуска.",
            "Ограничение: это набор разных проектов, поэтому выбор и настройка остаются на тебе.",
        ]
    else:
        tldr_sentences = [
            f"{name} — curated‑каталог/справочник по теме и набору рабочих AI‑проектов.",
            "Полезен, когда нужно быстро увидеть, какие готовые агенты/сценарии можно запустить сразу.",
            "Большинство пунктов — реальные проекты с собственными README и инструкциями запуска.",
            "Ограничение: это набор разных проектов, поэтому выбор и настройка остаются на тебе.",
        ]
    new_tldr = "**TL;DR:** " + " ".join(tldr_sentences)
    body = re.sub(r'\*\*TL;DR:\*\*[^\n]*', new_tldr, body)

    # Quick choice
    quick_block = "\n".join([
        "- ✅ Используй если: хочешь быстро запустить готовых агентов/проекты из списка",
        "- ✅ Используй если: нужен широкий обзор решений по теме",
        "- ✅ Используй если: выбираешь стек под задачу и хочешь сравнить подходы",
        "- ❌ Не используй если: нужен один стабильный продукт с единым API",
        "- ❌ Не используй если: нет времени на ручной выбор и настройку",
    ])
    body = replace_block(body, '### Быстрый выбор', quick_block)

    # Limits block
    limits_block = "\n".join([
        "- Проекты разной зрелости: качество и поддержка сильно отличаются",
        "- Запуск зависит от конкретного подпроекта и его README",
        "- Часто нужны ключи/модели/доступы — проверяй требования",
    ])
    body = replace_block(body, '### ⚠️ Ограничения', limits_block)

    section_map[name] = body.rstrip()

# Rebuild details
new_detail = header + '\n\n'
for name in section_order:
    body = section_map[name].strip()
    new_detail += f'## {name}\n\n{body}\n\n'

text = pre + new_detail
README.write_text(text, encoding='utf-8')
print('curated TL;DR titles prioritized')
