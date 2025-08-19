"""Core functionality for FLEXT dbt LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

This module eliminates code duplication by using the FLEXT LDIF infrastructure
implementation from flext-ldif project for ALL analytics functionality.
"""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from flext_core import FlextResult, get_logger
from flext_ldif import FlextLdifAPI, FlextLdifEntry, FlextLdifFactory

logger = get_logger(__name__)
# Constants for magic number elimination
HIGH_VALIDITY_THRESHOLD = 0.95
MEDIUM_VALIDITY_THRESHOLD = 0.8


class DBTModelGenerator:
    """Generates dbt models programmatically for LDIF analytics."""

    def __init__(self, project_dir: Path | None = None) -> None:
        """Initialize the model generator.

        Args:
            project_dir: Path to the dbt project directory (defaults to current)

        """
        self.project_dir = project_dir if project_dir is not None else Path.cwd()
        self.models_dir = self.project_dir / "models"

    def generate_staging_models(self) -> list[dict[str, object]]:
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
                "description": "Staging model for LDIF entries with "
                "data quality checks",
                "materialization": "view",
                "columns": [
                    {"name": "dn", "type": "varchar", "tests": ["not_null", "unique"]},
                    {"name": "object_class", "type": "varchar", "tests": ["not_null"]},
                    {"name": "is_valid_dn", "type": "boolean"},
                    {"name": "dn_depth", "type": "integer"},
                    {"name": "entry_type", "type": "varchar"},
                    {"name": "primary_object_class", "type": "varchar"},
                    {"name": "processed_at", "type": "timestamp"},
                ],
            },
        ]

    def generate_analytics_models(self) -> list[dict[str, object]]:
        """Generate analytics layer models.

        Returns:
            List of analytics model configurations

        """
        logger.info("Generating analytics models")

        return [
            {
                "name": "analytics_ldif_insights",
                "description": "Advanced analytics model with "
                "sophisticated SQL patterns",
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


class LDIFAnalytics:
    """LDIF-specific analytics functionality using flext-ldif infrastructure.

    This class eliminates code duplication by delegating ALL analytics operations
    to the FlextLdifAPI, maintaining business rule compliance.
    """

    def __init__(self) -> None:
        """Initialize analytics with flext-ldif API."""
        self._ldif_api = FlextLdifAPI()

    def _convert_dict_to_entries(  # noqa: PLR0912
        self,
        ldif_data: list[dict[str, object]],
    ) -> list[FlextLdifEntry]:
        """Convert dictionary data to FlextLdifEntry objects using flext-ldif factory.

        Args:
            ldif_data: List of LDIF entry dictionaries

        Returns:
            List of valid FlextLdifEntry objects

        """
        entries: list[FlextLdifEntry] = []
        for data in ldif_data:
            try:
                # Extract required data from dict with proper type checking
                dn = str(data.get("dn", ""))
                attributes = data.get("attributes", {})
                changetype = data.get("changetype")

                # Type guard for attributes
                formatted_attrs: dict[str, list[str]] = {}
                if isinstance(attributes, dict) and attributes:
                    # Ensure attributes are in the right format (dict[str, list[str]])
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
                    logger.warning("Invalid attributes type or empty, skipping entry")
                    continue

                # Type guard for changetype
                changetype_str: str | None = None
                if changetype is not None and isinstance(changetype, str):
                    changetype_str = changetype

                # Use flext-ldif factory for entry creation
                entry_result = FlextLdifFactory.create_entry(
                    dn=dn,
                    attributes=formatted_attrs,
                    changetype=changetype_str,
                )

                if entry_result.success and entry_result.data:
                    entries.append(entry_result.data)
                else:
                    logger.warning("Failed to create entry: %s", entry_result.error)

            except Exception as e:
                logger.warning("Skipping invalid entry: %s", e)

        return entries

    def analyze_entry_patterns(
        self,
        ldif_data: list[dict[str, object]],
    ) -> FlextResult[dict[str, object]]:
        """Analyze patterns in LDIF entries using flext-ldif infrastructure.

        Args:
            ldif_data: List of LDIF entry dictionaries

        Returns:
            FlextResult with analysis results or error

        """
        logger.info(
            "Analyzing patterns in %d LDIF entries using flext-ldif",
            len(ldif_data),
        )

        try:
            # Convert dict entries to FlextLdifEntry objects for proper analysis
            entries = self._convert_dict_to_entries(ldif_data)

            # Use flext-ldif API for statistics - NO local logic
            stats_result = self._ldif_api.get_entry_statistics(entries)
            if not stats_result.success:
                return FlextResult[None].fail(
                    f"Statistics generation failed: {stats_result.error}",
                )

            stats = stats_result.data or {}

            # Get object class distribution using flext-ldif filtering
            object_classes: dict[str, int] = {}
            for entry in entries:
                # Get object classes from the entry's attributes
                for obj_class in entry.attributes.get_object_classes():
                    object_classes[obj_class] = object_classes.get(obj_class, 0) + 1

            # Use flext-ldif hierarchical sorting for depth analysis
            sorted_result = self._ldif_api.sort_hierarchically(entries)
            dn_depth_distribution: dict[str, int] = {}
            if sorted_result.success and sorted_result.data:
                for entry in sorted_result.data:
                    depth = entry.dn.get_depth()
                    depth_key = f"depth_{depth}"
                    dn_depth_distribution[depth_key] = (
                        dn_depth_distribution.get(depth_key, 0) + 1
                    )

            # Use flext-ldif analysis patterns - NO local calculation
            risk_result = self._ldif_api.analyze_entry_patterns(
                entries,
            )
            risk_assessment = risk_result.data if risk_result.success else "unknown"

            return FlextResult[None].ok(
                {
                    "total_entries": stats.get("total_entries", 0),
                    "persons": stats.get("person_entries", 0),
                    "groups": stats.get("group_entries", 0),
                    "organizational_units": stats.get("other_entries", 0),
                    "valid_entries": stats.get("valid_entries", 0),
                    "unique_object_classes": list(object_classes.keys()),
                    "object_class_distribution": object_classes,
                    "dn_depth_distribution": dn_depth_distribution,
                    "risk_assessment": risk_assessment,
                },
            )

        except Exception as e:
            logger.exception("Entry pattern analysis failed")
            return FlextResult[None].fail(f"Analysis failed: {e}")

    def generate_quality_metrics(
        self,
        entries: list[dict[str, object]],
    ) -> FlextResult[dict[str, float]]:
        """Generate data quality metrics using flext-ldif validation.

        Args:
            entries: List of LDIF entries as dictionaries

        Returns:
            FlextResult with quality metrics or error

        """
        if not entries:
            return FlextResult[None].ok(
                {
                    "completeness": 0.0,
                    "validity": 0.0,
                    "consistency": 0.0,
                },
            )

        try:
            # Convert to FlextLdifEntry objects using helper method
            ldif_entries = self._convert_dict_to_entries(entries)

            total_entries = len(entries)
            converted_entries = len(ldif_entries)

            # Use flext-ldif validation - NO local validation logic
            valid_entries = len(self._ldif_api.filter_valid(ldif_entries).data or [])

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
            stats_result = self._ldif_api.get_entry_statistics(ldif_entries)
            consistency = 100.0  # Default high consistency
            if stats_result.success and stats_result.data:
                stats = stats_result.data
                # Check consistency based on valid vs total ratio
                if stats.get("total", 0) > 0:
                    consistency = (
                        stats.get("valid", 0) / stats.get("total", 1)
                    ) * 100.0

            return FlextResult[None].ok(
                {
                    "completeness": round(completeness, 2),
                    "validity": round(validity, 2),
                    "consistency": round(consistency, 2),
                },
            )

        except Exception as e:
            logger.exception("Quality metrics generation failed")
            return FlextResult[None].fail(f"Quality metrics failed: {e}")

    def get_statistics_for_dbt(
        self,
        entries: list[dict[str, object]],
    ) -> FlextResult[Mapping[str, object]]:
        """Get statistics formatted for dbt model generation.

        Args:
            entries: List of LDIF entry dictionaries

        Returns:
            FlextResult with dbt-compatible statistics or error

        """
        try:
            # Convert to FlextLdifEntry objects using helper method
            ldif_entries = self._convert_dict_to_entries(entries)

            # Use flext-ldif API for all statistics
            stats_result = self._ldif_api.get_entry_statistics(ldif_entries)
            if not stats_result.success:
                return FlextResult[None].fail(f"dbt statistics failed: {stats_result.error}")

            return FlextResult[None].ok(stats_result.data or {})

        except Exception as e:
            logger.exception("dbt statistics generation failed")
            return FlextResult[None].fail(f"dbt statistics error: {e}")
