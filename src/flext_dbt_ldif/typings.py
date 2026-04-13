"""Project type aliases for flext-dbt-ldif."""

from __future__ import annotations

from flext_ldif.typings import FlextLdifTypes
from flext_meltano.typings import FlextMeltanoTypes


class FlextDbtLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """Type namespace for DBT LDIF domain."""

    class DbtLdif:
        """DBT LDIF namespace."""


t = FlextDbtLdifTypes

__all__: list[str] = ["FlextDbtLdifTypes", "t"]
