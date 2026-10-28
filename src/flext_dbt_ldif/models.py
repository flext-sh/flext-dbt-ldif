# AUTO-GENERATED FILE — Regenerate with: make gen
"""Domain models for DBT LDIF transformations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import m as flext_meltano_m

from flext_dbt_ldif._models import FlextModelsDbtLdifBase, FlextModelsDbtLdifDbt


class FlextModelsDbtLdif(flext_meltano_m, FlextModelsDbtLdifBase):
    """Model namespace for DBT LDIF metadata objects."""

    class DbtLdif(FlextModelsDbtLdifBase, FlextModelsDbtLdifDbt):
        """DBT LDIF model namespace."""


m = FlextModelsDbtLdif
__all__: list[str] = ["FlextModelsDbtLdif", "m"]
