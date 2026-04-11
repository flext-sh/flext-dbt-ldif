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
    from flext_dbt_ldif.api import FlextDbtLdif
    from flext_dbt_ldif.base import FlextDbtLdifServiceBase
    from flext_dbt_ldif.constants import FlextDbtLdifConstants, c
    from flext_dbt_ldif.models import FlextDbtLdifModels, m
    from flext_dbt_ldif.protocols import FlextDbtLdifProtocols, p
    from flext_dbt_ldif.services.cli_service import FlextDbtLdifCliService
    from flext_dbt_ldif.services.client import FlextDbtLdifClient
    from flext_dbt_ldif.services.core import FlextDbtLdifCore
    from flext_dbt_ldif.services.error import FlextDbtLdifError
    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
    from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService
    from flext_dbt_ldif.settings import FlextDbtLdifSettings
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, t
    from flext_dbt_ldif.utilities import FlextDbtLdifUtilities, u
    from flext_meltano import d, e, h, r, s, x
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
            ".constants": (
                "FlextDbtLdifConstants",
                "c",
            ),
            ".models": (
                "FlextDbtLdifModels",
                "m",
            ),
            ".protocols": (
                "FlextDbtLdifProtocols",
                "p",
            ),
            ".settings": ("FlextDbtLdifSettings",),
            ".typings": (
                "FlextDbtLdifTypes",
                "t",
            ),
            ".utilities": (
                "FlextDbtLdifUtilities",
                "u",
            ),
            "flext_meltano": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
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


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

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
