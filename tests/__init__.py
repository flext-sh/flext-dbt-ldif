# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Tests package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

    from flext_dbt_ldif import d, e, h, r, s, x

    from . import unit as unit
    from .conftest import (
        dbt_ldif_profile,
        dbt_ldif_project_config,
        docker_control,
        ensure_shared_docker_container,
        ldif_source_config,
        pytest_configure,
        sample_ldif_entries,
        set_test_environment,
        shared_ldap_container,
    )
    from .constants import TestsFlextDbtLdifConstants, TestsFlextDbtLdifConstants as c
    from .models import TestsFlextDbtLdifModels, TestsFlextDbtLdifModels as m
    from .protocols import TestsFlextDbtLdifProtocols, TestsFlextDbtLdifProtocols as p
    from .typings import TestsFlextDbtLdifTypes, TestsFlextDbtLdifTypes as t
    from .unit.test_api_surface import test_api_imports
    from .unit.test_cli import TestFlextDbtLdifCliService, TestMainEntryPoint
    from .unit.test_core import TestAnalytics, TestModelGenerator
    from .unit.test_dbt_client import TestFlextDbtLdifClient
    from .unit.test_dbt_models import TestDbtModel, TestFlextDbtLdifUnifiedService
    from .unit.test_services import (
        svc,
        test_parse_and_validate_ldif_parse_fails,
        test_run_complete_workflow_all,
        test_run_data_quality_assessment,
    )
    from .unit.test_services_and_api import (
        service,
        test_api_generate_ldif_models,
        test_api_process_ldif_file,
        test_api_validate_ldif_quality,
        test_generate_and_write_models_ok,
        test_parse_and_validate_ldif_ok,
    )
    from .unit.test_version import test_dunder_alignment, test_version_is_string
    from .utilities import TestsFlextDbtLdifUtilities, TestsFlextDbtLdifUtilities as u

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "TestAnalytics": ("tests.unit.test_core", "TestAnalytics"),
    "TestDbtModel": ("tests.unit.test_dbt_models", "TestDbtModel"),
    "TestFlextDbtLdifCliService": ("tests.unit.test_cli", "TestFlextDbtLdifCliService"),
    "TestFlextDbtLdifClient": ("tests.unit.test_dbt_client", "TestFlextDbtLdifClient"),
    "TestFlextDbtLdifUnifiedService": (
        "tests.unit.test_dbt_models",
        "TestFlextDbtLdifUnifiedService",
    ),
    "TestMainEntryPoint": ("tests.unit.test_cli", "TestMainEntryPoint"),
    "TestModelGenerator": ("tests.unit.test_core", "TestModelGenerator"),
    "TestsFlextDbtLdifConstants": ("tests.constants", "TestsFlextDbtLdifConstants"),
    "TestsFlextDbtLdifModels": ("tests.models", "TestsFlextDbtLdifModels"),
    "TestsFlextDbtLdifProtocols": ("tests.protocols", "TestsFlextDbtLdifProtocols"),
    "TestsFlextDbtLdifTypes": ("tests.typings", "TestsFlextDbtLdifTypes"),
    "TestsFlextDbtLdifUtilities": ("tests.utilities", "TestsFlextDbtLdifUtilities"),
    "c": ("tests.constants", "TestsFlextDbtLdifConstants"),
    "d": ("flext_dbt_ldif", "d"),
    "dbt_ldif_profile": ("tests.conftest", "dbt_ldif_profile"),
    "dbt_ldif_project_config": ("tests.conftest", "dbt_ldif_project_config"),
    "docker_control": ("tests.conftest", "docker_control"),
    "e": ("flext_dbt_ldif", "e"),
    "ensure_shared_docker_container": (
        "tests.conftest",
        "ensure_shared_docker_container",
    ),
    "h": ("flext_dbt_ldif", "h"),
    "ldif_source_config": ("tests.conftest", "ldif_source_config"),
    "m": ("tests.models", "TestsFlextDbtLdifModels"),
    "p": ("tests.protocols", "TestsFlextDbtLdifProtocols"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "r": ("flext_dbt_ldif", "r"),
    "s": ("flext_dbt_ldif", "s"),
    "sample_ldif_entries": ("tests.conftest", "sample_ldif_entries"),
    "service": ("tests.unit.test_services_and_api", "service"),
    "set_test_environment": ("tests.conftest", "set_test_environment"),
    "shared_ldap_container": ("tests.conftest", "shared_ldap_container"),
    "svc": ("tests.unit.test_services", "svc"),
    "t": ("tests.typings", "TestsFlextDbtLdifTypes"),
    "test_api_generate_ldif_models": (
        "tests.unit.test_services_and_api",
        "test_api_generate_ldif_models",
    ),
    "test_api_imports": ("tests.unit.test_api_surface", "test_api_imports"),
    "test_api_process_ldif_file": (
        "tests.unit.test_services_and_api",
        "test_api_process_ldif_file",
    ),
    "test_api_validate_ldif_quality": (
        "tests.unit.test_services_and_api",
        "test_api_validate_ldif_quality",
    ),
    "test_dunder_alignment": ("tests.unit.test_version", "test_dunder_alignment"),
    "test_generate_and_write_models_ok": (
        "tests.unit.test_services_and_api",
        "test_generate_and_write_models_ok",
    ),
    "test_parse_and_validate_ldif_ok": (
        "tests.unit.test_services_and_api",
        "test_parse_and_validate_ldif_ok",
    ),
    "test_parse_and_validate_ldif_parse_fails": (
        "tests.unit.test_services",
        "test_parse_and_validate_ldif_parse_fails",
    ),
    "test_run_complete_workflow_all": (
        "tests.unit.test_services",
        "test_run_complete_workflow_all",
    ),
    "test_run_data_quality_assessment": (
        "tests.unit.test_services",
        "test_run_data_quality_assessment",
    ),
    "test_version_is_string": ("tests.unit.test_version", "test_version_is_string"),
    "u": ("tests.utilities", "TestsFlextDbtLdifUtilities"),
    "unit": ("tests.unit", ""),
    "x": ("flext_dbt_ldif", "x"),
}

__all__ = [
    "TestAnalytics",
    "TestDbtModel",
    "TestFlextDbtLdifCliService",
    "TestFlextDbtLdifClient",
    "TestFlextDbtLdifUnifiedService",
    "TestMainEntryPoint",
    "TestModelGenerator",
    "TestsFlextDbtLdifConstants",
    "TestsFlextDbtLdifModels",
    "TestsFlextDbtLdifProtocols",
    "TestsFlextDbtLdifTypes",
    "TestsFlextDbtLdifUtilities",
    "c",
    "d",
    "dbt_ldif_profile",
    "dbt_ldif_project_config",
    "docker_control",
    "e",
    "ensure_shared_docker_container",
    "h",
    "ldif_source_config",
    "m",
    "p",
    "pytest_configure",
    "r",
    "s",
    "sample_ldif_entries",
    "service",
    "set_test_environment",
    "shared_ldap_container",
    "svc",
    "t",
    "test_api_generate_ldif_models",
    "test_api_imports",
    "test_api_process_ldif_file",
    "test_api_validate_ldif_quality",
    "test_dunder_alignment",
    "test_generate_and_write_models_ok",
    "test_parse_and_validate_ldif_ok",
    "test_parse_and_validate_ldif_parse_fails",
    "test_run_complete_workflow_all",
    "test_run_data_quality_assessment",
    "test_version_is_string",
    "u",
    "unit",
    "x",
]


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
