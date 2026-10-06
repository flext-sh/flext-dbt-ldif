"""Protocols for DBT LDIF integration points.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/protocols
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifProtocols
from flext_meltano import FlextMeltanoProtocols


class FlextDbtLdifProtocols(FlextMeltanoProtocols, FlextLdifProtocols):
    """Namespace for DBT LDIF protocol contracts."""

    class DbtLdif:
        """DBT LDIF protocol namespace."""


p = FlextDbtLdifProtocols

__all__: list[str] = ["FlextDbtLdifProtocols", "p"]
