"""Utility functions for flext-dbt-ldif transformations."""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities


class FlextDbtLdifUtilities(FlextLdifUtilities):
    """Utilities for dbt-ldif operations inheriting LDIF processing capabilities."""

    class DbtLdif(FlextLdifUtilities):
        """DBT LDIF utilities namespace."""


__all__ = ["FlextDbtLdifUtilities"]

u = FlextDbtLdifUtilities
