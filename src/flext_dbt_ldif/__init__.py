# @generated AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

from .__version__ import __author__ as __author__
from .__version__ import __author_email__ as __author_email__
from .__version__ import __description__ as __description__
from .__version__ import __license__ as __license__
from .__version__ import __title__ as __title__
from .__version__ import __url__ as __url__
from .__version__ import __version__ as __version__
from .__version__ import __version_info__ as __version_info__

if TYPE_CHECKING:
    from flext_ldif import d as d
    from flext_ldif import e as e
    from flext_ldif import h as h
    from flext_ldif import r as r
    from flext_ldif import x as x

    from ._config import FlextDbtLdifConfig as FlextDbtLdifConfig
    from ._config import config as config
    from ._settings import FlextDbtLdifSettings as FlextDbtLdifSettings
    from ._settings import settings as settings
    from .api import FlextDbtLdif as FlextDbtLdif
    from .api import dbt_ldif as dbt_ldif
    from .base import FlextDbtLdifServiceBase as FlextDbtLdifServiceBase

    s: type[FlextDbtLdifServiceBase]
    from .constants import FlextDbtLdifConstants as FlextDbtLdifConstants

    c: type[FlextDbtLdifConstants]
    from .models import FlextDbtLdifModels as FlextDbtLdifModels

    m: type[FlextDbtLdifModels]
    from .protocols import FlextDbtLdifProtocols as FlextDbtLdifProtocols

    p: type[FlextDbtLdifProtocols]
    from .typings import FlextDbtLdifTypes as FlextDbtLdifTypes

    t: type[FlextDbtLdifTypes]
    from .utilities import FlextDbtLdifUtilities as FlextDbtLdifUtilities

    u: type[FlextDbtLdifUtilities]

_LAZY_MODULES: dict[str, tuple[str, ...]] = {
    "._config": ("FlextDbtLdifConfig", "config"),
    "._settings": ("FlextDbtLdifSettings", "settings"),
    ".api": ("FlextDbtLdif", "dbt_ldif"),
    ".base": ("FlextDbtLdifServiceBase", "s"),
    ".constants": ("FlextDbtLdifConstants", "c"),
    ".models": ("FlextDbtLdifModels", "m"),
    ".protocols": ("FlextDbtLdifProtocols", "p"),
    ".typings": ("FlextDbtLdifTypes", "t"),
    ".utilities": ("FlextDbtLdifUtilities", "u"),
    "flext_ldif": ("d", "e", "h", "r", "x"),
}


_LAZY_ALIAS_GROUPS: dict[str, tuple[tuple[str, str], ...]] = {}


_LAZY_IMPORTS = build_lazy_import_map(
    _LAZY_MODULES, alias_groups=_LAZY_ALIAS_GROUPS, sort_keys=False
)

_PUBLIC_EXPORTS: tuple[str, ...] = (
    "FlextDbtLdif",
    "FlextDbtLdifConfig",
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
    "x",
)

__all__: tuple[str, ...] = tuple(_PUBLIC_EXPORTS)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
