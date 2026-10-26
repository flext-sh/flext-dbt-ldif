# AUTO-GENERATED FILE — Regenerate with: make gen
"""Constants for DBT LDIF workflows.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/constants
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_ldif import c
from flext_meltano import c as flext_meltano_c

from flext_dbt_ldif._constants import FlextDbtLdifConstantsBase


class FlextDbtLdifConstants(
    FlextDbtLdifConstantsBase,
    flext_meltano_c,
    c,
):
    """Typed constants used by DBT LDIF modules."""


c = FlextDbtLdifConstants
__all__: list[str] = ["FlextDbtLdifConstants", "FlextDbtLdifConstantsBase", "c"]
