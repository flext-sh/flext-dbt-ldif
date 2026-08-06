# Triagem SonarCloud — flext-sh/flext-dbt-ldif

Gerado do dump da plataforma SonarCloud (2026-08-06).

Bead de rastreio: `mro-2wjm.4`

## Resumo

**91 issues** — BLOCKER 3, CRITICAL 61, MAJOR 23, MINOR 2
Tipos: VULNERABILITY 22, BUG 0, CODE_SMELL 69

| regra | issues |
|---|---|
| `plsql:LiteralsNonPrintableCharactersCheck` | 34 |
| `plsql:S1192` | 25 |
| `githubactions:S7637` | 6 |
| `githubactions:S8544` | 6 |
| `shelldre:S7688` | 3 |
| `githubactions:S7630` | 2 |
| `python:S1192` | 2 |
| `githubactions:S8233` | 2 |

## Issues

Coluna **Decisão**: `corrigir` / `falso-positivo` / `risco-aceito`.

| # | sev | tipo | regra | componente | linha | Decisão |
|---|---|---|---|---|---|---|
| 1 | BLOCKER | VULNERABILITY | `githubactions:S7630` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 49 | |
| 2 | BLOCKER | VULNERABILITY | `githubactions:S7630` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 55 | |
| 3 | BLOCKER | CODE_SMELL | `python:S1845` | `src/flext_dbt_ldif/api.py` | 49 | |
| 4 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 47 | |
| 5 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 65 | |
| 6 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 81 | |
| 7 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 88 | |
| 8 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 89 | |
| 9 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 105 | |
| 10 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 121 | |
| 11 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 129 | |
| 12 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 145 | |
| 13 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 153 | |
| 14 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 169 | |
| 15 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 185 | |
| 16 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 192 | |
| 17 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 193 | |
| 18 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 217 | |
| 19 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 227 | |
| 20 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 228 | |
| 21 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 245 | |
| 22 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 269 | |
| 23 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 279 | |
| 24 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 280 | |
| 25 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 297 | |
| 26 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 300 | |
| 27 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/codegen/macros/generate_model_import_ctes.sql` | 326 | |
| 28 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 12 | |
| 29 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 18 | |
| 30 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 19 | |
| 31 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 34 | |
| 32 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 45 | |
| 33 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 73 | |
| 34 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 79 | |
| 35 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/codegen/macros/helpers/helpers.sql` | 83 | |
| 36 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/integration_tests/models/sql/test_get_column_values.sql` | 2 | |
| 37 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/integration_tests/models/sql/test_get_single_value.sql` | 8 | |
| 38 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/dbt_utils/integration_tests/tests/assert_get_query_results_as_dict_objects_equal.sql` | 23 | |
| 39 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/dbt_utils/integration_tests/tests/generic/expect_table_columns_to_match_set.sql` | 3 | |
| 40 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/dbt_utils/integration_tests/tests/generic/expect_table_columns_to_match_set.sql` | 31 | |
| 41 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/generic_tests/equality.sql` | 2 | |
| 42 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/generic_tests/equality.sql` | 58 | |
| 43 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/generic_tests/mutually_exclusive_ranges.sql` | 1 | |
| 44 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/date_spine.sql` | 2 | |
| 45 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_column_values.sql` | 2 | |
| 46 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_filtered_columns_in_relation.sql` | 2 | |
| 47 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql` | 7 | |
| 48 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql` | 7 | |
| 49 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql` | 9 | |
| 50 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql` | 9 | |
| 51 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_table_types_sql.sql` | 11 | |
| 52 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql` | 9 | |
| 53 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql` | 10 | |
| 54 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql` | 13 | |
| 55 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql` | 14 | |
| 56 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/get_tables_by_pattern_sql.sql` | 15 | |
| 57 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/nullcheck_table.sql` | 2 | |
| 58 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/dbt_utils/macros/sql/safe_add.sql` | 9 | |
| 59 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/dbt_utils/macros/sql/safe_subtract.sql` | 9 | |
| 60 | CRITICAL | CODE_SMELL | `lsql:LiteralsNonPrintableCharactersCheck` | `dbt_packages/dbt_utils/macros/sql/surrogate_key.sql` | 8 | |
| 61 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/union.sql` | 2 | |
| 62 | CRITICAL | CODE_SMELL | `plsql:S1192` | `dbt_packages/dbt_utils/macros/sql/unpivot.sql` | 16 | |
| 63 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_dbt_ldif/models.py` | 52 | |
| 64 | CRITICAL | CODE_SMELL | `python:S1192` | `src/flext_dbt_ldif/models.py` | 62 | |
| 65 | MAJOR | CODE_SMELL | `shelldre:S7688` | `.github/scripts/install-git-hooks.sh` | 55 | |
| 66 | MAJOR | CODE_SMELL | `shelldre:S7688` | `.github/scripts/install-git-hooks.sh` | 104 | |
| 67 | MAJOR | CODE_SMELL | `shelldre:S7688` | `.github/scripts/install-git-hooks.sh` | 106 | |
| 68 | MAJOR | VULNERABILITY | `githubactions:S8264` | `.github/workflows/docs.yml` | 18 | |
| 69 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 19 | |
| 70 | MAJOR | VULNERABILITY | `githubactions:S8233` | `.github/workflows/docs.yml` | 20 | |
| 71 | MAJOR | VULNERABILITY | `githubactions:S7637` | `dbt_packages/codegen/.github/workflows/ci.yml` | 21 | |
| 72 | MAJOR | VULNERABILITY | `githubactions:S7637` | `dbt_packages/codegen/.github/workflows/stale.yml` | 30 | |
| 73 | MAJOR | VULNERABILITY | `githubactions:S7637` | `dbt_packages/codegen/.github/workflows/triage-labels.yml` | 27 | |
| 74 | MAJOR | VULNERABILITY | `githubactions:S7635` | `dbt_packages/codegen/.github/workflows/triage-labels.yml` | 31 | |
| 75 | MAJOR | VULNERABILITY | `githubactions:S8544` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 43 | |
| 76 | MAJOR | VULNERABILITY | `githubactions:S8541` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 44 | |
| 77 | MAJOR | VULNERABILITY | `githubactions:S8544` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 44 | |
| 78 | MAJOR | VULNERABILITY | `githubactions:S8544` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 106 | |
| 79 | MAJOR | VULNERABILITY | `githubactions:S8544` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 107 | |
| 80 | MAJOR | VULNERABILITY | `githubactions:S8544` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 111 | |
| 81 | MAJOR | VULNERABILITY | `githubactions:S8541` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 112 | |
| 82 | MAJOR | VULNERABILITY | `githubactions:S8544` | `dbt_packages/dbt_utils/.github/workflows/ci.yml` | 112 | |
| 83 | MAJOR | VULNERABILITY | `githubactions:S7637` | `dbt_packages/dbt_utils/.github/workflows/create-table-of-contents.yml` | 28 | |
| 84 | MAJOR | VULNERABILITY | `githubactions:S7637` | `dbt_packages/dbt_utils/.github/workflows/stale.yml` | 30 | |
| 85 | MAJOR | VULNERABILITY | `githubactions:S7637` | `dbt_packages/dbt_utils/.github/workflows/triage-labels.yml` | 27 | |
| 86 | MAJOR | VULNERABILITY | `githubactions:S7635` | `dbt_packages/dbt_utils/.github/workflows/triage-labels.yml` | 31 | |
| 87 | MAJOR | VULNERABILITY | `text:S8565` | `pyproject.toml` | - | |
| 88 | MINOR | CODE_SMELL | `python:S7504` | `conftest.py` | 20 | |
| 89 | MINOR | CODE_SMELL | `plsql:SingleLineCommentsSyntaxCheck` | `dbt_packages/dbt_utils/integration_tests/models/sql/test_star_aggregate.sql` | 1 | |
| 90 | INFO | CODE_SMELL | `plsql:S1135` | `dbt_packages/dbt_utils/integration_tests/models/sql/test_pivot.sql` | 2 | |
| 91 | INFO | CODE_SMELL | `plsql:S1135` | `dbt_packages/dbt_utils/integration_tests/models/sql/test_pivot_apostrophe.sql` | 2 | |

## Como triar

1. **BLOCKER e CRITICAL primeiro**, e todo VULNERABILITY independente de severidade.
2. Classificar: **corrigir**, **falso-positivo** (marcar na plataforma SonarCloud com justificativa), **risco-aceito** (com prazo).
3. CODE_SMELL em volume alto sugere padrão — corrigir a causa raiz, não issue a issue.

Dados brutos: `~/sonarqube-violations/by-repo/flext-sh__flext-dbt-ldif.json`

