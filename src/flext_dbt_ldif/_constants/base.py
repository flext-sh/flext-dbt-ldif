"""DBT LDIF domain constants namespace owner.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar


class FlextDbtLdifConstantsBase:
    """DBT LDIF domain constants declared under the ``_constants`` owner."""

    class DbtLdif:
        """DBT LDIF domain constants namespace."""

        GENERATOR_SERVICE_NAME: ClassVar[str] = "ldif_generator"
        STAGING_MODEL_NAME: ClassVar[str] = "stg_ldif_entries"
        STAGING_MODEL_DESCRIPTION: ClassVar[str] = "Staging model for LDIF entries"
        ANALYTICS_MODEL_NAME: ClassVar[str] = "analytics_ldif_insights"
        ANALYTICS_MODEL_DESCRIPTION: ClassVar[str] = "Analytics model for LDIF insights"
        DBT_MODEL_TYPE_STAGING: ClassVar[str] = "staging"
        DBT_MODEL_TYPE_ANALYTICS: ClassVar[str] = "analytics"
        DBT_MATERIALIZATION_VIEW: ClassVar[str] = "view"
        DBT_MATERIALIZATION_TABLE: ClassVar[str] = "table"
        LDIF_SOURCE_NAME: ClassVar[str] = "ldif_entries"
        SAMPLE_LDIF_DN: ClassVar[str] = "cn=sample,dc=example,dc=org"
        DEFAULT_QUALITY_SCORE: ClassVar[float] = 1.0
        VALIDATION_STATUS_PASSED: ClassVar[str] = "passed"
        TRANSFORMATION_STATUS_SUCCESS: ClassVar[str] = "success"
        WORKFLOW_STATUS_COMPLETED: ClassVar[str] = "completed"
        WORKFLOW_STATUS_READY: ClassVar[str] = "ready"


__all__: list[str] = ["FlextDbtLdifConstantsBase"]
