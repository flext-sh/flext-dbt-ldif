# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports
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
    from flext_ldif import d, e, h, r, x

    from ._settings import FlextDbtLdifSettings, settings
    from .api import FlextDbtLdif, dbt_ldif
    from .base import FlextDbtLdifServiceBase, s
    from .constants import FlextDbtLdifConstants, FlextDbtLdifConstants as c
    from .models import FlextDbtLdifModels, FlextDbtLdifModels as m
    from .protocols import FlextDbtLdifProtocols, FlextDbtLdifProtocols as p
    from .typings import FlextDbtLdifTypes, FlextDbtLdifTypes as t
    from .utilities import FlextDbtLdifUtilities, FlextDbtLdifUtilities as u

    _ = (
        c,
        FlextDbtLdifConstants,
        t,
        FlextDbtLdifTypes,
        p,
        FlextDbtLdifProtocols,
        m,
        FlextDbtLdifModels,
        u,
        FlextDbtLdifUtilities,
        d,
        e,
        h,
        r,
        x,
        s,
        FlextDbtLdifServiceBase,
        FlextDbtLdifSettings,
        settings,
        FlextDbtLdif,
        dbt_ldif,
    )


_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._settings": (
        "FlextDbtLdifSettings",
        "settings",
    ),
    ".api": (
        "FlextDbtLdif",
        "dbt_ldif",
    ),
    ".base": (
        "FlextDbtLdifServiceBase",
        "s",
    ),
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
    ".typings": (
        "FlextDbtLdifTypes",
        "t",
    ),
    ".utilities": (
        "FlextDbtLdifUtilities",
        "u",
    ),
    "flext_ldif": (
        "d",
        "e",
        "h",
        "r",
        "x",
    ),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES,
    alias_groups=_LAZY_ALIAS_GROUPS,
    sort_keys=False,
)

_DIRECT_IMPORTS: tuple[str, ...] = (
    "FlextDbtLdif",
    "FlextDbtLdifConstants",
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
    "build_lazy_import_map",
    "c",
    "d",
    "dbt_ldif",
    "e",
    "h",
    "install_lazy_exports",
    "m",
    "p",
    "r",
    "s",
    "settings",
    "t",
    "u",
    "x",
)

__all__: tuple[str, ...] = (
    "FlextDbtLdif",
    "FlextDbtLdifConstants",
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
    "x",
)


install_lazy_exports(
    __name__,
    globals(),
    _LAZY_IMPORTS,
    public_exports=__all__,
)
