.PHONY: help regenerate-stacked-bar regenerate-stacked-bar-commit

help:
	@echo "Available targets:"
	@echo "  make regenerate-stacked-bar         # Regenerate charts/stacked_bar.svg"
	@echo "  make regenerate-stacked-bar-commit  # Regenerate and commit charts/stacked_bar.svg if changed"

regenerate-stacked-bar:
	python scripts/plot_stacked_bar.py

regenerate-stacked-bar-commit: regenerate-stacked-bar
	git add charts/stacked_bar.svg
	@if git diff --cached --quiet; then \
		echo "No chart changes to commit."; \
	else \
		git commit -m "Regenerate stacked bar chart"; \
	fi
