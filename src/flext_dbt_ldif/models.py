"""Domain models for DBT LDIF transformations."""

from __future__ import annotations

from typing import Annotated

from flext_core import FlextModels, r, t
from flext_ldif import FlextLdifModels
from flext_meltano import FlextMeltanoModels
from pydantic import Field


class FlextDbtLdifModels(FlextMeltanoModels, FlextLdifModels):
    """Model namespace for DBT LDIF metadata objects."""

    class DbtModel(FlextModels.ArbitraryTypesModel):
        """Single DBT model definition payload."""

        name: str
        dbt_model_type: str
        ldif_source: str
        materialization: str = "view"
        sql_content: str
        description: str = ""
        columns: Annotated[
            list[dict[str, t.ContainerValue]],
            Field(default_factory=list),
        ]
        dependencies: Annotated[list[str], Field(default_factory=list)]

        def validate_business_rules(self) -> r[bool]:
            """Validate minimal model constraints."""
            if not self.name.strip():
                return r[bool].fail("Model name cannot be empty")
            if not self.ldif_source.strip():
                return r[bool].fail("LDIF source cannot be empty")
            if not self.sql_content.strip():
                return r[bool].fail("SQL content cannot be empty")
            return r[bool].ok(value=True)



__all__ = ["FlextDbtLdifModels", "m"]

m = FlextDbtLdifModels
