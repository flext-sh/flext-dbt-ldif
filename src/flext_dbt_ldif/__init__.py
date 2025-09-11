"""LDIF Data Analytics and Transformations for DBT.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

import importlib.metadata

from flext_core import FlextResult, FlextTypes

from flext_ldif import (
    FlextLDIFAPI,
    FlextLDIFModels,
    FlextLDIFServices,
)

from flext_dbt_ldif.dbt_client import FlextDbtLdifClient
from flext_dbt_ldif.dbt_config import FlextDbtLdifConfig
from flext_dbt_ldif.dbt_exceptions import (
    FlextDbtLdifError,
    FlextDbtLdifValidationError,
    FlextDbtLdifProcessingError,
    FlextDbtLdifConnectionError,
    FlextDbtLdifModelError,
    FlextDbtLdifTransformationError,
)
from flext_dbt_ldif.models import FlextDbtLdifModelGenerator, FlextLDIFDbtModel
from flext_dbt_ldif.dbt_services import (
    FlextDbtLdifService,
    FlextDbtLdifWorkflowManager,
)

from flext_dbt_ldif.core import DBTModelGenerator, LDIFAnalytics

from flext_dbt_ldif.simple_api import (
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)

# Create compatibility aliases for old API names (backward compatibility)
FlextLDIFParser = FlextLDIFAPI
FlextLDIFValidator = FlextLDIFAPI
FlextLDIFWriter = FlextLDIFAPI


# Function aliases using available API
def flext_ldif_parse(content):
    """Parse LDIF content using FlextLDIFAPI."""
    api = FlextLDIFAPI()
    return api.parse_string(content)


def flext_ldif_validate(content):
    """Validate LDIF content using FlextLDIFAPI."""
    api = FlextLDIFAPI()
    parse_result = api.parse_string(content)
    if parse_result.is_failure:
        return parse_result
    return api.validate_entries(parse_result.unwrap())


def flext_ldif_write(entries):
    """Write LDIF entries using FlextLDIFAPI."""
    api = FlextLDIFAPI()
    return api.write_entries(entries)


# Additional compatibility aliases
flext_ldif_format_entry = flext_ldif_write
flext_ldif_parse_content = flext_ldif_parse
flext_ldif_validate_syntax = flext_ldif_validate

try:
    __version__ = importlib.metadata.version("flext-dbt-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# Create convenience aliases for common usage patterns
LDIFAnalyzer = LDIFAnalytics
ModelGenerator = FlextDbtLdifModelGenerator


# Additional convenience classes
class ChangeTracker:
    """Change tracking functionality using LDIF comparison."""

    def __init__(self, service: FlextDbtLdifService | None = None) -> None:
        """Initialize change tracker."""
        self.service = service or FlextDbtLdifService()


class LDIFInsights:
    """LDIF insights functionality using analytics models."""

    def __init__(self, generator: FlextDbtLdifModelGenerator | None = None) -> None:
        """Initialize LDIF insights."""
        self.generator = generator or FlextDbtLdifModelGenerator()


class AnalyticsModel:
    """Analytics model functionality using DBT model generator."""

    def __init__(self, model: FlextLDIFDbtModel | None = None) -> None:
        """Initialize analytics model."""
        self.model = model


class DimensionModel:
    """Dimension model functionality using DBT patterns."""

    def __init__(self, model: FlextLDIFDbtModel | None = None) -> None:
        """Initialize dimension model."""
        self.model = model


__all__: FlextTypes.Core.StringList = [
    # Core DBT Pattern Components
    "FlextDbtLdifClient",  # Main client for LDIF-DBT operations
    "FlextDbtLdifConfig",  # Configuration management
    "FlextDbtLdifModelGenerator",  # Programmatic model generation
    "FlextDbtLdifService",  # High-level workflow orchestration
    "FlextDbtLdifWorkflowManager",  # Batch processing workflows
    "FlextLDIFDbtModel",  # DBT model value object
    # Exception Hierarchy
    "FlextDbtLdifError",  # Base exception
    "FlextDbtLdifValidationError",  # Validation errors
    "FlextDbtLdifProcessingError",  # Processing errors
    "FlextDbtLdifConnectionError",  # Connection errors
    "FlextDbtLdifModelError",  # Model-specific errors
    "FlextDbtLdifTransformationError",  # Transformation errors
    "generate_ldif_models",
    "process_ldif_file",
    "validate_ldif_quality",
    # Legacy Core Components (backward compatibility)
    "DBTModelGenerator",  # Legacy from core.py
    "LDIFAnalytics",  # Legacy analytics class
    # Foundation Components (from flext-core and flext-ldif)
    "FlextResult",  # FlextResult pattern
    "FlextLDIFAPI",  # LDIF API integration
    # Convenience Classes and Aliases
    "AnalyticsModel",  # Analytics model functionality
    "ChangeTracker",  # Change tracking functionality
    "DimensionModel",  # Dimension model functionality
    "LDIFAnalyzer",
    "LDIFInsights",  # LDIF insights functionality
    "ModelGenerator",
    # Compatibility Functions (backward compatibility)
    "flext_ldif_format_entry",
    "flext_ldif_parse",  # LDIF parsing function
    "flext_ldif_parse_content",
    "flext_ldif_validate",  # LDIF validation function
    "flext_ldif_validate_syntax",
    "flext_ldif_write",  # LDIF writing function
    # Version Information
    "__version__",
    "__version_info__",
]
