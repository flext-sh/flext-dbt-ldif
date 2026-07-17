"""Protocols for DBT LDIF integration points."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_ldif import FlextLdifProtocols
from flext_meltano import p

if TYPE_CHECKING:
    from flext_dbt_ldif import m, t


class FlextDbtLdifProtocols(p, FlextLdifProtocols):
    """Namespace for DBT LDIF protocol contracts."""

    class DbtLdif:
        """DBT LDIF protocol namespace."""

        @runtime_checkable
        class Dbt(Protocol):
            """Protocol for DBT model execution and testing."""

            def run_dbt_models(
                self,
                models: t.StrSequence | None = None,
            ) -> p.Result[m.DbtLdif.DbtTransformationResult]:
                """Run DBT models and return execution payload."""
                ...

            def test_dbt_models(
                self,
                models: t.StrSequence | None = None,
            ) -> p.Result[m.DbtLdif.DbtTransformationResult]:
                """Run DBT tests and return status payload."""
                ...


__all__: list[str] = ["FlextDbtLdifProtocols", "p"]

p = FlextDbtLdifProtocols
