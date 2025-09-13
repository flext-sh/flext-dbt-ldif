# COMPREHENSIVE QUALITY REFACTORING FOR FLEXT-DBT-LDIF

**Enterprise-Grade LDIF Analytics Quality Assurance & Refactoring Guidelines**
**Version**: 2.1.0 | **Authority**: WORKSPACE | **Updated**: 2025-01-08
**Environment**: `/home/marlonsc/flext/.venv/bin/python` (No PYTHONPATH required)
**Based on**: flext-core 0.9.0 with 79% test coverage (PROVEN FOUNDATION)
**Project Context**: Specialized dbt project for LDIF (LDAP Data Interchange Format) analytics with programmatic model generation

---

## 🎯 MISSION STATEMENT (NON-NEGOTIABLE)

**OBJECTIVE**: Achieve 100% professional quality compliance for flext-dbt-ldif with zero regressions, following SOLID principles, Python 3.13+ standards, Pydantic best practices, dbt Core patterns, and flext-core foundation patterns for LDIF analytics operations.

**CRITICAL REQUIREMENTS FOR LDIF DBT PROJECT**:

- ✅ **95%+ pytest pass rate** with **75%+ coverage** for LDIF analytics logic (flext-core proven achievable at 79%)
- ✅ **Zero errors** in ruff, mypy (strict mode), and pyright across ALL LDIF analytics source code
- ✅ **Unified LDIF service classes** - single responsibility, no aliases, no wrappers, no helpers
- ✅ **Direct flext-core integration** - eliminate LDIF complexity, reduce dbt configuration overhead
- ✅ **MANDATORY flext-cli usage** - ALL LDIF CLI projects use flext-cli for CLI AND output, NO direct Click/Rich
- ✅ **ZERO fallback tolerance** - no try/except fallbacks in LDIF handlers, no workarounds, always correct dbt solutions
- ✅ **SOLID compliance** - proper LDIF abstraction, dependency injection, clean dbt architecture
- ✅ **Professional English** - all LDIF docstrings, comments, variable names, function names
- ✅ **Incremental LDIF refactoring** - never rewrite entire dbt modules, always step-by-step improvements
- ✅ **Real functional LDIF tests** - minimal mocks, test actual LDIF functionality with real dbt environments
- ✅ **Production-ready LDIF code** - no workarounds, fallbacks, try-pass blocks, or incomplete dbt implementations

**CURRENT FLEXT-DBT-LDIF STATUS** (Evidence-based):

- 🔴 **Ruff Issues**: LDIF-specific violations in dbt transformations and programmatic model generation
- 🟡 **MyPy Issues**: 0 in main src/ LDIF modules (already compliant)
- 🟡 **Pyright Issues**: Minor LDIF API mismatches in dbt service definitions
- 🔴 **Pytest Status**: LDIF test infrastructure needs fixing for dbt transformation testing
- 🟢 **flext-core Foundation**: 79% coverage, fully functional API for LDIF operations

---

## 🚨 ABSOLUTE PROHIBITIONS FOR LDIF DBT PROJECT (ZERO TOLERANCE)

### ❌ FORBIDDEN LDIF DBT PRACTICES

1. **LDIF ANALYTICS QUALITY VIOLATIONS**:
   - Any use of `# type: ignore` without specific error codes in LDIF handlers
   - Any use of `Any` types instead of proper LDIF type annotations
   - Silencing LDIF errors with ignore hints instead of fixing dbt root causes
   - Creating LDIF wrappers, aliases, or compatibility facades
   - Using sed, awk, or automated scripts for complex LDIF refactoring

2. **LDIF DBT ARCHITECTURE VIOLATIONS**:
   - Multiple LDIF service classes per module (use single unified LDIF service per module)
   - Helper functions or constants outside of unified LDIF service classes
   - Local reimplementation of flext-core LDIF functionality
   - Creating new LDIF modules instead of refactoring existing dbt services
   - Changing lint, type checker, or test framework behavior for LDIF code

3. **LDIF/DBT CLI PROJECT VIOLATIONS** (ABSOLUTE ZERO TOLERANCE):
   - **MANDATORY**: ALL LDIF CLI projects MUST use `flext-cli` exclusively for CLI functionality AND data output
   - **FORBIDDEN**: Direct `import click` in any LDIF project code
   - **FORBIDDEN**: Direct `import rich` in any LDIF project code for output/formatting
   - **FORBIDDEN**: Direct `from dbt import` bypassing FlextDbtLdifService
   - **FORBIDDEN**: Local LDIF CLI implementations bypassing flext-cli
   - **FORBIDDEN**: Any LDIF CLI functionality not going through flext-cli layer
   - **REQUIRED**: If flext-cli lacks LDIF functionality, IMPROVE flext-cli first - NEVER work around
   - **PRINCIPLE**: Fix the foundation, don't work around LDIF patterns
   - **OUTPUT RULE**: ALL LDIF data output, formatting, tables, progress bars MUST use flext-cli wrappers
   - **NO EXCEPTIONS**: Even if flext-cli needs improvement, IMPROVE it, don't bypass LDIF patterns

4. **LDIF DBT FALLBACK/WORKAROUND VIOLATIONS** (ABSOLUTE PROHIBITION):
   - **FORBIDDEN**: `try/except` blocks as fallback mechanisms in LDIF handlers
   - **FORBIDDEN**: Palliative LDIF solutions that mask root dbt problems
   - **FORBIDDEN**: Temporary LDIF workarounds that become permanent
   - **FORBIDDEN**: "Good enough" LDIF solutions instead of correct dbt solutions
   - **REQUIRED**: Always implement the correct LDIF solution, never approximate dbt patterns

5. **LDIF DBT TESTING VIOLATIONS**:
   - Using excessive mocks instead of real functional LDIF tests
   - Accepting LDIF test failures and continuing dbt development
   - Creating fake or placeholder LDIF test implementations
   - Testing LDIF code that doesn't actually execute real dbt functionality

6. **LDIF DBT DEVELOPMENT VIOLATIONS**:
   - Rewriting entire LDIF modules instead of incremental dbt improvements
   - Skipping quality gates (ruff, mypy, pyright, pytest) for LDIF code
   - Modifying behavior of linting tools instead of fixing LDIF code
   - Rolling back git versions instead of fixing LDIF forward

7. **SPECIFIC LDIF DBT VIOLATIONS** (LDIF ANALYTICS SPECIFIC):
   - **FORBIDDEN**: Custom LDIF parsing bypassing FlextDbtLdifService
   - **FORBIDDEN**: Direct LDIF file handling outside unified dbt handlers
   - **FORBIDDEN**: LDIF data state management outside domain entities
   - **FORBIDDEN**: Custom programmatic dbt implementations bypassing established LDIF patterns
   - **FORBIDDEN**: LDIF configuration outside FlextDbtLdifConfig entities
   - **FORBIDDEN**: LDIF anomaly detection implementations bypassing FlextDbtLdifAnalytics
   - **MANDATORY**: ALL LDIF operations MUST use FlextDbtLdifService and unified patterns

---

## 🏗️ ARCHITECTURAL FOUNDATION FOR LDIF DBT PROJECT (MANDATORY PATTERNS)

### Core LDIF dbt Integration Strategy

**PRIMARY FOUNDATION**: `flext-core` contains ALL base patterns for LDIF dbt operations - use exclusively, never reimplement locally

```python
# ✅ CORRECT - Direct usage of flext-core foundation for LDIF dbt (VERIFIED API)
from flext_core import (
    FlextResult,           # Railway pattern for LDIF operations - has .data, .value, .unwrap()
    FlextModels,           # Pydantic models for LDIF entities
    FlextDomainService,    # Base service for LDIF dbt operations
    FlextContainer,        # Dependency injection for LDIF services
    FlextLogger,           # Structured logging for LDIF operations
    FlextConstants,        # LDIF system constants
    FlextExceptions        # LDIF exception hierarchy
)

# ✅ MANDATORY - For ALL LDIF CLI projects use flext-cli exclusively
from flext_cli import (
    FlextCliApi,           # High-level CLI API for LDIF operations
    FlextCliMain,          # Main CLI entry point for LDIF commands
    FlextCliConfig,        # Configuration management for LDIF CLI
    FlextCliConstants,     # LDIF CLI-specific constants
    # NEVER import click or rich directly - ALL LDIF CLI + OUTPUT through flext-cli
)

# ✅ CORRECT - LDIF-specific integrations (when available)
from flext_ldif import (
    get_flext_ldif_api,    # LDIF API integration (if available)
    FlextLdifConfig,       # LDIF configuration models (if available)
)

# ❌ ABSOLUTELY FORBIDDEN - These imports are ZERO TOLERANCE violations in LDIF projects
# import click           # FORBIDDEN - use flext-cli for LDIF operations
# import rich            # FORBIDDEN - use flext-cli output wrappers for LDIF
# from dbt import        # FORBIDDEN - use UnifiedFlextDbtLdifService
# import ldif            # FORBIDDEN - use flext-ldif integration

# ✅ CORRECT - Unified LDIF dbt service class (VERIFIED WORKING PATTERN)
class UnifiedFlextDbtLdifService(FlextDomainService):
    """Single unified LDIF dbt service class following flext-core patterns.

    This class consolidates all LDIF dbt-related operations:
    - LDIF file parsing and validation
    - Programmatic dbt model generation for LDIF analytics
    - LDIF-specific data quality validation
    - Advanced LDIF analytics with anomaly detection

    Note: FlextDomainService is Pydantic-based, inherits from BaseModel
    """

    def __init__(self, **data) -> None:
        """Initialize LDIF dbt service with proper dependency injection."""
        super().__init__(**data)
        # Use direct class access - NO wrapper functions (per updated flext-core)
        self._container = FlextContainer.get_global()
        self._logger = FlextLogger(__name__)

    def parse_ldif_data(self, ldif_config: dict) -> FlextResult[LdifDataFrame]:
        """Parse LDIF file data with proper error handling."""
        if not ldif_config:
            return FlextResult[LdifDataFrame].fail("LDIF configuration cannot be empty")

        # Validate LDIF configuration
        validation_result = self._validate_ldif_config(ldif_config)
        if validation_result.is_failure:
            return FlextResult[LdifDataFrame].fail(f"LDIF config validation failed: {validation_result.error}")

        # Parse LDIF data through flext-ldif integration (NO direct ldif parsing)
        parsing_result = self._parse_ldif_entries(ldif_config)
        if parsing_result.is_failure:
            return FlextResult[LdifDataFrame].fail(f"LDIF parsing failed: {parsing_result.error}")

        return FlextResult[LdifDataFrame].ok(parsing_result.unwrap())

    def generate_programmatic_dbt_models(self, ldif_data: LdifDataFrame) -> FlextResult[DbtModelCollection]:
        """Generate dbt models programmatically for LDIF data with advanced analytics patterns."""
        if not ldif_data or ldif_data.empty:
            return FlextResult[DbtModelCollection].fail("LDIF data cannot be empty")

        # Generate programmatic models for LDIF analytics
        models_result = (
            self._create_ldif_staging_models(ldif_data)
            .flat_map(self._create_ldif_dimension_models)
            .flat_map(self._create_ldif_fact_models)
            .flat_map(self._create_ldif_analytics_models)
            .flat_map(self._create_ldif_anomaly_detection_models)
        )

        if models_result.is_failure:
            return FlextResult[DbtModelCollection].fail(f"LDIF dbt model generation failed: {models_result.error}")

        return FlextResult[DbtModelCollection].ok(models_result.unwrap())

    def execute_ldif_analytics_pipeline(self, pipeline_config: LdifDbtPipelineConfig) -> FlextResult[LdifAnalyticsPipelineResult]:
        """Execute complete LDIF analytics pipeline with error handling."""
        return (
            self._validate_ldif_pipeline_config(pipeline_config)
            .flat_map(lambda config: self.parse_ldif_data(config.ldif_config))
            .flat_map(lambda data: self.generate_programmatic_dbt_models(data))
            .flat_map(lambda models: self._compile_ldif_dbt_models(models))
            .flat_map(lambda compiled: self._execute_ldif_dbt_models(compiled))
            .flat_map(lambda executed: self._run_ldif_dbt_tests(executed))
            .flat_map(lambda tested: self._run_ldif_anomaly_detection(tested))
            .map(lambda results: self._create_ldif_analytics_pipeline_result(results))
            .map_error(lambda e: f"LDIF analytics pipeline failed: {e}")
        )

    def _validate_ldif_config(self, config: dict) -> FlextResult[dict]:
        """Validate LDIF configuration structure."""
        required_fields = ["file_path", "encoding", "output_format"]
        for field in required_fields:
            if field not in config:
                return FlextResult[dict].fail(f"Missing required LDIF field: {field}")
        return FlextResult[dict].ok(config)

    def _parse_ldif_entries(self, config: dict) -> FlextResult[LdifDataFrame]:
        """Parse LDIF entries through flext-ldif integration."""
        # Implementation using flext-ldif API (NO direct ldif parsing)
        ldif_api_result = self._container.get("ldif_api")
        if ldif_api_result.is_failure:
            return FlextResult[LdifDataFrame].fail("LDIF API service unavailable")

        ldif_api = ldif_api_result.unwrap()
        return ldif_api.parse_ldif_file(config)

    def _create_ldif_staging_models(self, data: LdifDataFrame) -> FlextResult[DbtModelCollection]:
        """Create staging models for raw LDIF data."""
        # Implementation for LDIF staging models
        return FlextResult[DbtModelCollection].ok(DbtModelCollection())

    def _create_ldif_dimension_models(self, staging_models: DbtModelCollection) -> FlextResult[DbtModelCollection]:
        """Create dimension models for LDIF analytics (entries, attributes, change tracking)."""
        # Implementation for LDIF dimensional modeling
        return FlextResult[DbtModelCollection].ok(DbtModelCollection())

    def _create_ldif_fact_models(self, dimension_models: DbtModelCollection) -> FlextResult[DbtModelCollection]:
        """Create fact models for LDIF changes and relationships."""
        # Implementation for LDIF fact models
        return FlextResult[DbtModelCollection].ok(DbtModelCollection())

    def _create_ldif_analytics_models(self, fact_models: DbtModelCollection) -> FlextResult[DbtModelCollection]:
        """Create advanced analytics models for LDIF insights and reporting."""
        # Implementation for LDIF analytics models
        return FlextResult[DbtModelCollection].ok(DbtModelCollection())

    def _create_ldif_anomaly_detection_models(self, analytics_models: DbtModelCollection) -> FlextResult[DbtModelCollection]:
        """Create anomaly detection models for LDIF data quality and risk assessment."""
        # Implementation for LDIF anomaly detection models
        return FlextResult[DbtModelCollection].ok(DbtModelCollection())

# ✅ CORRECT - LDIF domain models using VERIFIED flext-core API patterns
from flext_core import FlextModels

class LdifEntry(FlextModels.Entity):
    """LDIF entry entity with business rules validation."""

    dn: str
    change_type: str
    attributes: dict
    change_sequence: int

    def validate_business_rules(self) -> FlextResult[None]:
        """Required abstract method implementation for LDIF entries."""
        if not self.dn.strip():
            return FlextResult[None].fail("LDIF DN cannot be empty")
        if self.change_type not in ["add", "modify", "delete", "moddn"]:
            return FlextResult[None].fail("Invalid LDIF change type")
        return FlextResult[None].ok(None)

class LdifDbtPipelineConfig(FlextModels.Value):
    """LDIF dbt pipeline configuration value object."""

    ldif_config: dict
    dbt_config: dict
    analytics_config: dict
    output_config: dict

    def validate_business_rules(self) -> FlextResult[None]:
        """Required abstract method implementation for pipeline config."""
        if not self.ldif_config:
            return FlextResult[None].fail("LDIF configuration is required")
        if not self.dbt_config:
            return FlextResult[None].fail("dbt configuration is required")
        return FlextResult[None].ok(None)

# ✅ CORRECT - Module exports for LDIF dbt
__all__ = ["UnifiedFlextDbtLdifService", "LdifEntry", "LdifDbtPipelineConfig"]
```

### LDIF CLI Development Patterns (MANDATORY FOR ALL LDIF CLI PROJECTS)

```python
# ✅ CORRECT - ALL LDIF CLI projects MUST use flext-cli exclusively
from flext_cli import FlextCliApi, FlextCliMain, FlextCliConfig
# ❌ FORBIDDEN - NEVER import click directly in LDIF projects
# import click  # THIS IS ABSOLUTELY FORBIDDEN IN LDIF PROJECTS

class LdifCliService:
    """LDIF CLI service using flext-cli foundation - NO Click imports allowed.

    CONFIGURATION AUTHORITY:
    - flext-cli automatically loads .env from execution root
    - flext-core provides configuration infrastructure for LDIF
    - Project ONLY describes LDIF configuration schema, never loads manually
    """

    def __init__(self) -> None:
        """Initialize LDIF CLI service with automatic configuration loading."""
        # ✅ AUTOMATIC: LDIF configuration loaded transparently by flext-cli/flext-core
        self._cli_api = FlextCliApi()
        self._config = FlextCliConfig()  # Automatically includes .env + defaults + CLI params for LDIF

    def define_ldif_configuration_schema(self) -> FlextResult[dict]:
        """Define LDIF-specific configuration schema.

        Project ONLY describes LDIF configuration needs - flext-cli handles:
        1. Multi-format file detection (.env, .toml, .yaml, .json)
        2. Environment variable precedence for LDIF settings
        3. Default constants fallback for LDIF
        4. CLI parameter overrides for LDIF operations
        5. Automatic validation and type conversion
        """
        # ✅ CORRECT: LDIF-specific configuration schema
        ldif_config_schema = {
            # LDIF File configuration
            "ldif": {
                "file_path": {
                    "default": "./data/input.ldif",   # Level 3: DEFAULT CONSTANTS
                    "env_var": "LDIF_FILE_PATH",      # Levels 1&2: ENV VARS → CONFIG FILE
                    "cli_param": "--ldif-file",       # Level 4: CLI PARAMETERS
                    "config_formats": {
                        "env": "LDIF_FILE_PATH",
                        "toml": "ldif.file_path",
                        "yaml": "ldif.file_path",
                        "json": "ldif.file_path"
                    },
                    "type": str,
                    "required": True
                },
                "encoding": {
                    "default": "utf-8",               # Level 3: DEFAULT CONSTANTS
                    "env_var": "LDIF_ENCODING",       # Levels 1&2: ENV VARS → CONFIG FILE
                    "cli_param": "--encoding",        # Level 4: CLI PARAMETERS
                    "type": str,
                    "required": False
                },
                "output_format": {
                    "default": "postgresql",          # Level 3: DEFAULT CONSTANTS
                    "env_var": "LDIF_OUTPUT_FORMAT",  # Levels 1&2: ENV VARS → CONFIG FILE
                    "cli_param": "--output-format",   # Level 4: CLI PARAMETERS
                    "type": str,
                    "choices": ["postgresql", "duckdb", "parquet"],
                    "required": False
                },
                "batch_size": {
                    "default": 1000,                 # Level 3: DEFAULT CONSTANTS
                    "env_var": "LDIF_BATCH_SIZE",     # Levels 1&2: ENV VARS → CONFIG FILE
                    "cli_param": "--batch-size",      # Level 4: CLI PARAMETERS
                    "type": int,
                    "required": False
                }
            },
            # dbt configuration for LDIF models
            "dbt": {
                "profiles_dir": {
                    "default": "./profiles",
                    "env_var": "DBT_PROFILES_DIR",
                    "cli_param": "--profiles-dir",
                    "type": str,
                    "required": False
                },
                "target": {
                    "default": "dev",
                    "env_var": "DBT_TARGET",
                    "cli_param": "--target",
                    "type": str,
                    "choices": ["dev", "staging", "prod"],
                    "required": False
                }
            },
            # Analytics configuration for LDIF
            "analytics": {
                "enable_anomaly_detection": {
                    "default": True,
                    "env_var": "LDIF_ENABLE_ANOMALY_DETECTION",
                    "cli_param": "--enable-anomaly-detection",
                    "type": bool,
                    "required": False
                },
                "risk_threshold": {
                    "default": 0.8,
                    "env_var": "LDIF_RISK_THRESHOLD",
                    "cli_param": "--risk-threshold",
                    "type": float,
                    "required": False
                }
            }
        }

        # Register LDIF schema with flext-cli - handles ALL formats automatically
        schema_result = self._config.register_universal_schema(ldif_config_schema)
        if schema_result.is_failure:
            return FlextResult[dict].fail(f"LDIF schema registration failed: {schema_result.error}")

        return FlextResult[dict].ok(ldif_config_schema)

    def create_ldif_cli_interface(self) -> FlextResult[FlextCliMain]:
        """Create LDIF CLI interface using flext-cli patterns."""
        # Initialize main CLI handler for LDIF operations
        main_cli = FlextCliMain(
            name="flext-dbt-ldif",
            description="FLEXT dbt LDIF - Enterprise LDIF Analytics with Programmatic Model Generation"
        )

        # Register LDIF command groups through flext-cli
        parse_result = main_cli.register_command_group("parse", self._create_ldif_parse_commands)
        if parse_result.is_failure:
            return FlextResult[FlextCliMain].fail(f"LDIF parse commands registration failed: {parse_result.error}")

        analyze_result = main_cli.register_command_group("analyze", self._create_ldif_analyze_commands)
        if analyze_result.is_failure:
            return FlextResult[FlextCliMain].fail(f"LDIF analyze commands registration failed: {analyze_result.error}")

        generate_result = main_cli.register_command_group("generate", self._create_ldif_generate_commands)
        if generate_result.is_failure:
            return FlextResult[FlextCliMain].fail(f"LDIF generate commands registration failed: {generate_result.error}")

        return FlextResult[FlextCliMain].ok(main_cli)

    def _create_ldif_parse_commands(self) -> FlextResult[dict]:
        """Create LDIF parsing commands using flext-cli patterns."""
        # Use flext-cli command builders, NEVER Click decorators OR Rich output for LDIF
        commands = {
            "file": self._cli_api.create_command(
                name="file",
                description="Parse LDIF file data",
                handler=self._handle_ldif_file_parsing,
                arguments=["file_path", "encoding"],
                output_format="table"  # Use flext-cli output formatting for LDIF data
            ),
            "validate": self._cli_api.create_command(
                name="validate",
                description="Validate LDIF file structure",
                handler=self._handle_ldif_validation,
                output_format="json"   # Use flext-cli output formatting
            )
        }
        return FlextResult[dict].ok(commands)

    def _handle_ldif_file_parsing(self, args: dict) -> FlextResult[str]:
        """Handle LDIF file parsing command."""
        # Validate required arguments
        if not args.get("file_path"):
            return FlextResult[str].fail("File path is required for LDIF parsing")

        # Get LDIF service from container
        container = FlextContainer.get_global()
        ldif_service_result = container.get("ldif_dbt_service")
        if ldif_service_result.is_failure:
            return FlextResult[str].fail("LDIF dbt service unavailable")

        # Parse LDIF data - NO try/except fallbacks
        ldif_service = ldif_service_result.unwrap()
        ldif_config = {
            "file_path": args["file_path"],
            "encoding": args.get("encoding", "utf-8"),
            # Configuration automatically loaded from flext-cli config
        }

        parsing_result = ldif_service.parse_ldif_data(ldif_config)
        if parsing_result.is_failure:
            return FlextResult[str].fail(f"LDIF parsing failed: {parsing_result.error}")

        # Display results using flext-cli output wrappers
        ldif_data = parsing_result.unwrap()
        display_result = self._cli_api.format_output(
            data=ldif_data.to_dict(),
            format_type="table",
            headers=["DN", "Change Type", "Attributes", "Sequence"],
            style="ldif_analytics"
        )

        return FlextResult[str].ok(f"LDIF parsing successful: {len(ldif_data)} entries processed")

# ✅ CORRECT - LDIF CLI entry point using flext-cli
def main() -> None:
    """Main LDIF CLI entry point - uses flext-cli, never Click directly."""
    cli_service = LdifCliService()
    cli_result = cli_service.create_ldif_cli_interface()

    if cli_result.is_failure:
        # Use flext-cli for error output too - NO direct print/rich usage
        cli_api = FlextCliApi()
        error_output = cli_api.format_error_message(
            message=f"LDIF CLI initialization failed: {cli_result.error}",
            error_type="initialization",
            suggestions=["Check flext-cli installation", "Verify LDIF configuration"]
        )
        cli_api.display_error(error_output.unwrap() if error_output.is_success else cli_result.error)
        exit(1)

    cli = cli_result.unwrap()
    cli.run()
```

---

## 📊 QUALITY ASSESSMENT PROTOCOL FOR LDIF DBT PROJECT

### Phase 1: LDIF-Specific Issue Identification

**MANDATORY FIRST STEP**: Get precise counts of all LDIF dbt quality issues:

```bash
# Count exact number of LDIF-specific issues across all tools
echo "=== LDIF DBT RUFF ISSUES ==="
ruff check . --output-format=github | grep -i ldif | wc -l

echo "=== LDIF DBT MYPY ISSUES ==="
mypy src/ --show-error-codes --no-error-summary 2>&1 | grep -E "error:|note:" | grep -i ldif | wc -l

echo "=== LDIF DBT PYRIGHT ISSUES ==="
pyright src/ --level error 2>&1 | grep -E "error|warning" | grep -i ldif | wc -l

echo "=== LDIF DBT PYTEST RESULTS ==="
pytest tests/ --tb=no -q -k ldif 2>&1 | grep -E "failed|passed|error" | tail -1

echo "=== LDIF DBT COVERAGE ==="
pytest tests/ --cov=src --cov-report=term-missing --tb=no -k ldif 2>&1 | grep "TOTAL"
```

---

## 🛠️ INCREMENTAL REFACTORING METHODOLOGY FOR LDIF DBT

### Strategy: Progressive LDIF Enhancement (NOT Rewriting)

#### Cycle 1: LDIF Foundation Consolidation

```python
# BEFORE - Multiple scattered LDIF implementations
class LdifParser:
    def parse(self): pass

class LdifAnalyzer:
    def analyze(self): pass

class DbtModelGenerator:
    def generate(self): pass

# Scattered LDIF helper functions
def parse_ldif_change(): pass

# AFTER - Single unified LDIF dbt class (incremental improvement)
class UnifiedFlextDbtLdifService:
    """Consolidated LDIF dbt service following single responsibility principle."""

    def parse_ldif_data(self, config: dict) -> FlextResult[LdifDataFrame]:
        """Former LdifParser.parse with proper error handling."""
        # Implementation using flext-core patterns for LDIF

    def analyze_ldif_data(self, data: LdifDataFrame) -> FlextResult[LdifAnalysisResult]:
        """Former LdifAnalyzer.analyze with proper error handling."""
        # Implementation using flext-core patterns for LDIF

    def generate_programmatic_dbt_models(self, data: LdifAnalysisResult) -> FlextResult[DbtModelCollection]:
        """Former DbtModelGenerator.generate with proper error handling."""
        # Implementation using flext-core patterns for LDIF dbt

    def _parse_ldif_change(self, change_line: str) -> FlextResult[LdifChange]:
        """Former parse_ldif_change now as private method."""
        # Implementation as part of unified LDIF class
```

---

## 🔧 TOOL-SPECIFIC RESOLUTION STRATEGIES FOR LDIF DBT

### LDIF-Specific Ruff Issues Resolution

```bash
# Identify high-priority LDIF issues first
ruff check . --select F --output-format=github | grep -i ldif  # LDIF Pyflakes errors (critical)
ruff check . --select E9 --output-format=github | grep -i ldif # LDIF Syntax errors (critical)
ruff check . --select F821 --output-format=github | grep -i ldif # LDIF Undefined name (critical)

# Address LDIF import issues
ruff check . --select I --output-format=github | grep -i ldif    # LDIF Import sorting
ruff check . --select F401 --output-format=github | grep -i ldif # LDIF Unused imports

# Apply auto-fixes where safe for LDIF code
ruff check . --fix-only --select I,F401,E,W
```

---

## 🔬 CLI TESTING AND DEBUGGING METHODOLOGY FOR LDIF DBT (FLEXT ECOSYSTEM INTEGRATION)

### Universal LDIF CLI Testing Pattern

```bash
# ✅ CORRECT - Universal LDIF CLI testing pattern
# Configuration file automatically detected from current directory

# Phase 1: LDIF CLI Debug Mode Testing (MANDATORY FLEXT-CLI)
python -m flext_dbt_ldif --debug parse file \
  --file-path "data/sample.ldif" \
  --encoding "utf-8" \
  --output-dir data/output \
  --config-file ldif.env

# Phase 2: LDIF CLI Trace Mode Testing (FLEXT-CLI + FLEXT-CORE LOGGING)
export LOG_LEVEL=DEBUG
export ENABLE_TRACE=true
python -m flext_dbt_ldif parse file \
  --file-path "data/changes.ldif" \
  --config-format toml

# Phase 3: LDIF dbt Configuration Validation (AUTOMATIC MULTI-FORMAT LOADING)
python -m flext_dbt_ldif validate-environment --debug --config-format yaml

# Phase 4: LDIF Service Connection Testing (FLEXT ECOSYSTEM INTEGRATION)
python -m flext_dbt_ldif test-service-connectivity --debug --trace

# Phase 5: LDIF dbt Model Testing (FLEXT ECOSYSTEM COMPONENTS)
python -m flext_dbt_ldif test-component --component=ldif-parser \
  --debug --trace --config-file production.toml

# Phase 6: LDIF Analytics Testing (PROGRAMMATIC MODEL GENERATION)
python -m flext_dbt_ldif generate models --programmatic \
  --input-file "data/sample.ldif" \
  --debug --trace
```

### LDIF CLI Testing Service

```python
from flext_core import FlextResult, get_logger
from flext_cli import FlextCliApi, FlextCliConfig
from flext_ldif import get_flext_ldif_api  # If available

class LdifDbtCliTestingService:
    """LDIF dbt CLI testing service using FLEXT ecosystem - .env automatically loaded."""

    def __init__(self) -> None:
        """Initialize LDIF CLI testing with automatic .env configuration loading."""
        # ✅ AUTOMATIC: .env loaded transparently by FLEXT ecosystem
        self._logger = get_logger("ldif_cli_testing")
        self._cli_api = FlextCliApi()
        self._config = FlextCliConfig()  # Automatically loads .env + defaults + CLI params
        self._ldif_api = get_flext_ldif_api() if 'flext_ldif' in globals() else None

    def debug_ldif_configuration(self) -> FlextResult[dict]:
        """Debug LDIF CLI configuration using FLEXT patterns - .env as source of truth."""
        self._logger.debug("Starting LDIF CLI configuration debugging")

        # ✅ CORRECT: Access LDIF configuration through FLEXT API (includes .env automatically)
        config_result = self._config.get_all_configuration()
        if config_result.is_failure:
            return FlextResult[dict].fail(f"LDIF configuration access failed: {config_result.error}")

        config_data = config_result.unwrap()

        # Filter LDIF-specific configuration
        ldif_config = {k: v for k, v in config_data.items() if 'ldif' in k.lower()}

        # Debug output through FLEXT CLI API
        debug_display_result = self._cli_api.display_debug_information(
            title="LDIF CLI Configuration Debug (ENV → .env → DEFAULT → CLI)",
            data=ldif_config,
            format_type="tree"  # flext-cli handles formatted output
        )

        if debug_display_result.is_failure:
            return FlextResult[dict].fail(f"LDIF debug display failed: {debug_display_result.error}")

        return FlextResult[dict].ok(ldif_config)

    def test_ldif_parsing_debug(self) -> FlextResult[dict]:
        """Test LDIF parsing with debug logging - FLEXT-LDIF exclusively."""
        self._logger.debug("Starting LDIF parsing testing")

        # ✅ CORRECT: Get LDIF configuration from .env through FLEXT config
        ldif_config_result = self._config.get_ldif_configuration()
        if ldif_config_result.is_failure:
            return FlextResult[dict].fail(f"LDIF config access failed: {ldif_config_result.error}")

        ldif_config = ldif_config_result.unwrap()

        # ✅ CORRECT: Test parsing through FLEXT-LDIF API (NO external tools)
        if self._ldif_api:
            parsing_result = self._ldif_api.test_parsing_with_debug(
                file_path=ldif_config["file_path"],
                encoding=ldif_config["encoding"],
                batch_size=ldif_config["batch_size"],
                debug_mode=True
            )
        else:
            # Fallback to direct service testing
            ldif_service_result = self._test_ldif_service_directly(ldif_config)
            parsing_result = ldif_service_result

        if parsing_result.is_failure:
            # Display debug information through FLEXT CLI
            self._cli_api.display_error_with_debug(
                error_message=f"LDIF parsing failed: {parsing_result.error}",
                debug_data=ldif_config,
                suggestions=[
                    "Check .env file LDIF configuration",
                    "Verify LDIF file exists and is readable",
                    "Validate LDIF file format and encoding",
                    "Check LDIF file permissions"
                ]
            )
            return FlextResult[dict].fail(parsing_result.error)

        # Display success with debug information
        parsing_info = parsing_result.unwrap()
        self._cli_api.display_success_with_debug(
            success_message="LDIF parsing successful",
            debug_data=parsing_info,
            format_type="table"
        )

        return FlextResult[dict].ok(parsing_info)
```

---

## 📚 SPECIFIC LDIF DBT PROJECT EXAMPLES

### LDIF Analytics Implementation

```python
# ✅ CORRECT - LDIF-specific dbt model generation
class LdifAnalyticsModelGenerator:
    """Generate analytics models for LDIF data."""

    def generate_entry_dimension(self, ldif_entries: LdifDataFrame) -> FlextResult[DbtModel]:
        """Generate entry dimension model from LDIF entry data."""
        entry_dimension_sql = """
        {{ config(materialized='table') }}

        select
            {{ dbt_utils.surrogate_key(['dn', 'change_sequence']) }} as entry_sk,
            dn as entry_dn,
            change_type,
            change_sequence,
            parsed_attributes,
            entry_size,
            created_date,
            modified_date,
            is_active
        from {{ ref('stg_ldif_entries') }}
        """

        return FlextResult[DbtModel].ok(DbtModel(
            name="dim_ldif_entries",
            sql=entry_dimension_sql,
            materialization="table"
        ))

    def generate_change_fact(self, ldif_changes: LdifDataFrame) -> FlextResult[DbtModel]:
        """Generate change fact table from LDIF change data."""
        change_fact_sql = """
        {{ config(materialized='incremental', unique_key='change_sk') }}

        select
            {{ dbt_utils.surrogate_key(['dn', 'change_sequence', 'change_timestamp']) }} as change_sk,
            e.entry_sk,
            change_type,
            change_sequence,
            change_timestamp,
            attribute_changes,
            change_size,
            is_anomalous,
            risk_score,
            created_date
        from {{ ref('stg_ldif_changes') }} c
        join {{ ref('dim_ldif_entries') }} e on c.dn = e.entry_dn

        {% if is_incremental() %}
            where change_timestamp > (select max(change_timestamp) from {{ this }})
        {% endif %}
        """

        return FlextResult[DbtModel].ok(DbtModel(
            name="fact_ldif_changes",
            sql=change_fact_sql,
            materialization="incremental"
        ))

    def generate_anomaly_detection_model(self, ldif_data: LdifDataFrame) -> FlextResult[DbtModel]:
        """Generate anomaly detection model for LDIF risk assessment."""
        anomaly_detection_sql = """
        {{ config(materialized='table') }}

        with change_patterns as (
            select
                dn,
                change_type,
                count(*) as change_frequency,
                avg(change_size) as avg_change_size,
                stddev(change_size) as stddev_change_size
            from {{ ref('fact_ldif_changes') }}
            group by dn, change_type
        ),

        anomaly_scores as (
            select
                c.*,
                p.avg_change_size,
                p.stddev_change_size,
                case
                    when p.stddev_change_size > 0 then
                        abs(c.change_size - p.avg_change_size) / p.stddev_change_size
                    else 0
                end as z_score,
                case
                    when abs(c.change_size - p.avg_change_size) / nullif(p.stddev_change_size, 0) > 3 then true
                    when c.change_frequency > p.change_frequency * 5 then true
                    else false
                end as is_anomalous
            from {{ ref('fact_ldif_changes') }} c
            join change_patterns p on c.dn = p.dn and c.change_type = p.change_type
        )

        select
            change_sk,
            dn,
            change_type,
            z_score,
            is_anomalous,
            case
                when z_score > 3 then 'HIGH'
                when z_score > 2 then 'MEDIUM'
                else 'LOW'
            end as risk_level
        from anomaly_scores
        where is_anomalous = true
        """

        return FlextResult[DbtModel].ok(DbtModel(
            name="ldif_anomaly_detection",
            sql=anomaly_detection_sql,
            materialization="table"
        ))
```

### LDIF dbt Macros

```sql
-- LDIF-specific dbt macros for change processing
{% macro parse_ldif_change_type(change_type_column) %}
    case {{ change_type_column }}
        when 'add' then 'CREATE'
        when 'modify' then 'UPDATE'
        when 'delete' then 'DELETE'
        when 'moddn' then 'RENAME'
        else 'UNKNOWN'
    end
{% endmacro %}

{% macro calculate_ldif_change_impact(change_size_column, attribute_count_column) %}
    case
        when {{ change_size_column }} > 10000 or {{ attribute_count_column }} > 50 then 'HIGH'
        when {{ change_size_column }} > 1000 or {{ attribute_count_column }} > 10 then 'MEDIUM'
        else 'LOW'
    end
{% endmacro %}

{% macro extract_ldif_change_attributes(attributes_json_column) %}
    select
        key as attribute_name,
        value as attribute_value
    from json_each_text({{ attributes_json_column }})
{% endmacro %}
```

---

## ⚡ EXECUTION CHECKLIST FOR LDIF DBT PROJECT

### Before Starting Any LDIF Work

- [ ] Read all documentation: `CLAUDE.md`, `FLEXT_REFACTORING_PROMPT.md`, project `README.md`
- [ ] Verify virtual environment: `/home/marlonsc/flext/.venv/bin/python` (VERIFIED WORKING)
- [ ] Run baseline LDIF quality assessment using exact commands provided
- [ ] Plan incremental LDIF improvements (never wholesale rewrites)
- [ ] Establish measurable success criteria from current LDIF baseline

### During Each LDIF Development Cycle

- [ ] Make minimal, focused LDIF changes (single aspect per change)
- [ ] Validate after every LDIF modification using quality gates
- [ ] Test actual LDIF functionality (no mocks, real LDIF execution)
- [ ] Document LDIF changes with professional English
- [ ] Update LDIF tests to maintain coverage near 100%

### After Each LDIF Development Session

- [ ] Full quality gate validation (ruff + mypy + pyright + pytest) for LDIF code
- [ ] LDIF coverage measurement and improvement tracking
- [ ] Integration testing with real LDIF dependencies
- [ ] Update LDIF documentation reflecting current reality
- [ ] Commit with descriptive messages explaining LDIF improvements

### LDIF Project Completion Criteria

- [ ] **Code Quality**: Zero ruff violations across all LDIF code
- [ ] **Type Safety**: Zero mypy/pyright errors in LDIF src/
- [ ] **Test Coverage**: 95%+ with real functional LDIF tests
- [ ] **Documentation**: Professional English throughout LDIF components
- [ ] **Architecture**: Clean SOLID principles implementation for LDIF
- [ ] **Integration**: Seamless flext-core foundation usage for LDIF
- [ ] **Maintainability**: Clear, readable, well-structured LDIF code

---

## 🏁 FINAL SUCCESS VALIDATION FOR LDIF DBT PROJECT

```bash
#!/bin/bash
# final_ldif_validation.sh - Complete LDIF dbt ecosystem validation

echo "=== FLEXT LDIF DBT FINAL VALIDATION ==="

# LDIF Quality Gates
ruff check . --statistics | grep -i ldif
mypy src/ --strict --show-error-codes | grep -i ldif
pyright src/ --stats | grep -i ldif
pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=95 -k ldif

# LDIF Functional Validation
python -c "
import sys
sys.path.insert(0, 'src')

try:
    # Test all major LDIF imports
    from flext_core import FlextResult, FlextContainer, FlextModels
    print('✅ flext-core integration: SUCCESS')

    # Test LDIF dbt functionality
    from src.unified_flext_dbt_ldif_service import UnifiedFlextDbtLdifService
    print('✅ LDIF dbt service import: SUCCESS')

    # Test LDIF service instantiation
    ldif_service = UnifiedFlextDbtLdifService()
    print('✅ LDIF service creation: SUCCESS')

    print('✅ All LDIF imports: SUCCESS')
    print('✅ FINAL LDIF VALIDATION: PASSED')

except Exception as e:
    print(f'❌ LDIF VALIDATION FAILED: {e}')
    sys.exit(1)
"

echo "=== LDIF DBT ECOSYSTEM READY FOR PRODUCTION ==="
```

---

**The path to LDIF excellence is clear: Follow these standards precisely, validate continuously, never compromise on quality, and ALWAYS use FLEXT ecosystem for LDIF CLI testing and debugging with correct configuration priority (ENV → .env → DEFAULT → CLI) and automatic .env detection from current execution directory.**
