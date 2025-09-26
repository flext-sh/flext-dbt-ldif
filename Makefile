# ============================================================================
# FLEXT-DBT-LDIF MAKEFILE
# dbt 1.7+ | LDIF Exchange | Python 3.13
# ============================================================================

PROJECT_NAME := flext-dbt-ldif
PYTHON_VERSION := 3.13
POETRY := poetry
SRC_DIR := src
TESTS_DIR := tests
MIN_COVERAGE := 100
DBT_PROFILES_DIR := profiles
DBT_TARGET := dev

# ============================================================================
# HELP
# ============================================================================

.DEFAULT_GOAL := help

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ============================================================================
# INSTALLATION
# ============================================================================

install: ## Install dependencies
	$(POETRY) install

setup: ## Complete development setup
	$(POETRY) install --with dev,test,docs
	mkdir -p $(DBT_PROFILES_DIR) logs target dbt_packages
	$(POETRY) run pre-commit install

# ============================================================================
# QUALITY GATES
# ============================================================================

validate: lint type-check security test dbt-test ## Run all quality gates

check: lint type-check dbt-compile ## Quick health check

lint: ## Run linting (ZERO TOLERANCE)
	$(POETRY) run ruff check .

format: ## Format code
	$(POETRY) run ruff format .

type-check: ## Run type checking with Pyrefly (ZERO TOLERANCE)
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pyrefly check .

security: ## Run security scanning
	$(POETRY) run bandit -r $(SRC_DIR)
	$(POETRY) run pip-audit

fix: ## Auto-fix code issues
	$(POETRY) run ruff check . --fix
	$(POETRY) run ruff format .

# ============================================================================
# TESTING (MANDATORY - 100% COVERAGE)
# ============================================================================

test: ## Run tests with 100% coverage (MANDATORY)
	$(POETRY) run pytest $(TESTS_DIR) --cov=$(SRC_DIR) --cov-report=term-missing --cov-fail-under=$(MIN_COVERAGE)

test-unit: ## Run unit tests only
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest -m "not integration" -v

test-integration: ## Run integration tests with Docker only
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest -m integration -v

test-fast: ## Run tests without coverage
	PYTHONPATH=$(SRC_DIR) $(POETRY) run pytest -v

coverage-html: ## Generate HTML coverage report
	$(POETRY) run pytest $(TESTS_DIR) --cov=$(SRC_DIR) --cov-report=html

# ============================================================================
# DBT OPERATIONS
# ============================================================================

dbt-deps: ## Install dbt dependencies
	$(POETRY) run dbt deps --profiles-dir $(DBT_PROFILES_DIR)

dbt-debug: ## Debug dbt configuration
	$(POETRY) run dbt debug --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

dbt-compile: dbt-deps ## Compile dbt models
	$(POETRY) run dbt compile --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

dbt-run: dbt-compile ## Run dbt models
	$(POETRY) run dbt run --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

dbt-test: dbt-compile ## Run dbt tests
	$(POETRY) run dbt test --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

dbt-docs: dbt-compile ## Generate dbt documentation
	$(POETRY) run dbt docs generate --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

dbt-seed: dbt-deps ## Load seed data
	$(POETRY) run dbt seed --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

dbt-snapshot: dbt-deps ## Run snapshots
	$(POETRY) run dbt snapshot --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

dbt-clean: ## Clean dbt artifacts
	$(POETRY) run dbt clean --profiles-dir $(DBT_PROFILES_DIR)
	rm -rf logs/dbt.log

# ============================================================================
# LDIF-SPECIFIC OPERATIONS
# ============================================================================

ldif-validate: dbt-compile ## Validate LDIF data integrity
	$(POETRY) run dbt test --models tag:data_quality --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

ldif-staging: dbt-run ## Run LDIF staging models
	$(POETRY) run dbt run --models tag:staging --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

ldif-marts: dbt-run ## Run LDIF marts models
	$(POETRY) run dbt run --models tag:marts --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

ldif-analytics: dbt-run ## Run LDIF analytics models
	$(POETRY) run dbt run --models tag:analytics --profiles-dir $(DBT_PROFILES_DIR) --target $(DBT_TARGET)

generate-models: ## Generate dbt models programmatically
	PYTHONPATH=$(SRC_DIR) $(POETRY) run python -m flext_dbt_ldif.generate_models

# ============================================================================
# BUILD & DOCS
# ============================================================================

build: dbt-compile ## Build package
	$(POETRY) build

docs: dbt-docs ## Build all documentation
	$(POETRY) run mkdocs build

docs-serve: ## Serve documentation locally
	$(POETRY) run mkdocs serve

# ============================================================================
# DEPENDENCIES
# ============================================================================

deps-update: ## Update all dependencies
	$(POETRY) update
	$(POETRY) run dbt deps --profiles-dir $(DBT_PROFILES_DIR)

deps-audit: ## Security audit dependencies
	$(POETRY) run pip-audit

# ============================================================================
# MAINTENANCE
# ============================================================================

clean: ## Clean build artifacts
	rm -rf build/ dist/ *.egg-info/ .pytest_cache/ htmlcov/ .coverage .mypy_cache/ .pyrefly_cache/ .ruff_cache/
	rm -rf target/ dbt_packages/ logs/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

clean-all: clean ## Deep clean including venv
	rm -rf .venv/

reset: clean-all setup ## Complete project reset

# ============================================================================
# DIAGNOSTICS
# ============================================================================

diagnose: ## Show environment diagnostics
	@echo "Python: $$(python --version)"
	@echo "Poetry: $$($(POETRY) --version)"
	@echo "DBT: $$($(POETRY) run dbt --version)"
	@$(POETRY) env info

doctor: diagnose check ## Full health check

# ============================================================================

# ============================================================================

t: test
l: lint
f: format
tc: type-check
c: clean
i: install
v: validate
dr: dbt-run
dt: dbt-test
dc: dbt-compile
gm: generate-models
ls: ldif-staging
lm: ldif-marts
la: ldif-analytics
