# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core import FlextTypes
    from flext_ldif import d, e, h, r, s, x

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
    from flext_dbt_ldif.cli import FlextDbtLdifCliService
    from flext_dbt_ldif.constants import (
        FlextDbtLdifConstants,
        FlextDbtLdifConstants as c,
    )
    from flext_dbt_ldif.core import FlextDbtLdifCore
    from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
    from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifError
    from flext_dbt_ldif.dbt_models import FlextDbtLdifUnifiedService
    from flext_dbt_ldif.models import FlextDbtLdifModels, FlextDbtLdifModels as m
    from flext_dbt_ldif.protocols import (
        FlextDbtLdifProtocols,
        FlextDbtLdifProtocols as p,
    )
    from flext_dbt_ldif.services import FlextDbtLdifService
    from flext_dbt_ldif.settings import FlextDbtLdifSettings
    from flext_dbt_ldif.simple_api import FlextDbtLdif
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, FlextDbtLdifTypes as t
    from flext_dbt_ldif.utilities import (
        FlextDbtLdifUtilities,
        FlextDbtLdifUtilities as u,
    )

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "FlextDbtLdif": ("flext_dbt_ldif.simple_api", "FlextDbtLdif"),
    "FlextDbtLdifCliService": ("flext_dbt_ldif.cli", "FlextDbtLdifCliService"),
    "FlextDbtLdifClient": ("flext_dbt_ldif.dbt_client", "FlextDbtLdifClient"),
    "FlextDbtLdifConstants": ("flext_dbt_ldif.constants", "FlextDbtLdifConstants"),
    "FlextDbtLdifCore": ("flext_dbt_ldif.core", "FlextDbtLdifCore"),
    "FlextDbtLdifError": ("flext_dbt_ldif.dbt_exceptions", "FlextDbtLdifError"),
    "FlextDbtLdifModels": ("flext_dbt_ldif.models", "FlextDbtLdifModels"),
    "FlextDbtLdifProtocols": ("flext_dbt_ldif.protocols", "FlextDbtLdifProtocols"),
    "FlextDbtLdifService": ("flext_dbt_ldif.services", "FlextDbtLdifService"),
    "FlextDbtLdifSettings": ("flext_dbt_ldif.settings", "FlextDbtLdifSettings"),
    "FlextDbtLdifTypes": ("flext_dbt_ldif.typings", "FlextDbtLdifTypes"),
    "FlextDbtLdifUnifiedService": (
        "flext_dbt_ldif.dbt_models",
        "FlextDbtLdifUnifiedService",
    ),
    "FlextDbtLdifUtilities": ("flext_dbt_ldif.utilities", "FlextDbtLdifUtilities"),
    "__all__": ("flext_dbt_ldif.__version__", "__all__"),
    "__author__": ("flext_dbt_ldif.__version__", "__author__"),
    "__author_email__": ("flext_dbt_ldif.__version__", "__author_email__"),
    "__description__": ("flext_dbt_ldif.__version__", "__description__"),
    "__license__": ("flext_dbt_ldif.__version__", "__license__"),
    "__title__": ("flext_dbt_ldif.__version__", "__title__"),
    "__url__": ("flext_dbt_ldif.__version__", "__url__"),
    "__version__": ("flext_dbt_ldif.__version__", "__version__"),
    "__version_info__": ("flext_dbt_ldif.__version__", "__version_info__"),
    "c": ("flext_dbt_ldif.constants", "FlextDbtLdifConstants"),
    "d": ("flext_ldif", "d"),
    "e": ("flext_ldif", "e"),
    "h": ("flext_ldif", "h"),
    "m": ("flext_dbt_ldif.models", "FlextDbtLdifModels"),
    "p": ("flext_dbt_ldif.protocols", "FlextDbtLdifProtocols"),
    "r": ("flext_ldif", "r"),
    "s": ("flext_ldif", "s"),
    "t": ("flext_dbt_ldif.typings", "FlextDbtLdifTypes"),
    "u": ("flext_dbt_ldif.utilities", "FlextDbtLdifUtilities"),
    "x": ("flext_ldif", "x"),
}

__all__ = [
    "FlextDbtLdif",
    "FlextDbtLdifCliService",
    "FlextDbtLdifClient",
    "FlextDbtLdifConstants",
    "FlextDbtLdifCore",
    "FlextDbtLdifError",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifService",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
    "FlextDbtLdifUnifiedService",
    "FlextDbtLdifUtilities",
    "__all__",
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


_LAZY_CACHE: dict[str, FlextTypes.ModuleExport] = {}


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562).

    A local cache ``_LAZY_CACHE`` persists resolved objects across repeated
    accesses during process lifetime.

    Args:
        name: Attribute name requested by dir()/import.

    Returns:
        Lazy-loaded module export type.

    Raises:
        AttributeError: If attribute not registered.

    """
    if name in _LAZY_CACHE:
        return _LAZY_CACHE[name]

    value = lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)
    _LAZY_CACHE[name] = value
    return value


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete.

    Returns:
        List of public names from module exports.

    """
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
