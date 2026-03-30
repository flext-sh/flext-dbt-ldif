# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import *

    from tests import conftest, constants, models, protocols, typings, utilities
    from tests.conftest import *
    from tests.constants import *
    from tests.models import *
    from tests.protocols import *
    from tests.typings import *
    from tests.unit import *
    from tests.utilities import *

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtLdifCliService": "tests.unit.test_cli",
    "FlextDbtLdifClient": "tests.unit.test_dbt_client",
    "FlextDbtLdifCore": "tests.unit.test_core",
    "FlextDbtLdifService": "tests.unit.test_services_and_api",
    "FlextDbtLdifTestConstants": "tests.constants",
    "FlextDbtLdifTestModels": "tests.models",
    "FlextDbtLdifTestProtocols": "tests.protocols",
    "FlextDbtLdifTestTypes": "tests.typings",
    "FlextDbtLdifTestUtilities": "tests.utilities",
    "FlextDbtLdifUnifiedService": "tests.unit.test_dbt_models",
    "TestAnalytics": "tests.unit.test_core",
    "TestDbtModel": "tests.unit.test_dbt_models",
    "TestFlextDbtLdifCliService": "tests.unit.test_cli",
    "TestFlextDbtLdifClient": "tests.unit.test_dbt_client",
    "TestFlextDbtLdifUnifiedService": "tests.unit.test_dbt_models",
    "TestMainEntryPoint": "tests.unit.test_cli",
    "TestModelGenerator": "tests.unit.test_core",
    "c": ["tests.constants", "FlextDbtLdifTestConstants"],
    "conftest": "tests.conftest",
    "constants": "tests.constants",
    "d": "flext_tests",
    "dbt_ldif_profile": "tests.conftest",
    "dbt_ldif_project_config": "tests.conftest",
    "docker_control": "tests.conftest",
    "e": "flext_tests",
    "ensure_shared_docker_container": "tests.conftest",
    "h": "flext_tests",
    "ldif_source_config": "tests.conftest",
    "m": ["tests.models", "FlextDbtLdifTestModels"],
    "models": "tests.models",
    "p": ["tests.protocols", "FlextDbtLdifTestProtocols"],
    "protocols": "tests.protocols",
    "pytest_configure": "tests.conftest",
    "r": "flext_tests",
    "s": "flext_tests",
    "sample_ldif_entries": "tests.conftest",
    "service": "tests.unit.test_services_and_api",
    "set_test_environment": "tests.conftest",
    "shared_ldap_container": "tests.conftest",
    "svc": "tests.unit.test_services",
    "t": ["tests.typings", "FlextDbtLdifTestTypes"],
    "test_api_generate_ldif_models": "tests.unit.test_services_and_api",
    "test_api_imports": "tests.unit.test_api_surface",
    "test_api_process_ldif_file": "tests.unit.test_services_and_api",
    "test_api_surface": "tests.unit.test_api_surface",
    "test_api_validate_ldif_quality": "tests.unit.test_services_and_api",
    "test_cli": "tests.unit.test_cli",
    "test_core": "tests.unit.test_core",
    "test_dbt_client": "tests.unit.test_dbt_client",
    "test_dbt_models": "tests.unit.test_dbt_models",
    "test_dunder_alignment": "tests.unit.test_version",
    "test_generate_and_write_models_ok": "tests.unit.test_services_and_api",
    "test_parse_and_validate_ldif_ok": "tests.unit.test_services_and_api",
    "test_parse_and_validate_ldif_parse_fails": "tests.unit.test_services",
    "test_run_complete_workflow_all": "tests.unit.test_services",
    "test_run_data_quality_assessment": "tests.unit.test_services",
    "test_services": "tests.unit.test_services",
    "test_services_and_api": "tests.unit.test_services_and_api",
    "test_version": "tests.unit.test_version",
    "test_version_is_string": "tests.unit.test_version",
    "typings": "tests.typings",
    "u": ["tests.utilities", "FlextDbtLdifTestUtilities"],
    "unit": "tests.unit",
    "utilities": "tests.utilities",
    "x": "flext_tests",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, sorted(_LAZY_IMPORTS))
