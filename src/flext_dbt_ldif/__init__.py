# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_ldif import ldif
    from flext_meltano import cli, d, e, h, meltano, r, x

    from flext_dbt_ldif.__version__ import (
        FlextDbtLdifVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
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
    "FlextDbtLdifVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "cli",
    "config",
    "d",
    "dbt_ldif",
    "e",
    "h",
    "ldif",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "FlextDbtLdif": ".api",
        "FlextDbtLdifConfig": "._config",
        "FlextDbtLdifConstants": ".constants",
        "FlextDbtLdifConstantsBase": ".constants",
        "FlextDbtLdifModels": ".models",
        "FlextDbtLdifProtocols": ".protocols",
        "FlextDbtLdifServiceBase": ".base",
        "FlextDbtLdifSettings": "._settings",
        "FlextDbtLdifTypes": ".typings",
        "FlextDbtLdifUtilities": ".utilities",
        "FlextDbtLdifVersion": ".__version__",
        "__author__": ".__version__",
        "__author_email__": ".__version__",
        "__description__": ".__version__",
        "__license__": ".__version__",
        "__title__": ".__version__",
        "__url__": ".__version__",
        "__version_info__": ".__version__",
        "c": ".constants",
        "cli": "flext_meltano",
        "config": "._config",
        "d": "flext_meltano",
        "dbt_ldif": ".api",
        "e": "flext_meltano",
        "h": "flext_meltano",
        "ldif": "flext_ldif",
        "m": ".models",
        "main": ".cli",
        "meltano": "flext_meltano",
        "p": ".protocols",
        "r": "flext_meltano",
        "s": ".base",
        "settings": "._settings",
        "t": ".typings",
        "u": ".utilities",
        "x": "flext_meltano",
    }),
    public_exports=__all__,
)

if not TYPE_CHECKING:
    from flext_dbt_ldif.__version__ import __version__
