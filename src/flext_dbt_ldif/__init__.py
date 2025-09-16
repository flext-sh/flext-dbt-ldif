"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import importlib.metadata

from flext_core import FlextResult, FlextTypes
from flext_ldif import FlextLDIFAPI

from flext_dbt_ldif.core import DBTModelGenerator, LDIFAnalytics
from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_config import FlextDbtLdifConfig
from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifError
from flext_dbt_ldif.dbt_models import FlextDbtLdifModelGenerator, FlextLDIFDbtModel
from flext_dbt_ldif.dbt_services import (
    FlextDbtLdifService,
    FlextDbtLdifWorkflowManager,
)
from flext_dbt_ldif.simple_api import (
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)

# Create compatibility aliases for old API names (backward compatibility)
FlextLDIFParser = FlextLDIFAPI
FlextLDIFValidator = FlextLDIFAPI
FlextLDIFWriter = FlextLDIFAPI

try:
    __version__ = importlib.metadata.version("flext-dbt-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# Create convenience aliases for common usage patterns
LDIFAnalyzer = LDIFAnalytics
ModelGenerator = FlextDbtLdifModelGenerator


__all__: FlextTypes.Core.StringList = [
    "DBTModelGenerator",  # Legacy from core.py
    "FlextDbtLdifClient",  # Main client for LDIF-DBT operations
    "FlextDbtLdifConfig",  # Configuration management
    "FlextDbtLdifError",  # Unified exception with error codes
    "FlextDbtLdifModelGenerator",  # Programmatic model generation
    "FlextDbtLdifService",  # High-level workflow orchestration
    "FlextDbtLdifWorkflowManager",  # Batch processing workflows
    "FlextLDIFAPI",  # LDIF API integration
    "FlextLDIFDbtModel",  # DBT model value object
    "FlextResult",  # FlextResult pattern
    "LDIFAnalytics",  # Legacy analytics class
    "LDIFAnalyzer",
    "ModelGenerator",
    "__version__",
    "__version_info__",
    "generate_ldif_models",
    "process_ldif_file",
    "validate_ldif_quality",
]
