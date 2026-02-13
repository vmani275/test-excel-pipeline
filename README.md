# test-excel-pipeline

## Generate stacked bar chart

Run:

```bash
python scripts/plot_stacked_bar.py
```

This writes `charts/stacked_bar.svg`, a stacked bar chart showing row counts per CSV split by primary label rows (`aaa`/`bbb`/`ccc`/`ddd`/`eee`/`fff`) and `test change2` rows, using only CSV files in `data/` and plotting file order `one`→`five`.



Repeatable commands:

```bash
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
