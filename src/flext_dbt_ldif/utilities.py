"""Utility functions for flext-dbt-ldif transformations."""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import FlextMeltanoUtilities


class FlextDbtLdifUtilities(FlextMeltanoUtilities, FlextLdifUtilities):
    """Utilities for dbt-ldif operations inheriting LDIF processing capabilities."""

    class DbtLdif(FlextLdifUtilities):
        """DBT LDIF utilities namespace — inherits LDIF utility methods."""


u = FlextDbtLdifUtilities

__all__ = [
    "FlextDbtLdifUtilities",
    "u",
]
