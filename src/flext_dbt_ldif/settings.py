"""Settings for DBT LDIF package."""

from __future__ import annotations

from flext_core import FlextLogger, FlextSettings
from pydantic import Field

logger = FlextLogger(__name__)


class FlextDbtLdifSettings(FlextSettings):
    """Runtime settings for DBT LDIF transformations."""

    ldif_file_path: str = Field(
        default="", description="Path to LDIF file for processing"
    )
    min_quality_threshold: float = Field(
        default=0.8, ge=0.0, le=1.0, description="Minimum data quality score threshold"
    )


__all__ = ["FlextDbtLdifSettings"]
