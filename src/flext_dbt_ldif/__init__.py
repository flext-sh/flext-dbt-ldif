"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import importlib.metadata

from flext_core import FlextResult
from flext_dbt_ldif.cli import main
from flext_dbt_ldif.config import FlextDbtLdifConfig
from flext_dbt_ldif.core import FlextDbtLdifCore
from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifError
from flext_dbt_ldif.dbt_models import FlextDbtLdifUnifiedService
from flext_dbt_ldif.dbt_services import FlextDbtLdifService
from flext_dbt_ldif.models import FlextDbtLdifModels
from flext_dbt_ldif.simple_api import (
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)
from flext_dbt_ldif.typings import FlextDbtLdifTypes
from flext_dbt_ldif.utilities import FlextDbtLdifUtilities
from flext_ldif import FlextLdifAPI

try:
    __version__ = importlib.metadata.version("flext-dbt-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


__all__: FlextDbtLdifTypes.Core.StringList = [
    "FlextDbtLdifClient",  # Main client for LDIF-DBT operations
    "FlextDbtLdifConfig",  # Configuration management
    "FlextDbtLdifCore",  # Core functionality
    "FlextDbtLdifError",  # Unified exception with error codes
    "FlextDbtLdifModels",  # Standardized [Project]Models pattern
    "FlextDbtLdifService",  # High-level workflow orchestration with integrated batch processing
    "FlextDbtLdifUnifiedService",  # Unified DBT model service (consolidated from old classes)
    "FlextDbtLdifUtilities",  # Standardized [Project]Utilities pattern
    "FlextLdifAPI",  # LDIF API integration
    "FlextResult",  # FlextResult pattern
    "__version__",
    "__version_info__",
    "generate_ldif_models",
    "main",  # CLI main entry point
    "process_ldif_file",
    "validate_ldif_quality",
]
