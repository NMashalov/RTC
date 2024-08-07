PROJECT_DIR='rtc/'

.PHONY: install
format:
	@poetry install

.PHONY: format
format:
	@ruff format $(PROJECT_DIR)