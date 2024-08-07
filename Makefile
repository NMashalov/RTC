PROJECT_DIR=rtc/

.PHONY: install
format:
	@poetry install
	@isort $(PROJECT_DIR)

.PHONY: format
format:
	@ruff format $(PROJECT_DIR)