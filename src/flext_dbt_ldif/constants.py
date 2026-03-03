"""Constants for DBT LDIF workflows."""

from __future__ import annotations

from enum import StrEnum
from typing import Final

from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants

from flext_dbt_ldif.__version__ import __version__

PROJECT_VERSION: Final[str] = __version__
VERSION: Final[str] = __version__


class FlextDbtLdifConstants(FlextMeltanoConstants, FlextLdifConstants):
    """Typed constants used by DBT LDIF modules."""

    DEFAULT_LDIF_ENCODING: Final[str] = "utf-8"
    DEFAULT_DBT_PROFILES_DIR: Final[str] = "./profiles"
    DEFAULT_DBT_TARGET: Final[str] = "dev"
    DEFAULT_OUTPUT_FORMAT: Final[str] = "duckdb"
    MIN_FILE_SIZE_KB: Final[int] = 1024
    MAX_FILE_SIZE_GB: Final[int] = 1024 * 1024 * 1024
    CLI_COMMAND_INFO: Final[str] = "info"
    CLI_COMMAND_GENERATE: Final[str] = "generate"
    CLI_COMMAND_VALIDATE: Final[str] = "validate"
    PACKAGE_NAME: Final[str] = "FLEXT dbt LDIF"
    PACKAGE_DESCRIPTION: Final[str] = "Advanced LDAP Data Analytics and Transformations"
    DEFAULT_OUTPUT_FORMAT_CLI: Final[str] = "json"
    STAGING_MODEL_NAME: Final[str] = "stg_ldif_entries"
    STAGING_MODEL_DESCRIPTION: Final[str] = "Staging model for LDIF entries"
    ANALYTICS_MODEL_NAME: Final[str] = "analytics_ldif_insights"
    ANALYTICS_MODEL_DESCRIPTION: Final[str] = "Analytics model for LDIF insights"
    DBT_MODEL_TYPE_STAGING: Final[str] = "staging"
    DBT_MODEL_TYPE_ANALYTICS: Final[str] = "analytics"
    DBT_MATERIALIZATION_VIEW: Final[str] = "view"
    DBT_MATERIALIZATION_TABLE: Final[str] = "table"
    LDIF_SOURCE_NAME: Final[str] = "ldif_entries"
    LDIF_RAW_SOURCE: Final[str] = "raw_ldif_entries"
    SAMPLE_LDIF_DN: Final[str] = "cn=sample,dc=example,dc=org"
    DEFAULT_QUALITY_SCORE: Final[float] = 1.0
    VALIDATION_STATUS_PASSED: Final[str] = "passed"
    VALIDATION_STATUS_COMPLETED: Final[str] = "completed"
    TRANSFORMATION_STATUS_SUCCESS: Final[str] = "success"
    WORKFLOW_STATUS_COMPLETED: Final[str] = "completed"
    WORKFLOW_STATUS_READY: Final[str] = "ready"
    EXIT_CODE_SUCCESS: Final[int] = 0
    EXIT_CODE_FAILURE: Final[int] = 1

    class DbtLogLevels(StrEnum):
        """Allowed DBT log levels."""

        DEBUG = "debug"
        INFO = "info"
        WARN = "warn"
        ERROR = "error"

    class DbtTargets(StrEnum):
        """Supported DBT targets."""

        DEV = "dev"
        STAGING = "staging"
        PROD = "prod"

    class ErrorCode(StrEnum):
        """DBT LDIF error code identifiers."""

        DBT_LDIF_ERROR = "DBT_LDIF_ERROR"
        VALIDATION_ERROR = "DBT_LDIF_VALIDATION_ERROR"
        CONFIGURATION_ERROR = "DBT_LDIF_CONFIGURATION_ERROR"
        CONNECTION_ERROR = "DBT_LDIF_CONNECTION_ERROR"
        PROCESSING_ERROR = "DBT_LDIF_PROCESSING_ERROR"
        AUTHENTICATION_ERROR = "DBT_LDIF_AUTHENTICATION_ERROR"
        TIMEOUT_ERROR = "DBT_LDIF_TIMEOUT_ERROR"
        PARSE_ERROR = "DBT_LDIF_PARSE_ERROR"
        MODEL_ERROR = "DBT_LDIF_MODEL_ERROR"
        TRANSFORMATION_ERROR = "DBT_LDIF_TRANSFORMATION_ERROR"
        TEST_ERROR = "DBT_LDIF_TEST_ERROR"


c = FlextDbtLdifConstants
__all__ = ["FlextDbtLdifConstants", "c"]
