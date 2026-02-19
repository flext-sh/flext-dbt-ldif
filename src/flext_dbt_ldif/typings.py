"""Project type aliases for flext-dbt-ldif."""

from __future__ import annotations

from flext_core import FlextTypes


class FlextDbtLdifTypes(FlextTypes):
    """Type namespace for DBT LDIF domain."""


t = FlextDbtLdifTypes

__all__ = ["FlextDbtLdifTypes", "t"]
