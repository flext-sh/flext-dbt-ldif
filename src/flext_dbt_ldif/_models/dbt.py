"""DBT LDIF domain models composed into the models facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m

from flext_dbt_ldif import c, t


class FlextDbtLdifModelsDbt:
    """DBT LDIF domain models namespace."""

    class DbtModel(m.ArbitraryTypesModel):
        """Single DBT model definition payload."""

        name: t.StrippedStr = m.Field(description="DBT model name.")
        dbt_model_type: str = m.Field(description="DBT model category.")
        ldif_source: t.StrippedStr = m.Field(description="LDIF source identifier.")
        materialization: str = m.Field(
            c.DbtLdif.DBT_MATERIALIZATION_VIEW,
            description="DBT materialization strategy.",
            validate_default=True,
        )
        sql_content: t.StrippedStr = m.Field(
            description="Rendered SQL for the DBT model.",
        )
        description: str = m.Field(
            "",
            description="Human-readable model description.",
            validate_default=True,
        )
        columns: t.SequenceOf[t.JsonMapping] = m.Field(
            default_factory=tuple,
            description="Column metadata for the DBT model",
        )
        dependencies: t.StrSequence = m.Field(
            default_factory=tuple,
            description="Upstream model dependencies",
        )

    class LdifValidationResult(m.ArbitraryTypesModel):
        """Validated LDIF quality metrics."""

        total_entries: int = m.Field(description="Total LDIF entries validated.")
        quality_score: float = m.Field(description="Aggregate LDIF quality score.")
        validation_status: str = m.Field(description="Validation lifecycle status.")

    class DbtTransformationResult(m.ArbitraryTypesModel):
        """DBT transformation execution summary."""

        records: int = m.Field(description="Number of transformed records.")
        models: t.StrSequence = m.Field(
            default_factory=tuple,
            description="Names of models produced by the transformation",
        )
        status: str = m.Field(description="Transformation lifecycle status.")

    class ModelGenerationResult(m.ArbitraryTypesModel):
        """Generated model metadata summary."""

        models_generated: int = m.Field(
            description="Number of generated DBT models.",
        )
        model_names: t.StrSequence = m.Field(
            default_factory=tuple,
            description="Names of generated DBT models",
        )

    class ParseValidationResult(m.ArbitraryTypesModel):
        """Combined parse and validation payload."""

        entry_count: int = m.Field(description="Number of parsed LDIF entries.")
        quality_score: float = m.Field(description="Validation quality score.")
        validation_status: str = m.Field(description="Validation lifecycle status.")

    class WorkflowResult(m.ArbitraryTypesModel):
        """End-to-end service workflow result."""

        ldif_file: str = m.Field(description="Input LDIF file path.")
        entry_count: int = m.Field(description="Processed LDIF entry count.")
        validation_status: str = m.Field(description="Validation lifecycle status.")
        models_generated: int = m.Field(
            0,
            description="Number of generated DBT models.",
            validate_default=True,
        )
        transformation_status: str = m.Field(
            "",
            description="Transformation lifecycle status.",
            validate_default=True,
        )
        workflow_status: str = m.Field(description="Overall workflow status.")

    class DbtConnectionProfile(m.ArbitraryTypesModel):
        """Typed dbt connection profile for LDIF-backed workflows."""

        type: str = m.Field(default="ldif", description="dbt adapter type")
        path: str = m.Field(description="LDIF source file path")
        project: str = m.Field(description="dbt project name")


__all__: list[str] = ["FlextDbtLdifModelsDbt"]
