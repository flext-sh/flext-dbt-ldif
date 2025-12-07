"""Models for LDIF DBT operations.

This module provides data models for LDIF DBT operations.
Uses types from typings.py and constants.py, no dict[str, object].
Uses Python 3.13+ PEP 695 syntax and FlextModels patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal, TypedDict, override

from flext_core import FlextModels, FlextResult, t

from flext_dbt_ldif.constants import FlextDbtLdifConstants
from flext_dbt_ldif.typings import t

# =============================================================================
# TYPEDDICT DEFINITIONS - Type-safe column and model definitions
# =============================================================================


class ColumnDefinition(TypedDict, total=False):
    """Type-safe column definition for DBT models."""

    name: str
    """Column name."""
    description: str
    """Column description."""
    data_type: str
    """Column data type."""


class ModelDefinition(TypedDict, total=True):
    """Type-safe model definition structure."""

    name: str
    """Model name."""
    description: str
    """Model description."""
    columns: Sequence[ColumnDefinition]
    """Model columns."""


# =============================================================================
# MODEL TYPES - Using Literals from constants
# =============================================================================

type DbtModelType = Literal[
    "staging",
    "intermediate",
    "marts",
    "analytics",
]
"""DBT model type literal."""

type MaterializationType = Literal[
    "view",
    "table",
    "incremental",
    "ephemeral",
]
"""DBT materialization type literal."""


# =============================================================================
# MAIN MODEL CLASS
# =============================================================================


class FlextDbtLdifModels(FlextModels):
    """Unified DBT LDIF models collection with analytics capabilities.

    Immutable representation of a generated DBT model with LDIF-specific metadata
    and integrated analytics functionality following FLEXT unified class pattern.
    Uses types from typings.py and constants.py - no dict[str, object].
    """

    name: str
    """DBT model name."""

    dbt_model_type: DbtModelType
    """DBT model type: staging, intermediate, marts, or analytics."""

    ldif_source: str
    """LDIF source identifier."""

    change_types: Sequence[FlextDbtLdifConstants.LdifOperationLiteral]
    """LDIF change types supported by this model."""

    columns: Sequence[ColumnDefinition]
    """Model column definitions."""

    materialization: MaterializationType
    """DBT materialization type."""

    sql_content: str
    """SQL content for the DBT model."""

    description: str
    """Model description."""

    dependencies: Sequence[str]
    """Model dependencies (other model names)."""

    def validate_business_rules(self) -> FlextResult[bool]:
        """Validate DBT LDIF model business rules."""
        try:
            if not self.name.strip():
                return FlextResult[bool].fail("Model name cannot be empty")
            if self.dbt_model_type not in {
                "staging",
                "intermediate",
                "marts",
                "analytics",
            }:
                return FlextResult[bool].fail("Invalid model_type")
            if not self.ldif_source.strip():
                return FlextResult[bool].fail("LDIF source cannot be empty")
            if not self.sql_content.strip():
                return FlextResult[bool].fail("SQL content cannot be empty")
            return FlextResult[bool].ok(True)
        except Exception as e:
            return FlextResult[bool].fail(f"Business rule validation failed: {e}")

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

    def to_schema_entry(self) -> FlextResult[t.JsonDict]:
        """Convert model to schema.yml entry.

        Returns:
            FlextResult[t.JsonDict]: Schema entry as JSON-compatible dict

        """
        try:
            schema_entry: t.JsonDict = {
                "name": self.name,
                "description": self.description,
                "columns": [
                    {
                        "name": col.get("name", ""),
                        "description": col.get("description", ""),
                        "data_type": col.get("data_type", ""),
                    }
                    for col in self.columns
                ],
            }
            return FlextResult[t.JsonDict].ok(schema_entry)
        except Exception as e:
            return FlextResult[t.JsonDict].fail(f"Schema entry generation failed: {e}")

    @classmethod
    def create_generator(
        cls,
        config: t.DbtLdifModel.LdifModelConfig,
    ) -> FlextDbtLdifModels.ModelGenerator:
        """Create a model generator instance.

        Args:
            config: Model generator configuration

        Returns:
            ModelGenerator instance

        """
        return cls.ModelGenerator(config)

    class ModelGenerator:
        """Internal model generator class for DBT LDIF models.

        Uses types from typings.py - no dict[str, object].
        """

        @override
        def __init__(
            self,
            config: t.DbtLdifModel.LdifModelConfig,
        ) -> None:
            """Initialize the LDIF model generator.

            Args:
                config: Model generator configuration

            """
            self.config = config

        def generate_staging_models(
            self,
            ldif_sources: Sequence[str],
        ) -> FlextResult[Sequence[FlextDbtLdifModels]]:
            """Generate staging models from LDIF sources.

            Args:
                ldif_sources: List of LDIF source identifiers

            Returns:
                FlextResult[Sequence[FlextDbtLdifModels]]: Generated staging models

            """
            staging_models: list[FlextDbtLdifModels] = []

            for ldif_source in ldif_sources:
                model_result = self._create_staging_model(ldif_source)
                if model_result.is_failure:
                    continue

                staging_models.append(model_result.unwrap())

            return FlextResult[Sequence[FlextDbtLdifModels]].ok(staging_models)

        def generate_analytics_models(
            self,
            staging_models: Sequence[FlextDbtLdifModels],
        ) -> FlextResult[Sequence[FlextDbtLdifModels]]:
            """Generate analytics models from staging models.

            Args:
                staging_models: List of staging models

            Returns:
                FlextResult[Sequence[FlextDbtLdifModels]]: Generated analytics models

            """
            analytics_models: list[FlextDbtLdifModels] = []

            for staging_model in staging_models:
                model_result = self._create_analytics_model(staging_model)
                if model_result.is_failure:
                    continue

                analytics_models.append(model_result.unwrap())

            return FlextResult[Sequence[FlextDbtLdifModels]].ok(analytics_models)

        def _create_staging_model(
            self,
            ldif_source: str,
        ) -> FlextResult[FlextDbtLdifModels]:
            """Create a staging model from LDIF source.

            Args:
                ldif_source: LDIF source identifier

            Returns:
                FlextResult[FlextDbtLdifModels]: Created staging model

            """
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
                    change_types=[
                        FlextDbtLdifConstants.LdifOperations.ADD,
                        FlextDbtLdifConstants.LdifOperations.MODIFY,
                        FlextDbtLdifConstants.LdifOperations.DELETE,
                    ],
                    columns=[],
                    materialization="view",
                    sql_content=sql_content.strip(),
                    description=f"Staging model for LDIF source {ldif_source}",
                    dependencies=[],
                )

                return FlextResult[FlextDbtLdifModels].ok(staging_model)

            except Exception as e:
                return FlextResult[FlextDbtLdifModels].fail(
                    f"Failed to create staging model: {e}",
                )

        def _create_analytics_model(
            self,
            staging_model: FlextDbtLdifModels,
        ) -> FlextResult[FlextDbtLdifModels]:
            """Create an analytics model from staging model.

            Args:
                staging_model: Source staging model

            Returns:
                FlextResult[FlextDbtLdifModels]: Created analytics model

            """
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
                        ColumnDefinition(
                            name="analytics_timestamp",
                            description="Analytics processing timestamp",
                            data_type="TIMESTAMP",
                        ),
                    ],
                    materialization="table",
                    sql_content=sql_content.strip(),
                    description=f"Analytics model for {staging_model.ldif_source}",
                    dependencies=[staging_model.name],
                )

                return FlextResult[FlextDbtLdifModels].ok(analytics_model)

            except Exception as e:
                return FlextResult[FlextDbtLdifModels].fail(
                    f"Failed to create analytics model: {e}",
                )


__all__: list[str] = [
    "ColumnDefinition",
    "DbtModelType",
    "FlextDbtLdifModels",
    "MaterializationType",
    "ModelDefinition",
]
