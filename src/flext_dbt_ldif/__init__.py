# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core import build_lazy_import_map, install_lazy_exports
from flext_dbt_ldif.__version__ import (
    __author__,
    __author_email__,
    __description__,
    __license__,
    __title__,
    __url__,
    __version__,
    __version_info__,
)

if TYPE_CHECKING:
    from flext_meltano import d, e, h, r, x

    from flext_dbt_ldif import services
    from flext_dbt_ldif._config import FlextDbtLdifConfig, config
    from flext_dbt_ldif._settings import FlextDbtLdifSettings, settings
    from flext_dbt_ldif.api import FlextDbtLdif, dbt_ldif
    from flext_dbt_ldif.base import FlextDbtLdifServiceBase, s
    from flext_dbt_ldif.cli import main
    from flext_dbt_ldif.constants import (
        FlextDbtLdifConstants,
        FlextDbtLdifConstantsBase,
        c,
    )
    from flext_dbt_ldif.models import FlextDbtLdifModels, m
    from flext_dbt_ldif.protocols import FlextDbtLdifProtocols, p
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, t
    from flext_dbt_ldif.utilities import FlextDbtLdifUtilities, u


__all__: tuple[str, ...] = (
    "FlextDbtLdif",
    "FlextDbtLdifConfig",
    "FlextDbtLdifConstants",
    "FlextDbtLdifConstantsBase",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifServiceBase",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
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
    "config",
    "d",
    "dbt_ldif",
    "e",
    "h",
    "m",
    "main",
    "p",
    "r",
    "s",
    "services",
    "settings",
    "t",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._config": ("FlextDbtLdifConfig", "config"),
            "._settings": ("FlextDbtLdifSettings", "settings"),
            ".api": ("FlextDbtLdif", "dbt_ldif"),
            ".base": ("FlextDbtLdifServiceBase", "s"),
            ".cli": ("main",),
            ".constants": ("FlextDbtLdifConstants", "FlextDbtLdifConstantsBase", "c"),
            ".models": ("FlextDbtLdifModels", "m"),
            ".protocols": ("FlextDbtLdifProtocols", "p"),
            ".services": ("services",),
            ".typings": ("FlextDbtLdifTypes", "t"),
            ".utilities": ("FlextDbtLdifUtilities", "u"),
            "flext_meltano": ("d", "e", "h", "r", "x"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    ),
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
