"""Project type aliases for flext-dbt-ldif."""

from __future__ import annotations

from collections.abc import Sequence

from flext_dbt_ldif import u
from flext_ldif.typings import FlextLdifTypes
from flext_meltano.typings import FlextMeltanoTypes


class FlextDbtLdifTypes(FlextMeltanoTypes, FlextLdifTypes):
    """Type namespace for DBT LDIF domain."""

    class DbtLdif:
        """DBT LDIF namespace."""

        ENTRY_CONTAINER_SEQUENCE_ADAPTER: u.TypeAdapter[
            Sequence[FlextMeltanoTypes.ContainerValueMapping]
        ] = u.TypeAdapter(Sequence[FlextMeltanoTypes.ContainerValueMapping])


t = FlextDbtLdifTypes

__all__: list[str] = ["FlextDbtLdifTypes", "t"]
