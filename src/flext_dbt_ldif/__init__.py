"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextResult
from flext_dbt_ldif.__version__ import __version__, __version_info__
from flext_dbt_ldif.cli import main
from flext_dbt_ldif.core import FlextDbtLdifCore
from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifError
from flext_dbt_ldif.dbt_models import (
    FlextDbtLdifUnifiedService,
    FlextDbtLdifUnifiedService as FlextDbtLdifModelGenerator,
)
from flext_dbt_ldif.dbt_services import FlextDbtLdifService
from flext_dbt_ldif.models import (
    FlextDbtLdifModels,
    FlextDbtLdifModels as FlextLdifDbtModel,
)
from flext_dbt_ldif.protocols import FlextDbtLdifProtocols
from flext_dbt_ldif.settings import FlextDbtLdifSettings
from flext_dbt_ldif.simple_api import (
    FlextDbtLdif,
    FlextDbtLdifAPI,
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)
from flext_dbt_ldif.typings import FlextDbtLdifTypes
from flext_dbt_ldif.utilities import FlextDbtLdifUtilities
from flext_dbt_ldif.version import PROJECT_VERSION, VERSION, FlextDbtLdifVersion
from flext_ldif import FlextLdif

__all__: list[str] = [
    "PROJECT_VERSION",
    "VERSION",
    "FlextDbtLdif",
    "FlextDbtLdifAPI",
    "FlextDbtLdifClient",
    "FlextDbtLdifCore",
    "FlextDbtLdifError",
    "FlextDbtLdifModelGenerator",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifService",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
    "FlextDbtLdifUnifiedService",
    "FlextDbtLdifUtilities",
    "FlextDbtLdifVersion",
    "FlextLdif",
    "FlextLdifDbtModel",
    "FlextResult",
    "__version__",
    "__version_info__",
    "generate_ldif_models",
    "main",
    "process_ldif_file",
    "validate_ldif_quality",
]
