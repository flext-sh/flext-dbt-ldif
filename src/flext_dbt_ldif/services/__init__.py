# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Services package."""

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
    from flext_dbt_ldif.services import (
        cli_service,
        client,
        core,
        error,
        service,
        unified_service,
    )
    from flext_dbt_ldif.services.cli_service import FlextDbtLdifCliService
    from flext_dbt_ldif.services.client import FlextDbtLdifClient
    from flext_dbt_ldif.services.core import FlextDbtLdifCore
    from flext_dbt_ldif.services.error import FlextDbtLdifError
    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin, logger
    from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = {
    "FlextDbtLdifCliService": "flext_dbt_ldif.services.cli_service",
    "FlextDbtLdifClient": "flext_dbt_ldif.services.client",
    "FlextDbtLdifCore": "flext_dbt_ldif.services.core",
    "FlextDbtLdifError": "flext_dbt_ldif.services.error",
    "FlextDbtLdifServiceMixin": "flext_dbt_ldif.services.service",
    "FlextDbtLdifUnifiedService": "flext_dbt_ldif.services.unified_service",
    "c": ("flext_core.constants", "FlextConstants"),
    "cli_service": "flext_dbt_ldif.services.cli_service",
    "client": "flext_dbt_ldif.services.client",
    "core": "flext_dbt_ldif.services.core",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "error": "flext_dbt_ldif.services.error",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "logger": "flext_dbt_ldif.services.service",
    "m": ("flext_core.models", "FlextModels"),
    "p": ("flext_core.protocols", "FlextProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "service": "flext_dbt_ldif.services.service",
    "t": ("flext_core.typings", "FlextTypes"),
    "u": ("flext_core.utilities", "FlextUtilities"),
    "unified_service": "flext_dbt_ldif.services.unified_service",
    "x": ("flext_core.mixins", "FlextMixins"),
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
