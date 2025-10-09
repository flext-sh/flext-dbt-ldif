"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldif.__version__ import __version__, __version_info__

from typing import Final

from flext_core import FlextResult
from flext_ldif import FlextLdif

from flext_dbt_ldif.cli import main
from flext_dbt_ldif.config import FlextDbtLdifConfig
from flext_dbt_ldif.core import FlextDbtLdifCore
from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifError
from flext_dbt_ldif.dbt_models import FlextDbtLdifUnifiedService
from flext_dbt_ldif.dbt_services import FlextDbtLdifService
from flext_dbt_ldif.models import FlextDbtLdifModels
from flext_dbt_ldif.protocols import FlextDbtLdifProtocols
from flext_dbt_ldif.simple_api import (
    FlextDbtLdif,
    FlextDbtLdifAPI,
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)
from flext_dbt_ldif.typings import FlextDbtLdifTypes
from flext_dbt_ldif.utilities import FlextDbtLdifUtilities
from flext_dbt_ldif.version import VERSION, FlextDbtLdifVersion

PROJECT_VERSION: Final[FlextDbtLdifVersion] = VERSION

__version__: str = VERSION.version
__version_info__: tuple[int | str, ...] = VERSION.version_info

__all__: FlextDbtLdifTypes.Core.StringList = [
    "FlextDbtLdif",
    "FlextDbtLdifAPI",
    "FlextDbtLdifClient",
    "FlextDbtLdifConfig",
    "FlextDbtLdifCore",
    "FlextDbtLdifError",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifService",
    "FlextDbtLdifUnifiedService",
    "FlextDbtLdifUtilities",
    "FlextLdif",
    "FlextResult",
    "__version__",
    "__version_info__",
    "generate_ldif_models",
    "main",
    "process_ldif_file",
    "validate_ldif_quality",
]
