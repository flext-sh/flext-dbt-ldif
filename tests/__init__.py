# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests import conftest, constants, models, protocols, typings, unit, utilities
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
    from tests.unit import (
        FlextDbtLdifService,
        TestAnalytics,
        TestDbtModel,
        TestFlextDbtLdifClient,
        TestFlextDbtLdifCliService,
        TestFlextDbtLdifUnifiedService,
        TestMainEntryPoint,
        TestModelGenerator,
        service,
        svc,
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
    )
    from tests.utilities import (
        FlextDbtLdifTestUtilities,
        FlextDbtLdifTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
