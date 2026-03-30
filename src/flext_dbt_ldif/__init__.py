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

if TYPE_CHECKING:
    from flext_dbt_ldif.__version__ import *
    from flext_dbt_ldif.constants import *
    from flext_dbt_ldif.models import *
    from flext_dbt_ldif.protocols import *
    from flext_dbt_ldif.settings import *
    from flext_dbt_ldif.simple_api import *
    from flext_dbt_ldif.typings import *
    from flext_dbt_ldif.utilities import *


_LAZY_IMPORTS: Mapping[str, str | Sequence[str]] = {
    "FlextDbtLdif": "flext_dbt_ldif.simple_api",
    "FlextDbtLdifConstants": "flext_dbt_ldif.constants",
    "FlextDbtLdifModels": "flext_dbt_ldif.models",
    "FlextDbtLdifProtocols": "flext_dbt_ldif.protocols",
    "FlextDbtLdifSettings": "flext_dbt_ldif.settings",
    "FlextDbtLdifTypes": "flext_dbt_ldif.typings",
    "FlextDbtLdifUtilities": "flext_dbt_ldif.utilities",
    "__author__": "flext_dbt_ldif.__version__",
    "__author_email__": "flext_dbt_ldif.__version__",
    "__description__": "flext_dbt_ldif.__version__",
    "__license__": "flext_dbt_ldif.__version__",
    "__title__": "flext_dbt_ldif.__version__",
    "__url__": "flext_dbt_ldif.__version__",
    "__version__": "flext_dbt_ldif.__version__",
    "__version_info__": "flext_dbt_ldif.__version__",
    "c": ("flext_dbt_ldif.constants", "FlextDbtLdifConstants"),
    "constants": "flext_dbt_ldif.constants",
    "d": "flext_ldif",
    "e": "flext_ldif",
    "h": "flext_ldif",
    "m": ("flext_dbt_ldif.models", "FlextDbtLdifModels"),
    "models": "flext_dbt_ldif.models",
    "p": ("flext_dbt_ldif.protocols", "FlextDbtLdifProtocols"),
    "protocols": "flext_dbt_ldif.protocols",
    "r": "flext_ldif",
    "s": "flext_ldif",
    "settings": "flext_dbt_ldif.settings",
    "simple_api": "flext_dbt_ldif.simple_api",
    "t": ("flext_dbt_ldif.typings", "FlextDbtLdifTypes"),
    "typings": "flext_dbt_ldif.typings",
    "u": ("flext_dbt_ldif.utilities", "FlextDbtLdifUtilities"),
    "utilities": "flext_dbt_ldif.utilities",
    "x": "flext_ldif",
}


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
