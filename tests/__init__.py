# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from tests import (
        conftest as conftest,
        constants as constants,
        models as models,
        protocols as protocols,
        typings as typings,
        unit as unit,
        utilities as utilities,
    )
    from tests.conftest import (
        dbt_ldif_profile as dbt_ldif_profile,
        dbt_ldif_project_config as dbt_ldif_project_config,
        docker_control as docker_control,
        ensure_shared_docker_container as ensure_shared_docker_container,
        ldif_source_config as ldif_source_config,
        pytest_configure as pytest_configure,
        sample_ldif_entries as sample_ldif_entries,
        set_test_environment as set_test_environment,
        shared_ldap_container as shared_ldap_container,
    )
    from tests.constants import (
        FlextDbtLdifTestConstants as FlextDbtLdifTestConstants,
        FlextDbtLdifTestConstants as c,
    )
    from tests.models import (
        FlextDbtLdifTestModels as FlextDbtLdifTestModels,
        FlextDbtLdifTestModels as m,
    )
    from tests.protocols import (
        FlextDbtLdifTestProtocols as FlextDbtLdifTestProtocols,
        FlextDbtLdifTestProtocols as p,
    )
    from tests.typings import (
        FlextDbtLdifTestTypes as FlextDbtLdifTestTypes,
        FlextDbtLdifTestTypes as t,
    )
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
    from tests.utilities import (
        FlextDbtLdifTestUtilities as FlextDbtLdifTestUtilities,
        FlextDbtLdifTestUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtLdifCliService": ["tests.unit.test_cli", "FlextDbtLdifCliService"],
    "FlextDbtLdifClient": ["tests.unit.test_dbt_client", "FlextDbtLdifClient"],
    "FlextDbtLdifCore": ["tests.unit.test_core", "FlextDbtLdifCore"],
    "FlextDbtLdifService": ["tests.unit.test_services_and_api", "FlextDbtLdifService"],
    "FlextDbtLdifTestConstants": ["tests.constants", "FlextDbtLdifTestConstants"],
    "FlextDbtLdifTestModels": ["tests.models", "FlextDbtLdifTestModels"],
    "FlextDbtLdifTestProtocols": ["tests.protocols", "FlextDbtLdifTestProtocols"],
    "FlextDbtLdifTestTypes": ["tests.typings", "FlextDbtLdifTestTypes"],
    "FlextDbtLdifTestUtilities": ["tests.utilities", "FlextDbtLdifTestUtilities"],
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
    "c": ["tests.constants", "FlextDbtLdifTestConstants"],
    "conftest": ["tests.conftest", ""],
    "constants": ["tests.constants", ""],
    "d": ["flext_tests", "d"],
    "dbt_ldif_profile": ["tests.conftest", "dbt_ldif_profile"],
    "dbt_ldif_project_config": ["tests.conftest", "dbt_ldif_project_config"],
    "docker_control": ["tests.conftest", "docker_control"],
    "e": ["flext_tests", "e"],
    "ensure_shared_docker_container": [
        "tests.conftest",
        "ensure_shared_docker_container",
    ],
    "h": ["flext_tests", "h"],
    "ldif_source_config": ["tests.conftest", "ldif_source_config"],
    "m": ["tests.models", "FlextDbtLdifTestModels"],
    "models": ["tests.models", ""],
    "p": ["tests.protocols", "FlextDbtLdifTestProtocols"],
    "protocols": ["tests.protocols", ""],
    "pytest_configure": ["tests.conftest", "pytest_configure"],
    "r": ["flext_tests", "r"],
    "s": ["flext_tests", "s"],
    "sample_ldif_entries": ["tests.conftest", "sample_ldif_entries"],
    "service": ["tests.unit.test_services_and_api", "service"],
    "set_test_environment": ["tests.conftest", "set_test_environment"],
    "shared_ldap_container": ["tests.conftest", "shared_ldap_container"],
    "svc": ["tests.unit.test_services", "svc"],
    "t": ["tests.typings", "FlextDbtLdifTestTypes"],
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
    "typings": ["tests.typings", ""],
    "u": ["tests.utilities", "FlextDbtLdifTestUtilities"],
    "unit": ["tests.unit", ""],
    "utilities": ["tests.utilities", ""],
    "x": ["flext_tests", "x"],
}

_EXPORTS: Sequence[str] = [
    "FlextDbtLdifCliService",
    "FlextDbtLdifClient",
    "FlextDbtLdifCore",
    "FlextDbtLdifService",
    "FlextDbtLdifTestConstants",
    "FlextDbtLdifTestModels",
    "FlextDbtLdifTestProtocols",
    "FlextDbtLdifTestTypes",
    "FlextDbtLdifTestUtilities",
    "FlextDbtLdifUnifiedService",
    "TestAnalytics",
    "TestDbtModel",
    "TestFlextDbtLdifCliService",
    "TestFlextDbtLdifClient",
    "TestFlextDbtLdifUnifiedService",
    "TestMainEntryPoint",
    "TestModelGenerator",
    "c",
    "conftest",
    "constants",
    "d",
    "dbt_ldif_profile",
    "dbt_ldif_project_config",
    "docker_control",
    "e",
    "ensure_shared_docker_container",
    "h",
    "ldif_source_config",
    "m",
    "models",
    "p",
    "protocols",
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
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
