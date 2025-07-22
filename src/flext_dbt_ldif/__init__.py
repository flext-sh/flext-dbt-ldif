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

# Foundation patterns - ALWAYS from flext-core
from flext_core import (
    BaseConfig,
    BaseConfig as LDIFBaseConfig,  # Configuration base
    DomainBaseModel,
    DomainBaseModel as BaseModel,  # Base for LDIF models
    DomainError as LDIFError,  # LDIF-specific errors
    ValidationError as ValidationError,  # Validation errors
)
from flext_core.domain.shared_types import ServiceResult

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


# ================================
# SIMPLIFIED PUBLIC API EXPORTS
# ================================

# Re-export commonly used imports from flext-core are now imported at top

# DBT LDIF Analytics exports - conditional imports (modules being developed)
try:
    from flext_dbt_ldif.analytics import (
        ChangeTracker,
        LDIFAnalyzer,
        LDIFInsights,
    )
except ImportError:
    # Analytics modules not yet implemented - part of programmatic dbt project generation
    pass

# DBT Model Generation exports - conditional imports (modules being developed)
try:
    from flext_dbt_ldif.models import (
        AnalyticsModel,
        DimensionModel,
        ModelGenerator,
    )
except ImportError:
    # Model generation modules not yet implemented - part of programmatic dbt project generation
    pass

# ================================
# PUBLIC API EXPORTS
# ================================

__all__ = [
    "AnalyticsModel",  # from flext_dbt_ldif import AnalyticsModel
    "BaseModel",  # from flext_dbt_ldif import BaseModel
    # Change Tracking (simplified access)
    "ChangeTracker",  # from flext_dbt_ldif import ChangeTracker
    # Dimension Modeling (simplified access)
    "DimensionModel",  # from flext_dbt_ldif import DimensionModel
    # Deprecation utilities
    "FlextDbtLdifDeprecationWarning",
    # LDIF Analytics (simplified access)
    "LDIFAnalyzer",  # from flext_dbt_ldif import LDIFAnalyzer
    # Core Patterns (from flext-core)
    "LDIFBaseConfig",  # from flext_dbt_ldif import LDIFBaseConfig
    "LDIFError",  # from flext_dbt_ldif import LDIFError
    "LDIFInsights",  # from flext_dbt_ldif import LDIFInsights
    # DBT Model Generation (simplified access)
    "ModelGenerator",  # from flext_dbt_ldif import ModelGenerator
    "ServiceResult",  # from flext_dbt_ldif import ServiceResult
    "ValidationError",  # from flext_dbt_ldif import ValidationError
    # Version
    "__version__",
    "__version_info__",
]
