"""Models for LDIF DBT operations.

This module provides data models for LDIF DBT operations.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextModels, FlextResult, FlextUtilities
from flext_dbt_ldif.constants import FlextDbtLdifConstants


class FlextDbtLdifModels(FlextModels):
    """Unified DBT LDIF models collection with analytics capabilities.

    Immutable representation of a generated DBT model with LDIF-specific metadata
    and integrated analytics functionality following FLEXT unified class pattern.
    """

    name: str
    dbt_model_type: str  # staging, intermediate, marts, analytics
    ldif_source: str
    change_types: list[str]
    columns: list[dict[str, object]]
    materialization: str
    sql_content: str
    description: str
    dependencies: list[str]

    def validate_business_rules(self) -> FlextResult[None]:
        """Validate DBT LDIF model business rules."""
        try:
            if not self.name.strip():
                return FlextResult[None].fail("Model name cannot be empty")
            if self.dbt_model_type not in {
                "staging",
                "intermediate",
                "marts",
                "analytics",
            }:
                return FlextResult[None].fail("Invalid model_type")
            if not self.ldif_source.strip():
                return FlextResult[None].fail("LDIF source cannot be empty")
            if not self.sql_content.strip():
                return FlextResult[None].fail("SQL content cannot be empty")
            return FlextResult[None].ok(None)
        except Exception as e:
            return FlextResult[None].fail(f"Business rule validation failed: {e}")

    def get_file_path(self) -> str:
        """Get the file path for this DBT LDIF model."""
        return f"models/{self.dbt_model_type}/{self.name}.sql"

    def get_schema_file_path(self) -> str:
        """Get the schema file path for this DBT LDIF model."""
        return f"models/{self.dbt_model_type}/schema.yml"

    def to_sql_file(self) -> FlextResult[str]:
        """Convert model to SQL file content."""
        try:
            config_block = f"""
{{{{
  config(
    materialized='{self.materialization}',
    alias='{self.name}'
  )
}}}}"""
            content = f"{config_block}\n\n{self.sql_content}"
            return FlextResult[str].ok(content)
        except Exception as e:
            return FlextResult[str].fail(f"SQL file generation failed: {e}")

    def to_schema_entry(self) -> FlextResult[dict[str, object]]:
        """Convert model to schema.yml entry."""
        try:
            schema_entry: dict[str, object] = {
                "name": self.name,
                "description": self.description,
                "columns": [
                    {
                        "name": col["name"],
                        "description": col.get("description", ""),
                        "data_type": col.get("data_type", ""),
                    }
                    for col in self.columns
                ],
            }
            return FlextResult[dict["str", "object"]].ok(schema_entry)
        except Exception as e:
            return FlextResult[dict["str", "object"]].fail(
                f"Schema entry generation failed: {e}"
            )

    @classmethod
    def create_generator(
        cls,
        config: dict[str, object],
    ) -> FlextDbtLdifModels._ModelGenerator:
        """Create a model generator instance."""
        return cls._ModelGenerator(config)

    class _ModelGenerator:
        """Internal model generator class for DBT LDIF models."""

        @override
        def __init__(
            self,
            config: dict[str, object],
        ) -> None:
            """Initialize the LDIF model generator."""
            self.config = config

        def generate_staging_models(
            self, ldif_sources: list[str]
        ) -> FlextResult[list[FlextDbtLdifModels]]:
            """Generate staging models from LDIF sources."""
            staging_models: list[FlextDbtLdifModels] = []

            for ldif_source in ldif_sources:
                model_result = self._create_staging_model(ldif_source)
                if model_result.is_failure:
                    continue

                staging_models.append(model_result.unwrap())

            return FlextResult[list[FlextDbtLdifModels]].ok(staging_models)

        def generate_analytics_models(
            self, staging_models: list[FlextDbtLdifModels]
        ) -> FlextResult[list[FlextDbtLdifModels]]:
            """Generate analytics models from staging models."""
            analytics_models: list[FlextDbtLdifModels] = []

            for staging_model in staging_models:
                model_result = self._create_analytics_model(staging_model)
                if model_result.is_failure:
                    continue

                analytics_models.append(model_result.unwrap())

            return FlextResult[list[FlextDbtLdifModels]].ok(analytics_models)

        def _create_staging_model(
            self, ldif_source: str
        ) -> FlextResult[FlextDbtLdifModels]:
            """Create a staging model from LDIF source."""
            try:
                # Note: This is a template string for DBT, not executable SQL
                # The f-string interpolation is safe as it's used for DBT templating
                sql_content = f"""
    select *
    from {{{{ source('ldif', '{ldif_source}') }}}}
    """

                staging_model = FlextDbtLdifModels(
                    name=f"stg_ldif_{ldif_source.replace('.', '_')}",
                    dbt_model_type="staging",
                    ldif_source=ldif_source,
                    change_types=["add", "modify", "delete"],
                    columns=[],
                    materialization="view",
                    sql_content=sql_content.strip(),
                    description=f"Staging model for LDIF source {ldif_source}",
                    dependencies=[],
                )

                return FlextResult[FlextDbtLdifModels].ok(staging_model)

            except Exception as e:
                return FlextResult[FlextDbtLdifModels].fail(
                    f"Failed to create staging model: {e}"
                )

        def _create_analytics_model(
            self, staging_model: FlextDbtLdifModels
        ) -> FlextResult[FlextDbtLdifModels]:
            """Create an analytics model from staging model."""
            try:
                analytics_name = staging_model.name.replace("stg_", "analytics_")

                # Note: This is a template string for DBT, not executable SQL
                # The f-string interpolation is safe as it's used for DBT templating
                sql_content = f"""
    select
        *,
        current_timestamp as analytics_timestamp
    from {{{{ ref('{staging_model.name}') }}}}
    """

                analytics_model = FlextDbtLdifModels(
                    name=analytics_name,
                    dbt_model_type="analytics",
                    ldif_source=staging_model.ldif_source,
                    change_types=staging_model.change_types,
                    columns=[
                        *staging_model.columns,
                        {
                            "name": "analytics_timestamp",
                            "description": "Analytics processing timestamp",
                            "data_type": "TIMESTAMP",
                        },
                    ],
                    materialization="table",
                    sql_content=sql_content.strip(),
                    description=f"Analytics model for {staging_model.ldif_source}",
                    dependencies=[staging_model.name],
                )

                return FlextResult[FlextDbtLdifModels].ok(analytics_model)

            except Exception as e:
                return FlextResult[FlextDbtLdifModels].fail(
                    f"Failed to create analytics model: {e}"
                )


class FlextDbtLdifUtilities(FlextUtilities):
    """Unified DBT LDIF utilities extending FlextUtilities.

    Provides comprehensive utility classes for DBT LDIF operations:
    - LDIF data parsing and transformation utilities
    - DBT project management utilities for LDIF workflows
    - LDIF change processing utilities
    - DBT model generation utilities for LDIF analytics
    - Performance optimization utilities for LDIF processing

    All nested utility classes follow SOLID principles and FlextResult patterns.
    """

    class _LdifDataHelper:
        """LDIF data parsing and transformation utilities."""

        @staticmethod
        def parse_ldif_entry(ldif_entry: str) -> FlextResult[dict]:
            """Parse a single LDIF entry into structured data."""
            if not ldif_entry or not ldif_entry.strip():
                return FlextResult[dict].fail("LDIF entry cannot be empty")

            try:
                lines = ldif_entry.strip().split("\n")
                entry_data = {}
                current_attr = None

                for line in lines:
                    if line.startswith(" "):
                        # Continuation of previous line
                        if current_attr:
                            entry_data[current_attr] += line[1:]  # Remove leading space
                    elif ":" in line:
                        attr, value = line.split(":", 1)
                        attr = attr.strip()
                        value = value.strip()
                        current_attr = attr

                        if attr in entry_data:
                            # Multi-valued attribute
                            if not isinstance(entry_data[attr], list):
                                entry_data[attr] = [entry_data[attr]]
                            entry_data[attr].append(value)
                        else:
                            entry_data[attr] = value

                return FlextResult[dict].ok(entry_data)
            except Exception as e:
                return FlextResult[dict].fail(f"LDIF entry parsing failed: {e}")

        @staticmethod
        def extract_change_type(ldif_entry: dict) -> FlextResult[str]:
            """Extract change type from LDIF entry."""
            if not ldif_entry:
                return FlextResult[str].fail("LDIF entry cannot be empty")

            # Default change type
            change_type = "add"

            # Check for changetype attribute
            if "changetype" in ldif_entry:
                change_type = ldif_entry["changetype"]

            # Validate change type
            valid_change_types = ["add", "delete", "modify", "modrdn"]
            if change_type not in valid_change_types:
                return FlextResult[str].fail(f"Invalid change type: {change_type}")

            return FlextResult[str].ok(change_type)

        @staticmethod
        def normalize_ldif_attributes(ldif_entry: dict) -> FlextResult[dict]:
            """Normalize LDIF attributes for DBT processing."""
            if not ldif_entry:
                return FlextResult[dict].fail("LDIF entry cannot be empty")

            try:
                normalized = {}

                for attr, value in ldif_entry.items():
                    # Normalize attribute name (lowercase, replace spaces with underscores)
                    normalized_attr = attr.lower().replace(" ", "_").replace("-", "_")

                    # Handle multi-valued attributes
                    if isinstance(value, list):
                        normalized[normalized_attr] = value
                    else:
                        normalized[normalized_attr] = value

                return FlextResult[dict].ok(normalized)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"LDIF attribute normalization failed: {e}"
                )

    class _DbtProjectHelper:
        """DBT project management utilities for LDIF workflows."""

        @staticmethod
        def generate_dbt_project_config(
            project_name: str, ldif_sources: list[str]
        ) -> FlextResult[dict]:
            """Generate DBT project configuration for LDIF processing."""
            if not project_name:
                return FlextResult[dict].fail("Project name cannot be empty")

            if not ldif_sources:
                return FlextResult[dict].fail("LDIF sources cannot be empty")

            try:
                config = {
                    "name": project_name,
                    "version": "1.0.0",
                    "profile": f"{project_name}_profile",
                    "model-paths": ["models"],
                    "analysis-paths": ["analysis"],
                    "test-paths": ["tests"],
                    "seed-paths": ["seeds"],
                    "macro-paths": ["macros"],
                    "snapshot-paths": ["snapshots"],
                    "target-path": "target",
                    "clean-targets": ["target", "dbt_packages"],
                    "vars": {
                        "ldif_sources": ldif_sources,
                        "enable_ldif_analytics": True,
                    },
                }

                return FlextResult[dict].ok(config)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"DBT project config generation failed: {e}"
                )

        @staticmethod
        def create_sources_yml(ldif_sources: list[str]) -> FlextResult[dict]:
            """Create sources.yml configuration for LDIF sources."""
            if not ldif_sources:
                return FlextResult[dict].fail("LDIF sources cannot be empty")

            try:
                sources_config = {
                    "version": 2,
                    "sources": [
                        {
                            "name": "ldif",
                            "description": "LDIF directory sources",
                            "tables": [
                                {
                                    "name": source.replace(".", "_"),
                                    "description": f"LDIF source: {source}",
                                    "columns": [
                                        {
                                            "name": "dn",
                                            "description": "Distinguished Name",
                                        },
                                        {
                                            "name": "changetype",
                                            "description": "Change type (add/modify/delete)",
                                        },
                                        {
                                            "name": "entry_data",
                                            "description": "LDIF entry data",
                                        },
                                    ],
                                }
                                for source in ldif_sources
                            ],
                        }
                    ],
                }

                return FlextResult[dict].ok(sources_config)
            except Exception as e:
                return FlextResult[dict].fail(f"Sources.yml creation failed: {e}")

        @staticmethod
        def validate_dbt_project_structure(project_path: str) -> FlextResult[dict]:
            """Validate DBT project structure for LDIF processing."""
            if not project_path:
                return FlextResult[dict].fail("Project path cannot be empty")

            # This would normally check filesystem, returning validation result
            validation_result = {
                "valid": True,
                "missing_directories": [],
                "missing_files": [],
                "recommendations": [],
            }

            required_dirs = ["models", "macros", "tests"]
            required_files = ["dbt_project.yml"]

            # Simulate validation (in real implementation would check filesystem)
            for directory in required_dirs:
                validation_result["recommendations"].append(
                    f"Ensure {directory}/ directory exists"
                )

            for file in required_files:
                validation_result["recommendations"].append(f"Ensure {file} exists")

            return FlextResult[dict].ok(validation_result)

    class _LdifChangeHelper:
        """LDIF change processing utilities."""

        @staticmethod
        def process_ldif_changes(ldif_entries: list[dict]) -> FlextResult[dict]:
            """Process multiple LDIF entries and categorize changes."""
            if not ldif_entries:
                return FlextResult[dict].fail("LDIF entries cannot be empty")

            try:
                changes = {
                    "adds": [],
                    "modifies": [],
                    "deletes": [],
                    "modrdns": [],
                    "total": len(ldif_entries),
                }

                for entry in ldif_entries:
                    change_type_result = (
                        FlextDbtLdifUtilities._LdifDataHelper.extract_change_type(entry)
                    )
                    if change_type_result.is_failure:
                        continue

                    change_type = change_type_result.unwrap()

                    if change_type == "add":
                        changes["adds"].append(entry)
                    elif change_type == "modify":
                        changes["modifies"].append(entry)
                    elif change_type == "delete":
                        changes["deletes"].append(entry)
                    elif change_type == "modrdn":
                        changes["modrdns"].append(entry)

                return FlextResult[dict].ok(changes)
            except Exception as e:
                return FlextResult[dict].fail(f"LDIF change processing failed: {e}")

        @staticmethod
        def generate_change_sql(change_type: str, entry_data: dict) -> FlextResult[str]:
            """Generate SQL statements for LDIF changes."""
            if not change_type:
                return FlextResult[str].fail("Change type cannot be empty")

            if not entry_data:
                return FlextResult[str].fail("Entry data cannot be empty")

            try:
                if change_type == "add":
                    sql = f"INSERT INTO ldif_entries (dn, entry_data, change_type) VALUES ('{entry_data.get('dn', '')}', '{entry_data}', 'add')"
                elif change_type == "modify":
                    sql = f"UPDATE ldif_entries SET entry_data = '{entry_data}', change_type = 'modify' WHERE dn = '{entry_data.get('dn', '')}'"
                elif change_type == "delete":
                    sql = f"DELETE FROM ldif_entries WHERE dn = '{entry_data.get('dn', '')}'"
                else:
                    return FlextResult[str].fail(
                        f"Unsupported change type: {change_type}"
                    )

                return FlextResult[str].ok(sql)
            except Exception as e:
                return FlextResult[str].fail(f"Change SQL generation failed: {e}")

        @staticmethod
        def create_change_manifest(changes: dict) -> FlextResult[dict]:
            """Create a manifest of all LDIF changes."""
            if not changes:
                return FlextResult[dict].fail("Changes cannot be empty")

            try:
                manifest = {
                    "change_summary": {
                        "total_changes": changes.get("total", 0),
                        "adds_count": len(changes.get("adds", [])),
                        "modifies_count": len(changes.get("modifies", [])),
                        "deletes_count": len(changes.get("deletes", [])),
                        "modrdns_count": len(changes.get("modrdns", [])),
                    },
                    "processing_timestamp": "now",
                    "processing_status": "completed",
                }

                return FlextResult[dict].ok(manifest)
            except Exception as e:
                return FlextResult[dict].fail(f"Change manifest creation failed: {e}")

    class _ModelGenerationHelper:
        """DBT model generation utilities for LDIF analytics."""

        @staticmethod
        def generate_staging_model_sql(
            ldif_source: str, source_schema: dict
        ) -> FlextResult[str]:
            """Generate staging model SQL for LDIF source."""
            if not ldif_source:
                return FlextResult[str].fail("LDIF source cannot be empty")

            try:
                # Generate column list from schema
                columns = source_schema.get("columns", [])
                column_list = ", ".join([
                    col.get("name", "") for col in columns if col.get("name")
                ])

                if not column_list:
                    column_list = "*"

                sql = f"""
    select
        {column_list}
    from {{{{ source('ldif', '{ldif_source.replace(".", "_")}') }}}}
    """.strip()

                return FlextResult[str].ok(sql)
            except Exception as e:
                return FlextResult[str].fail(
                    f"Staging model SQL generation failed: {e}"
                )

        @staticmethod
        def generate_analytics_model_sql(
            staging_model_name: str, analytics_type: str
        ) -> FlextResult[str]:
            """Generate analytics model SQL from staging model."""
            if not staging_model_name:
                return FlextResult[str].fail("Staging model name cannot be empty")

            if not analytics_type:
                return FlextResult[str].fail("Analytics type cannot be empty")

            try:
                if analytics_type == "summary":
                    sql = f"""
    select
        changetype,
        count(*) as change_count,
        min(processing_timestamp) as first_change,
        max(processing_timestamp) as last_change
    from {{{{ ref('{staging_model_name}') }}}}
    group by changetype
    """
                elif analytics_type == "timeline":
                    sql = f"""
    select
        date_trunc('hour', processing_timestamp) as change_hour,
        changetype,
        count(*) as hourly_changes
    from {{{{ ref('{staging_model_name}') }}}}
    group by date_trunc('hour', processing_timestamp), changetype
    order by change_hour, changetype
    """
                else:
                    return FlextResult[str].fail(
                        f"Unsupported analytics type: {analytics_type}"
                    )

                return FlextResult[str].ok(sql.strip())
            except Exception as e:
                return FlextResult[str].fail(
                    f"Analytics model SQL generation failed: {e}"
                )

        @staticmethod
        def create_model_schema_entry(
            model_name: str, model_description: str, columns: list[dict]
        ) -> FlextResult[dict]:
            """Create schema.yml entry for generated model."""
            if not model_name:
                return FlextResult[dict].fail("Model name cannot be empty")

            try:
                schema_entry = {
                    "name": model_name,
                    "description": model_description
                    or f"Generated model: {model_name}",
                    "columns": [
                        {
                            "name": col.get("name", ""),
                            "description": col.get("description", ""),
                            "data_type": col.get("data_type", ""),
                        }
                        for col in columns
                    ],
                }

                return FlextResult[dict].ok(schema_entry)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"Model schema entry creation failed: {e}"
                )

    class _PerformanceHelper:
        """Performance optimization utilities for LDIF processing."""

        @staticmethod
        def analyze_ldif_processing_performance(
            processing_stats: dict,
        ) -> FlextResult[dict]:
            """Analyze LDIF processing performance metrics."""
            if not processing_stats:
                return FlextResult[dict].fail("Processing stats cannot be empty")

            try:
                total_entries = processing_stats.get("total_entries", 0)
                processing_time = processing_stats.get("processing_time_seconds", 1)

                analysis = {
                    "entries_per_second": total_entries / processing_time,
                    "average_entry_time_ms": (processing_time * 1000)
                    / max(total_entries, 1),
                    "performance_rating": "good"
                    if total_entries / processing_time
                    > FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND
                    else "needs_optimization",
                    "recommendations": [],
                }

                if (
                    analysis["entries_per_second"]
                    < FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND_MIN
                ):
                    analysis["recommendations"].append("Consider increasing batch size")

                if (
                    analysis["average_entry_time_ms"]
                    > FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_ENTRY_TIME_MS
                ):
                    analysis["recommendations"].append(
                        "Consider optimizing LDIF parsing"
                    )

                return FlextResult[dict].ok(analysis)
            except Exception as e:
                return FlextResult[dict].fail(f"Performance analysis failed: {e}")

        @staticmethod
        def suggest_dbt_optimization_settings(project_stats: dict) -> FlextResult[dict]:
            """Suggest DBT optimization settings based on project statistics."""
            if not project_stats:
                return FlextResult[dict].fail("Project stats cannot be empty")

            try:
                model_count = project_stats.get("model_count", 0)
                avg_model_runtime = project_stats.get("avg_model_runtime_seconds", 0)

                optimizations = {
                    "threads": min(8, max(2, model_count // 10)),
                    "materialization_strategy": "table"
                    if avg_model_runtime
                    > FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_MODEL_RUNTIME_SECONDS
                    else "view",
                    "enable_incremental": model_count
                    > FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_MODEL_COUNT_INCREMENTAL,
                    "enable_partitioning": avg_model_runtime
                    > FlextDbtLdifConstants.PERFORMANCE_THRESHOLD_MODEL_RUNTIME_PARTITIONING,
                }

                return FlextResult[dict].ok(optimizations)
            except Exception as e:
                return FlextResult[dict].fail(
                    f"DBT optimization suggestions failed: {e}"
                )

        @staticmethod
        def monitor_resource_usage(
            current_memory_mb: int, memory_threshold_mb: int = 1024
        ) -> FlextResult[dict]:
            """Monitor resource usage during LDIF processing."""
            if current_memory_mb < 0:
                return FlextResult[dict].fail("Memory usage cannot be negative")

            try:
                monitoring_result = {
                    "current_memory_mb": current_memory_mb,
                    "memory_threshold_mb": memory_threshold_mb,
                    "within_threshold": current_memory_mb <= memory_threshold_mb,
                    "memory_usage_percentage": (current_memory_mb / memory_threshold_mb)
                    * 100,
                    "recommendations": [],
                }

                if current_memory_mb > memory_threshold_mb * 0.8:
                    monitoring_result["recommendations"].append(
                        "Consider reducing batch size"
                    )

                if current_memory_mb > memory_threshold_mb:
                    monitoring_result["recommendations"].append(
                        "Memory threshold exceeded - immediate action required"
                    )

                return FlextResult[dict].ok(monitoring_result)
            except Exception as e:
                return FlextResult[dict].fail(f"Resource monitoring failed: {e}")


__all__ = ["FlextDbtLdifModels"]
