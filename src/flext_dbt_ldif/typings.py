"""Project type aliases for flext-dbt-ldif."""

from __future__ import annotations

from collections.abc import (
    Sequence,
)

from flext_ldif import FlextLdifTypes
from flext_meltano import t

from flext_dbt_ldif import u


class FlextDbtLdifTypes(t, FlextLdifTypes):
    """Type namespace for DBT LDIF domain."""

    class DbtLdif:
        """DBT LDIF namespace."""

        ENTRY_CONTAINER_SEQUENCE_ADAPTER: u.TypeAdapter[Sequence[t.JsonMapping]] = (
            u.TypeAdapter(Sequence[t.JsonMapping])
        )


t = FlextDbtLdifTypes

__all__: list[str] = ["FlextDbtLdifTypes", "t"]
