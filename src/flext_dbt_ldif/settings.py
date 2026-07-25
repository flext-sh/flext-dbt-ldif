"""Settings for DBT LDIF package."""

from __future__ import annotations

from typing import Annotated, ClassVar

from flext_core import FlextSettingsBase
from flext_dbt_ldif import c, m, u


class FlextDbtLdifSettings(FlextSettingsBase):
    """Runtime settings for DBT LDIF transformations."""

    model_config: ClassVar[m.SettingsConfigDict] = m.SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDIF_", extra="ignore"
    )

    ldif_file_path: Annotated[
        str,
        u.Field(
            default=c.DbtLdif.DEFAULT_LDIF_FILE_PATH,
            description="Path to LDIF file for processing",
        ),
    ]
    min_quality_threshold: Annotated[
        float,
        u.Field(
            default=c.DbtLdif.DEFAULT_QUALITY_THRESHOLD,
            ge=0.0,
            le=1.0,
            description="Minimum data quality score threshold",
        ),
    ]
