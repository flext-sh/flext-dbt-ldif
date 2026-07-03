"""Constants for DBT LDIF workflows."""

from __future__ import annotations

from enum import StrEnum, unique
from typing import Final

from flext_ldif import FlextLdifConstants
from flext_meltano import c


class FlextDbtLdifConstants(c, FlextLdifConstants):
    """Typed constants used by DBT LDIF modules."""

    class DbtLdif:
        """DBT LDIF domain constants namespace."""

        DEFAULT_LDIF_FILE_PATH: Final[str] = ""
        DEFAULT_QUALITY_THRESHOLD: Final[float] = 0.8

        @unique
        class ErrorCode(StrEnum):
            """DBT LDIF error code identifiers."""

            VALIDATION_ERROR = "DBT_LDIF_VALIDATION_ERROR"
            CONFIGURATION_ERROR = "DBT_LDIF_CONFIGURATION_ERROR"
            CONNECTION_ERROR = "DBT_LDIF_CONNECTION_ERROR"
            PROCESSING_ERROR = "DBT_LDIF_PROCESSING_ERROR"
            AUTHENTICATION_ERROR = "DBT_LDIF_AUTHENTICATION_ERROR"
            TIMEOUT_ERROR = "DBT_LDIF_TIMEOUT_ERROR"
            PARSE_ERROR = "DBT_LDIF_PARSE_ERROR"
            TEST_ERROR = "DBT_LDIF_TEST_ERROR"

        STAGING_MODEL_NAME: Final[str] = "stg_ldif_entries"
        STAGING_MODEL_DESCRIPTION: Final[str] = "Staging model for LDIF entries"
        ANALYTICS_MODEL_NAME: Final[str] = "analytics_ldif_insights"
        ANALYTICS_MODEL_DESCRIPTION: Final[str] = "Analytics model for LDIF insights"
        DBT_MODEL_TYPE_STAGING: Final[str] = "staging"
        DBT_MODEL_TYPE_ANALYTICS: Final[str] = "analytics"
        DBT_MATERIALIZATION_VIEW: Final[str] = "view"
        DBT_MATERIALIZATION_TABLE: Final[str] = "table"
        LDIF_SOURCE_NAME: Final[str] = "ldif_entries"
        SAMPLE_LDIF_DN: Final[str] = "cn=sample,dc=example,dc=org"
        DEFAULT_QUALITY_SCORE: Final[float] = 1.0
        VALIDATION_STATUS_PASSED: Final[str] = "passed"
        TRANSFORMATION_STATUS_SUCCESS: Final[str] = "success"
        WORKFLOW_STATUS_COMPLETED: Final[str] = "completed"
        WORKFLOW_STATUS_READY: Final[str] = "ready"


__all__: list[str] = ["FlextDbtLdifConstants", "c"]

c = FlextDbtLdifConstants
