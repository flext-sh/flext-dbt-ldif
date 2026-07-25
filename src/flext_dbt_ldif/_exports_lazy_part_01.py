# AUTO-GENERATED FILE — Regenerate with: make gen
"""Lazy export map part."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map

FLEXT_DBT_LDIF_LAZY_IMPORTS_PART_01 = build_lazy_import_map(
    {
        ".api": (
            "FlextDbtLdif",
            "dbt_ldif",
        ),
        ".base": (
            "FlextDbtLdifServiceBase",
            "s",
        ),
        ".constants": (
            "FlextDbtLdifConstants",
            "c",
        ),
        ".models": (
            "FlextDbtLdifModels",
            "m",
        ),
        ".protocols": (
            "FlextDbtLdifProtocols",
            "p",
        ),
        ".services": ("services",),
        ".services.client": ("FlextDbtLdifClient",),
        ".services.core": ("FlextDbtLdifCore",),
        ".services.service": ("FlextDbtLdifServiceMixin",),
        ".services.unified_service": ("FlextDbtLdifUnifiedService",),
        ".settings": ("FlextDbtLdifSettings",),
        ".typings": (
            "FlextDbtLdifTypes",
            "t",
        ),
        ".utilities": (
            "FlextDbtLdifUtilities",
            "u",
        ),
        "flext_core": (
            "d",
            "e",
            "h",
            "r",
            "x",
        ),
    },
)

__all__: list[str] = ["FLEXT_DBT_LDIF_LAZY_IMPORTS_PART_01"]
