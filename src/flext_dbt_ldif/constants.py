"""Constants for DBT LDIF workflows."""

from __future__ import annotations

from enum import StrEnum
from typing import Final

from flext_core import FlextConstants


class FlextDbtLdifConstants(FlextConstants):
    """Typed constants used by DBT LDIF modules."""

    DEFAULT_LDIF_ENCODING: Final[str] = "utf-8"
    DEFAULT_DBT_PROFILES_DIR: Final[str] = "./profiles"
    DEFAULT_DBT_TARGET: Final[str] = "dev"
    DEFAULT_OUTPUT_FORMAT: Final[str] = "duckdb"
    MIN_FILE_SIZE_KB: Final[int] = 1024
    MAX_FILE_SIZE_GB: Final[int] = 1024 * 1024 * 1024

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
