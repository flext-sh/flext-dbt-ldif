"""Settings for DBT LDIF package."""

from __future__ import annotations

from typing import Annotated

from pydantic import Field

from flext_core import FlextLogger, FlextSettings

logger = FlextLogger(__name__)


class FlextDbtLdifSettings(FlextSettings):
    """Runtime settings for DBT LDIF transformations."""

    ldif_file_path: Annotated[
        str,
        Field(default="", description="Path to LDIF file for processing"),
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


__all__ = ["FlextDbtLdifSettings"]
