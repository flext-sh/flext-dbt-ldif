# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif. Models package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldif._models.base import FlextModelsDbtLdifBase
    from flext_dbt_ldif._models.dbt import FlextModelsDbtLdifDbt


__all__: tuple[str, ...] = ("FlextModelsDbtLdifBase", "FlextModelsDbtLdifDbt")

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextModelsDbtLdifBase": ".base",
        "FlextModelsDbtLdifDbt": ".dbt",
    }),
    public_exports=__all__,
)
