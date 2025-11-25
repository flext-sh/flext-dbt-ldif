# FLEXT-DBT-LDIF Project Guidelines

**Reference**: See [../CLAUDE.md](../CLAUDE.md) for FLEXT ecosystem standards and general rules.

---

## Project Overview

**FLEXT-DBT-LDIF** is the specialized dbt project for LDIF (LDAP Data Interchange Format) analytics with programmatic model generation.

**Version**: 2.1.0  
**Status**: Production-ready  
**Python**: 3.13+

**CRITICAL INTEGRATION DEPENDENCIES**:
- **flext-meltano**: MANDATORY for ALL DBT operations (ZERO TOLERANCE for direct dbt imports)
- **flext-ldif**: MANDATORY for ALL LDIF operations (ZERO TOLERANCE for direct LDIF parsing imports)
- **flext-core**: Foundation patterns (FlextResult, FlextService, FlextContainer)
- **flext-cli**: MANDATORY for ALL CLI operations (ZERO TOLERANCE for direct click/rich imports)

---

## Essential Commands

```bash
# Setup and validation
make setup                    # Complete development environment setup
make validate                 # Complete validation (lint + type + security + test)
make check                    # Quick check (lint + type)

# Quality gates
make lint                     # Ruff linting
make type-check               # Pyrefly type checking
make security                 # Bandit security scan
make test                     # Run tests
```

---

## Key Patterns

### DBT LDIF Analytics

```python
from flext_core import FlextResult
from flext_dbt_ldif import FlextDbtLdif

dbt = FlextDbtLdif()

# Run DBT models
result = dbt.run_models(models=["model1", "model2"])
if result.is_success:
    output = result.unwrap()
```

---

## Critical Development Rules

### ZERO TOLERANCE Policies

**ABSOLUTELY FORBIDDEN**:
- ❌ Direct dbt imports (use flext-meltano)
- ❌ Direct LDIF parsing imports (use flext-ldif)
- ❌ Direct click/rich imports (use flext-cli)
- ❌ Exception-based error handling (use FlextResult)
- ❌ Type ignores or `Any` types

**MANDATORY**:
- ✅ Use `FlextResult[T]` for all operations
- ✅ Use flext-meltano for DBT operations
- ✅ Use flext-ldif for LDIF operations
- ✅ Use flext-cli for CLI operations
- ✅ Complete type annotations
- ✅ Zero Ruff violations

---

**Additional Resources**: [../CLAUDE.md](../CLAUDE.md) (workspace), [README.md](README.md) (overview)
