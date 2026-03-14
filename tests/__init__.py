# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""FLEXT DBT LDIF Tests - Test infrastructure and utilities.

Provides TestsFlextDbtLdif classes extending FlextTests and FlextDbtLdif for comprehensive testing.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes
    from tests.conftest import (
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
    from tests.constants import TestsFlextDbtLdifConstants, c
    from tests.models import TestsFlextDbtLdifModels, m, tm
    from tests.protocols import TestsFlextDbtLdifProtocols, p
    from tests.typings import TestsFlextDbtLdifTypes, TestsFlextDbtLdifTypes as t
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
    from tests.utilities import (
        TestsFlextDbtLdifUtilities,
        TestsFlextDbtLdifUtilities as u,
    )

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
    "TestsFlextDbtLdifConstants": ("tests.constants", "TestsFlextDbtLdifConstants"),
    "TestsFlextDbtLdifModels": ("tests.models", "TestsFlextDbtLdifModels"),
    "TestsFlextDbtLdifProtocols": ("tests.protocols", "TestsFlextDbtLdifProtocols"),
    "TestsFlextDbtLdifTypes": ("tests.typings", "TestsFlextDbtLdifTypes"),
    "TestsFlextDbtLdifUtilities": ("tests.utilities", "TestsFlextDbtLdifUtilities"),
    "c": ("tests.constants", "c"),
    "dbt_ldif_profile": ("tests.conftest", "dbt_ldif_profile"),
    "dbt_ldif_project_config": ("tests.conftest", "dbt_ldif_project_config"),
    "docker_control": ("tests.conftest", "docker_control"),
    "ensure_shared_docker_container": (
        "tests.conftest",
        "ensure_shared_docker_container",
    ),
    "ldif_source_config": ("tests.conftest", "ldif_source_config"),
    "m": ("tests.models", "m"),
    "p": ("tests.protocols", "p"),
    "pytest_configure": ("tests.conftest", "pytest_configure"),
    "s": ("tests.unit.test_cli", "TestFlextDbtLdifCliService"),
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
    "tm": ("tests.models", "tm"),
    "u": ("tests.utilities", "TestsFlextDbtLdifUtilities"),
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
    "dbt_ldif_profile",
    "dbt_ldif_project_config",
    "docker_control",
    "ensure_shared_docker_container",
    "ldif_source_config",
    "m",
    "p",
    "pytest_configure",
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
    "tm",
    "u",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
