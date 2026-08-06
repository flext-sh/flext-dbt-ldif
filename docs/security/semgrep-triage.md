# Triagem Semgrep — flext-sh/flext-dbt-ldif

Gerado do dump da plataforma Semgrep (deployment `datacosmos`, 2026-08-06).

Bead de rastreio: `mro-p57t.8`

## Resumo

**13 findings** — high 3, medium 10, low 0
Confiança: high 13, medium 0, low 0

| regra | achados |
|---|---|
| `yaml.github-actions.security.github-actions-mutable-action-tag.github-actions-mutable-action-tag` | 6 |
| `package_managers.dependabot.dependabot-missing-cooldown.dependabot-missing-cooldown` | 3 |
| `yaml.github-actions.security.secrets-inherit.secrets-inherit` | 2 |
| `yaml.github-actions.security.run-shell-injection.run-shell-injection` | 1 |
| `package_managers.uv.uv-missing-dependency-cooldown.uv-missing-dependency-cooldown` | 1 |

## Findings

Coluna **Decisão** a preencher: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | conf | regra | arquivo | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | high | high | `secrets-inherit` | `dbt_packages/codegen/.github/workflows/triage-labels.yml` | 31 | |
| 2 | high | high | `run-shell-injection` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 48 | |
| 3 | high | high | `secrets-inherit` | `dbt_packages/dbt_utils/.github/workflows/triage-labels.yml` | 31 | |
| 4 | medium | high | `dependabot-missing-cooldown` | `.github/dependabot.yml` | 4 | |
| 5 | medium | high | `dependabot-missing-cooldown` | `.github/dependabot.yml` | 11 | |
| 6 | medium | high | `dependabot-missing-cooldown` | `.github/dependabot.yml` | 18 | |
| 7 | medium | high | `github-actions-mutable-action-tag` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 34 | |
| 8 | medium | high | `github-actions-mutable-action-tag` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 37 | |
| 9 | medium | high | `github-actions-mutable-action-tag` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 97 | |
| 10 | medium | high | `github-actions-mutable-action-tag` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 100 | |
| 11 | medium | high | `github-actions-mutable-action-tag` | `dbt_packages/dbt_utils/.github/workflows/create-table-of-contents.yml` | 22 | |
| 12 | medium | high | `github-actions-mutable-action-tag` | `dbt_packages/dbt_utils/.github/workflows/create-table-of-contents.yml` | 28 | |
| 13 | medium | high | `uv-missing-dependency-cooldown` | `pyproject.toml` | 603 | |

## Como triar

1. Abrir `arquivo:linha` e seguir o fluxo até o sink.
2. Classificar: **corrigir** (entrada externa alcança o sink), **falso-positivo** (registrar via `nosemgrep` ou `.semgrepignore` com justificativa), **risco-aceito** (com prazo de revisão).
3. Priorizar findings high com confidence=high.

Dados brutos: `~/semgrep-violations/by-repo/flext-sh__flext-dbt-ldif.json`

