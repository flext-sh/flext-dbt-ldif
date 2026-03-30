# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests.unit import (
        test_api_surface as test_api_surface,
        test_cli as test_cli,
        test_core as test_core,
        test_dbt_client as test_dbt_client,
        test_dbt_models as test_dbt_models,
        test_services as test_services,
        test_services_and_api as test_services_and_api,
        test_version as test_version,
    )
    from tests.unit.test_api_surface import test_api_imports as test_api_imports
    from tests.unit.test_cli import (
        FlextDbtLdifCliService as FlextDbtLdifCliService,
        TestFlextDbtLdifCliService as TestFlextDbtLdifCliService,
        TestMainEntryPoint as TestMainEntryPoint,
    )
    from tests.unit.test_core import (
        FlextDbtLdifCore as FlextDbtLdifCore,
        TestAnalytics as TestAnalytics,
        TestModelGenerator as TestModelGenerator,
    )
    from tests.unit.test_dbt_client import (
        FlextDbtLdifClient as FlextDbtLdifClient,
        TestFlextDbtLdifClient as TestFlextDbtLdifClient,
    )
    from tests.unit.test_dbt_models import (
        FlextDbtLdifUnifiedService as FlextDbtLdifUnifiedService,
        TestDbtModel as TestDbtModel,
        TestFlextDbtLdifUnifiedService as TestFlextDbtLdifUnifiedService,
    )
    from tests.unit.test_services import (
        svc as svc,
        test_parse_and_validate_ldif_parse_fails as test_parse_and_validate_ldif_parse_fails,
        test_run_complete_workflow_all as test_run_complete_workflow_all,
        test_run_data_quality_assessment as test_run_data_quality_assessment,
    )
    from tests.unit.test_services_and_api import (
        FlextDbtLdifService as FlextDbtLdifService,
        service as service,
        test_api_generate_ldif_models as test_api_generate_ldif_models,
        test_api_process_ldif_file as test_api_process_ldif_file,
        test_api_validate_ldif_quality as test_api_validate_ldif_quality,
        test_generate_and_write_models_ok as test_generate_and_write_models_ok,
        test_parse_and_validate_ldif_ok as test_parse_and_validate_ldif_ok,
    )
    from tests.unit.test_version import (
        test_dunder_alignment as test_dunder_alignment,
        test_version_is_string as test_version_is_string,
    )

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

_EXPORTS: Sequence[str] = [
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
