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
    from flext_dbt_ldif.api import FlextDbtLdif as FlextDbtLdif, dbt_ldif as dbt_ldif
    from flext_dbt_ldif.constants import (
        FlextDbtLdifConstants as FlextDbtLdifConstants,
        c as c,
    )
    from flext_dbt_ldif.models import FlextDbtLdifModels as FlextDbtLdifModels, m as m
    from flext_dbt_ldif.protocols import (
        FlextDbtLdifProtocols as FlextDbtLdifProtocols,
        p as p,
    )
    from flext_dbt_ldif.settings import FlextDbtLdifSettings as FlextDbtLdifSettings
    from flext_dbt_ldif.typings import FlextDbtLdifTypes as FlextDbtLdifTypes, t as t
    from flext_dbt_ldif.utilities import (
        FlextDbtLdifUtilities as FlextDbtLdifUtilities,
        u as u,
    )
    from flext_meltano import d as d, e as e, h as h, r as r, s as s, x as x
_LAZY_IMPORTS = build_lazy_import_map(
    {
        ".api": (
            "FlextDbtLdif",
            "dbt_ldif",
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
)


__all__: tuple[str, ...] = (
    "FlextDbtLdif",
    "FlextDbtLdifConstants",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
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
