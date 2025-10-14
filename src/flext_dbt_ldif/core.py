"""Core functionality for FLEXT dbt LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import override

from flext_core import FlextCore
from flext_ldif import FlextLdif, FlextLdifModels

from flext_dbt_ldif.typings import FlextDbtLdifTypes

logger = FlextCore.Logger(__name__)

# Constants for magic number elimination
HIGH_VALIDITY_THRESHOLD = 0.95
MEDIUM_VALIDITY_THRESHOLD = 0.8


class FlextDbtLdifCore:
    """Unified DBT LDIF core functionality with nested service classes."""

    class ModelGenerator:
        """Generates dbt models programmatically for LDIF analytics."""

        @override
        def __init__(self, project_dir: Path | None = None) -> None:
            """Initialize the model generator.

            Args:
                project_dir: Path to the dbt project directory (defaults to current)

            Returns:
                object: Description of return value.

            """
            self.project_dir = project_dir if project_dir is not None else Path.cwd()
            self.models_dir = self.project_dir / "models"

        def generate_staging_models(self: object) -> list[FlextCore.Types.Dict]:
            """Generate staging layer models for LDIF data.

            Returns:
                List of generated model configurations

            """
            logger.info("Generating staging models for LDIF data")

            # This is where the sophisticated model generation logic would go
            # Based on the manifest.json analysis, we know these models exist:
            return [
                {
                    "name": "stg_ldif_entries",
                    "description": "Staging model for LDIF entries with data quality checks",
                    "materialization": "view",
                    "columns": [
                        {
                            "name": "dn",
                            "type": "varchar",
                            "tests": ["not_null", "unique"],
                        },
                        {
                            "name": "object_class",
                            "type": "varchar",
                            "tests": ["not_null"],
                        },
                        {"name": "is_valid_dn", "type": "boolean"},
                        {"name": "dn_depth", "type": "integer"},
                        {"name": "entry_type", "type": "varchar"},
                        {"name": "primary_object_class", "type": "varchar"},
                        {"name": "processed_at", "type": "timestamp"},
                    ],
                },
            ]

        def generate_analytics_models(self: object) -> list[FlextCore.Types.Dict]:
            """Generate analytics layer models.

            Returns:
                List of analytics model configurations

            """
            logger.info("Generating analytics models")

            return [
                {
                    "name": "analytics_ldif_insights",
                    "description": "Advanced analytics model with sophisticated SQL patterns",
                    "materialization": "table",
                    "features": [
                        "time_series_analysis",
                        "anomaly_detection",
                        "statistical_methods",
                        "moving_averages",
                        "risk_assessment",
                    ],
                },
            ]

    class Analytics:
        """LDIF-specific analytics functionality using flext-ldif infrastructure.

        This class eliminates code duplication by delegating ALL analytics operations
        to the FlextLdif, maintaining business rule compliance.
        """

        @override
        def __init__(self: object) -> None:
            """Initialize analytics with flext-ldif API."""
            self._ldif_api = FlextLdif()

        def _convert_dict_to_entries(
            self,
            ldif_data: list[FlextCore.Types.Dict],
        ) -> list[FlextLdifModels.Entry]:
            """Convert dictionary data to FlextLdifModels.Entry objects using flext-ldif factory.

            Args:
                ldif_data: List of LDIF entry dictionaries

            Returns:
                List of valid FlextLdifModels.Entry objects

            """
            entries: list[FlextLdifModels.Entry] = []
            for data in ldif_data:
                try:
                    # Extract required data from dict[str, object] with proper type checking
                    str(data.get("dn", ""))
                    attributes: FlextCore.Types.Dict = data.get("attributes", {})
                    # Note: changetype is not used (Entry constructor only needs dn and attributes)

                    formatted_attrs: dict[str, FlextDbtLdifTypes.Core.StringList] = {}
                    if isinstance(attributes, dict) and attributes:
                        # Ensure attributes are in the right format (dict[str, FlextDbtLdifTypes.Core.StringList])
                        for key, value in attributes.items():
                            if isinstance(value, list):
                                formatted_attrs[str(key)] = [str(v) for v in value]
                            else:
                                formatted_attrs[str(key)] = [str(value)]
                    else:
                        # Build attributes from top-level keys when 'attributes' is absent
                        for key, value in data.items():
                            if key in {"dn", "changetype", "attributes"}:
                                continue
                            if isinstance(value, list):
                                formatted_attrs[str(key)] = [str(v) for v in value]
                            else:
                                formatted_attrs[str(key)] = [str(value)]

                    if not formatted_attrs:
                        logger.warning(
                            "Invalid attributes type or empty, skipping entry",
                        )
                        continue

                    # Note: changetype is not used in Entry constructor - Entry is for parsed entries only

                    # Use direct Entry.create() method for proper type construction
                    entry_result = FlextLdifModels.Entry.create({
                        "dn": "dn",
                        "attributes": "formatted_attrs",
                    })

                    if entry_result.success and entry_result.value:
                        entries.append(entry_result.value)
                    else:
                        logger.warning("Failed to create entry: %s", entry_result.error)

                except Exception as e:
                    logger.warning("Skipping invalid entry: %s", e)

            return entries

        def analyze_entry_patterns(
            self,
            ldif_data: list[FlextCore.Types.Dict],
        ) -> FlextCore.Result[FlextCore.Types.Dict]:
            """Analyze patterns in LDIF entries using flext-ldif infrastructure.

            Args:
                ldif_data: List of LDIF entry dictionaries

            Returns:
                FlextCore.Result with analysis results or error

            """
            logger.info(
                "Analyzing patterns in %d LDIF entries using flext-ldif",
                len(ldif_data),
            )

            try:
                # Convert dict[str, object] entries to FlextLdifModels.Entry objects for proper analysis
                entries = self._convert_dict_to_entries(ldif_data)

                # Use flext-ldif API for statistics - NO local logic
                stats_result: FlextCore.Result[object] = (
                    self._ldif_api.get_entry_statistics(entries)
                )
                if not stats_result.success:
                    return FlextCore.Result[FlextCore.Types.Dict].fail(
                        f"Statistics generation failed: {stats_result.error}",
                    )

                stats = stats_result.value or {}

                # Get object class distribution using flext-ldif filtering
                object_classes: FlextCore.Types.IntDict = {}
                for entry in entries:
                    # Get object classes from the entry's object classes method
                    for obj_class in entry.get_object_classes():
                        object_classes[obj_class] = object_classes.get(obj_class, 0) + 1

                # Use flext-ldif hierarchical sorting for depth analysis
                sorted_result: FlextCore.Result[object] = (
                    self._ldif_api.sort_hierarchically(entries)
                )
                dn_depth_distribution: FlextCore.Types.IntDict = {}
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

                return FlextCore.Result[FlextCore.Types.Dict].ok(
                    {
                        "total_entries": stats.get("total_entries", 0),
                        "persons": stats.get("person_entries", 0),
                        "groups": stats.get("group_entries", 0),
                        "organizational_units": stats.get("other_entries", 0),
                        "valid_entries": stats.get("valid_entries", 0),
                        "unique_object_classes": list(object_classes.keys()),
                        "object_class_distribution": "object_classes",
                        "dn_depth_distribution": "dn_depth_distribution",
                        "risk_assessment": "risk_assessment",
                    },
                )

            except Exception as e:
                logger.exception("Entry pattern analysis failed")
                return FlextCore.Result[FlextCore.Types.Dict].fail(
                    f"Analysis failed: {e}"
                )

        def generate_quality_metrics(
            self,
            entries: list[FlextCore.Types.Dict],
        ) -> FlextCore.Result[FlextCore.Types.FloatDict]:
            """Generate data quality metrics using flext-ldif validation.

            Args:
                entries: List of LDIF entries as dictionaries

            Returns:
                FlextCore.Result with quality metrics or error

            """
            if not entries:
                return FlextCore.Result[dict["str", "float"]].ok(
                    {
                        "completeness": 0.0,
                        "validity": 0.0,
                        "consistency": 0.0,
                    },
                )

            try:
                # Convert to FlextLdifModels.Entry objects using helper method
                ldif_entries = self._convert_dict_to_entries(entries)

                total_entries = len(entries)
                converted_entries = len(ldif_entries)

                # Use flext-ldif validation - NO local validation logic
                valid_entries = len(
                    self._ldif_api.filter_valid(ldif_entries).value or [],
                )

                # Calculate metrics based on flext-ldif operations
                completeness = (
                    (converted_entries / total_entries) * 100.0
                    if total_entries > 0
                    else 0.0
                )
                validity = (
                    (valid_entries / converted_entries) * 100.0
                    if converted_entries > 0
                    else 0.0
                )

                # Consistency check using flext-ldif entry statistics
                stats_result: FlextCore.Result[object] = (
                    self._ldif_api.get_entry_statistics(ldif_entries)
                )
                consistency = 100.0  # Default high consistency
                if stats_result.success and stats_result.value:
                    stats = stats_result.value
                    # Check consistency based on valid vs total ratio
                    if stats.get("total", 0) > 0:
                        consistency = (
                            stats.get("valid", 0) / stats.get("total", 1)
                        ) * 100.0

                return FlextCore.Result[dict["str", "float"]].ok(
                    {
                        "completeness": round(completeness, 2),
                        "validity": round(validity, 2),
                        "consistency": round(consistency, 2),
                    },
                )

            except Exception as e:
                logger.exception("Quality metrics generation failed")
                return FlextCore.Result[dict["str", "float"]].fail(
                    f"Quality metrics failed: {e}",
                )

        def get_statistics_for_dbt(
            self,
            entries: list[FlextCore.Types.Dict],
        ) -> FlextCore.Result[Mapping[str, object]]:
            """Get statistics formatted for dbt model generation.

            Args:
                entries: List of LDIF entry dictionaries

            Returns:
                FlextCore.Result with dbt-compatible statistics or error

            """
            try:
                # Convert to FlextLdifModels.Entry objects using helper method
                ldif_entries = self._convert_dict_to_entries(entries)

                # Use flext-ldif API for all statistics
                stats_result: FlextCore.Result[object] = (
                    self._ldif_api.get_entry_statistics(ldif_entries)
                )
                if not stats_result.success:
                    return FlextCore.Result[Mapping["str", "object"]].fail(
                        f"dbt statistics failed: {stats_result.error}",
                    )

                return FlextCore.Result[Mapping["str", "object"]].ok(
                    stats_result.value or {}
                )

            except Exception as e:
                logger.exception("dbt statistics generation failed")
                return FlextCore.Result[Mapping["str", "object"]].fail(
                    f"dbt statistics error: {e}",
                )


__all__: FlextDbtLdifTypes.Core.StringList = [
    "FlextDbtLdifCore",
]
