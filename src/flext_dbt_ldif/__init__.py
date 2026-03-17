# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make codegen
#
"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import cleanup_submodule_namespace, lazy_getattr

if TYPE_CHECKING:
    from flext_core.typings import FlextTypes

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
    from flext_dbt_ldif.cli import (
        FlextDbtLdifCliService,
        FlextDbtLdifCliService as s,
        logger,
    )
    from flext_dbt_ldif.constants import FlextDbtLdifConstants, c
    from flext_dbt_ldif.core import FlextDbtLdifCore
    from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
    from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifError
    from flext_dbt_ldif.dbt_models import FlextDbtLdifUnifiedService
    from flext_dbt_ldif.models import FlextDbtLdifModels, m
    from flext_dbt_ldif.protocols import FlextDbtLdifProtocols, p
    from flext_dbt_ldif.services import FlextDbtLdifService
    from flext_dbt_ldif.settings import FlextDbtLdifSettings
    from flext_dbt_ldif.simple_api import FlextDbtLdif
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, t
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
    "c": ("flext_dbt_ldif.constants", "c"),
    "logger": ("flext_dbt_ldif.cli", "logger"),
    "m": ("flext_dbt_ldif.models", "m"),
    "p": ("flext_dbt_ldif.protocols", "p"),
    "s": ("flext_dbt_ldif.cli", "FlextDbtLdifCliService"),
    "t": ("flext_dbt_ldif.typings", "t"),
    "u": ("flext_dbt_ldif.utilities", "FlextDbtLdifUtilities"),
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
    "logger",
    "m",
    "p",
    "s",
    "t",
    "u",
]


def __getattr__(name: str) -> FlextTypes.ModuleExport:
    """Lazy-load module attributes on first access (PEP 562)."""
    return lazy_getattr(name, _LAZY_IMPORTS, globals(), __name__)


def __dir__() -> list[str]:
    """Return list of available attributes for dir() and autocomplete."""
    return sorted(__all__)


cleanup_submodule_namespace(__name__, _LAZY_IMPORTS)
