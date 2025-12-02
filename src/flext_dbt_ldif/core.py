"""Core functionality for FLEXT dbt LDIF.

This module provides core DBT LDIF functionality using flext-ldif APIs directly.
Uses types from typings.py and FlextTypes, no dict[str, object].
Uses Python 3.13+ PEP 695 syntax and direct API calls.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import override

from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_ldif import FlextLdif, FlextLdifModels

from flext_dbt_ldif.typings import FlextDbtLdifTypes

logger = FlextLogger(__name__)

# Constants for magic number elimination
HIGH_VALIDITY_THRESHOLD = 0.95
MEDIUM_VALIDITY_THRESHOLD = 0.8


class FlextDbtLdifCore:
    """Unified DBT LDIF core functionality with nested service classes.

    Uses flext-ldif APIs directly - no wrappers or unnecessary conversions.
    Uses types from typings.py - no dict[str, object].
    """

    class ModelGenerator:
        """Generates dbt models programmatically for LDIF analytics.

        Uses types from typings.py - no dict[str, object].
        """

        @override
        def __init__(self, project_dir: Path | None = None) -> None:
            """Initialize the model generator.

            Args:
                project_dir: Path to the dbt project directory (defaults to current)

            """
            self.project_dir = project_dir if project_dir is not None else Path.cwd()
            self.models_dir = self.project_dir / "models"

        def generate_staging_models(
            self,
        ) -> Sequence[FlextDbtLdifTypes.DbtLdifModel.ModelDefinition]:
            """Generate staging layer models for LDIF data.

            Returns:
                Sequence of generated model definitions

            """
            logger.info("Generating staging models for LDIF data")

            # This is where the sophisticated model generation logic would go
            # Based on the manifest.json analysis, we know these models exist:
            return [
                FlextDbtLdifTypes.DbtLdifModel.ModelDefinition(
                    name="stg_ldif_entries",
                    description="Staging model for LDIF entries with data quality checks",
                    columns=[
                        {
                            "name": "dn",
                            "description": "Distinguished Name",
                            "data_type": "varchar",
                        },
                        {
                            "name": "object_class",
                            "description": "Object class",
                            "data_type": "varchar",
                        },
                        {
                            "name": "is_valid_dn",
                            "description": "DN validity flag",
                            "data_type": "boolean",
                        },
                        {
                            "name": "dn_depth",
                            "description": "DN depth",
                            "data_type": "integer",
                        },
                        {
                            "name": "entry_type",
                            "description": "Entry type",
                            "data_type": "varchar",
                        },
                        {
                            "name": "primary_object_class",
                            "description": "Primary object class",
                            "data_type": "varchar",
                        },
                        {
                            "name": "processed_at",
                            "description": "Processing timestamp",
                            "data_type": "timestamp",
                        },
                    ],
                ),
            ]

        def generate_analytics_models(
            self,
        ) -> Sequence[FlextDbtLdifTypes.DbtLdifModel.ModelDefinition]:
            """Generate analytics layer models.

            Returns:
                Sequence of analytics model definitions

            """
            logger.info("Generating analytics models")

            return [
                FlextDbtLdifTypes.DbtLdifModel.ModelDefinition(
                    name="analytics_ldif_insights",
                    description="Advanced analytics model with sophisticated SQL patterns",
                    columns=[],
                ),
            ]

    class Analytics:
        """LDIF-specific analytics functionality using flext-ldif infrastructure.

        This class eliminates code duplication by delegating ALL analytics operations
        to the FlextLdif API directly, maintaining business rule compliance.
        Uses flext-ldif Entry objects directly - no dict conversions.
        """

        @override
        def __init__(self) -> None:
            """Initialize analytics with flext-ldif API."""
            self._ldif_api = FlextLdif()

        def analyze_entry_patterns(
            self,
            entries: Sequence[FlextLdifModels.Entry],
        ) -> FlextResult[FlextTypes.JsonDict]:
            """Analyze patterns in LDIF entries using flext-ldif infrastructure.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects

            Returns:
                FlextResult[FlextTypes.JsonDict]: Analysis results or error

            """
            logger.info(
                "Analyzing patterns in %d LDIF entries using flext-ldif",
                len(entries),
            )

            try:
                # Use flext-ldif API for statistics - NO local logic
                stats_result = self._ldif_api.get_entry_statistics(entries)
                if not stats_result.success:
                    return FlextResult[FlextTypes.JsonDict].fail(
                        f"Statistics generation failed: {stats_result.error}",
                    )

                stats = stats_result.value or {}

                # Get object class distribution using flext-ldif filtering
                object_classes: FlextTypes.IntDict = {}
                for entry in entries:
                    # Get object classes from the entry's object classes method
                    for obj_class in entry.get_object_classes():
                        object_classes[obj_class] = object_classes.get(obj_class, 0) + 1

                # Use flext-ldif hierarchical sorting for depth analysis
                sorted_result = self._ldif_api.sort_hierarchically(entries)
                dn_depth_distribution: FlextTypes.IntDict = {}
                if sorted_result.success and sorted_result.value:
                    for entry in sorted_result.value:
                        depth = entry.dn.get_depth()
                        depth_key = f"depth_{depth}"
                        dn_depth_distribution[depth_key] = (
                            dn_depth_distribution.get(depth_key, 0) + 1
                        )

                # Simple risk assessment based on entry count and validity
                total_entries = len(entries)
                valid_entries = len(
                    [e for e in entries if e.validate_business_rules().success],
                )
                validity_ratio = (
                    valid_entries / total_entries if total_entries > 0 else 0.0
                )

                if (
                    validity_ratio >= HIGH_VALIDITY_THRESHOLD
                    or validity_ratio >= MEDIUM_VALIDITY_THRESHOLD
                ):
                    pass

                return FlextResult[FlextTypes.JsonDict].ok(
                    {
                        "total_entries": stats.get("total_entries", 0),
                        "persons": stats.get("person_entries", 0),
                        "groups": stats.get("group_entries", 0),
                        "organizational_units": stats.get("other_entries", 0),
                        "valid_entries": stats.get("valid_entries", 0),
                        "unique_object_classes": list(object_classes.keys()),
                        "object_class_distribution": dict(object_classes),
                        "dn_depth_distribution": dict(dn_depth_distribution),
                        "risk_assessment": {
                            "validity_ratio": validity_ratio,
                            "threshold": HIGH_VALIDITY_THRESHOLD,
                        },
                    },
                )

            except Exception as e:
                logger.exception("Entry pattern analysis failed")
                return FlextResult[FlextTypes.JsonDict].fail(f"Analysis failed: {e}")

        def generate_quality_metrics(
            self,
            entries: Sequence[FlextLdifModels.Entry],
        ) -> FlextResult[FlextTypes.FloatDict]:
            """Generate data quality metrics using flext-ldif validation.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects

            Returns:
                FlextResult[FlextTypes.FloatDict]: Quality metrics or error

            """
            if not entries:
                return FlextResult[FlextTypes.FloatDict].ok({
                    "completeness": 0.0,
                    "validity": 0.0,
                    "consistency": 0.0,
                })

            try:
                total_entries = len(entries)

                # Use flext-ldif validation - NO local validation logic
                valid_result = self._ldif_api.filter_valid(entries)
                valid_entries = len(valid_result.value or [])

                # Calculate metrics based on flext-ldif operations
                completeness = (
                    100.0  # All entries are complete if they're Entry objects
                )
                validity = (
                    (valid_entries / total_entries) * 100.0
                    if total_entries > 0
                    else 0.0
                )

                # Consistency check using flext-ldif entry statistics
                stats_result = self._ldif_api.get_entry_statistics(entries)
                consistency = 100.0  # Default high consistency
                if stats_result.success and stats_result.value:
                    stats = stats_result.value
                    # Check consistency based on valid vs total ratio
                    if stats.get("total", 0) > 0:
                        consistency = (
                            stats.get("valid", 0) / stats.get("total", 1)
                        ) * 100.0

                return FlextResult[FlextTypes.FloatDict].ok({
                    "completeness": round(completeness, 2),
                    "validity": round(validity, 2),
                    "consistency": round(consistency, 2),
                })

            except Exception as e:
                logger.exception("Quality metrics generation failed")
                return FlextResult[FlextTypes.FloatDict].fail(
                    f"Quality metrics failed: {e}",
                )

        def get_statistics_for_dbt(
            self,
            entries: Sequence[FlextLdifModels.Entry],
        ) -> FlextResult[FlextTypes.JsonDict]:
            """Get statistics formatted for dbt model generation.

            Args:
                entries: Sequence of FlextLdifModels.Entry objects

            Returns:
                FlextResult[FlextTypes.JsonDict]: DBT-compatible statistics or error

            """
            try:
                # Use flext-ldif API for all statistics
                stats_result = self._ldif_api.get_entry_statistics(entries)
                if not stats_result.success:
                    return FlextResult[FlextTypes.JsonDict].fail(
                        f"dbt statistics failed: {stats_result.error}",
                    )

                return FlextResult[FlextTypes.JsonDict].ok(
                    stats_result.value or {},
                )

            except Exception as e:
                logger.exception("dbt statistics generation failed")
                return FlextResult[FlextTypes.JsonDict].fail(
                    f"dbt statistics error: {e}",
                )


__all__: list[str] = [
    "FlextDbtLdifCore",
]
