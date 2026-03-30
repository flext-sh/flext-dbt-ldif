# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

from flext_dbt_ldif.__version__ import (
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
    from flext_dbt_ldif import (
        constants as constants,
        models as models,
        protocols as protocols,
        settings as settings,
        simple_api as simple_api,
        typings as typings,
        utilities as utilities,
    )
    from flext_dbt_ldif.constants import (
        FlextDbtLdifConstants as FlextDbtLdifConstants,
        FlextDbtLdifConstants as c,
    )
    from flext_dbt_ldif.models import (
        FlextDbtLdifModels as FlextDbtLdifModels,
        FlextDbtLdifModels as m,
    )
    from flext_dbt_ldif.protocols import (
        FlextDbtLdifProtocols as FlextDbtLdifProtocols,
        FlextDbtLdifProtocols as p,
    )
    from flext_dbt_ldif.settings import FlextDbtLdifSettings as FlextDbtLdifSettings
    from flext_dbt_ldif.simple_api import FlextDbtLdif as FlextDbtLdif
    from flext_dbt_ldif.typings import (
        FlextDbtLdifTypes as FlextDbtLdifTypes,
        FlextDbtLdifTypes as t,
    )
    from flext_dbt_ldif.utilities import (
        FlextDbtLdifUtilities as FlextDbtLdifUtilities,
        FlextDbtLdifUtilities as u,
    )

_LAZY_IMPORTS: Mapping[str, Sequence[str]] = {
    "FlextDbtLdif": ["flext_dbt_ldif.simple_api", "FlextDbtLdif"],
    "FlextDbtLdifConstants": ["flext_dbt_ldif.constants", "FlextDbtLdifConstants"],
    "FlextDbtLdifModels": ["flext_dbt_ldif.models", "FlextDbtLdifModels"],
    "FlextDbtLdifProtocols": ["flext_dbt_ldif.protocols", "FlextDbtLdifProtocols"],
    "FlextDbtLdifSettings": ["flext_dbt_ldif.settings", "FlextDbtLdifSettings"],
    "FlextDbtLdifTypes": ["flext_dbt_ldif.typings", "FlextDbtLdifTypes"],
    "FlextDbtLdifUtilities": ["flext_dbt_ldif.utilities", "FlextDbtLdifUtilities"],
    "c": ["flext_dbt_ldif.constants", "FlextDbtLdifConstants"],
    "constants": ["flext_dbt_ldif.constants", ""],
    "d": ["flext_ldif", "d"],
    "e": ["flext_ldif", "e"],
    "h": ["flext_ldif", "h"],
    "m": ["flext_dbt_ldif.models", "FlextDbtLdifModels"],
    "models": ["flext_dbt_ldif.models", ""],
    "p": ["flext_dbt_ldif.protocols", "FlextDbtLdifProtocols"],
    "protocols": ["flext_dbt_ldif.protocols", ""],
    "r": ["flext_ldif", "r"],
    "s": ["flext_ldif", "s"],
    "settings": ["flext_dbt_ldif.settings", ""],
    "simple_api": ["flext_dbt_ldif.simple_api", ""],
    "t": ["flext_dbt_ldif.typings", "FlextDbtLdifTypes"],
    "typings": ["flext_dbt_ldif.typings", ""],
    "u": ["flext_dbt_ldif.utilities", "FlextDbtLdifUtilities"],
    "utilities": ["flext_dbt_ldif.utilities", ""],
    "x": ["flext_ldif", "x"],
}

_EXPORTS: Sequence[str] = [
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
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "settings",
    "simple_api",
    "t",
    "typings",
    "u",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, _EXPORTS)
