# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if TYPE_CHECKING:
    from flext_tests import d, e, h, r, td, tf, tk, tm, tv, x

    from tests.base import TestsFlextDbtLdifServiceBase, s
    from tests.constants import TestsFlextDbtLdifConstants, c
    from tests.models import TestsFlextDbtLdifModels, m
    from tests.protocols import TestsFlextDbtLdifProtocols, p
    from tests.settings import TestsFlextDbtLdifSettings
    from tests.typings import TestsFlextDbtLdifTypes, t
    from tests.unit._services_parts.data_quality import (
        TestsFlextDbtLdifServicesDataQuality,
    )
    from tests.unit.test_api_surface import TestsFlextDbtLdifApiSurface
    from tests.unit.test_cli import TestsFlextDbtLdifCli
    from tests.unit.test_core import TestsFlextDbtLdifCore
    from tests.unit.test_dbt_client import TestsFlextDbtLdifClient
    from tests.unit.test_dbt_models import TestsFlextDbtLdifDbtModels
    from tests.unit.test_services import TestsFlextDbtLdifServices
    from tests.unit.test_services_and_api import TestsFlextDbtLdifServicesAndApi
    from tests.unit.test_version import TestsFlextDbtLdifVersion
    from tests.utilities import TestsFlextDbtLdifUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".base": (
                "TestsFlextDbtLdifServiceBase",
                "s",
            ),
            ".conftest": ("conftest",),
            ".constants": (
                "TestsFlextDbtLdifConstants",
                "c",
            ),
            ".models": (
                "TestsFlextDbtLdifModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextDbtLdifProtocols",
                "p",
            ),
            ".settings": ("TestsFlextDbtLdifSettings",),
            ".typings": (
                "TestsFlextDbtLdifTypes",
                "t",
            ),
            ".unit": ("unit",),
            ".unit._services_parts.data_quality": (
                "TestsFlextDbtLdifServicesDataQuality",
            ),
            ".unit.test_api_surface": ("TestsFlextDbtLdifApiSurface",),
            ".unit.test_cli": ("TestsFlextDbtLdifCli",),
            ".unit.test_core": ("TestsFlextDbtLdifCore",),
            ".unit.test_dbt_client": ("TestsFlextDbtLdifClient",),
            ".unit.test_dbt_models": ("TestsFlextDbtLdifDbtModels",),
            ".unit.test_services": ("TestsFlextDbtLdifServices",),
            ".unit.test_services_and_api": ("TestsFlextDbtLdifServicesAndApi",),
            ".unit.test_version": ("TestsFlextDbtLdifVersion",),
            ".utilities": (
                "TestsFlextDbtLdifUtilities",
                "u",
            ),
            "flext_tests": (
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        },
    ),
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


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    publish_all=False,
)
