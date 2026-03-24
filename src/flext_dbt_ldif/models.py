"""Domain models for DBT LDIF transformations."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Annotated

from flext_core import FlextModels, r
from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels
from pydantic import Field

from flext_dbt_ldif import t


class FlextDbtLdifModels(FlextMeltanoModels, FlextLdifModels):
    """Model namespace for DBT LDIF metadata objects."""

    class DbtLdif:
        """DBT LDIF model namespace."""

        class DbtModel(FlextModels.ArbitraryTypesModel):
            """Single DBT model definition payload."""

            name: str
            dbt_model_type: str
            ldif_source: str
            materialization: str = "view"
            sql_content: str
            description: str = ""
            columns: Annotated[
                Sequence[Mapping[str, t.ContainerValue]],
                Field(default_factory=list),
            ]
            dependencies: Annotated[Sequence[str], Field(default_factory=list)]

            def validate_business_rules(self) -> r[bool]:
                """Validate minimal model constraints."""
                if not self.name.strip():
                    return r[bool].fail("Model name cannot be empty")
                if not self.ldif_source.strip():
                    return r[bool].fail("LDIF source cannot be empty")
                if not self.sql_content.strip():
                    return r[bool].fail("SQL content cannot be empty")
                return r[bool].ok(value=True)

        class LdifValidationResult(FlextModels.ArbitraryTypesModel):
            """Validated LDIF quality metrics."""

            total_entries: int
            quality_score: float
            validation_status: str

        class DbtTransformationResult(FlextModels.ArbitraryTypesModel):
            """DBT transformation execution summary."""

            records: int
            models: Annotated[Sequence[str], Field(default_factory=list)]
            status: str

        class ModelGenerationResult(FlextModels.ArbitraryTypesModel):
            """Generated model metadata summary."""

            models_generated: int
            model_names: Annotated[Sequence[str], Field(default_factory=list)]

        class ParseValidationResult(FlextModels.ArbitraryTypesModel):
            """Combined parse and validation payload."""

            entry_count: int
            quality_score: float
            validation_status: str

        class WorkflowResult(FlextModels.ArbitraryTypesModel):
            """End-to-end service workflow result."""

            ldif_file: str
            entry_count: int
            validation_status: str
            models_generated: int = 0
            transformation_status: str = ""
            workflow_status: str

        class PipelineResult(FlextModels.ArbitraryTypesModel):
            """Client pipeline status payload."""

            parsed_entries: int
            validation_status: str
            transformation_status: str
            pipeline_status: str


__all__ = ["FlextDbtLdifModels", "m"]

m = FlextDbtLdifModels
