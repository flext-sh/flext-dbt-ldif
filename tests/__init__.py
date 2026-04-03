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
    from flext_dbt_ldif import (
        conftest,
        constants,
        models,
        protocols,
        test_api_surface,
        test_cli,
        test_core,
        test_dbt_client,
        test_dbt_models,
        test_services,
        test_services_and_api,
        test_version,
        typings,
        unit,
        utilities,
    )
    from flext_dbt_ldif.conftest import (
        dbt_ldif_profile,
        dbt_ldif_project_config,
        docker_control,
        ensure_shared_docker_container,
        ldif_source_config,
        result,
        sample_ldif_entries,
        set_test_environment,
        shared_ldap_container,
    )
    from flext_dbt_ldif.constants import (
        FlextDbtLdifTestConstants,
        FlextDbtLdifTestConstants as c,
    )
    from flext_dbt_ldif.models import (
        FlextDbtLdifTestModels,
        FlextDbtLdifTestModels as m,
    )
    from flext_dbt_ldif.protocols import (
        FlextDbtLdifTestProtocols,
        FlextDbtLdifTestProtocols as p,
    )
    from flext_dbt_ldif.typings import FlextDbtLdifTestTypes, FlextDbtLdifTestTypes as t
    from flext_dbt_ldif.unit import (
        FlextDbtLdifService,
        TestFlextDbtLdifClient,
        TestFlextDbtLdifCliService,
        TestFlextDbtLdifUnifiedService,
        TestModelGenerator,
        analytics_model,
        columns,
        dbt_model_type,
        dependencies,
        entries,
        ldif_source,
        name,
        service,
        sql_content,
        staging_model,
        svc,
        test_api_imports,
        test_dunder_alignment,
    )
    from flext_dbt_ldif.utilities import (
        FlextDbtLdifTestUtilities,
        FlextDbtLdifTestUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_dbt_ldif.unit",),
    {
        "FlextDbtLdifTestConstants": "flext_dbt_ldif.constants",
        "FlextDbtLdifTestModels": "flext_dbt_ldif.models",
        "FlextDbtLdifTestProtocols": "flext_dbt_ldif.protocols",
        "FlextDbtLdifTestTypes": "flext_dbt_ldif.typings",
        "FlextDbtLdifTestUtilities": "flext_dbt_ldif.utilities",
        "c": ("flext_dbt_ldif.constants", "FlextDbtLdifTestConstants"),
        "conftest": "flext_dbt_ldif.conftest",
        "constants": "flext_dbt_ldif.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "dbt_ldif_profile": "flext_dbt_ldif.conftest",
        "dbt_ldif_project_config": "flext_dbt_ldif.conftest",
        "docker_control": "flext_dbt_ldif.conftest",
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "ensure_shared_docker_container": "flext_dbt_ldif.conftest",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "ldif_source_config": "flext_dbt_ldif.conftest",
        "m": ("flext_dbt_ldif.models", "FlextDbtLdifTestModels"),
        "models": "flext_dbt_ldif.models",
        "p": ("flext_dbt_ldif.protocols", "FlextDbtLdifTestProtocols"),
        "protocols": "flext_dbt_ldif.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "result": "flext_dbt_ldif.conftest",
        "s": ("flext_core.service", "FlextService"),
        "sample_ldif_entries": "flext_dbt_ldif.conftest",
        "set_test_environment": "flext_dbt_ldif.conftest",
        "shared_ldap_container": "flext_dbt_ldif.conftest",
        "t": ("flext_dbt_ldif.typings", "FlextDbtLdifTestTypes"),
        "test_api_surface": "flext_dbt_ldif.test_api_surface",
        "test_cli": "flext_dbt_ldif.test_cli",
        "test_core": "flext_dbt_ldif.test_core",
        "test_dbt_client": "flext_dbt_ldif.test_dbt_client",
        "test_dbt_models": "flext_dbt_ldif.test_dbt_models",
        "test_services": "flext_dbt_ldif.test_services",
        "test_services_and_api": "flext_dbt_ldif.test_services_and_api",
        "test_version": "flext_dbt_ldif.test_version",
        "typings": "flext_dbt_ldif.typings",
        "u": ("flext_dbt_ldif.utilities", "FlextDbtLdifTestUtilities"),
        "unit": "flext_dbt_ldif.unit",
        "utilities": "flext_dbt_ldif.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
