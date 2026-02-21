"""Domain models for DBT LDIF transformations."""

from __future__ import annotations

from flext_core import FlextModels, FlextResult, t
from pydantic import Field


class FlextDbtLdifModels(FlextModels):
    """Model namespace for DBT LDIF metadata objects."""

    class DbtModel(FlextModels.ArbitraryTypesModel):
        """Single DBT model definition payload."""

        name: str
        dbt_model_type: str
        ldif_source: str
        materialization: str = "view"
        sql_content: str
        description: str = ""
        columns: list[dict[str, t.GeneralValueType]] = Field(default_factory=list)
        dependencies: list[str] = Field(default_factory=list)

        def validate_business_rules(self) -> FlextResult[bool]:
            """Validate minimal model constraints."""
            if not self.name.strip():
                return FlextResult[bool].fail("Model name cannot be empty")
            if not self.ldif_source.strip():
                return FlextResult[bool].fail("LDIF source cannot be empty")
            if not self.sql_content.strip():
                return FlextResult[bool].fail("SQL content cannot be empty")
            return FlextResult[bool].ok(value=True)


m = FlextDbtLdifModels

__all__ = ["FlextDbtLdifModels", "m"]
