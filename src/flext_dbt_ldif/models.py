"""Domain models for DBT LDIF transformations."""

from __future__ import annotations

from flext_dbt_ldif import c, t
from flext_ldif import FlextLdifModels
from flext_meltano import m, u


class FlextDbtLdifModels(m, FlextLdifModels):
    """Model namespace for DBT LDIF metadata objects."""

    class DbtLdif:
        """DBT LDIF model namespace."""

        class DbtModel(m.ArbitraryTypesModel):
            """Single DBT model definition payload."""

            name: t.StrippedStr = u.Field(description="DBT model name.")
            dbt_model_type: str = u.Field(description="DBT model category.")
            ldif_source: t.StrippedStr = u.Field(description="LDIF source identifier.")
            materialization: str = u.Field(
                c.DbtLdif.DBT_MATERIALIZATION_VIEW,
                description="DBT materialization strategy.",
                validate_default=True,
            )
            sql_content: t.StrippedStr = u.Field(
                description="Rendered SQL for the DBT model.",
            )
            description: str = u.Field(
                "",
                description="Human-readable model description.",
                validate_default=True,
            )
            columns: t.SequenceOf[t.JsonMapping] = u.Field(
                default_factory=tuple,
                description="Column metadata for the DBT model",
            )
            dependencies: t.StrSequence = u.Field(
                default_factory=tuple,
                description="Upstream model dependencies",
            )

            # NOTE (multi-agent, bead mro-wfc8): validate_business_rules() removed — the
            # name/ldif_source/sql_content non-empty checks are now field-level via
            # t.StrippedStr (strip + reject blank at construction). Models are pure
            # pydantic-2-way (flext-law §2a): no methods.

        class LdifValidationResult(m.ArbitraryTypesModel):
            """Validated LDIF quality metrics."""

            total_entries: int = u.Field(description="Total LDIF entries validated.")
            quality_score: float = u.Field(description="Aggregate LDIF quality score.")
            validation_status: str = u.Field(description="Validation lifecycle status.")

        class DbtTransformationResult(m.ArbitraryTypesModel):
            """DBT transformation execution summary."""

            records: int = u.Field(description="Number of transformed records.")
            models: t.StrSequence = u.Field(
                default_factory=tuple,
                description="Names of models produced by the transformation",
            )
            status: str = u.Field(description="Transformation lifecycle status.")

        class ModelGenerationResult(m.ArbitraryTypesModel):
            """Generated model metadata summary."""

            models_generated: int = u.Field(
                description="Number of generated DBT models.",
            )
            model_names: t.StrSequence = u.Field(
                default_factory=tuple,
                description="Names of generated DBT models",
            )

        class ParseValidationResult(m.ArbitraryTypesModel):
            """Combined parse and validation payload."""

            entry_count: int = u.Field(description="Number of parsed LDIF entries.")
            quality_score: float = u.Field(description="Validation quality score.")
            validation_status: str = u.Field(description="Validation lifecycle status.")

        class WorkflowResult(m.ArbitraryTypesModel):
            """End-to-end service workflow result."""

            ldif_file: str = u.Field(description="Input LDIF file path.")
            entry_count: int = u.Field(description="Processed LDIF entry count.")
            validation_status: str = u.Field(description="Validation lifecycle status.")
            models_generated: int = u.Field(
                0,
                description="Number of generated DBT models.",
                validate_default=True,
            )
            transformation_status: str = u.Field(
                "",
                description="Transformation lifecycle status.",
                validate_default=True,
            )
            workflow_status: str = u.Field(description="Overall workflow status.")

        class PipelineResult(m.ArbitraryTypesModel):
            """Client pipeline status payload."""

            parsed_entries: int = u.Field(description="Number of parsed LDIF entries.")
            validation_status: str = u.Field(description="Validation lifecycle status.")
            transformation_status: str = u.Field(
                description="Transformation lifecycle status.",
            )
            pipeline_status: str = u.Field(description="Overall pipeline status.")

        class DbtConnectionProfile(m.ArbitraryTypesModel):
            """Typed dbt connection profile for LDIF-backed workflows."""

            # NOTE (multi-agent): mro-rn88 ADR-006 thin-driver — typed connection_profile.
            type: str = u.Field(default="ldif", description="dbt adapter type")
            path: str = u.Field(description="LDIF source file path")
            project: str = u.Field(description="dbt project name")


__all__: list[str] = ["FlextDbtLdifModels", "m"]

m = FlextDbtLdifModels
