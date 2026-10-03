"""Protocols for DBT LDIF integration points."""

from __future__ import annotations

from flext_ldif import FlextLdifProtocols
from flext_meltano import FlextMeltanoProtocols


class FlextDbtLdifProtocols(FlextMeltanoProtocols, FlextLdifProtocols):
    """Namespace for DBT LDIF protocol contracts."""

    class DbtLdif:
        """DBT LDIF protocol namespace."""


__all__: list[str] = ["FlextDbtLdifProtocols", "p"]

p = FlextDbtLdifProtocols
