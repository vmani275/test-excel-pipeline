# test-excel-pipeline

## Generate stacked bar chart

Run:

```bash
python scripts/plot_stacked_bar.py
```

This writes `charts/stacked_bar.svg`, a stacked bar chart showing row counts per CSV split by primary label rows (`aaa`/`bbb`/`ccc`/`ddd`/`eee`/`fff`) and `test change2` rows. It automatically includes all CSV files in `data/` (case-insensitive `.csv` extension) and plots them alphabetically by filename.



Repeatable commands (run from the repository root):

```bash
make help
make regenerate-stacked-bar
```

To regenerate and auto-commit the SVG when it changed:

```bash
make regenerate-stacked-bar-commit
```

To also generate a PowerPoint slide containing this chart:

```bash
python scripts/create_stacked_bar_ppt.py
```

This writes `charts/stacked_bar.pptx` locally (it is gitignored to avoid binary-file PR issues).
