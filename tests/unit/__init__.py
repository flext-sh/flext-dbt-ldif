# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".test_api_surface": ("test_api_surface",),
        ".test_cli": (
            "TestFlextDbtLdifCliService",
            "TestMainEntryPoint",
        ),
        ".test_core": ("TestsFlextDbtLdifCore",),
        ".test_dbt_client": ("TestsFlextDbtLdifClient",),
        ".test_dbt_models": ("TestsFlextDbtLdifDbtModels",),
        ".test_services": ("test_services",),
        ".test_services_and_api": ("test_services_and_api",),
        ".test_version": ("test_version",),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
