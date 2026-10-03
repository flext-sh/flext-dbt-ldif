"""DBT LDIF domain constants namespace owner.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextDbtLdifConstantsBase:
    """DBT LDIF domain constants declared under the ``_constants`` owner."""

    class DbtLdif:
        """DBT LDIF domain constants namespace."""

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


__all__: list[str] = ["FlextDbtLdifConstantsBase"]
