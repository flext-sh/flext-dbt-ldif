"""Constants for DBT LDIF workflows.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/constants
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import FlextLdifConstants
from flext_meltano import FlextMeltanoConstants

from flext_dbt_ldif._constants.base import FlextDbtLdifConstantsBase


class FlextDbtLdifConstants(
    FlextMeltanoConstants,
    FlextLdifConstants,
    FlextDbtLdifConstantsBase,
):
    """Typed constants used by DBT LDIF modules."""


c = FlextDbtLdifConstants

__all__: list[str] = ["FlextDbtLdifConstants", "FlextDbtLdifConstantsBase", "c"]
