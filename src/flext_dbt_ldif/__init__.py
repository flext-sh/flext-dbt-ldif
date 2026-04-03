# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Flext dbt ldif package."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING as _TYPE_CHECKING

from flext_core.lazy import install_lazy_exports, merge_lazy_imports
from flext_dbt_ldif.__version__ import (
    __all__,
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if _TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from flext_dbt_ldif import (
        api,
        base,
        cli_service,
        client,
        constants,
        core,
        error,
        models,
        protocols,
        service,
        services,
        settings,
        typings,
        unified_service,
        utilities,
    )
    from flext_dbt_ldif.api import FlextDbtLdif, FlextDbtLdifEntryListAdapter
    from flext_dbt_ldif.base import FlextDbtLdifServiceBase
    from flext_dbt_ldif.constants import (
        FlextDbtLdifConstants,
        FlextDbtLdifConstants as c,
    )
    from flext_dbt_ldif.models import FlextDbtLdifModels, FlextDbtLdifModels as m
    from flext_dbt_ldif.protocols import (
        FlextDbtLdifProtocols,
        FlextDbtLdifProtocols as p,
    )
    from flext_dbt_ldif.services import (
        FlextDbtLdifClient,
        FlextDbtLdifCliService,
        FlextDbtLdifCore,
        FlextDbtLdifError,
        FlextDbtLdifServiceMixin,
        FlextDbtLdifUnifiedService,
        logger,
    )
    from flext_dbt_ldif.settings import FlextDbtLdifSettings
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, FlextDbtLdifTypes as t
    from flext_dbt_ldif.utilities import (
        FlextDbtLdifUtilities,
        FlextDbtLdifUtilities as u,
    )

_LAZY_IMPORTS: FlextTypes.LazyImportIndex = merge_lazy_imports(
    ("flext_dbt_ldif.services",),
    {
        "FlextDbtLdif": "flext_dbt_ldif.api",
        "FlextDbtLdifConstants": "flext_dbt_ldif.constants",
        "FlextDbtLdifEntryListAdapter": "flext_dbt_ldif.api",
        "FlextDbtLdifModels": "flext_dbt_ldif.models",
        "FlextDbtLdifProtocols": "flext_dbt_ldif.protocols",
        "FlextDbtLdifServiceBase": "flext_dbt_ldif.base",
        "FlextDbtLdifSettings": "flext_dbt_ldif.settings",
        "FlextDbtLdifTypes": "flext_dbt_ldif.typings",
        "FlextDbtLdifUtilities": "flext_dbt_ldif.utilities",
        "api": "flext_dbt_ldif.api",
        "base": "flext_dbt_ldif.base",
        "c": ("flext_dbt_ldif.constants", "FlextDbtLdifConstants"),
        "cli_service": "flext_dbt_ldif.cli_service",
        "client": "flext_dbt_ldif.client",
        "constants": "flext_dbt_ldif.constants",
        "core": "flext_dbt_ldif.core",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "error": "flext_dbt_ldif.error",
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("flext_dbt_ldif.models", "FlextDbtLdifModels"),
        "models": "flext_dbt_ldif.models",
        "p": ("flext_dbt_ldif.protocols", "FlextDbtLdifProtocols"),
        "protocols": "flext_dbt_ldif.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "service": "flext_dbt_ldif.service",
        "services": "flext_dbt_ldif.services",
        "settings": "flext_dbt_ldif.settings",
        "t": ("flext_dbt_ldif.typings", "FlextDbtLdifTypes"),
        "typings": "flext_dbt_ldif.typings",
        "u": ("flext_dbt_ldif.utilities", "FlextDbtLdifUtilities"),
        "unified_service": "flext_dbt_ldif.unified_service",
        "utilities": "flext_dbt_ldif.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    [
        "__all__",
        "__author__",
        "__author_email__",
        "__description__",
        "__license__",
        "__title__",
        "__url__",
        "__version__",
        "__version_info__",
    ],
)
