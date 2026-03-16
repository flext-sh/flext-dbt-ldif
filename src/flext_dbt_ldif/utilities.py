"""Utility functions for flext-dbt-ldif transformations."""

from __future__ import annotations

from flext_ldif import FlextLdifUtilities


class FlextDbtLdifUtilities(FlextLdifUtilities):
    """Utilities for dbt-ldif operations inheriting LDIF processing capabilities."""


__all__ = ["FlextDbtLdifUtilities"]

u = FlextDbtLdifUtilities
