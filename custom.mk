# Private project handlers for flext-dbt-ldif.
# Strict extension: only `_custom_<verb>_<what>` handlers and `(pre|post)-<verb>[-<what>]`
# hooks. Public targets, toolchain vars, .DEFAULT_GOAL, includes, and help are
# invalid (base.mk owns those). Invoke via `make run WHAT=<what>`.
.PHONY: _custom_run_dbt _custom_run_dbt-test _custom_run_dbt-docs
_custom_run_dbt: ## make run WHAT=dbt — run dbt models
	$(Q)$(POETRY) run dbt run
_custom_run_dbt-test: ## make run WHAT=dbt-test — run dbt tests
	$(Q)$(POETRY) run dbt test
_custom_run_dbt-docs: ## make run WHAT=dbt-docs — generate + serve dbt docs
	$(Q)$(POETRY) run dbt docs generate
	$(Q)$(POETRY) run dbt docs serve
