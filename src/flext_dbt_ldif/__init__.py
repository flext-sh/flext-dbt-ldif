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
    from flext_cli.base import s

    from flext_core.decorators import d
    from flext_core.exceptions import e
    from flext_core.handlers import h
    from flext_core.mixins import x
    from flext_core.result import r
    from flext_dbt_ldif.api import FlextDbtLdif
    from flext_dbt_ldif.base import FlextDbtLdifServiceBase
    from flext_dbt_ldif.cli_service import FlextDbtLdifCliService
    from flext_dbt_ldif.client import FlextDbtLdifClient
    from flext_dbt_ldif.constants import FlextDbtLdifConstants, c
    from flext_dbt_ldif.core import FlextDbtLdifCore
    from flext_dbt_ldif.error import FlextDbtLdifError
    from flext_dbt_ldif.models import FlextDbtLdifModels, m
    from flext_dbt_ldif.protocols import FlextDbtLdifProtocols, p
    from flext_dbt_ldif.service import FlextDbtLdifServiceMixin
    from flext_dbt_ldif.settings import FlextDbtLdifSettings
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, t
    from flext_dbt_ldif.unified_service import FlextDbtLdifUnifiedService
    from flext_dbt_ldif.utilities import FlextDbtLdifUtilities, u
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
            ".cli_service": ("FlextDbtLdifCliService",),
            ".client": ("FlextDbtLdifClient",),
            ".constants": (
                "FlextDbtLdifConstants",
                "c",
            ),
            ".core": ("FlextDbtLdifCore",),
            ".error": ("FlextDbtLdifError",),
            ".models": (
                "FlextDbtLdifModels",
                "m",
            ),
            ".protocols": (
                "FlextDbtLdifProtocols",
                "p",
            ),
            ".service": ("FlextDbtLdifServiceMixin",),
            ".settings": ("FlextDbtLdifSettings",),
            ".typings": (
                "FlextDbtLdifTypes",
                "t",
            ),
            ".unified_service": ("FlextDbtLdifUnifiedService",),
            ".utilities": (
                "FlextDbtLdifUtilities",
                "u",
            ),
            "flext_cli.base": ("s",),
            "flext_core.decorators": ("d",),
            "flext_core.exceptions": ("e",),
            "flext_core.handlers": ("h",),
            "flext_core.mixins": ("x",),
            "flext_core.result": ("r",),
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
