# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Services package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    import flext_dbt_ldif.services.cli_service as _flext_dbt_ldif_services_cli_service

    cli_service = _flext_dbt_ldif_services_cli_service
    import flext_dbt_ldif.services.client as _flext_dbt_ldif_services_client
    from flext_dbt_ldif.services.cli_service import FlextDbtLdifCliService

    client = _flext_dbt_ldif_services_client
    import flext_dbt_ldif.services.core as _flext_dbt_ldif_services_core
    from flext_dbt_ldif.services.client import FlextDbtLdifClient

    core = _flext_dbt_ldif_services_core
    import flext_dbt_ldif.services.error as _flext_dbt_ldif_services_error
    from flext_dbt_ldif.services.core import FlextDbtLdifCore

    error = _flext_dbt_ldif_services_error
    import flext_dbt_ldif.services.service as _flext_dbt_ldif_services_service
    from flext_dbt_ldif.services.error import FlextDbtLdifError

    service = _flext_dbt_ldif_services_service
    import flext_dbt_ldif.services.unified_service as _flext_dbt_ldif_services_unified_service
    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin, logger

    unified_service = _flext_dbt_ldif_services_unified_service
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
    from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService
_LAZY_IMPORTS = {
    "FlextDbtLdifCliService": (
        "flext_dbt_ldif.services.cli_service",
        "FlextDbtLdifCliService",
    ),
    "FlextDbtLdifClient": ("flext_dbt_ldif.services.client", "FlextDbtLdifClient"),
    "FlextDbtLdifCore": ("flext_dbt_ldif.services.core", "FlextDbtLdifCore"),
    "FlextDbtLdifError": ("flext_dbt_ldif.services.error", "FlextDbtLdifError"),
    "FlextDbtLdifServiceMixin": (
        "flext_dbt_ldif.services.service",
        "FlextDbtLdifServiceMixin",
    ),
    "FlextDbtLdifUnifiedService": (
        "flext_dbt_ldif.services.unified_service",
        "FlextDbtLdifUnifiedService",
    ),
    "c": ("flext_core.constants", "FlextConstants"),
    "cli_service": "flext_dbt_ldif.services.cli_service",
    "client": "flext_dbt_ldif.services.client",
    "core": "flext_dbt_ldif.services.core",
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "error": "flext_dbt_ldif.services.error",
    "h": ("flext_core.handlers", "FlextHandlers"),
    "logger": ("flext_dbt_ldif.services.service", "logger"),
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

__all__ = [
    "FlextDbtLdifCliService",
    "FlextDbtLdifClient",
    "FlextDbtLdifCore",
    "FlextDbtLdifError",
    "FlextDbtLdifServiceMixin",
    "FlextDbtLdifUnifiedService",
    "c",
    "cli_service",
    "client",
    "core",
    "d",
    "e",
    "error",
    "h",
    "logger",
    "m",
    "p",
    "r",
    "s",
    "service",
    "t",
    "u",
    "unified_service",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
