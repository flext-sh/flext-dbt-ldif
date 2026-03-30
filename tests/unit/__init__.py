# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes

    from tests.unit import (
        test_api_surface,
        test_cli,
        test_core,
        test_dbt_client,
        test_dbt_models,
        test_services,
        test_services_and_api,
        test_version,
    )
    from tests.unit.test_api_surface import test_api_imports
    from tests.unit.test_cli import (
        FlextDbtLdifCliService,
        TestFlextDbtLdifCliService,
        TestMainEntryPoint,
    )
    from tests.unit.test_core import FlextDbtLdifCore, TestAnalytics, TestModelGenerator
    from tests.unit.test_dbt_client import FlextDbtLdifClient, TestFlextDbtLdifClient
    from tests.unit.test_dbt_models import (
        FlextDbtLdifUnifiedService,
        TestDbtModel,
        TestFlextDbtLdifUnifiedService,
    )
    from tests.unit.test_services import (
        svc,
        test_parse_and_validate_ldif_parse_fails,
        test_run_complete_workflow_all,
        test_run_data_quality_assessment,
    )
    from tests.unit.test_services_and_api import (
        FlextDbtLdifService,
        service,
        test_api_generate_ldif_models,
        test_api_process_ldif_file,
        test_api_validate_ldif_quality,
        test_generate_and_write_models_ok,
        test_parse_and_validate_ldif_ok,
    )
    from tests.unit.test_version import test_dunder_alignment, test_version_is_string

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtLdifCliService": ["tests.unit.test_cli", "FlextDbtLdifCliService"],
    "FlextDbtLdifClient": ["tests.unit.test_dbt_client", "FlextDbtLdifClient"],
    "FlextDbtLdifCore": ["tests.unit.test_core", "FlextDbtLdifCore"],
    "FlextDbtLdifService": ["tests.unit.test_services_and_api", "FlextDbtLdifService"],
    "FlextDbtLdifUnifiedService": [
        "tests.unit.test_dbt_models",
        "FlextDbtLdifUnifiedService",
    ],
    "TestAnalytics": ["tests.unit.test_core", "TestAnalytics"],
    "TestDbtModel": ["tests.unit.test_dbt_models", "TestDbtModel"],
    "TestFlextDbtLdifCliService": ["tests.unit.test_cli", "TestFlextDbtLdifCliService"],
    "TestFlextDbtLdifClient": ["tests.unit.test_dbt_client", "TestFlextDbtLdifClient"],
    "TestFlextDbtLdifUnifiedService": [
        "tests.unit.test_dbt_models",
        "TestFlextDbtLdifUnifiedService",
    ],
    "TestMainEntryPoint": ["tests.unit.test_cli", "TestMainEntryPoint"],
    "TestModelGenerator": ["tests.unit.test_core", "TestModelGenerator"],
    "service": ["tests.unit.test_services_and_api", "service"],
    "svc": ["tests.unit.test_services", "svc"],
    "test_api_generate_ldif_models": [
        "tests.unit.test_services_and_api",
        "test_api_generate_ldif_models",
    ],
    "test_api_imports": ["tests.unit.test_api_surface", "test_api_imports"],
    "test_api_process_ldif_file": [
        "tests.unit.test_services_and_api",
        "test_api_process_ldif_file",
    ],
    "test_api_surface": ["tests.unit.test_api_surface", ""],
    "test_api_validate_ldif_quality": [
        "tests.unit.test_services_and_api",
        "test_api_validate_ldif_quality",
    ],
    "test_cli": ["tests.unit.test_cli", ""],
    "test_core": ["tests.unit.test_core", ""],
    "test_dbt_client": ["tests.unit.test_dbt_client", ""],
    "test_dbt_models": ["tests.unit.test_dbt_models", ""],
    "test_dunder_alignment": ["tests.unit.test_version", "test_dunder_alignment"],
    "test_generate_and_write_models_ok": [
        "tests.unit.test_services_and_api",
        "test_generate_and_write_models_ok",
    ],
    "test_parse_and_validate_ldif_ok": [
        "tests.unit.test_services_and_api",
        "test_parse_and_validate_ldif_ok",
    ],
    "test_parse_and_validate_ldif_parse_fails": [
        "tests.unit.test_services",
        "test_parse_and_validate_ldif_parse_fails",
    ],
    "test_run_complete_workflow_all": [
        "tests.unit.test_services",
        "test_run_complete_workflow_all",
    ],
    "test_run_data_quality_assessment": [
        "tests.unit.test_services",
        "test_run_data_quality_assessment",
    ],
    "test_services": ["tests.unit.test_services", ""],
    "test_services_and_api": ["tests.unit.test_services_and_api", ""],
    "test_version": ["tests.unit.test_version", ""],
    "test_version_is_string": ["tests.unit.test_version", "test_version_is_string"],
}

__all__ = [
    "FlextDbtLdifCliService",
    "FlextDbtLdifClient",
    "FlextDbtLdifCore",
    "FlextDbtLdifService",
    "FlextDbtLdifUnifiedService",
    "TestAnalytics",
    "TestDbtModel",
    "TestFlextDbtLdifCliService",
    "TestFlextDbtLdifClient",
    "TestFlextDbtLdifUnifiedService",
    "TestMainEntryPoint",
    "TestModelGenerator",
    "service",
    "svc",
    "test_api_generate_ldif_models",
    "test_api_imports",
    "test_api_process_ldif_file",
    "test_api_surface",
    "test_api_validate_ldif_quality",
    "test_cli",
    "test_core",
    "test_dbt_client",
    "test_dbt_models",
    "test_dunder_alignment",
    "test_generate_and_write_models_ok",
    "test_parse_and_validate_ldif_ok",
    "test_parse_and_validate_ldif_parse_fails",
    "test_run_complete_workflow_all",
    "test_run_data_quality_assessment",
    "test_services",
    "test_services_and_api",
    "test_version",
    "test_version_is_string",
]


_LAZY_CACHE: MutableMapping[str, FlextTypes.ModuleExport] = {}


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


def __dir__() -> Sequence[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
