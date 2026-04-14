"""Domain models for DBT LDIF transformations."""

from __future__ import annotations

from collections.abc import Sequence

from flext_dbt_ldif import c, p, r, t, u
from flext_ldif import FlextLdifModels
from flext_meltano import m


class FlextDbtLdifModels(m, FlextLdifModels):
    """Model namespace for DBT LDIF metadata objects."""

    class DbtLdif:
        """DBT LDIF model namespace."""

        class DbtModel(m.ArbitraryTypesModel):
            """Single DBT model definition payload."""

            name: str = u.Field(description="DBT model name.")
            dbt_model_type: str = u.Field(description="DBT model category.")
            ldif_source: str = u.Field(description="LDIF source identifier.")
            materialization: str = u.Field(
                c.DbtLdif.DBT_MATERIALIZATION_VIEW,
                description="DBT materialization strategy.",
                validate_default=True,
            )
            sql_content: str = u.Field(description="Rendered SQL for the DBT model.")
            description: str = u.Field(
                "",
                description="Human-readable model description.",
                validate_default=True,
            )
            columns: Sequence[t.ContainerValueMapping] = u.Field(
                default_factory=list,
                description="Column metadata payloads for the model.",
            )
            dependencies: t.StrSequence = u.Field(
                default_factory=list,
                description="Upstream DBT model dependencies.",
            )

            def validate_business_rules(self) -> p.Result[bool]:
                """Validate minimal model constraints."""
                if not self.name.strip():
                    return r[bool].fail("Model name cannot be empty")
                if not self.ldif_source.strip():
                    return r[bool].fail("LDIF source cannot be empty")
                if not self.sql_content.strip():
                    return r[bool].fail("SQL content cannot be empty")
                return r[bool].ok(value=True)

        class LdifValidationResult(m.ArbitraryTypesModel):
            """Validated LDIF quality metrics."""

            total_entries: int = u.Field(description="Total LDIF entries validated.")
            quality_score: float = u.Field(description="Aggregate LDIF quality score.")
            validation_status: str = u.Field(description="Validation lifecycle status.")

        class DbtTransformationResult(m.ArbitraryTypesModel):
            """DBT transformation execution summary."""

            records: int = u.Field(description="Number of transformed records.")
            models: t.StrSequence = u.Field(
                default_factory=list,
                description="Names of transformed DBT models.",
            )
            status: str = u.Field(description="Transformation lifecycle status.")

        class ModelGenerationResult(m.ArbitraryTypesModel):
            """Generated model metadata summary."""

            models_generated: int = u.Field(
                description="Number of generated DBT models.",
            )
            model_names: t.StrSequence = u.Field(
                default_factory=list,
                description="Generated DBT model names.",
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


__all__: list[str] = ["FlextDbtLdifModels", "m"]

m = FlextDbtLdifModels
