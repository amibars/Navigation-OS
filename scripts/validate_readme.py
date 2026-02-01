import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

H_CATALOG = '## ' + '\U0001F4CB' + ' Catalog Table'
H_DETAILS = '## ' + '\U0001F4D6' + ' Detailed Descriptions'
H_QUICK = '### ' + '\u0411\u044b\u0441\u0442\u0440\u044b\u0439 \u0432\u044b\u0431\u043e\u0440'
H_START = '### ' + '\U0001F680' + ' ' + '\u0417\u0430\u043f\u0443\u0441\u043a'
H_ARCH = '### ' + '\U0001F9E9' + ' ' + '\u0410\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u0430'
H_EX = '### ' + '\U0001F9EA' + ' ' + '\u041f\u0440\u0438\u043c\u0435\u0440\u044b \u0437\u0430\u0434\u0430\u0447'
H_LIMITS = '### ' + '\u26A0\uFE0F' + ' ' + '\u041e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u044f'
H_FIT = '### ' + '\U0001F9ED' + ' Fit / Maturity / Ops'
H_FIT_ALT = '### ' + '\U0001F9ED' + ' Fit/Maturity/Ops'

readme = Path('README.md')
text = readme.read_text(encoding='utf-8')

errors = []
warnings = []

if re.search(r'\?{4,}', text):
    errors.append('Found "????" sequences (likely encoding corruption) in README.')
if re.search(r'^### \?+', text, re.M):
    errors.append('Found corrupted section headings ("### ??") in README.')

if H_CATALOG not in text:
    errors.append(f'Missing catalog heading: {H_CATALOG}')
if H_DETAILS not in text:
    errors.append(f'Missing details heading: {H_DETAILS}')

required = [
    '**TL;DR:**',
    H_QUICK,
    H_START,
    H_ARCH,
    H_EX,
    H_LIMITS,
    H_FIT,
    '### Full links',
]

EM_DASH = '\u2014'

# Validate catalog table
table_match = re.search(r'^\| # \| Repo \|', text, re.M)
if not table_match:
    errors.append('Catalog table header not found.')
else:
    lines = text.splitlines()
    start_line = 0
    for i, line in enumerate(lines):
        if re.match(r'^\| # \| Repo \|', line):
            start_line = i
            break

    header_line = lines[start_line]
    columns = [c.strip() for c in header_line.strip().strip('|').split('|')]
    required_cols = {
        '#', 'Repo', 'Category', 'Best for', 'Not for', 'Quickstart',
        'Maturity', 'Latency/Cost', 'Inputs', 'Source', 'Type', 'Deployable'
    }
    missing_cols = [c for c in required_cols if c not in columns]
    if missing_cols:
        errors.append(f'Catalog table missing columns: {", ".join(sorted(missing_cols))}')

    rows = []
    for line in lines[start_line + 1:]:
        if line.startswith('## '):
            break
        if re.match(r'^\|\s*\d+\s*\|', line):
            rows.append(line)
    if not rows:
        errors.append('Catalog table rows not found.')
    else:
        allowed_maturity = {
            'active', 'maintained', 'experimental', 'stale', 'curated', 'deprecated',
            'unknown', 'demo', 'early', 'educational', 'design-doc',
            'skeleton', 'empty'
        }
        allowed_latency = {'fast', 'balanced', 'quality', 'medium'}
        allowed_source = {'owned', 'forked', 'starred', 'curated', 'unknown'}
        allowed_type = {'app', 'service', 'cli', 'sdk', 'reference', 'template', 'unknown'}
        allowed_deployable = {'yes', 'no', 'unknown'}
        col_idx = {c: i for i, c in enumerate(columns)}

        bad_quickstart = []
        bad_inputs = []
        bad_notfor = []
        bad_maturity = []
        bad_latency = []
        bad_source = []
        bad_type = []
        bad_deployable = []
        for row in rows:
            parts = [p.strip() for p in row.strip().strip('|').split('|')]
            if len(parts) != len(columns):
                continue
            quick = parts[col_idx['Quickstart']]
            maturity = parts[col_idx['Maturity']].lower()
            latency = parts[col_idx['Latency/Cost']].lower()
            inputs = parts[col_idx['Inputs']]
            notfor = parts[col_idx['Not for']]
            source = parts[col_idx['Source']].lower()
            dtype = parts[col_idx['Type']].lower()
            deployable = parts[col_idx['Deployable']].lower()
            repo_cell = parts[col_idx['Repo']]

            is_reference = dtype in {'reference', 'template'}
            if not is_reference:
                if re.search(r'\bTODO\b', quick, re.I) or quick in {EM_DASH, '-', 'see README', 'reference'}:
                    bad_quickstart.append(repo_cell)
                if inputs in {EM_DASH, '?', ''}:
                    bad_inputs.append(repo_cell)
            if re.search(r'Other stacks / needs review', notfor, re.I):
                bad_notfor.append(repo_cell)
            if maturity not in allowed_maturity:
                bad_maturity.append(f'{repo_cell} ({parts[col_idx["Maturity"]]})')
            if latency not in allowed_latency:
                bad_latency.append(f'{repo_cell} ({parts[col_idx["Latency/Cost"]]})')
            if source not in allowed_source:
                bad_source.append(f'{repo_cell} ({parts[col_idx["Source"]]})')
            if dtype not in allowed_type:
                bad_type.append(f'{repo_cell} ({parts[col_idx["Type"]]})')
            if deployable not in allowed_deployable:
                bad_deployable.append(f'{repo_cell} ({parts[col_idx["Deployable"]]})')

        if bad_quickstart:
            errors.append(f'Quickstart placeholders found in {len(bad_quickstart)} rows.')
        if bad_inputs:
            errors.append(f'Inputs missing/unknown in {len(bad_inputs)} rows.')
        if bad_notfor:
            errors.append(f'Generic "Not for" in {len(bad_notfor)} rows.')
        if bad_maturity:
            warnings.append(f'Nonstandard Maturity values in {len(bad_maturity)} rows.')
        if bad_latency:
            warnings.append(f'Nonstandard Latency/Cost values in {len(bad_latency)} rows.')
        if bad_source:
            warnings.append(f'Nonstandard Source values in {len(bad_source)} rows.')
        if bad_type:
            warnings.append(f'Nonstandard Type values in {len(bad_type)} rows.')
        if bad_deployable:
            warnings.append(f'Nonstandard Deployable values in {len(bad_deployable)} rows.')

# Validate detailed descriptions inside README
if H_DETAILS in text:
    detail_part = text.split(H_DETAILS, 1)[1]
    sections = re.split(r'(?m)^## ', detail_part)
    for sec in sections[1:]:
        name = sec.splitlines()[0].strip() if sec.splitlines() else '<unknown>'
        body = '\n'.join(sec.splitlines()[1:])
        missing = [r for r in required if r not in body]
        # allow alternate Fit heading
        if H_FIT in missing and H_FIT_ALT in body:
            missing = [r for r in missing if r != H_FIT]
        if missing:
            errors.append(f'Section "{name}" missing: {", ".join(missing)}')
        # TL;DR sentence count (>=3)
        tldr_match = re.search(r'\*\*TL;DR:\*\*([^\n]+)', body)
        if tldr_match:
            tldr = tldr_match.group(1).strip()
            sentences = [s for s in re.split(r'[.!?]+', tldr) if s.strip()]
            if len(sentences) < 3:
                errors.append(f'Section "{name}" TL;DR too short (<3 sentences).')

if errors:
    print('README validation FAILED:')
    for err in errors:
        print(' -', err)
    for warn in warnings:
        print(' !', warn)
    sys.exit(1)

if warnings:
    print('README validation WARNINGS:')
    for warn in warnings:
        print(' !', warn)

print('README validation OK')
