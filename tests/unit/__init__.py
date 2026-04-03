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
    from flext_dbt_ldif import (
        test_api_surface,
        test_cli,
        test_core,
        test_dbt_client,
        test_dbt_models,
        test_services,
        test_services_and_api,
        test_version,
    )
    from flext_dbt_ldif.test_api_surface import test_api_imports
    from flext_dbt_ldif.test_cli import TestFlextDbtLdifCliService
    from flext_dbt_ldif.test_core import TestModelGenerator
    from flext_dbt_ldif.test_dbt_client import TestFlextDbtLdifClient
    from flext_dbt_ldif.test_dbt_models import TestFlextDbtLdifUnifiedService
    from flext_dbt_ldif.test_services import svc
    from flext_dbt_ldif.test_services_and_api import (
        FlextDbtLdifService,
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
    )
    from flext_dbt_ldif.test_version import test_dunder_alignment

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextDbtLdifService": "flext_dbt_ldif.test_services_and_api",
    "TestFlextDbtLdifCliService": "flext_dbt_ldif.test_cli",
    "TestFlextDbtLdifClient": "flext_dbt_ldif.test_dbt_client",
    "TestFlextDbtLdifUnifiedService": "flext_dbt_ldif.test_dbt_models",
    "TestModelGenerator": "flext_dbt_ldif.test_core",
    "analytics_model": "flext_dbt_ldif.test_services_and_api",
    "c": ("flext_core.constants", "FlextConstants"),
    "columns": "flext_dbt_ldif.test_services_and_api",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "dbt_model_type": "flext_dbt_ldif.test_services_and_api",
    "dependencies": "flext_dbt_ldif.test_services_and_api",
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "entries": "flext_dbt_ldif.test_services_and_api",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "ldif_source": "flext_dbt_ldif.test_services_and_api",
    "m": ("flext_core.models", "FlextModels"),
    "name": "flext_dbt_ldif.test_services_and_api",
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "service": "flext_dbt_ldif.test_services_and_api",
    "sql_content": "flext_dbt_ldif.test_services_and_api",
    "staging_model": "flext_dbt_ldif.test_services_and_api",
    "svc": "flext_dbt_ldif.test_services",
    "t": ("flext_core.typings", "FlextTypes"),
    "test_api_imports": "flext_dbt_ldif.test_api_surface",
    "test_api_surface": "flext_dbt_ldif.test_api_surface",
    "test_cli": "flext_dbt_ldif.test_cli",
    "test_core": "flext_dbt_ldif.test_core",
    "test_dbt_client": "flext_dbt_ldif.test_dbt_client",
    "test_dbt_models": "flext_dbt_ldif.test_dbt_models",
    "test_dunder_alignment": "flext_dbt_ldif.test_version",
    "test_services": "flext_dbt_ldif.test_services",
    "test_services_and_api": "flext_dbt_ldif.test_services_and_api",
    "test_version": "flext_dbt_ldif.test_version",
    "u": ("flext_core.utilities", "FlextUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
