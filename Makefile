# flext-dbt-ldif - LDIF dbt Package
PROJECT_NAME := flext-dbt-ldif
ifneq ("$(wildcard ../base.mk)", "")
include ../base.mk
else
include base.mk
endif

# === PROJECT-SPECIFIC TARGETS ===
.PHONY: dbt-run dbt-test dbt-docs test-unit test-integration build shell

dbt-run: ## Run dbt models
	$(Q)$(POETRY) run dbt run

dbt-test: ## Run dbt tests
	$(Q)$(POETRY) run dbt test

dbt-docs: ## Generate dbt documentation
	$(Q)$(POETRY) run dbt docs generate
	$(Q)$(POETRY) run dbt docs serve

.DEFAULT_GOAL := help
