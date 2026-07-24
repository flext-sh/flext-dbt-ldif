"""Utility functions for flext-dbt-ldif transformations."""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities
from flext_meltano import u


class FlextDbtLdifUtilities(u, FlextLdifUtilities):
    """Utilities for dbt-ldif operations inheriting LDIF processing capabilities."""

    class DbtLdif:
        """DBT LDIF namespace over the canonical LDIF utility branch."""


u = FlextDbtLdifUtilities

__all__: list[str] = ["FlextDbtLdifUtilities", "u"]
