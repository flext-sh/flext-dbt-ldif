"""Models for LDIF DBT operations.

This module provides data models for LDIF DBT operations.
"""

from flext_core import FlextModels


class FlextDbtLdifModels:
    """Models for LDIF DBT operations."""

    Core = FlextModels

    LdifRecord = dict[str, object]
    LdifRecords = list[LdifRecord]
