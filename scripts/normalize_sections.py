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


def is_generic(text: str) -> bool:
    t = (text or '').strip().lower()
    if not t:
        return True
    if 'non-matching stack or use case' in t:
        return True
    if 'see readme' in t:
        return True
    if 'other stacks' in t and 'review' in t:
        return True
    if t in {'production', 'non-telegram', 'non-solana', 'non-mev', 'non-osint', 'non-n8n', 'non-js', 'non-python'}:
        return True
    return False


def clean_best(best: str, category: str) -> str:
    if is_generic(best):
        return f"{category.lower()}‑задачи"
    return best.strip()


def build_tldr(name: str, row, curated_titles=None) -> str:
    category = row[col_idx['Category']]
    best = row[col_idx['Best for']]
    not_for = row[col_idx['Not for']]
    inputs = row[col_idx['Inputs']]
    dtype = row[col_idx['Type']].lower()
    source = row[col_idx['Source']].lower()
    maturity = row[col_idx['Maturity']]
    latency = row[col_idx['Latency/Cost']]

    best_clean = clean_best(best, category)
    not_for_clean = None if is_generic(not_for) else not_for

    is_reference = dtype in {'reference', 'template'} or category.lower() in {'curated', 'reference'} or source == 'curated'

    sentences = []
    if is_reference:
        sentences.append(f"{name} — curated‑каталог/справочник по теме {category.lower()} и смежным инструментам.")
        sentences.append("Полезен, когда нужно быстро понять, какие решения существуют и что выбрать под задачу.")
        if curated_titles:
            sentences.append("Содержит разделы: " + ", ".join(curated_titles) + ".")
        else:
            sentences.append(f"Внутри: {best_clean} и связанные примеры/ссылки.")
        sentences.append("Подходит для обзора, сравнения и поиска идей для интеграции в свой стек.")
        sentences.append("Ограничение: это не готовый продукт — придётся вручную выбрать и внедрить нужные решения.")
    else:
        sentences.append(f"{name} — {best_clean}.")
        sentences.append(f"Относится к категории {category} и закрывает типичные практические задачи без лишней сборки с нуля.")
        if inputs and inputs.lower() != 'none':
            sentences.append(f"Для работы обычно нужны входы: {inputs}.")
        else:
            sentences.append("Запускается без внешних ключей/данных или требует минимальных вводных.")
        sentences.append(f"Подходит, если устраивает зрелость {maturity} и баланс {latency}.")
        if not_for_clean:
            sentences.append(f"Ограничение: не подходит для сценария '{not_for_clean}'.")
        else:
            sentences.append("Ограничение: может требовать настройки и не всегда подходит для узких или production‑only сценариев.")

    # keep 4–6 sentences
    while len(sentences) > 6:
        sentences.pop(-2)
    return "**TL;DR:** " + " ".join(sentences)


def gen_quick_choice(row):
    category = row[col_idx['Category']]
    best = row[col_idx['Best for']]
    not_for = row[col_idx['Not for']]
    inputs = row[col_idx['Inputs']]
    dtype = row[col_idx['Type']].lower()
    source = row[col_idx['Source']].lower()
    deployable = row[col_idx['Deployable']]

    best_clean = clean_best(best, category)
    is_reference = dtype in {'reference', 'template'} or category.lower() in {'curated', 'reference'} or source == 'curated'

    ok = []
    no = []
    if is_reference:
        ok = [
            f"- ✅ Используй если: нужна подборка/справочник по теме {category}",
            f"- ✅ Используй если: хочешь быстро найти решения под {best_clean}",
        ]
        no = [
            "- ❌ Не используй если: нужен готовый прод‑сервис (это список, а не продукт)",
            "- ❌ Не используй если: нужен один конкретный инструмент без выбора",
        ]
    else:
        ok = [
            f"- ✅ Используй если: нужен инструмент категории {category}",
            f"- ✅ Используй если: решаешь задачу '{best_clean}'",
        ]
        if inputs and inputs.lower() != 'none':
            ok.append(f"- ✅ Используй если: есть доступ к {inputs}")
        if deployable == 'yes':
            ok.append("- ✅ Используй если: нужен разворачиваемый сервис/приложение")
        no = []
        if not is_generic(not_for):
            no.append(f"- ❌ Не используй если: {not_for}")
        if inputs and inputs.lower() != 'none':
            no.append(f"- ❌ Не используй если: нет доступа к {inputs}")
        no.append("- ❌ Не используй если: нужен другой стек или узкая ниша")

    # keep 2–3 each
    ok = ok[:3]
    no = no[:3]
    return "\n".join(ok + no)


def gen_examples(row, existing_lines):
    category = row[col_idx['Category']]
    best = row[col_idx['Best for']]
    inputs = row[col_idx['Inputs']]
    best_clean = clean_best(best, category)

    lines_out = [l for l in existing_lines if l.strip().startswith('- ')]
    # dedupe
    seen = set()
    uniq = []
    for l in lines_out:
        if l not in seen:
            seen.add(l)
            uniq.append(l)
    lines_out = uniq

    candidates = []
    if not is_generic(best):
        candidates.append(f"- {best_clean}")
    candidates.append(f"- Быстрый прототип/интеграция под {category}")
    if inputs and inputs.lower() != 'none':
        if 'api key' in inputs.lower():
            candidates.append("- Интеграция с внешним API через ключ")
        if 'wallet' in inputs.lower():
            candidates.append("- Работа с кошельком/транзакциями для тестового сценария")
        if 'browser' in inputs.lower():
            candidates.append("- Браузерная автоматизация/скрейпинг")
        if 'db' in inputs.lower():
            candidates.append("- Сбор и хранение данных в БД")
        if 'gpu' in inputs.lower():
            candidates.append("- GPU‑задачи/ускорение моделей")

    for c in candidates:
        if len(lines_out) >= 3:
            break
        if c not in lines_out:
            lines_out.append(c)

    return "\n".join(lines_out)


def build_fit_block(row, existing_block: str) -> str:
    maturity = row[col_idx['Maturity']]
    latency = row[col_idx['Latency/Cost']]
    fit = clean_best(row[col_idx['Best for']], row[col_idx['Category']])
    inputs = row[col_idx['Inputs']]

    def find_line(label):
        m = re.search(rf'^- \*\*{label}:\*\*\s*(.*)$', existing_block, flags=re.M)
        return m.group(1).strip() if m else None

    data_constraints = find_line('Data constraints')
    ops = find_line('Ops friction')
    if not data_constraints:
        data_constraints = inputs if inputs and inputs.lower() != 'none' else 'none'
    if not ops:
        ops = 'low' if inputs.lower() == 'none' else 'medium'

    return "\n".join([
        f"- **Fit:** {fit}",
        f"- **Maturity:** {maturity}",
        f"- **Latency/Cost:** {latency}",
        f"- **Data constraints:** {data_constraints}",
        f"- **Ops friction:** {ops}",
    ])


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

# Normalize each section
for name in section_order:
    row = row_for(name)
    if not row:
        continue
    body = section_map[name]

    # Extract TL;DR
    tldr_line = None
    m_tldr = re.search(r'\*\*TL;DR:\*\*[^\n]*', body)
    if m_tldr:
        tldr_line = m_tldr.group(0)

    # Extract blocks by headings
    blocks = {}
    current = None
    buf = []
    for line in body.splitlines():
        if line.startswith('### '):
            if current:
                blocks[current] = "\n".join(buf).strip()
            current = line.strip()
            buf = []
        else:
            if current:
                buf.append(line)
    if current:
        blocks[current] = "\n".join(buf).strip()

    curated_block = blocks.get('### 📚 Содержание (из README)', '')
    curated_titles = []
    if curated_block:
        for line in curated_block.splitlines():
            if line.startswith('#### '):
                title = line.replace('#### ', '').strip()
                if title:
                    curated_titles.append(title)
            if len(curated_titles) >= 4:
                break

    # Build TL;DR
    tldr_new = build_tldr(name, row, curated_titles or None)

    # Blocks
    quick_block = gen_quick_choice(row)

    launch = blocks.get('### 🚀 Запуск', '').strip()
    if not launch:
        launch = row[col_idx['Quickstart']]

    arch = blocks.get('### 🧩 Архитектура', '').strip()
    if not arch:
        arch = "\n".join([
            f"- **Category:** {row[col_idx['Category']]}",
            f"- **Type:** {row[col_idx['Type']]}",
            f"- **Language:** unknown",
            f"- **Inputs:** {row[col_idx['Inputs']]}",
        ])

    examples_block = blocks.get('### 🧪 Примеры задач', '')
    examples_lines = examples_block.splitlines() if examples_block else []
    examples = gen_examples(row, examples_lines)

    limits = blocks.get('### ⚠️ Ограничения', '').strip()
    if not limits:
        limits = "\n".join([
            "- Качество/полнота зависит от исходного README",
            "- Требуются настройки или ключи, если указано в Inputs",
            "- Может быть экспериментальным или нишевым",
        ])

    fit_block = build_fit_block(row, blocks.get('### 🧭 Fit / Maturity / Ops', ''))

    links = blocks.get('### Full links', '').strip()

    # Rebuild
    parts = [tldr_new, "", "### Быстрый выбор", quick_block, "", "### 🚀 Запуск", launch, "", "### 🧩 Архитектура", arch]
    if curated_block:
        parts += ["", "### 📚 Содержание (из README)", curated_block]
    parts += ["", "### 🧪 Примеры задач", examples, "", "### ⚠️ Ограничения", limits, "", "### 🧭 Fit / Maturity / Ops", fit_block, "", "### Full links", links]

    section_map[name] = "\n".join([p for p in parts if p is not None]).strip()

# Rebuild details
new_detail = header + "\n\n"
for name in section_order:
    body = section_map[name].strip()
    new_detail += f"## {name}\n\n{body}\n\n"

text = pre + new_detail
README.write_text(text, encoding='utf-8')
print('sections normalized')
