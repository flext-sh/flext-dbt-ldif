# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`flext-dbt-ldif` is a specialized dbt project for LDIF (LDAP Data Interchange Format) analytics within the FLEXT ecosystem. It provides advanced data transformations, programmatic model generation, and comprehensive analytics for LDAP directory data.

**Key Characteristics:**

- **Python 3.13** with strict typing and zero-tolerance quality gates
- **dbt Core** for data transformations with PostgreSQL backend
- **Programmatic Model Generation** via Python code
- **Enterprise-grade Quality Controls** with 90%+ test coverage requirement
- **Advanced Analytics** with anomaly detection and risk assessment capabilities

## Architecture

### Project Structure

```
├── src/flext_dbt_ldif/           # Python package for programmatic features
│   ├── core.py                   # DBTModelGenerator and LDIFAnalytics classes
│   ├── cli.py                    # Command-line interface
│   └── infrastructure/           # DI container and infrastructure code
├── models/                       # dbt models (programmatically generated)
│   └── staging/                  # Staging layer with schema.yml
├── profiles/                     # dbt profiles for PostgreSQL connection
├── tests/                        # Python unit and integration tests
├── dbt_project.yml              # dbt project configuration
├── packages.yml                 # dbt package dependencies (dbt_utils, codegen)
└── pyproject.toml               # Python dependencies and tool configuration
```

### Key Components

1. **DBTModelGenerator**: Programmatically generates dbt models for LDIF analytics
2. **LDIFAnalytics**: Provides advanced analytics capabilities including pattern analysis and quality metrics
3. **dbt Models**: Layered architecture with staging, intermediate, and marts
4. **Quality Gates**: Comprehensive linting, type checking, security scanning, and testing

## Development Commands

### Essential Quality Gates (Run Before Commits)

```bash
make validate          # Complete validation: lint + type + security + test + dbt-test
make check            # Quick validation: lint + type + test + dbt-compile
```

### Core dbt Operations

```bash
# dbt workflow
make dbt-deps         # Install dbt dependencies (dbt_utils, codegen)
make dbt-compile      # Compile dbt models
make dbt-run          # Execute dbt models
make dbt-test         # Run dbt data tests
make dbt-docs         # Generate dbt documentation
make dbt-debug        # Debug dbt configuration

# LDIF-specific operations
make ldif-models-test      # Test LDIF-specific staging and marts models
make ldif-transformations  # Run LDIF transformation pipeline
make ldif-validate        # Validate LDIF data integrity
```

### Python Development

```bash
# Quality gates
make lint             # Ruff linting with ALL rules enabled
make type-check       # MyPy strict type checking
make security         # Bandit + pip-audit + detect-secrets
make format           # Auto-format code with ruff

# Testing
make test             # Run pytest with 90% coverage requirement
make test-unit        # Unit tests only
make test-integration # Integration tests only
make coverage-html    # Generate HTML coverage report
```

### Programmatic Model Generation

```bash
make generate-models     # Generate dbt models programmatically
make update-schemas      # Update model schemas
make validate-generated  # Validate generated models
```

### Setup and Installation

```bash
make setup           # Complete development setup
make install         # Install Poetry dependencies
make dev-install     # Development environment setup with pre-commit
```

## Configuration

### Database Connection

- **Profile**: `flext_ldif` (defined in `profiles/profiles.yml`)
- **Database**: PostgreSQL with configurable connection via environment variables
- **Default Target**: `dev` (uses localhost:5432)
- **Schemas**: Layered approach with `ldif_staging`, `ldif_intermediate`, `ldif_marts`

### Environment Variables

```bash
# Database configuration
DBT_POSTGRES_HOST=localhost
DBT_POSTGRES_USER=postgres
DBT_POSTGRES_PASSWORD=password
DBT_POSTGRES_DATABASE=ldif_analytics
DBT_POSTGRES_SCHEMA=ldif_dev

# dbt settings
DBT_PROFILES_DIR=profiles/
DBT_TARGET=dev
DBT_THREADS=4

# Analytics settings
ANALYTICS_ENABLE_ANOMALY_DETECTION=true
ANALYTICS_ENABLE_RISK_ASSESSMENT=true
```

## dbt Project Details

### Model Layers

1. **Staging** (`staging/`): Raw LDIF data transformation with quality checks
   - `stg_ldif_entries`: Core staging model with DN validation and categorization
2. **Intermediate** (`intermediate/`): Business logic transformations
3. **Marts** (`marts/`): Business-ready analytics models

### Key Models

- **stg_ldif_entries**: Validates DN format, calculates depth, categorizes entry types
- **analytics_ldif_insights**: Advanced analytics with time series, anomaly detection

### dbt Packages

- **dbt_utils**: Utility macros for data transformations
- **codegen**: Code generation helpers

## Testing Strategy

### Python Tests

- **Unit Tests**: Test DBTModelGenerator and LDIFAnalytics classes
- **Integration Tests**: Test dbt model execution and data quality
- **Coverage Requirement**: 90% minimum coverage enforced

### dbt Tests

- **Schema Tests**: Data quality checks on staging models (not_null, unique, accepted_values)
- **Custom Tests**: LDIF-specific compliance and integrity checks
- **Data Tests**: Validate transformed data meets business requirements

### Test Markers

```bash
pytest -m unit           # Unit tests only
pytest -m integration    # Integration tests only
pytest -m slow          # Slow tests (excluded for fast feedback)
```

## Quality Standards

### Zero Tolerance Quality Gates

1. **Ruff Linting**: ALL rule categories enabled with comprehensive coverage
2. **MyPy Type Checking**: Strict mode with no untyped code allowed
3. **Security Scanning**: Bandit + pip-audit + detect-secrets
4. **Test Coverage**: 90% minimum coverage required
5. **dbt Compilation**: All models must compile without errors
6. **dbt Tests**: All data quality tests must pass

### Code Standards

- **Python 3.13**: Latest Python with full type hint support
- **Strict Typing**: MyPy strict mode enforced
- **Import Management**: First-party imports properly organized
- **Security**: No secrets in code, comprehensive security scanning

## Dependencies

### Core Dependencies

- **flext-core**: Base FLEXT patterns and utilities
- **flext-meltano**: Meltano integration platform
- **flext-ldif**: LDIF processing capabilities
- **flext-observability**: Monitoring and metrics
- **pydantic**: Data validation and settings
- **click**: CLI framework
- **rich**: Enhanced terminal output

### Development Dependencies

- **ruff**: Linting and formatting
- **mypy**: Static type checking
- **pytest**: Testing framework with coverage
- **bandit**: Security scanning
- **pre-commit**: Git hook management

## TODO: GAPS DE ARQUITETURA IDENTIFICADOS - PRIORIDADE ALTA

### 🚨 GAP 1: LDIF Processing Integration Efficiency

**Status**: ALTO - Integration com flext-ldif pode ser optimized
**Problema**:

- Python components em dbt project podem duplicate flext-ldif functionality
- LDIF parsing patterns podem divergir between projects
- File processing logic pode be duplicated em core.py

**TODO**:

- [ ] Optimize integration com flext-ldif library
- [ ] Eliminate duplication de LDIF processing functionality
- [ ] Align LDIF parsing patterns com shared library
- [ ] Consolidate file processing logic

### 🚨 GAP 2: DBT-Python Hybrid Architecture Complexity

**Status**: ALTO - Hybrid dbt-Python architecture pode ser over-engineered
**Problema**:

- Programmatic model generation via Python pode criar maintenance overhead
- DI container em dbt context (infrastructure/) pode be overkill
- DBTModelGenerator complexity pode não justify benefits

**TODO**:

- [ ] Simplify dbt-Python integration architecture
- [ ] Review necessity de programmatic model generation
- [ ] Evaluate DI container need em dbt context
- [ ] Document architectural decisions clearly

### 🚨 GAP 3: Singer Ecosystem Integration Incomplete

**Status**: ALTO - Integration com Singer ecosystem não clearly defined
**Problema**:

- dbt project relationship com flext-tap-ldif patterns podem be suboptimal
- Data flow from LDIF taps → dbt → targets não fully documented
- Meltano integration patterns podem be incomplete

**TODO**:

- [ ] Define clear integration patterns com flext-meltano
- [ ] Document comprehensive data flow from flext-tap-ldif to dbt models
- [ ] Optimize integration com LDIF Singer ecosystem
- [ ] Create integrated pipeline documentation e examples

## Integration with FLEXT Ecosystem

This project is part of the larger FLEXT ecosystem:

- Integrates with `flext-core` for base patterns
- Uses `flext-ldif` for LDIF processing
- Connects to `flext-meltano` for orchestration
- Follows FLEXT architectural patterns and quality standards

## Common Workflows

### Adding New Models

1. Use `DBTModelGenerator` class to programmatically create models
2. Run `make generate-models` to create model files
3. Update `schema.yml` with model documentation and tests
4. Run `make dbt-compile` to validate syntax
5. Run `make validate` to ensure quality gates pass

### Debugging dbt Issues

1. Run `make dbt-debug` to check configuration
2. Use `make dbt-compile` to identify compilation errors
3. Check `profiles/profiles.yml` for connection issues
4. Verify environment variables are set correctly

### Performance Optimization

1. Monitor model execution times in dbt logs
2. Use `dbt run --models <model_name>` for targeted execution
3. Adjust materialization strategies (view vs table)
4. Optimize SQL queries in generated models
