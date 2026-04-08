# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)
from flext_dbt_ldif.__version__ import *

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_dbt_ldif.api import FlextDbtLdif
    from flext_dbt_ldif.base import (
        FlextDbtLdifServiceBase,
        FlextDbtLdifServiceBase as s,
    )
    from flext_dbt_ldif.constants import (
        FlextDbtLdifConstants,
        FlextDbtLdifConstants as c,
    )
    from flext_dbt_ldif.models import FlextDbtLdifModels, FlextDbtLdifModels as m
    from flext_dbt_ldif.protocols import (
        FlextDbtLdifProtocols,
        FlextDbtLdifProtocols as p,
    )
    from flext_dbt_ldif.services.cli_service import FlextDbtLdifCliService
    from flext_dbt_ldif.services.client import FlextDbtLdifClient
    from flext_dbt_ldif.services.core import FlextDbtLdifCore
    from flext_dbt_ldif.services.error import FlextDbtLdifError
    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
    from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService
    from flext_dbt_ldif.settings import FlextDbtLdifSettings
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, FlextDbtLdifTypes as t
    from flext_dbt_ldif.utilities import (
        FlextDbtLdifUtilities,
        FlextDbtLdifUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    (".services",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".api": ("FlextDbtLdif",),
            ".base": ("FlextDbtLdifServiceBase",),
            ".constants": ("FlextDbtLdifConstants",),
            ".models": ("FlextDbtLdifModels",),
            ".protocols": ("FlextDbtLdifProtocols",),
            ".settings": ("FlextDbtLdifSettings",),
            ".typings": ("FlextDbtLdifTypes",),
            ".utilities": ("FlextDbtLdifUtilities",),
        },
        alias_groups={
            ".base": (("s", "FlextDbtLdifServiceBase"),),
            ".constants": (("c", "FlextDbtLdifConstants"),),
            ".models": (("m", "FlextDbtLdifModels"),),
            ".protocols": (("p", "FlextDbtLdifProtocols"),),
            ".typings": (("t", "FlextDbtLdifTypes"),),
            ".utilities": (("u", "FlextDbtLdifUtilities"),),
            "flext_core.decorators": (("d", "FlextDecorators"),),
            "flext_core.exceptions": (("e", "FlextExceptions"),),
            "flext_core.handlers": (("h", "FlextHandlers"),),
            "flext_core.mixins": (("x", "FlextMixins"),),
            "flext_core.result": (("r", "FlextResult"),),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)

__all__ = [
    "FlextDbtLdif",
    "FlextDbtLdifCliService",
    "FlextDbtLdifClient",
    "FlextDbtLdifConstants",
    "FlextDbtLdifCore",
    "FlextDbtLdifError",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifServiceBase",
    "FlextDbtLdifServiceMixin",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
    "FlextDbtLdifUnifiedService",
    "FlextDbtLdifUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
