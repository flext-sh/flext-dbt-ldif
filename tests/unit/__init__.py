# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Unit package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if _TYPE_CHECKING:
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

_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtLdifCliService": "tests.unit.test_cli",
    "FlextDbtLdifClient": "tests.unit.test_dbt_client",
    "FlextDbtLdifCore": "tests.unit.test_core",
    "FlextDbtLdifService": "tests.unit.test_services_and_api",
    "FlextDbtLdifUnifiedService": "tests.unit.test_dbt_models",
    "TestAnalytics": "tests.unit.test_core",
    "TestDbtModel": "tests.unit.test_dbt_models",
    "TestFlextDbtLdifCliService": "tests.unit.test_cli",
    "TestFlextDbtLdifClient": "tests.unit.test_dbt_client",
    "TestFlextDbtLdifUnifiedService": "tests.unit.test_dbt_models",
    "TestMainEntryPoint": "tests.unit.test_cli",
    "TestModelGenerator": "tests.unit.test_core",
    "service": "tests.unit.test_services_and_api",
    "svc": "tests.unit.test_services",
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
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
