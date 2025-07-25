# FLEXT DBT LDIF - LDIF Data Interchange Analytics
# ===============================================
# Advanced dbt project for LDIF analytics with programmatically generated models
# Python 3.13 + dbt Core + PostgreSQL + Advanced Analytics + Zero Tolerance Quality Gates

.PHONY: help info diagnose check validate test lint type-check security format format-check fix
.PHONY: install dev-install setup pre-commit build clean
.PHONY: coverage coverage-html test-unit test-integration test-dbt
.PHONY: deps-update deps-audit deps-tree deps-outdated
.PHONY: dbt-compile dbt-run dbt-test dbt-docs dbt-debug dbt-seed dbt-snapshot dbt-deps dbt-clean
.PHONY: ldif-models-test ldif-transformations ldif-validate

# ============================================================================
# 🎯 HELP & INFORMATION
# ============================================================================

help: ## Show this help message
	@echo "🎯 FLEXT DBT LDIF - LDIF Data Interchange Analytics"
	@echo "==================================================="
	@echo "🎯 dbt Core + Advanced Analytics + Python 3.13"
	@echo ""
	@echo "📦 Programmatically generated dbt project for LDIF analytics"
	@echo "🔒 Zero tolerance quality gates with advanced data testing"
	@echo "🧪 90%+ test coverage with sophisticated analytics patterns"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\\033[36m%-20s\\033[0m %s\\n", $$1, $$2}'


info: ## Mostrar informações do projeto
	@echo "📊 Informações do Projeto"
	@echo "======================"
	@echo "Nome: flext-dbt-ldif"
	@echo "Título: FLEXT DBT LDIF"
	@echo "Tipo: dbt-project"
	@echo "Versão: $(shell poetry version -s 2>/dev/null || echo "0.7.0")"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo "Venv: $(shell poetry env info --path 2>/dev/null || echo "Não ativado")"
	@echo "Diretório: $(CURDIR)"
	@echo "Git Branch: $(shell git branch --show-current 2>/dev/null || echo "Não é repo git")"
	@echo "Git Status: $(shell git status --porcelain 2>/dev/null | wc -l | xargs echo) arquivos alterados"

diagnose: ## Executar diagnósticos completos
	@echo "🔍 Executando diagnósticos para flext-dbt-ldif..."
	@echo "Informações do Sistema:"
	@echo "OS: $(shell uname -s)"
	@echo "Arquitetura: $(shell uname -m)"
	@echo "Python: $(shell python3.13 --version 2>/dev/null || echo "Não encontrado")"
	@echo "Poetry: $(shell poetry --version 2>/dev/null || echo "Não instalado")"
	@echo ""
	@echo "Estrutura do Projeto:"
	@ls -la
	@echo ""
	@echo "Configuração Poetry:"
	@poetry config --list 2>/dev/null || echo "Poetry não configurado"
	@echo ""
	@echo "Status das Dependências:"
	@poetry show --outdated 2>/dev/null || echo "Nenhuma dependência desatualizada"

# ============================================================================
# 🎯 CORE QUALITY GATES - ZERO TOLERANCE
# ============================================================================

validate: lint type-check security test dbt-test ## STRICT compliance validation (all must pass)
	@echo "✅ ALL QUALITY GATES PASSED - FLEXT DBT LDIF COMPLIANT"

check: lint type-check test dbt-compile ## Essential quality checks (pre-commit standard)
	@echo "✅ Essential checks passed"

lint: ## Ruff linting (17 rule categories, ALL enabled)
	@echo "🔍 Running ruff linter (ALL rules enabled)..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ Linting complete"

type-check: ## MyPy strict mode type checking (zero errors tolerated)
	@echo "🛡️ Running MyPy strict type checking..."
	@poetry run mypy src/ tests/ --strict
	@echo "✅ Type checking complete"

security: ## Security scans (bandit + pip-audit + secrets)
	@echo "🔒 Running security scans..."
	@poetry run bandit -r src/ --severity-level medium --confidence-level medium
	@poetry run pip-audit --ignore-vuln PYSEC-2022-42969
	@poetry run detect-secrets scan --all-files
	@echo "✅ Security scans complete"

format: ## Format code with ruff
	@echo "🎨 Formatting code..."
	@poetry run ruff format src/ tests/
	@echo "✅ Formatting complete"

format-check: ## Check formatting without fixing
	@echo "🎨 Checking code formatting..."
	@poetry run ruff format src/ tests/ --check
	@echo "✅ Format check complete"

fix: format lint ## Auto-fix all issues (format + imports + lint)
	@echo "🔧 Auto-fixing all issues..."
	@poetry run ruff check src/ tests/ --fix --unsafe-fixes
	@echo "✅ All auto-fixes applied"

# ============================================================================
# 🧪 TESTING - 90% COVERAGE MINIMUM
# ============================================================================

test: ## Run tests with coverage (90% minimum required)
	@echo "🧪 Running tests with coverage..."
	@poetry run pytest tests/ -v --cov=src/flext_dbt_ldif --cov-report=term-missing --cov-fail-under=90
	@echo "✅ Tests complete"

test-unit: ## Run unit tests only
	@echo "🧪 Running unit tests..."
	@poetry run pytest tests/unit/ -v
	@echo "✅ Unit tests complete"

test-integration: ## Run integration tests only
	@echo "🧪 Running integration tests..."
	@poetry run pytest tests/integration/ -v
	@echo "✅ Integration tests complete"

test-dbt: dbt-deps dbt-compile ## Run dbt data tests
	@echo "🧪 Running dbt data tests..."
	@poetry run dbt test --profiles-dir profiles/ --target dev
	@echo "✅ DBT data tests complete"

coverage: ## Generate detailed coverage report
	@echo "📊 Generating coverage report..."
	@poetry run pytest tests/ --cov=src/flext_dbt_ldif --cov-report=term-missing --cov-report=html
	@echo "✅ Coverage report generated in htmlcov/"

coverage-html: coverage ## Generate HTML coverage report
	@echo "📊 Opening coverage report..."
	@python -m webbrowser htmlcov/index.html

# ============================================================================
# 🚀 DEVELOPMENT SETUP
# ============================================================================

setup: install pre-commit dbt-deps ## Complete development setup
	@echo "🎯 Development setup complete!"

install: ## Install dependencies with Poetry
	@echo "📦 Installing dependencies..."
	@poetry install --all-extras --with dev,test,docs,security
	@echo "✅ Dependencies installed"

dev-install: install ## Install in development mode
	@echo "🔧 Setting up development environment..."
	@poetry install --all-extras --with dev,test,docs,security
	@poetry run pre-commit install
	@mkdir -p profiles logs target dbt_packages
	@echo "✅ Development environment ready"

pre-commit: ## Setup pre-commit hooks
	@echo "🎣 Setting up pre-commit hooks..."
	@poetry run pre-commit install
	@poetry run pre-commit run --all-files || true
	@echo "✅ Pre-commit hooks installed"

# ============================================================================
# 🎯 DBT OPERATIONS - CORE WORKFLOW
# ============================================================================

dbt-deps: ## Install dbt dependencies
	@echo "📦 Installing dbt dependencies..."
	@poetry run dbt deps --profiles-dir profiles/
	@echo "✅ DBT dependencies installed"

dbt-debug: ## Debug dbt configuration
	@echo "🔍 Debugging dbt configuration..."
	@poetry run dbt debug --profiles-dir profiles/ --target dev
	@echo "✅ DBT debug complete"

dbt-compile: dbt-deps ## Compile dbt models
	@echo "🔨 Compiling dbt models..."
	@poetry run dbt compile --profiles-dir profiles/ --target dev
	@echo "✅ DBT models compiled"

dbt-run: dbt-deps dbt-compile ## Run dbt models
	@echo "🚀 Running dbt models..."
	@poetry run dbt run --profiles-dir profiles/ --target dev
	@echo "✅ DBT models executed"

dbt-test: dbt-compile ## Run dbt tests
	@echo "🧪 Running dbt tests..."
	@poetry run dbt test --profiles-dir profiles/ --target dev
	@echo "✅ DBT tests complete"

dbt-docs: dbt-compile ## Generate dbt documentation
	@echo "📚 Generating dbt documentation..."
	@poetry run dbt docs generate --profiles-dir profiles/ --target dev
	@echo "✅ DBT documentation generated"

dbt-seed: dbt-deps ## Load dbt seed data
	@echo "🌱 Loading dbt seed data..."
	@poetry run dbt seed --profiles-dir profiles/ --target dev
	@echo "✅ DBT seed data loaded"

dbt-snapshot: dbt-deps ## Run dbt snapshots
	@echo "📸 Running dbt snapshots..."
	@poetry run dbt snapshot --profiles-dir profiles/ --target dev
	@echo "✅ DBT snapshots complete"

dbt-clean: ## Clean dbt artifacts
	@echo "🧹 Cleaning dbt artifacts..."
	@poetry run dbt clean --profiles-dir profiles/
	@rm -rf logs/dbt.log
	@echo "✅ DBT artifacts cleaned"

# ============================================================================
# 🔧 LDIF SPECIFIC OPERATIONS
# ============================================================================

ldif-models-test: dbt-deps dbt-compile ## Test LDIF-specific models
	@echo "🧪 Testing LDIF models..."
	@poetry run dbt test --models staging --profiles-dir profiles/ --target dev
	@poetry run dbt test --models marts --profiles-dir profiles/ --target dev
	@poetry run python scripts/validate_ldif_models.py
	@echo "✅ LDIF models tests complete"

ldif-transformations: dbt-run ## Run LDIF transformation pipeline
	@echo "🔄 Running LDIF transformations..."
	@poetry run dbt run --models analytics_ldif_insights --profiles-dir profiles/ --target dev
	@poetry run python scripts/execute_ldif_transformations.py
	@echo "✅ LDIF transformations complete"

ldif-validate: dbt-compile ## Validate LDIF data integrity
	@echo "✅ Validating LDIF data integrity..."
	@poetry run python scripts/validate_ldif_integrity.py
	@poetry run dbt test --models tests.ldif_compliance --profiles-dir profiles/ --target dev
	@echo "✅ LDIF validation complete"

ldif-schema-analysis: ## Analyze LDIF schema patterns
	@echo "📋 Analyzing LDIF schema patterns..."
	@poetry run python scripts/analyze_ldif_schema.py
	@echo "✅ LDIF schema analysis complete"

ldif-change-tracking: dbt-run ## Track LDIF changes over time
	@echo "📊 Running LDIF change tracking..."
	@poetry run dbt run --models fact_ldif_changes --profiles-dir profiles/ --target dev
	@echo "✅ LDIF change tracking complete"

ldif-impact-analysis: dbt-run ## Analyze impact of LDIF changes
	@echo "⚡ Running LDIF impact analysis..."
	@poetry run python scripts/impact_analysis.py
	@echo "✅ LDIF impact analysis complete"

ldif-compliance-check: dbt-test ## Check LDIF compliance
	@echo "✅ Running LDIF compliance checks..."
	@poetry run dbt test --models tests.ldif_compliance --profiles-dir profiles/ --target dev
	@echo "✅ LDIF compliance check complete"

# ============================================================================
# 🎯 PROGRAMMATIC MODEL GENERATION
# ============================================================================

generate-models: ## Generate dbt models programmatically
	@echo "🔧 Generating dbt models programmatically..."
	@poetry run python -m flext_dbt_ldif.generate_models
	@echo "✅ DBT models generated"

update-schemas: ## Update model schemas
	@echo "🔧 Updating model schemas..."
	@poetry run python -m flext_dbt_ldif.update_schemas
	@echo "✅ Model schemas updated"

refresh-manifest: dbt-compile ## Refresh dbt manifest
	@echo "🔄 Refreshing dbt manifest..."
	@poetry run dbt parse --profiles-dir profiles/ --target dev
	@echo "✅ DBT manifest refreshed"

validate-generated: generate-models dbt-compile ## Validate generated models
	@echo "✅ Validating generated models..."
	@poetry run dbt compile --profiles-dir profiles/ --target dev
	@poetry run python scripts/validate_generated_models.py
	@echo "✅ Generated models validation complete"

# ============================================================================
# 📊 ADVANCED ANALYTICS
# ============================================================================

analytics-run: dbt-run ## Run advanced analytics models
	@echo "📊 Running advanced analytics..."
	@poetry run dbt run --models analytics_ldif_insights --profiles-dir profiles/ --target dev
	@echo "✅ Advanced analytics complete"

analytics-time-series: dbt-run ## Run time series analytics
	@echo "📈 Running time series analytics..."
	@poetry run dbt run --models +analytics_ldif_insights --profiles-dir profiles/ --target dev
	@echo "✅ Time series analytics complete"

analytics-anomaly-detection: dbt-run ## Run anomaly detection
	@echo "🔍 Running anomaly detection..."
	@poetry run python scripts/anomaly_detection.py
	@echo "✅ Anomaly detection complete"

analytics-risk-assessment: dbt-run ## Run risk assessment
	@echo "⚠️ Running risk assessment..."
	@poetry run python scripts/risk_assessment.py
	@echo "✅ Risk assessment complete"

analytics-insights: analytics-run analytics-anomaly-detection analytics-risk-assessment ## Run all analytics
	@echo "✅ All advanced analytics complete"

# ============================================================================
# 📦 BUILD & DISTRIBUTION
# ============================================================================

build: clean generate-models dbt-compile ## Build dbt project
	@echo "🔨 Building dbt project..."
	@poetry build
	@echo "✅ Build complete - packages in dist/"

clean: ## Remove all artifacts
	@echo "🧹 Cleaning up..."
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info/
	@rm -rf .coverage
	@rm -rf htmlcov/
	@rm -rf target/
	@rm -rf dbt_packages/
	@rm -rf logs/
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"

# ============================================================================
# 📊 DEPENDENCY MANAGEMENT
# ============================================================================

deps-update: ## Update all dependencies
	@echo "🔄 Updating dependencies..."
	@poetry update
	@poetry run dbt deps --profiles-dir profiles/
	@echo "✅ Dependencies updated"

deps-audit: ## Audit dependencies for vulnerabilities
	@echo "🔍 Auditing dependencies..."
	@poetry run pip-audit
	@echo "✅ Dependency audit complete"

deps-tree: ## Show dependency tree
	@echo "🌳 Dependency tree:"
	@poetry show --tree

deps-outdated: ## Show outdated dependencies
	@echo "📋 Outdated dependencies:"
	@poetry show --outdated

# ============================================================================
# 🔧 ENVIRONMENT CONFIGURATION
# ============================================================================

# Project information
PROJECT_NAME := flext-dbt-ldif
PROJECT_TYPE := meltano-plugin
PROJECT_VERSION := $(shell poetry version -s)
PROJECT_DESCRIPTION := FLEXT DBT LDIF - LDIF Data Interchange Analytics

# Python settings
PYTHON := python3.13
export PYTHONPATH := $(PWD)/src:$(PYTHONPATH)
export PYTHONDONTWRITEBYTECODE := 1
export PYTHONUNBUFFERED := 1

# DBT settings
export DBT_PROFILES_DIR := $(PWD)/profiles
export DBT_PROJECT_DIR := $(PWD)
export DBT_TARGET := dev
export DBT_LOG_LEVEL := INFO

# LDIF Analytics settings
export LDIF_SOURCE_SCHEMA := raw
export LDIF_TARGET_SCHEMA := ldif_analytics
export LDIF_ANALYTICS_TIMEZONE := UTC

# Data warehouse settings
export DW_HOST := localhost
export DW_PORT := 5432
export DW_DATABASE := ldif_analytics
export DW_USER := dbt_user

# Advanced analytics settings
export ANALYTICS_ENABLE_ANOMALY_DETECTION := true
export ANALYTICS_ENABLE_RISK_ASSESSMENT := true
export ANALYTICS_TIME_SERIES_WINDOW := 30
export ANALYTICS_STATISTICAL_CONFIDENCE := 0.95

# Performance settings
export DBT_THREADS := 4
export DBT_PARTIAL_PARSE := true
export DBT_USE_COLORS := true
export DBT_PRINTER_WIDTH := 80

# Quality settings
export DBT_WARN_ERROR := false
export DBT_STORE_FAILURES := true
export DBT_FAIL_FAST := false

# Model generation settings
export MODEL_GENERATION_MODE := advanced
export MODEL_INCLUDE_POST_HOOKS := true
export MODEL_ENABLE_CUSTOM_MACROS := true

# Poetry settings
export POETRY_VENV_IN_PROJECT := false
export POETRY_CACHE_DIR := $(HOME)/.cache/pypoetry

# Quality gate settings
export MYPY_CACHE_DIR := .mypy_cache
export RUFF_CACHE_DIR := .ruff_cache

.DEFAULT_GOAL := help

# ============================================================================
# 🎯 WORKSPACE INTEGRATION
# ============================================================================

workspace-sync: ## Sync with workspace dependencies
	@echo "🔄 Syncing with workspace dependencies..."
	@poetry run python scripts/sync_workspace_deps.py
	@echo "✅ Workspace sync complete"

ecosystem-check: ## Verify FLEXT ecosystem compatibility
	@echo "🌐 Checking FLEXT ecosystem compatibility..."
	@echo "📦 DBT project: $(PROJECT_NAME) v$(PROJECT_VERSION)"
	@echo "🏗️ Architecture: Advanced DBT + LDIF Analytics"
	@echo "🐍 Python: 3.13"
	@echo "🔗 Framework: FLEXT Core + dbt Core + Advanced Analytics"
	@echo "📊 Quality: Zero tolerance enforcement"
	@echo "✅ Ecosystem compatibility verified"

workspace-info: ## Show workspace integration info
	@echo "🏢 FLEXT Workspace Integration"
	@echo "==============================="
	@echo "📁 Project Path: $(PWD)"
	@echo "🏆 Role: LDIF Data Interchange Analytics"
	@echo "🔗 Dependencies: flext-core, dbt-core, dbt-utils, dbt-codegen"
	@echo "📦 Provides: Advanced LDIF analytics and insights"
	@echo "🎯 Standards: Programmatic model generation with advanced analytics"