.PHONY: clean
clean:
	@find . -type f -name "*.py[co]" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
	@find . -type d -name ".pytest_cache" -exec rm -rf {} +

.PHONY: format_black
format_black:
	@black .

.PHONY: format_prettier
format_prettier:
	@npx prettier --write .

.PHONY: format
format: format_prettier format_black clean

.PHONY: lint_black
lint_black:
	@black --check .

.PHONY: lint_pylint
lint_pylint:
	@pylint contribution_graph_plotter

.PHONY: lint_prettier
lint_prettier:
	@npx prettier --check .

.PHONY: lint
lint: lint_prettier lint_black lint_pylint clean

example:
	@jupytext notebooks/example.ipynb --output notebooks/example.py
