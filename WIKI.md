# Program Wiki — Landing Page

Welcome to the **test-excel-pipeline** wiki. This page is the central starting point for understanding what the program does, how to run it, and where to look next.

## Program at a glance

**Purpose:**
- Build a repeatable data-visualization pipeline from CSV files.
- Generate a stacked bar chart that summarizes row counts by category.
- Optionally package the chart into a PowerPoint slide.

**Primary workflow:**
1. Read every `.csv` file in `data/`.
2. Count rows by primary labels (`aaa`, `bbb`, `ccc`, `ddd`, `eee`, `fff`) and `test change2` rows.
3. Render a stacked bar chart ordered alphabetically by filename.
4. Output the chart to `charts/stacked_bar.svg`.
5. (Optional) Create `charts/stacked_bar.pptx` containing the chart.

## Repository layout

- `scripts/build_main.py` — data build/helper script.
- `scripts/plot_stacked_bar.py` — chart generation script.
- `scripts/create_stacked_bar_ppt.py` — PowerPoint generation script.
- `data/` — source CSV files for chart input.
- `charts/` — generated visual artifacts (SVG committed; PPTX local only).
- `main.csv` — primary CSV artifact in repository root.
- `Makefile` — repeatable commands for pipeline tasks.

## Quick start

From the repository root:

```bash
make help
make regenerate-stacked-bar
```

Or run scripts directly:

```bash
python scripts/plot_stacked_bar.py
python scripts/create_stacked_bar_ppt.py
```

## Key outputs

- `charts/stacked_bar.svg` (version-controlled)
- `charts/stacked_bar.pptx` (generated locally; gitignored)

## Operational notes

- CSV discovery is automatic for files in `data/` with case-insensitive `.csv` extension.
- The chart includes all discovered CSV files and sorts them alphabetically.
- Use `make regenerate-stacked-bar-commit` when you want to regenerate and auto-commit the SVG if it changes.

## Typical use cases

- **Data quality check:** Compare category distributions across many CSV inputs.
- **Reporting:** Embed the chart in a slide deck for review.
- **Repeatable automation:** Use `make` targets for consistent local or CI runs.

## Where to start next

- Read `README.md` for concise usage details.
- Run `make help` to see available commands.
- Inspect `scripts/plot_stacked_bar.py` to customize chart behavior.
