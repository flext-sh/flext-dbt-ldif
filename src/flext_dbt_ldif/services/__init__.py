# AUTO-GENERATED FILE — Regenerate with: make gen
"""Services package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldif.services.client import FlextDbtLdifClient as FlextDbtLdifClient
    from flext_dbt_ldif.services.core import FlextDbtLdifCore as FlextDbtLdifCore
    from flext_dbt_ldif.services.service import (
        FlextDbtLdifServiceMixin as FlextDbtLdifServiceMixin,
    )
    from flext_dbt_ldif.services.unified_service import (
        FlextDbtLdifUnifiedService as FlextDbtLdifUnifiedService,
    )
_LAZY_IMPORTS = build_lazy_import_map({
    ".client": ("FlextDbtLdifClient",),
    ".core": ("FlextDbtLdifCore",),
    ".service": ("FlextDbtLdifServiceMixin",),
    ".unified_service": ("FlextDbtLdifUnifiedService",),
})


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
