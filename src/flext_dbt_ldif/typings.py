"""Project type aliases for flext-dbt-ldif."""

from __future__ import annotations

from flext_ldif import FlextLdifTypes
from flext_meltano import FlextMeltanoTypes


class FlextDbtLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """Type namespace for DBT LDIF domain."""

    class DbtLdif:
        """DBT LDIF namespace."""


t = FlextDbtLdifTypes

__all__ = ["FlextDbtLdifTypes", "t"]
