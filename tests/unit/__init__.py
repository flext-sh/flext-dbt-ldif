# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import tests.unit.test_api_surface as _tests_unit_test_api_surface

    test_api_surface = _tests_unit_test_api_surface
    import tests.unit.test_cli as _tests_unit_test_cli
    from tests.unit.test_api_surface import test_api_imports

    test_cli = _tests_unit_test_cli
    import tests.unit.test_core as _tests_unit_test_core
    from tests.unit.test_cli import TestFlextDbtLdifCliService, TestMainEntryPoint

    test_core = _tests_unit_test_core
    import tests.unit.test_dbt_client as _tests_unit_test_dbt_client
    from tests.unit.test_core import TestAnalytics, TestModelGenerator

    test_dbt_client = _tests_unit_test_dbt_client
    import tests.unit.test_dbt_models as _tests_unit_test_dbt_models
    from tests.unit.test_dbt_client import TestFlextDbtLdifClient

    test_dbt_models = _tests_unit_test_dbt_models
    import tests.unit.test_services as _tests_unit_test_services
    from tests.unit.test_dbt_models import TestDbtModel, TestFlextDbtLdifUnifiedService

    test_services = _tests_unit_test_services
    import tests.unit.test_services_and_api as _tests_unit_test_services_and_api
    from tests.unit.test_services import (
        svc,
        test_parse_and_validate_ldif_parse_fails,
        test_run_complete_workflow_all,
        test_run_data_quality_assessment,
    )

    test_services_and_api = _tests_unit_test_services_and_api
    import tests.unit.test_version as _tests_unit_test_version
    from tests.unit.test_services_and_api import (
        service,
        test_api_generate_ldif_models,
        test_api_process_ldif_file,
        test_api_validate_ldif_quality,
        test_generate_and_write_models_ok,
        test_parse_and_validate_ldif_ok,
    )

    test_version = _tests_unit_test_version
    from flext_core.constants import FlextConstants as c
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.models import FlextModels as m
    from flext_core.protocols import FlextProtocols as p
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_core.typings import FlextTypes as t
    from flext_core.utilities import FlextUtilities as u
    from tests.unit.test_version import test_dunder_alignment, test_version_is_string
_LAZY_IMPORTS = {
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
    "c": ("flext_core.constants", "FlextConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "service": ("tests.unit.test_services_and_api", "service"),
    "svc": ("tests.unit.test_services", "svc"),
    "t": ("flext_core.typings", "FlextTypes"),
    "test_api_generate_ldif_models": (
        "tests.unit.test_services_and_api",
        "test_api_generate_ldif_models",
    ),
    "test_api_imports": ("tests.unit.test_api_surface", "test_api_imports"),
    "test_api_process_ldif_file": (
        "tests.unit.test_services_and_api",
        "test_api_process_ldif_file",
    ),
    "test_api_surface": "tests.unit.test_api_surface",
    "test_api_validate_ldif_quality": (
        "tests.unit.test_services_and_api",
        "test_api_validate_ldif_quality",
    ),
    "test_cli": "tests.unit.test_cli",
    "test_core": "tests.unit.test_core",
    "test_dbt_client": "tests.unit.test_dbt_client",
    "test_dbt_models": "tests.unit.test_dbt_models",
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
    "test_services": "tests.unit.test_services",
    "test_services_and_api": "tests.unit.test_services_and_api",
    "test_version": "tests.unit.test_version",
    "test_version_is_string": ("tests.unit.test_version", "test_version_is_string"),
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

__all__ = [
    "TestAnalytics",
    "TestDbtModel",
    "TestFlextDbtLdifCliService",
    "TestFlextDbtLdifClient",
    "TestFlextDbtLdifUnifiedService",
    "TestMainEntryPoint",
    "TestModelGenerator",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "service",
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
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
