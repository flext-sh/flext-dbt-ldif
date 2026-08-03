# AUTO-GENERATED FILE — Regenerate with: make gen
"""Unit package."""

from __future__ import annotations

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

_LAZY_IMPORTS = merge_lazy_imports(
    ("._services_parts",),
    build_lazy_import_map({
        "._services_parts": ("_services_parts",),
        "._services_parts.data_quality": ("TestsFlextDbtLdifServicesDataQuality",),
        ".test_api_surface": ("TestsFlextDbtLdifApiSurface",),
        ".test_cli": ("TestsFlextDbtLdifCli",),
        ".test_core": ("TestsFlextDbtLdifCore",),
        ".test_dbt_client": ("TestsFlextDbtLdifClient",),
        ".test_dbt_models": ("TestsFlextDbtLdifDbtModels",),
        ".test_services": ("TestsFlextDbtLdifServices",),
        ".test_services_and_api": ("TestsFlextDbtLdifServicesAndApi",),
        ".test_version": ("TestsFlextDbtLdifVersion",),
        "flext_tests": (
            "c",
            "d",
            "e",
            "h",
            "m",
            "p",
            "r",
            "s",
            "t",
            "td",
            "tf",
            "tk",
            "tm",
            "tv",
            "u",
            "x",
        ),
    }),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, publish_all=False)
