"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import (
    FlextDecorators,
    FlextExceptions,
    FlextHandlers,
    FlextMixins,
    FlextService,
    r,
)
from flext_ldif import FlextLdif

from flext_dbt_ldif.__version__ import __version__, __version_info__
from flext_dbt_ldif.cli import FlextDbtLdifCliService
from flext_dbt_ldif.constants import FlextDbtLdifConstants as FlextDbtLdifConstants
from flext_dbt_ldif.core import FlextDbtLdifCore
from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifError
from flext_dbt_ldif.dbt_models import FlextDbtLdifUnifiedService
from flext_dbt_ldif.dbt_services import FlextDbtLdifService
from flext_dbt_ldif.models import FlextDbtLdifModels
from flext_dbt_ldif.protocols import FlextDbtLdifProtocols
from flext_dbt_ldif.settings import FlextDbtLdifSettings
from flext_dbt_ldif.simple_api import FlextDbtLdif
from flext_dbt_ldif.typings import FlextDbtLdifTypes, t
from flext_dbt_ldif.utilities import FlextDbtLdifUtilities

c = FlextDbtLdifConstants
d = FlextDecorators
e = FlextExceptions
h = FlextHandlers
m = FlextDbtLdifModels
p = FlextDbtLdifProtocols
r = r
s = FlextService
u = FlextDbtLdifUtilities
x = FlextMixins
__all__: list[str] = [
    "FlextDbtLdif",
    "FlextDbtLdifCliService",
    "FlextDbtLdifClient",
    "FlextDbtLdifCore",
    "FlextDbtLdifError",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifService",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
    "FlextDbtLdifUnifiedService",
    "FlextDbtLdifUtilities",
    "FlextLdif",
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
