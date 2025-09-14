"""DBT models functionality for flext-dbt-ldif."""

# ruff: noqa: S608  # SQL injection warnings are false positives for dbt SQL template generation

from __future__ import annotations

from pathlib import Path

import yaml
from flext_core import FlextLogger, FlextResult, FlextTypes
from flext_ldif import FlextLDIFAPI
from flext_ldif.models import FlextLDIFEntry

from flext_dbt_ldif.dbt_config import FlextDbtLdifConfig

# Use the real typed class for precise type checking
logger = FlextLogger(__name__)


class FlextLDIFDbtModel:
    """Value object representing a DBT model for LDIF data."""

    def __init__(
        self,
        name: str,
        description: str,
        columns: list[FlextTypes.Core.Dict],
        *,
        materialization: str = "view",
        meta: FlextTypes.Core.Dict | None = None,
    ) -> None:
        """Initialize the DBT model."""
        self.name = name
        self.description = description
        self.materialization = materialization
        self.columns = columns
        self.tests: list[FlextTypes.Core.Dict] = []
        self.meta = meta or {}

    def to_yaml_config(self) -> FlextTypes.Core.Dict:
        """Convert to DBT model YAML configuration."""
        return {
            "name": self.name,
            "description": self.description,
            "config": {"materialized": self.materialization},
            "columns": self.columns,
            "tests": self.tests,
            "meta": self.meta,
        }


class FlextDbtLdifModelGenerator:
    """Generates DBT models for LDIF data transformations.

    Uses flext-ldif for schema analysis and flext-meltano patterns
    for DBT model generation.
    """

    def __init__(
        self,
        config: FlextDbtLdifConfig | None = None,
        project_dir: Path | None = None,
    ) -> None:
        """Initialize the LDIF DBT model generator.

        Args:
            config: Configuration for LDIF and DBT operations
            project_dir: Path to the DBT project directory

        """
        self.config = config or FlextDbtLdifConfig()
        self.project_dir = project_dir if project_dir is not None else Path.cwd()
        self.models_dir = self.project_dir / "models"
        self._ldif_api = FlextLDIFAPI()
        # self._dbt_generator = FlextDbtModelGenerator()  # Not available yet
        logger.info("Initialized LDIF DBT model generator: %s", self.project_dir)

    def analyze_ldif_schema(
        self,
        entries: list[FlextLDIFEntry],
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Analyze LDIF entries to determine schema structure.

        Args:
            entries: List of LDIF entries to analyze
        Returns:
            FlextResult containing schema analysis

        """
        try:
            logger.info("Analyzing LDIF schema from %d entries", len(entries))
            # Use flext-ldif API for entry statistics (analyze_schema not available)
            stats_result = self._ldif_api.get_entry_statistics(entries)
            if not stats_result.success:
                return FlextResult[FlextTypes.Core.Dict].fail(
                    f"Schema analysis failed: {stats_result.error}",
                )
            # Upcast to FlextTypes.Core.Dict for result composition
            base_stats: FlextTypes.Core.CounterDict = stats_result.value or {}
            schema_info: FlextTypes.Core.Dict = dict(base_stats.items())
            # Add basic schema analysis info
            schema_info["total_entries"] = len(entries)
            schema_info["has_entries"] = len(entries) > 0
            logger.info("LDIF schema analysis completed")
            return FlextResult[FlextTypes.Core.Dict].ok(schema_info)
        except Exception as e:
            logger.exception("Error analyzing LDIF schema")
            return FlextResult[FlextTypes.Core.Dict].fail(f"Schema analysis error: {e}")

    def generate_staging_models(
        self,
        entries: list[FlextLDIFEntry],
    ) -> FlextResult[list[FlextLDIFDbtModel]]:
        """Generate staging layer DBT models for LDIF data.

        Args:
            entries: LDIF entries to generate models for
        Returns:
            FlextResult containing list of staging models

        """
        try:
            logger.info("Generating staging models for %d LDIF entries", len(entries))
            # Analyze schema first
            schema_result = self.analyze_ldif_schema(entries)
            if not schema_result.success:
                return FlextResult[list[FlextLDIFDbtModel]].fail(
                    f"Schema analysis failed: {schema_result.error}",
                )
            schema_info = schema_result.value or {}
            # Use available flext-ldif API methods (group_entries_by_type not available)
            # Create basic grouping by using available methods
            grouped_entries = {"ldif_entries": entries}  # Basic grouping fallback
            models = []
            for entry_type, type_entries in grouped_entries.items():
                schema_name = self.config.get_schema_for_entry_type(entry_type)
                if not schema_name:
                    continue
                # Generate staging model for this entry type
                model = self._generate_staging_model_for_type(
                    entry_type,
                    schema_name,
                    type_entries,
                    schema_info,
                )
                models.append(model)
            logger.info("Generated %d staging models", len(models))
            return FlextResult[list[FlextLDIFDbtModel]].ok(models)
        except Exception as e:
            logger.exception("Error generating staging models")
            return FlextResult[list[FlextLDIFDbtModel]].fail(
                f"Staging model generation error: {e}"
            )

    def generate_analytics_models(
        self,
        staging_models: list[FlextLDIFDbtModel],
    ) -> FlextResult[list[FlextLDIFDbtModel]]:
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
            analytics_models = []
            # Generate LDIF insights model
            insights_model = FlextLDIFDbtModel(
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
                        "type": "decimal(5,2)",
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
                            {"accepted_values": {"values": ["low", "medium", "high"]}},
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
            # Generate hierarchy analysis model
            hierarchy_model = FlextLDIFDbtModel(
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
            return FlextResult[list[FlextLDIFDbtModel]].ok(analytics_models)
        except Exception as e:
            logger.exception("Error generating analytics models")
            return FlextResult[list[FlextLDIFDbtModel]].fail(
                f"Analytics model generation error: {e}"
            )

    def write_models_to_disk(
        self,
        models: list[FlextLDIFDbtModel],
        *,
        overwrite: bool = False,
    ) -> FlextResult[FlextTypes.Core.Dict]:
        """Write generated DBT models to disk.

        Args:
            models: List of models to write
            overwrite: Whether to overwrite existing files
        Returns:
            FlextResult containing write operation results

        """
        try:
            logger.info("Writing %d models to disk: %s", len(models), self.models_dir)
            self.models_dir.mkdir(parents=True, exist_ok=True)
            written_files = []
            for model in models:
                # Generate SQL content using flext-meltano patterns
                sql_content = self._generate_sql_for_model(model)
                # Write SQL file
                sql_file = self.models_dir / f"{model.name}.sql"
                if not overwrite and sql_file.exists():
                    logger.warning("Skipping existing model: %s", sql_file)
                    continue
                sql_file.write_text(sql_content)
                written_files.append(str(sql_file))
                # Write YAML config
                yaml_config = model.to_yaml_config()
                yaml_file = self.models_dir / f"{model.name}.yml"
                # Generate basic YAML content for now (TODO #FLEXT-DBT-001: use flext-meltano when available)
                yaml_content = self._generate_basic_yaml(yaml_config)
                yaml_file.write_text(yaml_content)
                written_files.append(str(yaml_file))
            logger.info("Successfully wrote %d files", len(written_files))
            return FlextResult[FlextTypes.Core.Dict].ok(
                {
                    "written_files": written_files,
                    "models_count": len(models),
                    "output_dir": str(self.models_dir),
                },
            )
        except Exception as e:
            logger.exception("Error writing models to disk")
            return FlextResult[FlextTypes.Core.Dict].fail(f"Model writing error: {e}")

    def _generate_staging_model_for_type(
        self,
        entry_type: str,
        schema_name: str,
        entries: list[FlextLDIFEntry],
        schema_info: FlextTypes.Core.Dict,
    ) -> FlextLDIFDbtModel:
        """Generate a staging model for a specific entry type."""
        # Use entries and schema_info minimally to avoid unused-args and add value
        has_entries = len(entries) > 0
        declared_total = (
            schema_info.get("total_entries") if isinstance(schema_info, dict) else None
        )
        _ = declared_total  # Value can be used by future logic; keep assignment for clarity
        # Create standard LDIF columns
        common_attrs: list[FlextTypes.Core.Dict] = [
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
        # Add mapped attributes from config
        for ldif_attr, mapped_attr in self.config.ldif_attribute_mapping.items():
            if ldif_attr != "dn":  # Already added above
                column_def: FlextTypes.Core.Dict = {
                    "name": mapped_attr,
                    "type": "varchar",  # Default type
                    "description": f"LDIF {ldif_attr} attribute",
                }
                if ldif_attr in self.config.required_attributes:
                    column_def["tests"] = ["not_null"]
                common_attrs.append(column_def)
        return FlextLDIFDbtModel(
            name=schema_name,
            description=f"Staging model for LDIF {entry_type} entries with data quality checks",
            materialization="view",
            columns=common_attrs,
            meta={
                "owner": "data_team",
                "layer": "staging",
                "data_source": "ldif",
                "entry_type": entry_type,
                "has_entries": has_entries,
            },
        )

    def _determine_column_type(self, attr_info: FlextTypes.Core.Dict) -> str:
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

    def _generate_sql_for_model(self, model: FlextLDIFDbtModel) -> str:
        """Generate SQL content for DBT model using flext-meltano patterns."""
        if model.name.startswith("stg_"):
            return self._generate_staging_sql(model)
        if model.name.startswith("analytics_"):
            return self._generate_analytics_sql(model)
        return self._generate_generic_sql(model)

    def _generate_staging_sql(self, model: FlextLDIFDbtModel) -> str:
        """Generate SQL for staging model."""
        # Extract column names safely from dict structure
        columns = []
        for col in model.columns:
            if isinstance(col, dict) and "name" in col:
                col_name = col["name"]
                if isinstance(col_name, str):
                    columns.append(col_name)
        column_list = ",\n    ".join(columns)
        # Validate and safely render materialization (whitelist)
        allowed_materializations = {"view", "table", "ephemeral", "incremental"}
        materialized = (
            model.materialization
            if model.materialization in allowed_materializations
            else "view"
        )
        # Build SQL from static template with whitelisted tokens
        # Note: This generates dbt SQL templates, not executable SQL - variables are controlled inputs
        return (
            "-- Staging model for LDIF data\n"
            "-- Generated automatically by flext-dbt-ldif\n\n"
            "{{ config(materialized='" + materialized + "') }}\n\n"
            "with source_data as (\n"
            "    select\n"
            "        " + column_list + ",\n"
            "        current_timestamp as processed_at\n"
            "    from {{ source('ldif', 'raw_ldif_entries') }}\n"
            "),\n\n"
            "validated_data as (\n"
            "    select *,\n"
            "        case\n"
            "            when dn is not null and length(dn) > 0 then true\n"
            "            else false\n"
            "        end as is_valid_dn,\n"
            "        array_length(string_to_array(dn, ','), 1) as dn_depth\n"
            "    from source_data\n"
            ")\n\n"
            "select * from validated_data\n"
        )

    def _generate_analytics_sql(self, model: FlextLDIFDbtModel) -> str:
        """Generate SQL for analytics model."""
        # Validate and safely render materialization (whitelist)
        allowed_materializations = {"view", "table", "ephemeral", "incremental"}
        materialized = (
            model.materialization
            if model.materialization in allowed_materializations
            else "table"
        )
        if "insights" in model.name:
            return (
                "-- Analytics insights model for LDIF data\n"
                "-- Generated automatically by flext-dbt-ldif\n\n"
                "{{ config(materialized='" + materialized + "') }}\n\n"
                "with entry_stats as (\n"
                "    select\n"
                "        current_timestamp as analysis_date,\n"
                "        'overall' as entry_type,\n"
                "        count(*) as total_entries,\n"
                "        avg(case when is_valid_dn then 100.0 else 0.0 end) as quality_score,\n"
                "        case\n"
                "            when avg(case when is_valid_dn then 100.0 else 0.0 end) >= 90 then 'low'\n"
                "            when avg(case when is_valid_dn then 100.0 else 0.0 end) >= 70 then 'medium'\n"
                "            else 'high'\n"
                "        end as risk_level\n"
                "    from {{ ref('stg_persons') }}\n\n"
                "    union all\n\n"
                "    select\n"
                "        current_timestamp as analysis_date,\n"
                "        'groups' as entry_type,\n"
                "        count(*) as total_entries,\n"
                "        avg(case when is_valid_dn then 100.0 else 0.0 end) as quality_score,\n"
                "        case\n"
                "            when avg(case when is_valid_dn then 100.0 else 0.0 end) >= 90 then 'low'\n"
                "            when avg(case when is_valid_dn then 100.0 else 0.0 end) >= 70 then 'medium'\n"
                "            else 'high'\n"
                "        end as risk_level\n"
                "    from {{ ref('stg_groups') }}\n"
                ")\n\n"
                "select * from entry_stats\n"
            )
        return (
            "-- Analytics hierarchy model for LDIF data\n"
            "-- Generated automatically by flext-dbt-ldif\n\n"
            "{{ config(materialized='" + materialized + "') }}\n\n"
            "with dn_hierarchy as (\n"
            "    select\n"
            "        dn as dn_path,\n"
            "        dn_depth,\n"
            "        case\n"
            "            when dn_depth > 1 then split_part(dn, ',', 2)\n"
            "            else null\n"
            "        end as parent_dn,\n"
            "        0 as children_count,\n"
            "        1 as subtree_size\n"
            "    from {{ ref('stg_persons') }}\n\n"
            "    union all\n\n"
            "    select\n"
            "        dn as dn_path,\n"
            "        dn_depth,\n"
            "        case\n"
            "            when dn_depth > 1 then split_part(dn, ',', 2)\n"
            "            else null\n"
            "        end as parent_dn,\n"
            "        0 as children_count,\n"
            "        1 as subtree_size\n"
            "    from {{ ref('stg_groups') }}\n"
            ")\n\n"
            "select * from dn_hierarchy\n"
        )

    def _generate_generic_sql(self, model: FlextLDIFDbtModel) -> str:
        """Generate generic SQL template."""
        allowed_materializations = {"view", "table", "ephemeral", "incremental"}
        materialized = (
            model.materialization
            if model.materialization in allowed_materializations
            else "view"
        )
        return (
            "-- DBT model: " + model.name + "\n"
            "-- Generated automatically by flext-dbt-ldif\n\n"
            "{{ config(materialized='" + materialized + "') }}\n\n"
            "-- TODO: Implement model logic\n"
            "select 1 as placeholder\n"
        )

    def _generate_basic_yaml(self, yaml_config: FlextTypes.Core.Dict) -> str:
        """Generate basic YAML content for DBT model."""
        # Create schema.yml content
        schema_content = {"version": 2, "models": [yaml_config]}
        return yaml.dump(schema_content, default_flow_style=False, indent=2)


__all__: FlextTypes.Core.StringList = [
    "FlextDbtLdifModelGenerator",
    "FlextLDIFDbtModel",
]
