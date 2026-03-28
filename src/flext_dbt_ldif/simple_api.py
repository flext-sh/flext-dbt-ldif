"""Re-export shim — canonical implementation lives in _utilities.simple_api."""

from __future__ import annotations

from flext_dbt_ldif._utilities.simple_api import (
    FlextDbtLdif,
    FlextDbtLdifEntryListAdapter,
)

__all__ = ["FlextDbtLdif", "FlextDbtLdifEntryListAdapter"]
