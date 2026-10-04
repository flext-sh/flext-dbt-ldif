"""Core mixin for dbt-ldif utilities.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/services/core
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_dbt_ldif import c, p, r, t


class FlextDbtLdifCore:
    """Mixin providing Core namespace for dbt-ldif utilities."""

    class Core:
        """Core namespace containing simple model and analytics helpers."""

        class ModelGenerator:
            """Generate static model metadata used by higher services."""

            def __init__(self, project_dir: Path | None = None) -> None:
                """Initialize model generator."""
                self.project_dir = project_dir or Path.cwd()

            @staticmethod
            def generate_analytics_models() -> t.SequenceOf[t.StrMapping]:
                """Generate default analytics model metadata.

                Returns:
                    The resulting ``t.SequenceOf[t.StrMapping]``.
                """
                return [
                    {
                        "name": c.DbtLdif.ANALYTICS_MODEL_NAME,
                        "description": c.DbtLdif.ANALYTICS_MODEL_DESCRIPTION,
                    },
                ]

            @staticmethod
            def generate_staging_models() -> t.SequenceOf[t.StrMapping]:
                """Generate default staging model metadata.

                Returns:
                    The resulting ``t.SequenceOf[t.StrMapping]``.
                """
                return [
                    {
                        "name": c.DbtLdif.STAGING_MODEL_NAME,
                        "description": c.DbtLdif.STAGING_MODEL_DESCRIPTION,
                    },
                ]

        class Analytics:
            """Compute basic analysis metrics for LDIF-like payloads."""

            @staticmethod
            def analyze_entry_patterns(
                entries: t.SequenceOf[t.StrMapping],
            ) -> p.Result[t.JsonMapping]:
                """Analyze input entries and return summary payload.

                Returns:
                    The resulting ``p.Result[t.JsonMapping]``.
                """
                return r[t.JsonMapping].ok({
                    "total_entries": len(entries),
                    "unique_dns": len({entry.get("dn", "") for entry in entries}),
                })
