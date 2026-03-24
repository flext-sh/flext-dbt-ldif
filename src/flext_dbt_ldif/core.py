"""Core helpers for DBT LDIF model metadata."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from flext_core import r

from flext_dbt_ldif import c, t


class FlextDbtLdifCore:
    """Core namespace containing simple model and analytics helpers."""

    class ModelGenerator:
        """Generate static model metadata used by higher services."""

        def __init__(self, project_dir: Path | None = None) -> None:
            """Initialize model generator."""
            self.project_dir = project_dir or Path.cwd()

        def generate_analytics_models(self) -> Sequence[t.StrMapping]:
            """Generate default analytics model metadata."""
            return [
                {
                    "name": c.DbtLdif.ANALYTICS_MODEL_NAME,
                    "description": c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION,
                }
            ]

        def generate_staging_models(self) -> Sequence[t.StrMapping]:
            """Generate default staging model metadata."""
            return [
                {
                    "name": c.DbtLdif.STAGING_MODEL_NAME,
                    "description": c.DbtLdif.STAGING_MODEL_DESCRIPTION,
                }
            ]

    class Analytics:
        """Compute basic analysis metrics for LDIF-like payloads."""

        def analyze_entry_patterns(
            self, entries: Sequence[t.StrMapping]
        ) -> r[Mapping[str, t.ContainerValue]]:
            """Analyze input entries and return summary payload."""
            return r[t.ContainerValueMapping].ok({
                "total_entries": len(entries),
                "unique_dns": len({entry.get("dn", "") for entry in entries}),
            })


__all__ = ["FlextDbtLdifCore"]
