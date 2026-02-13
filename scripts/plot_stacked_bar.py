from pathlib import Path
import csv


PRIMARY_LABELS = {'aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'}
TEST_CHANGE_LABELS = {'test change 2'}


def normalize(value: str) -> str:
    return ' '.join(value.strip().lower().split())


def load_counts(data_dir: Path):
    csv_paths = {
        path.stem: path
        for path in data_dir.iterdir()
        if path.is_file() and path.suffix.lower() == '.csv'
    }
    ordered_names = sorted(csv_paths, key=str.lower)

    if not ordered_names:
        raise SystemExit(f'No CSV files found in {data_dir}')

    results = []
    for base in ordered_names:
        path = csv_paths[base]
        with path.open('r', newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            primary_label = 0
            test_change2 = 0
            for row in reader:
                value = normalize(row.get('File', ''))
                if value in TEST_CHANGE_LABELS:
                    test_change2 += 1
                elif value in PRIMARY_LABELS:
                    primary_label += 1
        results.append((base, primary_label, test_change2))
    return results


def render_svg(data, out_path: Path):
    width = 900
    height = 520
    margin_left = 90
    margin_right = 40
    margin_top = 70
    margin_bottom = 100

    chart_w = width - margin_left - margin_right
    chart_h = height - margin_top - margin_bottom

    max_total = max(primary + test for _, primary, test in data)
    y_max = max_total

    n = len(data)
    slot_w = chart_w / n
    bar_w = slot_w * 0.55

    def y_scale(value: float) -> float:
        return margin_top + chart_h - (value / y_max) * chart_h

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">')
    lines.append('<style>')
    lines.append('text { font-family: Arial, Helvetica, sans-serif; fill: #222; }')
    lines.append('.title { font-size: 24px; font-weight: 700; }')
    lines.append('.subtitle { font-size: 14px; fill: #555; }')
    lines.append('.axis-label { font-size: 14px; font-weight: 600; }')
    lines.append('.tick { font-size: 12px; fill: #555; }')
    lines.append('.legend { font-size: 13px; }')
    lines.append('</style>')

    lines.append(f'<text class="title" x="{width/2}" y="36" text-anchor="middle">Rows per CSV (Stacked)</text>')
    lines.append(f'<text class="subtitle" x="{width/2}" y="58" text-anchor="middle">Primary label rows + test change2 rows</text>')

    ticks = [0, 3, 6, 9, 12]
    for t in ticks:
        y = y_scale(t)
        lines.append(f'<line x1="{margin_left}" y1="{y:.2f}" x2="{width-margin_right}" y2="{y:.2f}" stroke="#e5e7eb" stroke-width="1" />')
        lines.append(f'<text class="tick" x="{margin_left-10}" y="{y+4:.2f}" text-anchor="end">{t}</text>')

    x_axis_y = margin_top + chart_h
    lines.append(f'<line x1="{margin_left}" y1="{x_axis_y}" x2="{width-margin_right}" y2="{x_axis_y}" stroke="#333" stroke-width="1.5" />')
    lines.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{x_axis_y}" stroke="#333" stroke-width="1.5" />')

    primary_color = '#4f46e5'
    test_color = '#f97316'

    for idx, (name, primary, test) in enumerate(data):
        x_center = margin_left + (idx + 0.5) * slot_w
        x = x_center - bar_w / 2

        primary_top = y_scale(primary)
        primary_h = x_axis_y - primary_top
        lines.append(f'<rect x="{x:.2f}" y="{primary_top:.2f}" width="{bar_w:.2f}" height="{primary_h:.2f}" fill="{primary_color}" />')

        test_top = y_scale(primary + test)
        test_h = primary_top - test_top
        lines.append(f'<rect x="{x:.2f}" y="{test_top:.2f}" width="{bar_w:.2f}" height="{test_h:.2f}" fill="{test_color}" />')

        lines.append(f'<text class="tick" x="{x_center:.2f}" y="{x_axis_y+22}" text-anchor="middle">{name}</text>')
        lines.append(f'<text class="tick" x="{x_center:.2f}" y="{test_top-8:.2f}" text-anchor="middle">{primary+test}</text>')

    lines.append(f'<text class="axis-label" x="{width/2}" y="{height-40}" text-anchor="middle">CSV file</text>')
    lines.append(f'<text class="axis-label" transform="translate(25 {height/2}) rotate(-90)" text-anchor="middle">Row count</text>')

    legend_x = width - 250
    legend_y = 20
    lines.append(f'<rect x="{legend_x}" y="{legend_y}" width="14" height="14" fill="{primary_color}" />')
    lines.append(f'<text class="legend" x="{legend_x+22}" y="{legend_y+12}">Primary label rows (aaa/bbb/ccc/ddd/eee/fff)</text>')
    lines.append(f'<rect x="{legend_x}" y="{legend_y+22}" width="14" height="14" fill="{test_color}" />')
    lines.append(f'<text class="legend" x="{legend_x+22}" y="{legend_y+34}">test change2 rows</text>')

    lines.append('</svg>')

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text('\n'.join(lines), encoding='utf-8')


def main():
    repo_root = Path(__file__).resolve().parents[1]
    data_dir = repo_root / 'data'
    out_path = repo_root / 'charts' / 'stacked_bar.svg'

    data = load_counts(data_dir)
    render_svg(data, out_path)

    print(f'Wrote stacked bar chart to {out_path}')


if __name__ == '__main__':
    main()
