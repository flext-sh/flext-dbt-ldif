# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.decorators import FlextDecorators as d
from flext_core.exceptions import FlextExceptions as e
from flext_core.handlers import FlextHandlers as h
from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_core.mixins import FlextMixins as x
from flext_core.result import FlextResult as r
from flext_core.service import FlextService as s
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
from tests.constants import (
    FlextDbtLdifTestConstants,
    FlextDbtLdifTestConstants as c,
)
from tests.models import FlextDbtLdifTestModels, FlextDbtLdifTestModels as m
from tests.protocols import (
    FlextDbtLdifTestProtocols,
    FlextDbtLdifTestProtocols as p,
)
from tests.typings import FlextDbtLdifTestTypes, FlextDbtLdifTestTypes as t
from tests.unit.test_api_surface import test_api_imports
from tests.unit.test_cli import TestFlextDbtLdifCliService, TestMainEntryPoint
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
    FlextDbtLdifService,
    service,
    test_api_generate_ldif_models,
    test_api_process_ldif_file,
    test_api_validate_ldif_quality,
    test_generate_and_write_models_ok,
    test_parse_and_validate_ldif_ok,
)
from tests.unit.test_version import test_dunder_alignment, test_version_is_string
from tests.utilities import (
    FlextDbtLdifTestUtilities,
    FlextDbtLdifTestUtilities as u,
)

if _t.TYPE_CHECKING:
    import tests.conftest as _tests_conftest

    conftest = _tests_conftest
    import tests.constants as _tests_constants

    constants = _tests_constants
    import tests.models as _tests_models

    models = _tests_models
    import tests.protocols as _tests_protocols

    protocols = _tests_protocols
    import tests.typings as _tests_typings

    typings = _tests_typings
    import tests.unit as _tests_unit

    unit = _tests_unit
    import tests.unit.test_api_surface as _tests_unit_test_api_surface

    test_api_surface = _tests_unit_test_api_surface
    import tests.unit.test_cli as _tests_unit_test_cli

    test_cli = _tests_unit_test_cli
    import tests.unit.test_core as _tests_unit_test_core

    test_core = _tests_unit_test_core
    import tests.unit.test_dbt_client as _tests_unit_test_dbt_client

    test_dbt_client = _tests_unit_test_dbt_client
    import tests.unit.test_dbt_models as _tests_unit_test_dbt_models

    test_dbt_models = _tests_unit_test_dbt_models
    import tests.unit.test_services as _tests_unit_test_services

    test_services = _tests_unit_test_services
    import tests.unit.test_services_and_api as _tests_unit_test_services_and_api

    test_services_and_api = _tests_unit_test_services_and_api
    import tests.unit.test_version as _tests_unit_test_version

    test_version = _tests_unit_test_version
    import tests.utilities as _tests_utilities

    utilities = _tests_utilities

    _ = (
        FlextDbtLdifService,
        FlextDbtLdifTestConstants,
        FlextDbtLdifTestModels,
        FlextDbtLdifTestProtocols,
        FlextDbtLdifTestTypes,
        FlextDbtLdifTestUtilities,
        TestAnalytics,
        TestDbtModel,
        TestFlextDbtLdifCliService,
        TestFlextDbtLdifClient,
        TestFlextDbtLdifUnifiedService,
        TestMainEntryPoint,
        TestModelGenerator,
        c,
        conftest,
        constants,
        d,
        dbt_ldif_profile,
        dbt_ldif_project_config,
        docker_control,
        e,
        ensure_shared_docker_container,
        h,
        ldif_source_config,
        m,
        models,
        p,
        protocols,
        pytest_configure,
        r,
        s,
        sample_ldif_entries,
        service,
        set_test_environment,
        shared_ldap_container,
        svc,
        t,
        test_api_generate_ldif_models,
        test_api_imports,
        test_api_process_ldif_file,
        test_api_surface,
        test_api_validate_ldif_quality,
        test_cli,
        test_core,
        test_dbt_client,
        test_dbt_models,
        test_dunder_alignment,
        test_generate_and_write_models_ok,
        test_parse_and_validate_ldif_ok,
        test_parse_and_validate_ldif_parse_fails,
        test_run_complete_workflow_all,
        test_run_data_quality_assessment,
        test_services,
        test_services_and_api,
        test_version,
        test_version_is_string,
        typings,
        u,
        unit,
        utilities,
        x,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "FlextDbtLdifTestConstants": "tests.constants",
        "FlextDbtLdifTestModels": "tests.models",
        "FlextDbtLdifTestProtocols": "tests.protocols",
        "FlextDbtLdifTestTypes": "tests.typings",
        "FlextDbtLdifTestUtilities": "tests.utilities",
        "c": ("tests.constants", "FlextDbtLdifTestConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "dbt_ldif_profile": "tests.conftest",
        "dbt_ldif_project_config": "tests.conftest",
        "docker_control": "tests.conftest",
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "ensure_shared_docker_container": "tests.conftest",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "ldif_source_config": "tests.conftest",
        "m": ("tests.models", "FlextDbtLdifTestModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "FlextDbtLdifTestProtocols"),
        "protocols": "tests.protocols",
        "pytest_configure": "tests.conftest",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "sample_ldif_entries": "tests.conftest",
        "set_test_environment": "tests.conftest",
        "shared_ldap_container": "tests.conftest",
        "t": ("tests.typings", "FlextDbtLdifTestTypes"),
        "typings": "tests.typings",
        "u": ("tests.utilities", "FlextDbtLdifTestUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)

__all__ = [
    "FlextDbtLdifService",
    "FlextDbtLdifTestConstants",
    "FlextDbtLdifTestModels",
    "FlextDbtLdifTestProtocols",
    "FlextDbtLdifTestTypes",
    "FlextDbtLdifTestUtilities",
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
