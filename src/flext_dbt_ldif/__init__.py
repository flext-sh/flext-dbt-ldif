"""FLEXT DBT LDIF - LDIF Data Analytics and Transformations with simplified imports.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Version 0.7.0 - DBT LDIF Analytics with simplified public API:
- All common imports available from root: from flext_dbt_ldif import LDIFAnalyzer
- Built on flext-core foundation for robust LDIF data transformations
- Deprecation warnings for internal imports
"""

from __future__ import annotations

import contextlib
import importlib.metadata
import warnings

# Import from flext-core for foundational patterns (standardized)
from flext_core import (
    FlextBaseSettings as BaseConfig,
    FlextEntity as DomainEntity,
    FlextFields as Field,
    FlextResult,
    FlextValueObject as BaseModel,
    FlextValueObject as DomainBaseModel,
    FlextValueObject as DomainValueObject,
)

# Import real APIs from flext-ldif (no fallbacks)
from flext_ldif import (
    FlextLdifAPI,
    FlextLdifEntry,
    flext_ldif_parse,
    flext_ldif_validate,
    flext_ldif_write,
)

# Import real DBT APIs from flext-meltano (no fallbacks)
from flext_meltano.dbt import (
    FlextMeltanoDbtManager,
    FlextMeltanoDbtProject,
    FlextMeltanoDbtRunner,
)

# Import from core module - using available classes
from flext_dbt_ldif.core import (
    DBTModelGenerator,
    LDIFAnalytics,
)

# Create compatibility aliases for old API names
FlextLdifParser = FlextLdifAPI
FlextLdifValidator = FlextLdifAPI
FlextLdifWriter = FlextLdifAPI
flext_ldif_format_entry = flext_ldif_write
flext_ldif_parse_content = flext_ldif_parse
flext_ldif_validate_syntax = flext_ldif_validate

try:
    __version__ = importlib.metadata.version("flext-dbt-ldif")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.7.0"

__version_info__ = tuple(int(x) for x in __version__.split(".") if x.isdigit())


class FlextDbtLdifDeprecationWarning(DeprecationWarning):
    """Custom deprecation warning for FLEXT DBT LDIF import changes."""


def _show_deprecation_warning(old_import: str, new_import: str) -> None:
    """Show deprecation warning for import paths."""
    message_parts = [
        f"⚠️  DEPRECATED IMPORT: {old_import}",
        f"✅ USE INSTEAD: {new_import}",
        "🔗 This will be removed in version 1.0.0",
        "📖 See FLEXT DBT LDIF docs for migration guide",
    ]
    warnings.warn(
        "\n".join(message_parts),
        FlextDbtLdifDeprecationWarning,
        stacklevel=3,
    )


# Note: analytics and models modules are planned for future implementation
# Using core functionality from flext-dbt-ldif for now


# Create placeholder classes that will be implemented when analytics/models modules are created
class ChangeTracker:
    """Placeholder for future analytics change tracking functionality."""


class LDIFAnalyzer:
    """Placeholder for future LDIF analysis functionality."""


class LDIFInsights:
    """Placeholder for future LDIF insights functionality."""


class AnalyticsModel:
    """Placeholder for future analytics model functionality."""


class DimensionModel:
    """Placeholder for future dimension model functionality."""


class ModelGenerator:
    """Placeholder for future model generation functionality."""



__all__ = [
    "AnalyticsModel",  # from flext_dbt_ldif import AnalyticsModel
    "BaseModel",  # from flext_dbt_ldif import BaseModel
    # Change Tracking (simplified access)
    "ChangeTracker",  # from flext_dbt_ldif import ChangeTracker
    # Dimension Modeling (simplified access)
    "DimensionModel",  # from flext_dbt_ldif import DimensionModel
    # Deprecation utilities
    "FlextDbtLdifDeprecationWarning",
    "FlextResult",  # from flext_dbt_ldif import FlextResult
    # LDIF Analytics (simplified access)
    "LDIFAnalyzer",  # from flext_dbt_ldif import LDIFAnalyzer
    # Core Patterns (from flext-core)
    "LDIFBaseConfig",  # from flext_dbt_ldif import LDIFBaseConfig
    "LDIFError",  # from flext_dbt_ldif import LDIFError
    "LDIFInsights",  # from flext_dbt_ldif import LDIFInsights
    # DBT Model Generation (simplified access)
    "ModelGenerator",  # from flext_dbt_ldif import ModelGenerator
    "ValidationError",  # from flext_dbt_ldif import ValidationError
    # Version
    "__version__",
    "__version_info__",
]
