"""Models for LDIF DBT operations.

This module provides data models for LDIF DBT operations.
"""

from __future__ import annotations

from typing import override

from flext_core import FlextCore


class FlextDbtLdifModels(FlextCore.Models):
    """Unified DBT LDIF models collection with analytics capabilities.

    Immutable representation of a generated DBT model with LDIF-specific metadata
    and integrated analytics functionality following FLEXT unified class pattern.
    """

    name: str
    dbt_model_type: str  # staging, intermediate, marts, analytics
    ldif_source: str
    change_types: FlextCore.Types.StringList
    columns: list[FlextCore.Types.Dict]
    materialization: str
    sql_content: str
    description: str
    dependencies: FlextCore.Types.StringList

    def validate_business_rules(self) -> FlextCore.Result[None]:
        """Validate DBT LDIF model business rules."""
        try:
            if not self.name.strip():
                return FlextCore.Result[None].fail("Model name cannot be empty")
            if self.dbt_model_type not in {
                "staging",
                "intermediate",
                "marts",
                "analytics",
            }:
                return FlextCore.Result[None].fail("Invalid model_type")
            if not self.ldif_source.strip():
                return FlextCore.Result[None].fail("LDIF source cannot be empty")
            if not self.sql_content.strip():
                return FlextCore.Result[None].fail("SQL content cannot be empty")
            return FlextCore.Result[None].ok(None)
        except Exception as e:
            return FlextCore.Result[None].fail(f"Business rule validation failed: {e}")

    def get_file_path(self) -> str:
        """Get the file path for this DBT LDIF model."""
        return f"models/{self.dbt_model_type}/{self.name}.sql"

    def get_schema_file_path(self) -> str:
        """Get the schema file path for this DBT LDIF model."""
        return f"models/{self.dbt_model_type}/schema.yml"

    def to_sql_file(self) -> FlextCore.Result[str]:
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
            return FlextCore.Result[str].ok(content)
        except Exception as e:
            return FlextCore.Result[str].fail(f"SQL file generation failed: {e}")

    def to_schema_entry(self) -> FlextCore.Result[FlextCore.Types.Dict]:
        """Convert model to schema.yml entry."""
        try:
            schema_entry: FlextCore.Types.Dict = {
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
            return FlextCore.Result[dict["str", "object"]].ok(schema_entry)
        except Exception as e:
            return FlextCore.Result[dict["str", "object"]].fail(
                f"Schema entry generation failed: {e}"
            )

    @classmethod
    def create_generator(
        cls,
        config: FlextCore.Types.Dict,
    ) -> FlextDbtLdifModels.ModelGenerator:
        """Create a model generator instance."""
        return cls.ModelGenerator(config)

    class ModelGenerator:
        """Internal model generator class for DBT LDIF models."""

        @override
        def __init__(
            self,
            config: FlextCore.Types.Dict,
        ) -> None:
            """Initialize the LDIF model generator."""
            self.config = config

        def generate_staging_models(
            self, ldif_sources: FlextCore.Types.StringList
        ) -> FlextCore.Result[list[FlextDbtLdifModels]]:
            """Generate staging models from LDIF sources."""
            staging_models: list[FlextDbtLdifModels] = []

            for ldif_source in ldif_sources:
                model_result = self._create_staging_model(ldif_source)
                if model_result.is_failure:
                    continue

                staging_models.append(model_result.unwrap())

            return FlextCore.Result[list[FlextDbtLdifModels]].ok(staging_models)

        def generate_analytics_models(
            self, staging_models: list[FlextDbtLdifModels]
        ) -> FlextCore.Result[list[FlextDbtLdifModels]]:
            """Generate analytics models from staging models."""
            analytics_models: list[FlextDbtLdifModels] = []

            for staging_model in staging_models:
                model_result = self._create_analytics_model(staging_model)
                if model_result.is_failure:
                    continue

                analytics_models.append(model_result.unwrap())

            return FlextCore.Result[list[FlextDbtLdifModels]].ok(analytics_models)

        def _create_staging_model(
            self, ldif_source: str
        ) -> FlextCore.Result[FlextDbtLdifModels]:
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

                return FlextCore.Result[FlextDbtLdifModels].ok(staging_model)

            except Exception as e:
                return FlextCore.Result[FlextDbtLdifModels].fail(
                    f"Failed to create staging model: {e}"
                )

        def _create_analytics_model(
            self, staging_model: FlextDbtLdifModels
        ) -> FlextCore.Result[FlextDbtLdifModels]:
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

                return FlextCore.Result[FlextDbtLdifModels].ok(analytics_model)

            except Exception as e:
                return FlextCore.Result[FlextDbtLdifModels].fail(
                    f"Failed to create analytics model: {e}"
                )


# ZERO TOLERANCE CONSOLIDATION - FlextDbtLdifUtilities moved to utilities.py
#
# CRITICAL: FlextDbtLdifUtilities was DUPLICATED between models.py and utilities.py.
# This was a ZERO TOLERANCE violation of the user's explicit requirements.
#
# RESOLUTION: Import from utilities.py to eliminate duplication completely.


# Note: This import ensures backward compatibility while eliminating duplication


__all__ = ["FlextDbtLdifModels"]
