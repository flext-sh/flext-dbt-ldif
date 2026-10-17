# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif.services package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldif.services.client import FlextDbtLdifClient
    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
    from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService


__all__: tuple[str, ...] = (
    "FlextDbtLdifClient",
    "FlextDbtLdifServiceMixin",
    "FlextDbtLdifUnifiedService",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtLdifClient": ".client",
        "FlextDbtLdifServiceMixin": ".service",
        "FlextDbtLdifUnifiedService": ".unified_service",
    }),
    public_exports=__all__,
)
