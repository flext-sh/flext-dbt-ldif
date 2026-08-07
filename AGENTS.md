# AGENTS.md — flext-dbt-ldif

> **Parent workspace law** lives in [`../AGENTS.md`](../AGENTS.md) — read it first.
> Universal engineering core: `~/.agents/UNIVERSAL_CORE.md`. Composition: global skills + parent/root `AGENTS.md` + this scope delta. Do not re-embed universal law.
>
> **Standalone / independent mode:** when `../AGENTS.md` does not resolve, pin the parent raw `AGENTS.md` URL to the same branch/release as this package (never `main`).

<!-- AIHUB-AGENTS-SCOPE-LOCAL-BEGIN -->
**Package:** `flext_dbt_ldif` · deps: `flext-core`, `flext-ldif`, `flext-meltano`

## Overview

dbt models for LDIF data transformation. Thin driver over `flext-meltano` dbt runner (ADR-006).

## Structure

```text
src/flext_dbt_ldif/
├── api.py            # FlextDbtLdif — generate_ldif_models / process_ldif_file
├── base.py
├── services/         # client.py, service.py, unified_service.py, core.py
├── constants.py typings.py protocols.py models.py utilities.py   # AUTO-GENERATED facets
```

## Code Map

| Symbol | Kind | Location | Role |
|--------|------|----------|------|
| `FlextDbtLdif` | class | `api.py` | facade: `generate_ldif_models`, `process_ldif_file` |
| `UnifiedService` | class | `services/unified_service.py` | `generate_staging_models`, `generate_analytics_models` |

## Conventions (specific to this package)

- Model generation emits typed `m.DbtLdif.DbtModel` instances for staging and analytics artifacts (no dict roundtrip).
- Config/settings canonical pattern: ADR-012.
- Codemod governance (ast-grep + make mod): ADR-014.

## Commands

```bash
make check PROJECT=flext-dbt-ldif
make test  PROJECT=flext-dbt-ldif       # tests/unit
```
<!-- AIHUB-AGENTS-SCOPE-LOCAL-END -->
