"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import importlib.metadata

from flext_core import FlextResult, FlextTypes
from flext_ldif import FlextLDIFAPI

# NOTE: Analytics classes and compatibility functions are available through existing modules
# Core components
from flext_dbt_ldif.core import DBTModelGenerator, LDIFAnalytics
from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_config import FlextDbtLdifConfig
from flext_dbt_ldif.dbt_exceptions import (
    FlextDbtLdifConnectionError,
    FlextDbtLdifError,
    FlextDbtLdifModelError,
    FlextDbtLdifProcessingError,
    FlextDbtLdifTransformationError,
    FlextDbtLdifValidationError,
)
from flext_dbt_ldif.dbt_services import (
    FlextDbtLdifService,
    FlextDbtLdifWorkflowManager,
)
from flext_dbt_ldif.models import FlextDbtLdifModelGenerator, FlextLDIFDbtModel
from flext_dbt_ldif.simple_api import (
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)

# NOTE: ChangeTracker functionality available through existing service modules

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


# Import convenience classes from dedicated modules

__all__: FlextTypes.Core.StringList = [
    # Legacy Core Components (backward compatibility)
    "DBTModelGenerator",  # Legacy from core.py
    # Core DBT Pattern Components
    "FlextDbtLdifClient",  # Main client for LDIF-DBT operations
    "FlextDbtLdifConfig",  # Configuration management
    "FlextDbtLdifConnectionError",  # Connection errors
    # Exception Hierarchy
    "FlextDbtLdifError",  # Base exception
    "FlextDbtLdifModelError",  # Model-specific errors
    "FlextDbtLdifModelGenerator",  # Programmatic model generation
    "FlextDbtLdifProcessingError",  # Processing errors
    "FlextDbtLdifService",  # High-level workflow orchestration
    "FlextDbtLdifTransformationError",  # Transformation errors
    "FlextDbtLdifValidationError",  # Validation errors
    "FlextDbtLdifWorkflowManager",  # Batch processing workflows
    "FlextLDIFAPI",  # LDIF API integration
    "FlextLDIFDbtModel",  # DBT model value object
    # Foundation Components (from flext-core and flext-ldif)
    "FlextResult",  # FlextResult pattern
    "LDIFAnalytics",  # Legacy analytics class
    "LDIFAnalyzer",
    "ModelGenerator",
    # Version Information
    "__version__",
    "__version_info__",
    "generate_ldif_models",
    "process_ldif_file",
    "validate_ldif_quality",
]
