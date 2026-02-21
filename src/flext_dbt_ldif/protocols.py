"""Protocols for DBT LDIF integration points."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, t


class FlextDbtLdifProtocols:
    """Namespace for DBT LDIF protocol contracts."""

    class DbtLdif:
        """DBT LDIF protocol namespace."""

        @runtime_checkable
        class DbtProtocol(Protocol):
            """Protocol for DBT model execution and testing."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
            ) -> FlextResult[dict[str, t.JsonValue]]:
                """Run DBT models and return execution payload."""
                ...

            def test_dbt_models(
                self,
                models: list[str] | None = None,
            ) -> FlextResult[dict[str, t.JsonValue]]:
                """Run DBT tests and return status payload."""
                ...


p = FlextDbtLdifProtocols

__all__ = ["FlextDbtLdifProtocols", "p"]
