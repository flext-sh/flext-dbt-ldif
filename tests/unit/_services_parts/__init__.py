# AUTO-GENERATED FILE — Regenerate with: make gen
"""Services Parts package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_dbt_ldif.tests.unit._services_parts.data_quality import (
        TestsFlextDbtLdifServicesDataQuality as TestsFlextDbtLdifServicesDataQuality,
    )
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".data_quality": ("TestsFlextDbtLdifServicesDataQuality",),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
