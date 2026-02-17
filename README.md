# FLEXT-DBT-LDIF

[![dbt 1.6+](https://img.shields.io/badge/dbt-1.6+-orange.svg)](https://getdbt.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**FLEXT-DBT-LDIF** specializes in advanced analytics for LDAP Data Interchange Format (LDIF) sources. It offers programmatic dbt model generation and anomaly detection for LDIF exports, providing a robust pipeline for directory audits and data quality assessment.

Part of the [FLEXT](https://github.com/flext-sh/flext) ecosystem.

## 🚀 Key Features

- **Programmatic Model Generation**: Automatically generates dbt models from LDIF schemas (`make generate-models`), ensuring up-to-date transformations.
- **Anomaly Detection**: Built-in SQL logic to identify unusual patterns in directory data (e.g., sudden mass deletions, malformed DNs).
- **Risk Assessment**: Classifies entries based on sensitive attribute changes and security compliance rules.
- **Audit Readiness**: Tracks historical snapshots of LDIF exports for complete audit trails.
- **Validation Macros**: Custom dbt tests for strict RFC-compliant DN validation and attribute format checks.

## 📦 Installation

To usage in your dbt project, add to your `packages.yml`:

```yaml
packages:
  - git: "https://github.com/organization/flext.git"
    subdirectory: "flext-dbt-ldif"
    revision: "main" 
```

Run dependencies:

```bash
dbt deps
```

## 🛠️ Usage

### Generate Models

Use the CLI to scaffold models from your raw LDIF data source:

```bash
# Generate staging models based on current schema
make generate-models
```

### Anomaly Detection Query

Identify potential security risks in your directory data:

```sql
SELECT
    entry_dn,
    risk_score,
    detection_reason
FROM {{ ref('fct_ldif_anomalies') }}
WHERE risk_score > 80
ORDER BY detected_at DESC
```

### Time-Travel Analysis

Analyze historical changes between LDIF exports:

```sql
SELECT
    entry_dn,
    attribute_name,
    old_value,
    new_value,
    change_type -- 'ADD', 'DELETE', 'MODIFY'
FROM {{ ref('fct_ldif_changes') }}
WHERE change_date BETWEEN '2023-01-01' AND '2023-01-31'
```

## 🏗️ Architecture

FLEXT-DBT-LDIF bridges static file analysis with dynamic modeling:

- **Generator**: Python scripts inspect raw data to build `schema.yml` and model files dynamically.
- **Analytics Layer**: Advanced SQL logic for security and operational insights without impacting production directories.
- **Quality Layer**: Automated tests ensure the integrity of parsed LDIF data.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/development.md) for details on enhancing generator logic and adding new detection rules.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
