"""Domain models for DBT LDIF transformations.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_meltano import FlextMeltanoModels

from flext_dbt_ldif._models import FlextDbtLdifModelsBase, FlextDbtLdifModelsDbt


class FlextDbtLdifModels(FlextMeltanoModels, FlextDbtLdifModelsBase):
    """Model namespace for DBT LDIF metadata objects."""

    class DbtLdif(FlextDbtLdifModelsBase, FlextDbtLdifModelsDbt):
        """DBT LDIF model namespace."""


m = FlextDbtLdifModels

__all__: list[str] = ["FlextDbtLdifModels", "m"]
