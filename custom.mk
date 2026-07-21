# Private project handlers for flext-dbt-ldif.
# Strict extension: only `_custom_<verb>_<what>` handlers and `(pre|post)-<verb>[-<what>]`
# hooks. Public targets, toolchain vars, .DEFAULT_GOAL, includes, and help are
# invalid (base.mk owns those). Run project actions via `make run WHAT=<what>`.
.PHONY: _custom_run_dbt _custom_test_dbt _custom_docs_dbt
_custom_run_dbt: ## make run WHAT=dbt — run dbt models
	$(Q)$(POETRY) run dbt run
_custom_test_dbt: ## make test WHAT=dbt — run dbt tests
	$(Q)$(POETRY) run dbt test
_custom_docs_dbt: ## make docs WHAT=dbt — generate + serve dbt docs
	$(Q)$(POETRY) run dbt docs generate
	$(Q)$(POETRY) run dbt docs serve
