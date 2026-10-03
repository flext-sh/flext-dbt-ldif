"""Constants for DBT LDIF workflows."""

from __future__ import annotations

from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants

from ._constants.base import FlextDbtLdifConstantsBase


class FlextDbtLdifConstants(
    FlextMeltanoConstants, FlextLdifConstants, FlextDbtLdifConstantsBase
):
    """Typed constants used by DBT LDIF modules."""


c = FlextDbtLdifConstants

__all__: list[str] = ["FlextDbtLdifConstants", "FlextDbtLdifConstantsBase", "c"]
