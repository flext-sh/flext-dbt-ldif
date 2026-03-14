# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""Unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes
    from tests.unit.test_api_surface import test_api_imports
    from tests.unit.test_cli import (
        TestFlextDbtLdifCliService,
        TestFlextDbtLdifCliService as s,
        TestMainEntryPoint,
    )
    from tests.unit.test_core import TestAnalytics, TestModelGenerator
    from tests.unit.test_dbt_client import TestFlextDbtLdifClient
    from tests.unit.test_dbt_models import TestDbtModel, TestFlextDbtLdifUnifiedService
    from tests.unit.test_services import (
        svc,
        test_parse_and_validate_ldif_parse_fails,
        test_run_complete_workflow_all,
        test_run_data_quality_assessment,
    )
    from tests.unit.test_services_and_api import (
        service,
        test_api_generate_ldif_models,
        test_api_process_ldif_file,
        test_api_validate_ldif_quality,
        test_generate_and_write_models_ok,
        test_parse_and_validate_ldif_ok,
    )
    from tests.unit.test_version import test_dunder_alignment, test_version_is_string

# Lazy import mapping: export_name -> (module_path, attr_name)
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
    "s": ("tests.unit.test_cli", "TestFlextDbtLdifCliService"),
    "service": ("tests.unit.test_services_and_api", "service"),
    "svc": ("tests.unit.test_services", "svc"),
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
}

__all__ = [
    "TestAnalytics",
    "TestDbtModel",
    "TestFlextDbtLdifCliService",
    "TestFlextDbtLdifClient",
    "TestFlextDbtLdifUnifiedService",
    "TestMainEntryPoint",
    "TestModelGenerator",
    "s",
    "service",
    "svc",
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
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
