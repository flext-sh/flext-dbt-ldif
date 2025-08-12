"""FLEXT DBT LDIF - LDIF Data Analytics and Transformations.

Version 0.9.0 - Complete DBT LDIF platform following established patterns:
- DBT Configuration: FlextDbtLdifConfig for LDIF + DBT settings
- DBT Client: FlextDbtLdifClient for high-level operations
- DBT Models: FlextDbtLdifModelGenerator for programmatic model generation
- DBT Services: FlextDbtLdifService for complete workflow orchestration
- Simple API: Convenience functions for common operations
- Maximum integration with flext-core, flext-ldif, and flext-meltano

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import importlib.metadata

# Import from flext-core for foundational patterns
from flext_core import FlextResult

# Import real APIs from flext-ldif (maximum composition)
from flext_ldif import (
    FlextLdifAPI,
    flext_ldif_parse,
    flext_ldif_validate,
    flext_ldif_write,
)

# Import DBT pattern components
from .dbt_client import FlextDbtLdifClient
from .dbt_config import FlextDbtLdifConfig
from .dbt_exceptions import (
    FlextDbtLdifError,
    FlextDbtLdifValidationError,
    FlextDbtLdifProcessingError,
    FlextDbtLdifConnectionError,
    FlextDbtLdifModelError,
    FlextDbtLdifTransformationError,
)
from .dbt_models import FlextDbtLdifModelGenerator, FlextLdifDbtModel
from .dbt_services import FlextDbtLdifService, FlextDbtLdifWorkflowManager

# Import legacy core functionality (backward compatibility)
from .core import DBTModelGenerator, LDIFAnalytics

# Import simple API
from .simple_api import (
    generate_ldif_models,
    process_ldif_file,
    validate_ldif_quality,
)

# Create compatibility aliases for old API names (backward compatibility)
FlextLdifParser = FlextLdifAPI
FlextLdifValidator = FlextLdifAPI
FlextLdifWriter = FlextLdifAPI
flext_ldif_format_entry = flext_ldif_write
flext_ldif_parse_content = flext_ldif_parse
flext_ldif_validate_syntax = flext_ldif_validate

try:
    __version__ = importlib.metadata.version("flext-dbt-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.9.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())

# Create convenience aliases for common usage patterns
LDIFAnalyzer = LDIFAnalytics  # Alias for backward compatibility
ModelGenerator = FlextDbtLdifModelGenerator  # Alias for convenience


# Additional convenience classes
class ChangeTracker:
    """Change tracking functionality using LDIF comparison."""

    def __init__(self, service: FlextDbtLdifService | None = None) -> None:
        self.service = service or FlextDbtLdifService()


class LDIFInsights:
    """LDIF insights functionality using analytics models."""

    def __init__(self, generator: FlextDbtLdifModelGenerator | None = None) -> None:
        self.generator = generator or FlextDbtLdifModelGenerator()


class AnalyticsModel:
    """Analytics model functionality using DBT model generator."""

    def __init__(self, model: FlextLdifDbtModel | None = None) -> None:
        self.model = model


class DimensionModel:
    """Dimension model functionality using DBT patterns."""

    def __init__(self, model: FlextLdifDbtModel | None = None) -> None:
        self.model = model


__all__: list[str] = [
    "annotations", "FlextResult", "FlextLdifAPI", "flext_ldif_parse", "flext_ldif_validate",
    "flext_ldif_write", "FlextDbtLdifClient", "FlextDbtLdifConfig", "FlextDbtLdifError",
    "FlextDbtLdifValidationError", "FlextDbtLdifProcessingError", "FlextDbtLdifConnectionError",
    "FlextDbtLdifModelError", "FlextDbtLdifTransformationError", "FlextDbtLdifModelGenerator",
    "FlextLdifDbtModel", "FlextDbtLdifService", "FlextDbtLdifWorkflowManager", "DBTModelGenerator",
    "LDIFAnalytics", "generate_ldif_models", "process_ldif_file", "validate_ldif_quality",
    "FlextLdifParser", "FlextLdifValidator", "FlextLdifWriter", "flext_ldif_format_entry",
    "flext_ldif_parse_content", "flext_ldif_validate_syntax", "__version_info__", "LDIFAnalyzer",
    "ModelGenerator", "ChangeTracker", "LDIFInsights", "AnalyticsModel", "DimensionModel",
] = [
    # Core DBT Pattern Components
    "FlextDbtLdifClient",  # Main client for LDIF-DBT operations
    "FlextDbtLdifConfig",  # Configuration management
    "FlextDbtLdifModelGenerator",  # Programmatic model generation
    "FlextDbtLdifService",  # High-level workflow orchestration
    "FlextDbtLdifWorkflowManager",  # Batch processing workflows
    "FlextLdifDbtModel",  # DBT model value object
    # Exception Hierarchy
    "FlextDbtLdifError",  # Base exception
    "FlextDbtLdifValidationError",  # Validation errors
    "FlextDbtLdifProcessingError",  # Processing errors
    "FlextDbtLdifConnectionError",  # Connection errors
    "FlextDbtLdifModelError",  # Model-specific errors
    "FlextDbtLdifTransformationError",  # Transformation errors
    # Simple API (convenience functions)
    "generate_ldif_models",  # Simple model generation
    "process_ldif_file",  # Simple file processing
    "validate_ldif_quality",  # Simple quality validation
    # Legacy Core Components (backward compatibility)
    "DBTModelGenerator",  # Legacy from core.py
    "LDIFAnalytics",  # Legacy analytics class
    # Foundation Components (from flext-core and flext-ldif)
    "FlextResult",  # FlextResult pattern
    "FlextLdifAPI",  # LDIF API integration
    # Convenience Classes and Aliases
    "AnalyticsModel",  # Analytics model functionality
    "ChangeTracker",  # Change tracking functionality
    "DimensionModel",  # Dimension model functionality
    "LDIFAnalyzer",  # Alias for LDIFAnalytics
    "LDIFInsights",  # LDIF insights functionality
    "ModelGenerator",  # Alias for FlextDbtLdifModelGenerator
    # Compatibility Functions (backward compatibility)
    "flext_ldif_format_entry",  # Alias for flext_ldif_write
    "flext_ldif_parse",  # LDIF parsing function
    "flext_ldif_parse_content",  # Alias for flext_ldif_parse
    "flext_ldif_validate",  # LDIF validation function
    "flext_ldif_validate_syntax",  # Alias for flext_ldif_validate
    "flext_ldif_write",  # LDIF writing function
    # Version Information
    "__version__",
    "__version_info__",
]
