"""Settings for DBT LDIF package."""

from __future__ import annotations

from typing import Annotated, ClassVar

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from flext_core import FlextSettings
from flext_dbt_ldif import c


@FlextSettings.auto_register("dbt-ldif")
class FlextDbtLdifSettings(FlextSettings):
    """Runtime settings for DBT LDIF transformations."""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDIF_",
        extra="ignore",
    )

    ldif_file_path: Annotated[
        str,
        Field(
            default=c.DbtLdif.DEFAULT_LDIF_FILE_PATH,
            description="Path to LDIF file for processing",
        ),
    ]
    min_quality_threshold: Annotated[
        float,
        Field(
            default=c.DbtLdif.DEFAULT_QUALITY_THRESHOLD,
            ge=0.0,
            le=1.0,
            description="Minimum data quality score threshold",
        ),
    ]
