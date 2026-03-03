"""Protocols for DBT LDIF integration points."""

from __future__ import annotations

from typing import Protocol, runtime_checkable

from flext_core import FlextResult, m
from flext_ldif import FlextLdifProtocols
from flext_meltano import FlextMeltanoProtocols

type LdifPayload = m.Dict


class FlextDbtLdifProtocols(FlextMeltanoProtocols, FlextLdifProtocols):
    """Namespace for DBT LDIF protocol contracts."""

    class DbtLdif:
        """DBT LDIF protocol namespace."""

        @runtime_checkable
        class DbtProtocol(Protocol):
            """Protocol for DBT model execution and testing."""

            def run_dbt_models(
                self,
                models: list[str] | None = None,
            ) -> FlextResult[LdifPayload]:
                """Run DBT models and return execution payload."""
                ...

            def test_dbt_models(
                self,
                models: list[str] | None = None,
            ) -> FlextResult[LdifPayload]:
                """Run DBT tests and return status payload."""
                ...


p = FlextDbtLdifProtocols

__all__ = ["FlextDbtLdifProtocols", "p"]
