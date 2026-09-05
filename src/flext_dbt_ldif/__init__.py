# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import (
    __author__ as __author__,
    __author_email__ as __author_email__,
    __description__ as __description__,
    __license__ as __license__,
    __title__ as __title__,
    __url__ as __url__,
    __version__ as __version__,
    __version_info__ as __version_info__,
)

if TYPE_CHECKING:
    from enum import StrEnum, unique
    from typing import Final

    from flext_ldif import FlextLdifConstants, d, e, h, r, x

    from ._config import FlextDbtLdifConfig, config
    from ._settings import FlextDbtLdifSettings, settings
    from .api import FlextDbtLdif, dbt_ldif
    from .base import FlextDbtLdifServiceBase, FlextDbtLdifServiceBase as s
    from .constants import FlextDbtLdifConstants, FlextDbtLdifConstants as c
    from .models import FlextDbtLdifModels, FlextDbtLdifModels as m
    from .protocols import FlextDbtLdifProtocols, FlextDbtLdifProtocols as p
    from .typings import FlextDbtLdifTypes, FlextDbtLdifTypes as t
    from .utilities import FlextDbtLdifUtilities, FlextDbtLdifUtilities as u
__all__: tuple[str, ...] = (
    "Final",
    "FlextDbtLdif",
    "FlextDbtLdifConfig",
    "FlextDbtLdifConstants",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifServiceBase",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
    "FlextDbtLdifUtilities",
    "FlextLdifConstants",
    "StrEnum",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "config",
    "d",
    "dbt_ldif",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "u",
    "unique",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextDbtLdifConfig", "config"),
            "._settings": ("FlextDbtLdifSettings", "settings"),
            ".api": ("FlextDbtLdif", "dbt_ldif"),
            ".base": ("FlextDbtLdifServiceBase", "s"),
            ".constants": ("FlextDbtLdifConstants", "c"),
            ".models": ("FlextDbtLdifModels", "m"),
            ".protocols": ("FlextDbtLdifProtocols", "p"),
            ".typings": ("FlextDbtLdifTypes", "t"),
            ".utilities": ("FlextDbtLdifUtilities", "u"),
            "enum": ("StrEnum", "unique"),
            "flext_ldif": ("FlextLdifConstants", "d", "e", "h", "r", "x"),
            "typing": ("Final",),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
