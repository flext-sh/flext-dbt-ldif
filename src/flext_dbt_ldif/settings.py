"""Settings for DBT LDIF package."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextResult, FlextSettings
from pydantic import Field
from pydantic_settings import SettingsConfigDict

from .constants import c


class FlextDbtLdifSettings(FlextSettings):
    """Runtime settings model for LDIF to DBT workflow."""

    model_config = SettingsConfigDict(
        env_prefix="FLEXT_DBT_LDIF_",
        case_sensitive=False,
        extra="ignore",
    )

    ldif_file_path: str = ""
    ldif_encoding: str = c.DEFAULT_LDIF_ENCODING
    ldif_max_file_size: int = c.MAX_FILE_SIZE_GB
    dbt_project_dir: str = "."
    dbt_profiles_dir: str = c.DEFAULT_DBT_PROFILES_DIR
    dbt_target: str = c.DEFAULT_DBT_TARGET
    dbt_threads: int = 4
    dbt_log_level: str = c.DbtLogLevels.INFO.value
    min_quality_threshold: float = Field(default=0.8, ge=0.0, le=1.0)

    def get_schema_for_entry_type(self, entry_type: str) -> str:
        """Get deterministic schema name for LDIF entry type."""
        return f"stg_{entry_type}"

    def validate_runtime(self) -> FlextResult[bool]:
        """Validate basic runtime invariants."""
        if self.dbt_threads <= 0:
            return FlextResult[bool].fail("dbt_threads must be positive")
        if not (0.0 <= self.min_quality_threshold <= 1.0):
            return FlextResult[bool].fail("min_quality_threshold must be in [0, 1]")
        return FlextResult[bool].ok(value=True)

    @property
    def dbt_project_path(self) -> Path:
        """Resolved project path helper."""
        return Path(self.dbt_project_dir)


__all__ = ["FlextDbtLdifSettings"]
