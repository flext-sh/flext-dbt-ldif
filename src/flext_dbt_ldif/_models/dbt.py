"""DBT LDIF domain models composed into the models facade.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Annotated

from flext_meltano import m

from flext_dbt_ldif import c, t


class FlextModelsDbtLdifDbt:
    """DBT LDIF domain models namespace."""

    class DbtModel(m.ArbitraryTypesModel):
        """Single DBT model definition payload."""

        name: Annotated[t.StrippedStr, m.Field(description="DBT model name.")]
        dbt_model_type: Annotated[
            str,
            m.Field(description="DBT model category."),
        ]
        ldif_source: Annotated[
            t.StrippedStr,
            m.Field(description="LDIF source identifier."),
        ]
        materialization: Annotated[
            str,
            m.Field(
                description="DBT materialization strategy.",
                validate_default=True,
            ),
        ] = c.DbtLdif.DBT_MATERIALIZATION_VIEW
        sql_content: Annotated[
            t.StrippedStr,
            m.Field(description="Rendered SQL for the DBT model."),
        ]
        description: Annotated[
            str,
            m.Field(
                description="Human-readable model description.",
                validate_default=True,
            ),
        ] = ""
        columns: Annotated[
            t.SequenceOf[t.JsonMapping],
            m.Field(description="Column metadata for the DBT model"),
        ] = ()
        dependencies: Annotated[
            t.StrSequence,
            m.Field(description="Upstream model dependencies"),
        ] = ()

    class LdifValidationResult(m.ArbitraryTypesModel):
        """Validated LDIF quality metrics."""

        total_entries: Annotated[
            int,
            m.Field(description="Total LDIF entries validated."),
        ]
        quality_score: Annotated[
            float,
            m.Field(description="Aggregate LDIF quality score."),
        ]
        validation_status: Annotated[
            str,
            m.Field(description="Validation lifecycle status."),
        ]

    class DbtTransformationResult(m.ArbitraryTypesModel):
        """DBT transformation execution summary."""

        records: Annotated[int, m.Field(description="Number of transformed records.")]
        models: Annotated[
            t.StrSequence,
            m.Field(description="Names of models produced by the transformation"),
        ] = ()
        status: Annotated[str, m.Field(description="Transformation lifecycle status.")]

    class ModelGenerationResult(m.ArbitraryTypesModel):
        """Generated model metadata summary."""

        models_generated: Annotated[
            int,
            m.Field(description="Number of generated DBT models."),
        ]
        model_names: Annotated[
            t.StrSequence,
            m.Field(description="Names of generated DBT models"),
        ] = ()

    class ParseValidationResult(m.ArbitraryTypesModel):
        """Combined parse and validation payload."""

        entry_count: Annotated[
            int,
            m.Field(description="Number of parsed LDIF entries."),
        ]
        quality_score: Annotated[
            float, m.Field(description="Validation quality score.")
        ]
        validation_status: Annotated[
            str,
            m.Field(description="Validation lifecycle status."),
        ]

    class WorkflowResult(m.ArbitraryTypesModel):
        """End-to-end service workflow result."""

        ldif_file: Annotated[str, m.Field(description="Input LDIF file path.")]
        entry_count: Annotated[int, m.Field(description="Processed LDIF entry count.")]
        validation_status: Annotated[
            str,
            m.Field(description="Validation lifecycle status."),
        ]
        models_generated: Annotated[
            int,
            m.Field(
                description="Number of generated DBT models.",
                validate_default=True,
            ),
        ] = 0
        transformation_status: Annotated[
            str,
            m.Field(
                description="Transformation lifecycle status.",
                validate_default=True,
            ),
        ] = ""
        workflow_status: Annotated[str, m.Field(description="Overall workflow status.")]

    class DbtConnectionProfile(m.ArbitraryTypesModel):
        """Typed dbt connection profile for LDIF-backed workflows."""

        type: Annotated[str, m.Field(description="dbt adapter type")] = "ldif"
        path: Annotated[str, m.Field(description="LDIF source file path")]
        project: Annotated[str, m.Field(description="dbt project name")]


__all__: list[str] = ["FlextModelsDbtLdifDbt"]
