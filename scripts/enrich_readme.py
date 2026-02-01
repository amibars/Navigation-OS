import re
from pathlib import Path

path = Path('README.md')
text = path.read_text(encoding='utf-8')

# Parse catalog table
lines = text.splitlines()
header_idx = next((i for i,l in enumerate(lines) if l.startswith('| # | Repo |')), None)
if header_idx is None:
    raise SystemExit('Catalog table header not found')
end_idx = next((i for i in range(header_idx+1, len(lines)) if lines[i].startswith('## ')), len(lines))
columns = [c.strip() for c in lines[header_idx].strip().strip('|').split('|')]
col_idx = {c: i for i,c in enumerate(columns)}
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


def sentence_count(text: str) -> int:
    parts = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    return len(parts)


def clean_best(best: str, category: str) -> str:
    if is_generic(best):
        return f"{category.lower()}‑задачи"
    return best.strip()


def build_tldr(name: str, row) -> str:
    category = row[col_idx['Category']]
    best = row[col_idx['Best for']]
    not_for = row[col_idx['Not for']]
    inputs = row[col_idx['Inputs']]
    dtype = row[col_idx['Type']]
    source = row[col_idx['Source']]
    maturity = row[col_idx['Maturity']]
    latency = row[col_idx['Latency/Cost']]

    best_clean = clean_best(best, category)
    not_for_clean = None if is_generic(not_for) else not_for

    is_reference = dtype in {'reference', 'template'} or category.lower() in {'curated', 'reference'} or source == 'curated'

    sentences = []
    if is_reference:
        sentences.append(f"{name} — curated‑каталог/справочник по теме {category.lower()} и смежным инструментам.")
        sentences.append("Полезен, когда нужно быстро понять, какие решения существуют и что выбрать под задачу.")
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

    target_min = 5 if is_reference else 4
    while len(sentences) > 6:
        sentences.pop(-2)
    if len(sentences) < target_min:
        sentences.append("Если нужно быстро понять, что это и зачем — это хороший стартовый ориентир.")
    return "**TL;DR:** " + " ".join(sentences)


def gen_quick_choice(name: str, row, existing_lines):
    category = row[col_idx['Category']]
    best = row[col_idx['Best for']]
    not_for = row[col_idx['Not for']]
    inputs = row[col_idx['Inputs']]
    dtype = row[col_idx['Type']]
    source = row[col_idx['Source']]
    deployable = row[col_idx['Deployable']]

    lines_out = existing_lines[:]

    ok_count = sum(1 for l in lines_out if '✅' in l)
    no_count = sum(1 for l in lines_out if '❌' in l)

    candidates_ok = []
    candidates_no = []

    best_clean = clean_best(best, category)
    is_reference = dtype in {'reference', 'template'} or category.lower() in {'curated', 'reference'} or source == 'curated'

    if is_reference:
        candidates_ok.append(f"- ✅ Используй если: нужна подборка/справочник по теме {category}")
        candidates_ok.append(f"- ✅ Используй если: хочешь быстро найти решения под {best_clean}")
        candidates_no.append("- ❌ Не используй если: нужен готовый прод‑сервис (это список, а не продукт)")
    else:
        candidates_ok.append(f"- ✅ Используй если: нужен инструмент категории {category}")
        if not is_generic(best):
            candidates_ok.append(f"- ✅ Используй если: решаешь задачу '{best_clean}'")
        if inputs and inputs.lower() != 'none':
            candidates_ok.append(f"- ✅ Используй если: есть доступ к {inputs}")
        if deployable == 'yes':
            candidates_ok.append("- ✅ Используй если: нужен разворачиваемый сервис/приложение")
        if not is_generic(not_for):
            candidates_no.append(f"- ❌ Не используй если: {not_for}")
        if inputs and inputs.lower() != 'none':
            candidates_no.append(f"- ❌ Не используй если: нет доступа к {inputs}")
        candidates_no.append("- ❌ Не используй если: нужен другой стек или узкая ниша")

    while ok_count < 2 and candidates_ok:
        lines_out.append(candidates_ok.pop(0))
        ok_count += 1
    while no_count < 2 and candidates_no:
        lines_out.append(candidates_no.pop(0))
        no_count += 1

    return lines_out


def gen_examples(row, existing_lines):
    category = row[col_idx['Category']]
    best = row[col_idx['Best for']]
    inputs = row[col_idx['Inputs']]
    best_clean = clean_best(best, category)

    lines_out = existing_lines[:]
    count = sum(1 for l in lines_out if l.strip().startswith('- '))

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

    while count < 3 and candidates:
        item = candidates.pop(0)
        if item not in lines_out:
            lines_out.append(item)
            count += 1

    return lines_out


# Parse Detailed Descriptions
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

for name in section_order:
    row = row_for(name)
    if not row:
        continue
    body = section_map[name]

    # TL;DR
    tldr_match = re.search(r'\*\*TL;DR:\*\*[^\n]*', body)
    if tldr_match:
        existing = tldr_match.group(0).replace('**TL;DR:**', '').strip()
        min_sent = 5 if row[col_idx['Type']] in {'reference', 'template'} or row[col_idx['Source']] == 'curated' else 4
        if sentence_count(existing) < min_sent or 'repository' in existing.lower() or 'подходит для задач категории' in existing.lower() or '?' in existing:
            new_tldr = build_tldr(name, row)
            body = body.replace(tldr_match.group(0), new_tldr)

    # Быстрый выбор
    lines_body = body.splitlines()
    try:
        idx = lines_body.index('### Быстрый выбор')
    except ValueError:
        idx = None
    if idx is not None:
        end = idx + 1
        while end < len(lines_body) and not lines_body[end].startswith('### ') and not lines_body[end].startswith('## '):
            end += 1
        block = lines_body[idx+1:end]
        new_block = gen_quick_choice(name, row, block)
        lines_body = lines_body[:idx+1] + new_block + lines_body[end:]

    # Примеры задач
    try:
        idx = lines_body.index('### 🧪 Примеры задач')
    except ValueError:
        idx = None
    if idx is not None:
        end = idx + 1
        while end < len(lines_body) and not lines_body[end].startswith('### ') and not lines_body[end].startswith('## '):
            end += 1
        block = lines_body[idx+1:end]
        new_block = gen_examples(row, block)
        lines_body = lines_body[:idx+1] + new_block + lines_body[end:]

    section_map[name] = '\n'.join(lines_body).rstrip()

new_detail = header + '\n\n'
for name in section_order:
    body = section_map[name].strip()
    new_detail += f'## {name}\n\n{body}\n\n'

text = pre + new_detail
path.write_text(text, encoding='utf-8')
print('TL;DR/quick choice/examples enriched (utf8)')
