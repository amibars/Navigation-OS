import argparse
import datetime as _dt
import re
import sys
from collections import Counter
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

REQUIRED_DETAIL = [
    '**TL;DR:**',
    H_QUICK,
    H_START,
    H_ARCH,
    H_EX,
    H_LIMITS,
    H_FIT,
    '### Full links',
]

PLACEHOLDER_QUICK = {'todo', '—', '-', 'see readme', 'reference'}
PLACEHOLDER_INPUTS = {'—', '?', ''}


def _read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8', errors='replace')


def _find_table(text: str):
    lines = text.splitlines()
    header_idx = None
    for i, line in enumerate(lines):
        if re.match(r'^\| # \| Repo \|', line):
            header_idx = i
            break
    if header_idx is None:
        return None, None, []

    header_line = lines[header_idx]
    columns = [c.strip() for c in header_line.strip().strip('|').split('|')]
    rows = []
    for line in lines[header_idx + 2:]:
        if line.startswith('## '):
            break
        if re.match(r'^\|\s*\d+\s*\|', line):
            rows.append(line)
    return columns, header_idx, rows


def _parse_rows(columns, rows):
    parsed = []
    for line in rows:
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) != len(columns):
            continue
        parsed.append(cells)
    return parsed


def _build_report(readme_text: str):
    columns, header_idx, row_lines = _find_table(readme_text)

    report = {}
    report['catalog_header_found'] = columns is not None
    report['columns'] = columns or []

    parsed_rows = _parse_rows(columns, row_lines) if columns else []
    report['row_count'] = len(parsed_rows)

    if columns:
        col_map = {c.lower(): i for i, c in enumerate(columns)}
        quick_idx = col_map.get('quickstart')
        inputs_idx = col_map.get('inputs')
        notfor_idx = col_map.get('not for')
        repo_idx = col_map.get('repo')
        type_idx = col_map.get('type')

        quick_placeholders = 0
        inputs_placeholders = 0
        generic_notfor = 0
        anchors = []

        for row in parsed_rows:
            dtype = row[type_idx].strip().lower() if type_idx is not None else ''
            is_reference = dtype in {'reference', 'template'}
            if quick_idx is not None and not is_reference:
                quick = row[quick_idx].strip().lower()
                if quick in PLACEHOLDER_QUICK or re.search(r'\btodo\b', quick, re.I):
                    quick_placeholders += 1
            if inputs_idx is not None and not is_reference:
                inputs = row[inputs_idx].strip()
                if inputs in PLACEHOLDER_INPUTS:
                    inputs_placeholders += 1
            if notfor_idx is not None:
                notfor = row[notfor_idx]
                if re.search(r'Other stacks / needs review', notfor, re.I):
                    generic_notfor += 1
            if repo_idx is not None:
                repo_cell = row[repo_idx]
                m = re.search(r'\((#[^)]+)\)', repo_cell)
                key = (m.group(1).lower() if m else repo_cell.lower())
                anchors.append(key)

        report['quick_placeholders'] = quick_placeholders
        report['inputs_placeholders'] = inputs_placeholders
        report['generic_notfor'] = generic_notfor
        dupes = {k: v for k, v in Counter(anchors).items() if v > 1}
        report['duplicate_count'] = len(dupes)
        report['duplicate_top'] = sorted(dupes.items(), key=lambda kv: (-kv[1], kv[0]))[:8]
    else:
        report['quick_placeholders'] = None
        report['inputs_placeholders'] = None
        report['generic_notfor'] = None
        report['duplicate_count'] = None
        report['duplicate_top'] = []

    # Details validation
    missing_sections = []
    short_tldr = []
    total_sections = 0

    if H_DETAILS in readme_text:
        detail_part = readme_text.split(H_DETAILS, 1)[1]
        sections = re.split(r'(?m)^## ', detail_part)
        for sec in sections[1:]:
            lines = sec.splitlines()
            name = lines[0].strip() if lines else '<unknown>'
            body = '\n'.join(lines[1:])
            total_sections += 1
            missing = [r for r in REQUIRED_DETAIL if r not in body]
            if H_FIT in missing and H_FIT_ALT in body:
                missing = [r for r in missing if r != H_FIT]
            if missing:
                missing_sections.append(name)
            tldr_match = re.search(r'\*\*TL;DR:\*\*([^\n]+)', body)
            if tldr_match:
                tldr = tldr_match.group(1).strip()
                sentences = [s for s in re.split(r'[.!?]+', tldr) if s.strip()]
                if len(sentences) < 3:
                    short_tldr.append(name)

    report['detail_sections'] = total_sections
    report['detail_missing_count'] = len(missing_sections)
    report['detail_missing_sample'] = missing_sections[:15]
    report['tldr_short_count'] = len(short_tldr)
    report['tldr_short_sample'] = short_tldr[:15]

    # Legend / definitions presence
    legend_present = bool(re.search(r'\bLegend\b|\bDefinitions\b|\bMaturity\b|\u041b\u0435\u0433\u0435\u043d\u0434\u0430|\u041e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u044f', readme_text))
    report['legend_present'] = legend_present

    return report


def _render_entry(report: dict, readme_path: Path):
    today = _dt.date.today().isoformat()
    lines = []
    lines.append(f'## {today}')

    size_bytes = readme_path.stat().st_size if readme_path.exists() else 0
    lines.append(f'- Snapshot: README size {size_bytes} bytes; catalog rows {report.get("row_count", 0)}; detail sections {report.get("detail_sections", 0)}.')

    if not report.get('catalog_header_found'):
        lines.append('- Catalog table: header not found (parser failed to locate the table).')
    else:
        cols = ', '.join(report.get('columns', []))
        lines.append(f'- Catalog table: columns = {cols}.')

    missing_cols = []
    for col in ('Source', 'Type', 'Deployable'):
        if col not in report.get('columns', []):
            missing_cols.append(col)
    if missing_cols:
        lines.append(f'- Missing columns vs TASKS model: {", ".join(missing_cols)}.')

    qp = report.get('quick_placeholders')
    ip = report.get('inputs_placeholders')
    if qp is not None and ip is not None:
        total = report.get('row_count', 0) or 1
        lines.append(f'- Coverage: Quickstart placeholders {qp} ({qp/total:.1%}); Inputs placeholders {ip} ({ip/total:.1%}).')

    if report.get('detail_sections'):
        lines.append(f'- Details: sections missing required blocks {report.get("detail_missing_count", 0)}; TL;DR too short {report.get("tldr_short_count", 0)}.')

    if report.get('duplicate_count') is not None:
        if report.get('duplicate_count'):
            top_dupes = ', '.join([f'{k} x{v}' for k, v in report.get('duplicate_top', [])])
            lines.append(f'- Duplicates: {report.get("duplicate_count")} anchors repeated. Top: {top_dupes}.')
        else:
            lines.append('- Duplicates: none detected by anchor.')

    if not report.get('legend_present'):
        lines.append('- Legend/definitions block not detected (Maturity/Latency/Inputs/Ops).')

    if report.get('detail_missing_sample'):
        sample = ', '.join(report.get('detail_missing_sample'))
        lines.append(f'- Missing detail blocks (sample): {sample}.')
    if report.get('tldr_short_sample'):
        sample = ', '.join(report.get('tldr_short_sample'))
        lines.append(f'- TL;DR <3 sentences (sample): {sample}.')

    return '\n'.join(lines)


def _append_report(report_path: Path, entry: str):
    header = '# REPORT — README/TASKS changes\n\n'
    if report_path.exists():
        existing = report_path.read_text(encoding='utf-8', errors='replace')
        if not existing.strip():
            content = header + entry + '\n'
        else:
            prefix = '' if existing.endswith('\n') else '\n'
            content = existing + prefix + entry + '\n'
    else:
        content = header + entry + '\n'
    report_path.write_text(content, encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Generate README/TASKS report entry.')
    parser.add_argument('--readme', default='README.md')
    parser.add_argument('--report', default='REPORT.md')
    parser.add_argument('--print-only', action='store_true')
    args = parser.parse_args()

    readme_path = Path(args.readme)
    if not readme_path.exists():
        print(f'Readme not found: {readme_path}', file=sys.stderr)
        return 1

    readme_text = _read_text(readme_path)
    report = _build_report(readme_text)
    entry = _render_entry(report, readme_path)

    if args.print_only:
        print(entry)
    else:
        _append_report(Path(args.report), entry)
        print(f'Report appended to {args.report}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
