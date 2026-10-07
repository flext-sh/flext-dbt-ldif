# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif. Constants package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldif._constants.base import FlextDbtLdifConstantsBase


__all__: tuple[str, ...] = ("FlextDbtLdifConstantsBase",)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({"FlextDbtLdifConstantsBase": ".base"}),
    public_exports=__all__,
)
