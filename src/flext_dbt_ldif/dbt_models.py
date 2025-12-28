"""DBT models functionality for flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

# SQL injection warnings are false positives for DBT template strings
from __future__ import annotations

from decimal import Decimal
from pathlib import Path
from typing import override

import yaml
from flext_core import FlextLogger, FlextResult, FlextService
from flext_ldif import FlextLdif, FlextLdifModels

from flext_dbt_ldif.settings import FlextDbtLdifSettings
from flext_dbt_ldif.typings import t

# Use the real typed class for precise type checking
logger = FlextLogger(__name__)


class FlextDbtLdifUnifiedService(FlextService[t.JsonDict]):
    """Unified DBT LDIF service class consolidating model definition and generation.

    This unified service follows the mandatory single-class-per-module pattern,
    combining model value object functionality with programmatic generation capabilities.
    Eliminates code duplication by providing both model representation and generation
    within a single cohesive service architecture.
    """

    @override
    def __init__(
        self,
        name: str,
        description: str = "",
        materialization: str = "view",
        columns: list[t.JsonDict] | None = None,
        meta: t.JsonDict | None = None,
        config: FlextDbtLdifSettings | None = None,
        project_dir: Path | None = None,
    ) -> None:
        """Initialize unified LDIF DBT service with model configuration.

        Args:
        name: Model name
        description: Model description
        materialization: DBT materialization type
        columns: Model column definitions
        meta: Model metadata
        config: Configuration for LDIF and DBT operations
        project_dir: Path to the DBT project directory

        """
        # Model definition properties
        self.name = name
        self.description = description
        self.materialization = materialization
        self.columns = columns or []
        self.meta = meta or {}

        # Generation service properties
        self.config: FlextDbtLdifSettings = (
            config or FlextDbtLdifSettings.get_global_instance()
        )
        self.project_dir = project_dir if project_dir is not None else Path.cwd()
        self.models_dir = self.project_dir / "models"
        self._ldif_api = FlextLdif()
        logger.info("Initialized unified LDIF DBT service: %s", self.project_dir)

    @override
    def execute(self) -> FlextResult[t.JsonDict]:
        """Execute the DBT model service.

        Returns:
        FlextResult[t.JsonDict]: Execution result

        """
        try:
            # Basic execution logic - can be extended based on requirements
            result_data: t.JsonDict = {
                "model_name": self.name,
                "status": "executed",
                "timestamp": "2025-01-01T00:00:00Z",  # Placeholder
            }
            return FlextResult[t.JsonDict].ok(result_data)
        except Exception as e:
            return FlextResult[t.JsonDict].fail(f"Execution failed: {e}")

    class _ModelDefinition:
        """Nested helper class for model definition operations."""

        @staticmethod
        def to_yaml_config(
            model_instance: FlextDbtLdifUnifiedService,
        ) -> t.JsonDict:
            """Convert model to YAML configuration format.

            Args:
            model_instance: The parent model instance

            Returns:
            Dictionary representing YAML configuration

            """
            return {
                "name": model_instance.name,
                "description": model_instance.description,
                "materialization": model_instance.materialization,
                "columns": model_instance.columns,
                "meta": model_instance.meta,
            }

        @staticmethod
        def to_dict(model_instance: FlextDbtLdifUnifiedService) -> t.JsonDict:
            """Convert model to dictionary representation.

            Args:
            model_instance: The parent model instance

            Returns:
            Dictionary representation of the model

            """
            return {
                "name": model_instance.name,
                "description": model_instance.description,
                "materialization": model_instance.materialization,
                "columns": model_instance.columns,
                "meta": model_instance.meta,
            }

    class _SchemaAnalysis:
        """Nested helper class for LDIF schema analysis operations."""

        @staticmethod
        def analyze_ldif_schema(
            service_instance: FlextDbtLdifUnifiedService,
            entries: list[FlextLdifModels.Entry],
        ) -> FlextResult[t.JsonDict]:
            """Analyze LDIF entries to determine schema structure.

            Args:
            service_instance: The parent service instance
            entries: List of LDIF entries to analyze

            Returns:
            FlextResult containing schema analysis

            """
            try:
                logger.info("Analyzing LDIF schema from %d entries", len(entries))
                stats_result = service_instance._ldif_api.entry_statistics(entries)
                if not stats_result.is_success:
                    return FlextResult[t.JsonDict].fail(
                        f"Schema analysis failed: {stats_result.error}",
                    )
                base_stats = stats_result.value or {}
                schema_info: t.JsonDict = dict(base_stats.items())
                schema_info["total_entries"] = len(entries)
                schema_info["has_entries"] = len(entries) > 0
                logger.info("LDIF schema analysis completed")
                return FlextResult[t.JsonDict].ok(schema_info)
            except Exception as e:
                logger.exception("Error analyzing LDIF schema")
                return FlextResult[t.JsonDict].fail(
                    f"Schema analysis error: {e}",
                )

    class ModelGeneration:
        """Nested helper class for DBT model generation operations."""

        @staticmethod
        def generate_staging_models(
            service_instance: FlextDbtLdifUnifiedService,
            entries: list[FlextLdifModels.Entry],
        ) -> FlextResult[list[FlextDbtLdifUnifiedService]]:
            """Generate staging layer DBT models for LDIF data.

            Args:
            service_instance: The parent service instance
            entries: LDIF entries to generate models for

            Returns:
            FlextResult containing list of staging models

            """
            try:
                logger.info(
                    "Generating staging models for %d LDIF entries",
                    len(entries),
                )
                schema_result = service_instance._SchemaAnalysis.analyze_ldif_schema(
                    service_instance,
                    entries,
                )
                if not schema_result.is_success:
                    return FlextResult[list[FlextDbtLdifUnifiedService]].fail(
                        f"Schema analysis failed: {schema_result.error}",
                    )
                schema_info = schema_result.value or {}
                grouped_entries = {"ldif_entries": "entries"}
                models = []
                for entry_type, type_entries in grouped_entries.items():
                    schema_name = service_instance.config.get_schema_for_entry_type(
                        entry_type,
                    )
                    if not schema_name:
                        continue
                    model = service_instance.ModelGeneration.generate_staging_model_for_type(
                        entry_type,
                        schema_name,
                        type_entries,
                        schema_info,
                    )
                    models.append(model)
                logger.info("Generated %d staging models", len(models))
                return FlextResult[list[FlextDbtLdifUnifiedService]].ok(models)
            except Exception as e:
                logger.exception("Error generating staging models")
                return FlextResult[list[FlextDbtLdifUnifiedService]].fail(
                    f"Staging model generation error: {e}",
                )

        @staticmethod
        def generate_analytics_models(
            staging_models: list[FlextDbtLdifUnifiedService],
        ) -> FlextResult[list[FlextDbtLdifUnifiedService]]:
            """Generate analytics layer DBT models.

            Args:
            staging_models: List of staging models to build upon

            Returns:
            FlextResult containing list of analytics models

            """
            try:
                logger.info(
                    "Generating analytics models from %d staging models",
                    len(staging_models),
                )
                analytics_models: list[FlextDbtLdifUnifiedService] = []

                # Create insights model
                insights_model = FlextDbtLdifUnifiedService(
                    name="analytics_ldif_insights",
                    description="Advanced analytics for LDIF data with statistical insights",
                    materialization="table",
                    columns=[
                        {
                            "name": "analysis_date",
                            "type": "timestamp",
                            "description": "Date of analysis",
                            "tests": ["not_null"],
                        },
                        {
                            "name": "total_entries",
                            "type": "integer",
                            "description": "Total number of LDIF entries",
                            "tests": [
                                "not_null",
                                {"accepted_values": {"values": [">= 0"]}},
                            ],
                        },
                        {
                            "name": "entry_type",
                            "type": "varchar",
                            "description": "Type of LDIF entry",
                            "tests": ["not_null"],
                        },
                        {
                            "name": "quality_score",
                            "type": Decimal(5, 2),
                            "description": "Data quality score (0-100)",
                            "tests": [
                                "not_null",
                                {"accepted_values": {"values": ["between 0 and 100"]}},
                            ],
                        },
                        {
                            "name": "risk_level",
                            "type": "varchar",
                            "description": "Risk assessment level",
                            "tests": [
                                "not_null",
                                {
                                    "accepted_values": {
                                        "values": ["low", "medium", "high"],
                                    },
                                },
                            ],
                        },
                    ],
                    meta={
                        "owner": "data_team",
                        "layer": "analytics",
                        "data_source": "ldif",
                    },
                )
                analytics_models.append(insights_model)

                # Create hierarchy model
                hierarchy_model = FlextDbtLdifUnifiedService(
                    name="analytics_ldif_hierarchy",
                    description="Hierarchical analysis of LDIF DN structures",
                    materialization="table",
                    columns=[
                        {
                            "name": "dn_path",
                            "type": "varchar",
                            "description": "Full distinguished name path",
                            "tests": ["not_null", "unique"],
                        },
                        {
                            "name": "dn_depth",
                            "type": "integer",
                            "description": "Depth level in DN hierarchy",
                            "tests": [
                                "not_null",
                                {"accepted_values": {"values": [">= 0"]}},
                            ],
                        },
                        {
                            "name": "parent_dn",
                            "type": "varchar",
                            "description": "Parent DN in hierarchy",
                        },
                        {
                            "name": "children_count",
                            "type": "integer",
                            "description": "Number of child entries",
                            "tests": [
                                "not_null",
                                {"accepted_values": {"values": [">= 0"]}},
                            ],
                        },
                        {
                            "name": "subtree_size",
                            "type": "integer",
                            "description": "Total entries in subtree",
                            "tests": [
                                "not_null",
                                {"accepted_values": {"values": [">= 1"]}},
                            ],
                        },
                    ],
                    meta={
                        "owner": "data_team",
                        "layer": "analytics",
                        "data_source": "ldif",
                    },
                )
                analytics_models.append(hierarchy_model)
                logger.info("Generated %d analytics models", len(analytics_models))
                return FlextResult[list[FlextDbtLdifUnifiedService]].ok(
                    analytics_models,
                )
            except Exception as e:
                logger.exception("Error generating analytics models")
                return FlextResult[list[FlextDbtLdifUnifiedService]].fail(
                    f"Analytics model generation error: {e}",
                )

        @staticmethod
        def _generate_staging_model_for_type(
            entry_type: str,
            schema_name: str,
            entries: list[FlextLdifModels.Entry],
            schema_info: t.JsonDict,
        ) -> FlextDbtLdifUnifiedService:
            """Generate a staging model for a specific entry type."""
            if not entries:
                error_msg = "Entries list cannot be empty"
                raise ValueError(error_msg)
            declared_total = (
                schema_info.get("total_entries")
                if isinstance(schema_info, dict)
                else None
            )
            _ = declared_total

            common_attrs: list[t.JsonDict] = [
                {
                    "name": "dn",
                    "type": "varchar",
                    "description": "LDIF Distinguished Name",
                    "tests": ["not_null", "unique"],
                },
                {
                    "name": "object_class",
                    "type": "varchar",
                    "description": "LDIF objectClass attribute",
                    "tests": ["not_null"],
                },
                {
                    "name": "entry_type",
                    "type": "varchar",
                    "description": "Type classification of LDIF entry",
                },
                {
                    "name": "has_entries_flag",
                    "type": "boolean",
                    "description": "Indicates whether source had any entries at generation time",
                },
            ]

            for ldif_attr in FlextDbtLdifSettings.ldif_attribute_mapping:
                if ldif_attr != "dn":
                    column_def: t.JsonDict = {
                        "name": "mapped_attr",
                        "type": "varchar",
                        "description": f"LDIF {ldif_attr} attribute",
                    }
                    if ldif_attr in FlextDbtLdifSettings.required_attributes:
                        column_def["tests"] = ["not_null"]
                    common_attrs.append(column_def)

            return FlextDbtLdifUnifiedService(
                name=schema_name,
                description=f"Staging model for LDIF {entry_type} entries with data quality checks",
                materialization="view",
                columns=common_attrs,
                meta={
                    "owner": "data_team",
                    "layer": "staging",
                    "data_source": "ldif",
                    "entry_type": "entry_type",
                    "has_entries": "has_entries",
                },
            )

    class _FileOperations:
        """Nested helper class for file writing operations."""

        @staticmethod
        def write_models_to_disk(
            service_instance: FlextDbtLdifUnifiedService,
            models: list[FlextDbtLdifUnifiedService],
            *,
            overwrite: bool = False,
        ) -> FlextResult[t.JsonDict]:
            """Write generated DBT models to disk.

            Args:
            service_instance: The parent service instance
            models: List of models to write
            overwrite: Whether to overwrite existing files

            Returns:
            FlextResult containing write operation results

            """
            try:
                logger.info(
                    "Writing %d models to disk: %s",
                    len(models),
                    service_instance.models_dir,
                )
                service_instance.models_dir.mkdir(parents=True, exist_ok=True)
                written_files = []
                for model in models:
                    sql_content = service_instance.SQLGeneration.generate_sql_for_model(
                        model,
                    )
                    sql_file = service_instance.models_dir / f"{model.name}.sql"
                    if not overwrite and sql_file.exists():
                        logger.warning("Skipping existing model: %s", sql_file)
                        continue
                    sql_file.write_text(sql_content)
                    written_files.append(str(sql_file))

                    yaml_config = service_instance._ModelDefinition.to_yaml_config(
                        model,
                    )
                    yaml_file = service_instance.models_dir / f"{model.name}.yml"
                    yaml_content = service_instance.SQLGeneration.generate_basic_yaml(
                        yaml_config,
                    )
                    yaml_file.write_text(yaml_content)
                    written_files.append(str(yaml_file))
                logger.info("Successfully wrote %d files", len(written_files))
                return FlextResult[t.JsonDict].ok(
                    {
                        "written_files": "written_files",
                        "models_count": len(models),
                        "output_dir": str(service_instance.models_dir),
                    },
                )
            except Exception as e:
                logger.exception("Error writing models to disk")
                return FlextResult[t.JsonDict].fail(f"Model writing error: {e}")

    class SQLGeneration:
        """Nested helper class for SQL generation operations."""

        @staticmethod
        def _generate_sql_for_model(model: FlextDbtLdifUnifiedService) -> str:
            """Generate SQL content for DBT model using flext-meltano patterns."""
            if model.name.startswith("stg_"):
                return FlextDbtLdifUnifiedService.SQLGeneration.generate_staging_sql(
                    model,
                )
            if model.name.startswith("analytics_"):
                return FlextDbtLdifUnifiedService.SQLGeneration.generate_analytics_sql(
                    model,
                )
            return FlextDbtLdifUnifiedService.SQLGeneration.generate_generic_sql(model)

        @staticmethod
        def _generate_staging_sql(model: FlextDbtLdifUnifiedService) -> str:
            """Generate SQL for staging model."""
            columns: list[str] = []
            for col in model.columns:
                if isinstance(col, dict) and "name" in col:
                    col_name = col["name"]
                    if isinstance(col_name, str):
                        columns.append(col_name)
            column_list: str = ",\n    ".join(columns)

            allowed_materializations = {"view", "table", "ephemeral", "incremental"}
            materialized = (
                model.materialization
                if model.materialization in allowed_materializations
                else "view"
            )

            # Generate DBT template string (not executable SQL)
            # Note: This is a template string for DBT, not executable SQL
            # The f-string interpolation is safe as it's used for DBT templating
            # This generates DBT SQL templates, not executable queries
            return f"""-- Staging model for LDIF data
-- Generated automatically by flext-dbt-ldif

{{{{ config(materialized='{materialized}') }}}}

with source_data as (
    select
        {column_list},
        current_timestamp as processed_at
    from {{{{ source('ldif', 'raw_ldif_entries') }}}}
),

validated_data as (
    select *,
        case
            when dn is not null and length(dn) > 0 then true
            else false
        end as is_valid_dn,
        array_length(string_to_array(dn, ','), 1) as dn_depth
    from source_data
)

select * from validated_data
"""

        @staticmethod
        def _generate_analytics_sql(model: FlextDbtLdifUnifiedService) -> str:
            """Generate analytics SQL for DBT model."""
            # Use model configuration for SQL generation
            table_name = getattr(model, "table_name", "analytics_table")
            # Generate DBT template string (not executable SQL)
            # Note: This is a template string for DBT, not executable SQL
            # The f-string interpolation is safe as it's used for DBT templating
            return f"SELECT * FROM {{ ref('{table_name}') }}"

        @staticmethod
        def _generate_generic_sql(model: FlextDbtLdifUnifiedService) -> str:
            """Generate generic SQL for DBT model."""
            # Generate SQL based on model configuration
            columns = []
            for col in model.columns:
                if isinstance(col, dict) and "name" in col:
                    col_name = col["name"]
                    if isinstance(col_name, str):
                        columns.append(col_name)

            column_list: str = ",\n    ".join(columns) if columns else "*"

            return (
                "-- Generic model for LDIF data\n"
                f"-- Model: {model.name}\n"
                f"-- Description: {model.description}\n\n"
                f"{{{{ config(materialized='{model.materialization}') }}}}\n\n"
                "select\n"
                f"    {column_list}\n"
                "from {{ ref('stg_ldif_entries') }}"
            )

        @staticmethod
        def _generate_basic_yaml(yaml_config: t.JsonDict) -> str:
            """Generate basic YAML content for DBT model."""
            schema_content = {"version": 2, "models": [yaml_config]}
            return yaml.dump(schema_content, default_flow_style=False, indent=2)

    class _ColumnTypeHelpers:
        """Nested helper class for column type determination."""

        @staticmethod
        def _determine_column_type(attr_info: t.JsonDict) -> str:
            """Determine appropriate column type based on attribute analysis."""
            max_varchar_length = 255
            if attr_info.get("is_numeric"):
                return "integer"
            if attr_info.get("is_timestamp"):
                return "timestamp"
            if attr_info.get("is_boolean"):
                return "boolean"
            max_length = attr_info.get("max_length", 0)
            if isinstance(max_length, int) and max_length > max_varchar_length:
                return "text"
            return "varchar"

    # Public interface methods (delegate to nested classes)
    def to_yaml_config(self) -> t.JsonDict:
        """Convert model to YAML configuration format."""
        return self._ModelDefinition.to_yaml_config(self)

    def to_dict(self) -> t.JsonDict:
        """Convert model to dictionary representation."""
        return self._ModelDefinition.to_dict(self)

    def analyze_ldif_schema(
        self,
        entries: list[FlextLdifModels.Entry],
    ) -> FlextResult[t.JsonDict]:
        """Analyze LDIF entries to determine schema structure."""
        return self._SchemaAnalysis.analyze_ldif_schema(self, entries)

    def generate_staging_models(
        self,
        entries: list[FlextLdifModels.Entry],
    ) -> FlextResult[list[FlextDbtLdifUnifiedService]]:
        """Generate staging layer DBT models for LDIF data."""
        return self._ModelGeneration.generate_staging_models(self, entries)

    def generate_analytics_models(
        self,
        staging_models: list[FlextDbtLdifUnifiedService],
    ) -> FlextResult[list[FlextDbtLdifUnifiedService]]:
        """Generate analytics layer DBT models."""
        return self._ModelGeneration.generate_analytics_models(staging_models)

    def write_models_to_disk(
        self,
        models: list[FlextDbtLdifUnifiedService],
        *,
        overwrite: bool = False,
    ) -> FlextResult[t.JsonDict]:
        """Write generated DBT models to disk."""
        return self._FileOperations.write_models_to_disk(
            self,
            models,
            overwrite=overwrite,
        )


__all__: list[str] = [
    "FlextDbtLdifUnifiedService",
]
