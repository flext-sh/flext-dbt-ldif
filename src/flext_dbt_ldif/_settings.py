"""Settings for DBT LDIF package."""

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated

from pydantic import BaseModel, Field
from pydantic_settings import SettingsConfigDict

from flext_meltano import FlextMeltanoSettings


class FlextDbtLdifSettings(FlextMeltanoSettings):
    """Runtime settings for DBT LDIF transformations."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDIF_", env_nested_delimiter="__", extra="ignore"
    )

    class _DbtLdif(BaseModel):
        """Namespaced dbt-LDIF transformation settings."""

        ldif_file_path: Annotated[
            str, Field(default="", description="Path to LDIF file for processing")
        ]
        min_quality_threshold: Annotated[
            float,
            Field(
                default=0.8,
                ge=0.0,
                le=1.0,
                description="Minimum data quality score threshold",
            ),
        ]

    if TYPE_CHECKING:
        DbtLdif: _DbtLdif
    else:
        DbtLdif: _DbtLdif = Field(
            default_factory=_DbtLdif, description="Namespaced dbt-LDIF settings."
        )


settings: FlextDbtLdifSettings = FlextDbtLdifSettings.fetch_global()
"""Pre-instantiated project settings singleton — ``from flext_dbt_ldif import settings``."""
