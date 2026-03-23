"""Protocols for DBT LDIF integration points."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_core import r
from flext_ldif import FlextLdifProtocols
from flext_meltano import FlextMeltanoProtocols

from flext_dbt_ldif import m


class FlextDbtLdifProtocols(FlextMeltanoProtocols, FlextLdifProtocols):
    """Namespace for DBT LDIF protocol contracts."""

    class DbtLdif:
        """DBT LDIF protocol namespace."""

        @runtime_checkable
        class Dbt(Protocol):
            """Protocol for DBT model execution and testing."""

            def run_dbt_models(
                self, models: Sequence[str] | None = None
            ) -> r[m.DbtLdif.DbtTransformationResult]:
                """Run DBT models and return execution payload."""
                ...

            def test_dbt_models(
                self, models: Sequence[str] | None = None
            ) -> r[m.DbtLdif.DbtTransformationResult]:
                """Run DBT tests and return status payload."""
                ...


__all__ = ["FlextDbtLdifProtocols", "p"]

p = FlextDbtLdifProtocols
