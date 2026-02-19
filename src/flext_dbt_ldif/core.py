"""Core helpers for DBT LDIF model metadata."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextResult


class FlextDbtLdifCore:
    """Core namespace containing simple model and analytics helpers."""

    class ModelGenerator:
        """Generate static model metadata used by higher services."""

        def __init__(self, project_dir: Path | None = None) -> None:
            """Initialize model generator."""
            self.project_dir = project_dir or Path.cwd()

        def generate_staging_models(self) -> list[dict[str, str]]:
            """Generate default staging model metadata."""
            return [
                {
                    "name": "stg_ldif_entries",
                    "description": "Staging model for LDIF entries",
                },
            ]

        def generate_analytics_models(self) -> list[dict[str, str]]:
            """Generate default analytics model metadata."""
            return [
                {
                    "name": "analytics_ldif_insights",
                    "description": "Analytics model for LDIF insights",
                },
            ]

    class Analytics:
        """Compute basic analysis metrics for LDIF-like payloads."""

        def analyze_entry_patterns(
            self,
            entries: list[dict[str, str]],
        ) -> FlextResult[dict[str, object]]:
            """Analyze input entries and return summary payload."""
            return FlextResult[dict[str, object]].ok(
                {
                    "total_entries": len(entries),
                    "unique_dns": len({entry.get("dn", "") for entry in entries}),
                },
            )


__all__ = ["FlextDbtLdifCore"]
