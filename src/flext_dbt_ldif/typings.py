"""Project type aliases for flext-dbt-ldif.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/typings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes


class FlextDbtLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """Type namespace for DBT LDIF domain."""

    class DbtLdif:
        """DBT LDIF namespace."""


t = FlextDbtLdifTypes

__all__: list[str] = ["FlextDbtLdifTypes", "t"]
