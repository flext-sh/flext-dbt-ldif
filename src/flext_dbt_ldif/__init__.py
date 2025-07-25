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
    FlextCoreSettings as BaseConfig,
    FlextEntity as DomainEntity,
    FlextField as Field,
    FlextResult,
    FlextValueObject as BaseModel,
    FlextValueObject as DomainBaseModel,
    FlextValueObject as DomainValueObject,
)
from flext_ldif import (
    FlextLdifParser,
    FlextLdifValidator,
    FlextLdifWriter,
    flext_ldif_format_entry,
    flext_ldif_parse_content,
    flext_ldif_validate_syntax,
)

# Import from flext-meltano for DBT integration
# MIGRATED: Singer SDK imports centralized via flext-meltano
from flext_meltano.dbt import (
    FlextMeltanoDbtManager,
    FlextMeltanoDbtProject,
    FlextMeltanoDbtRunner,
)

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

    from flext_dbt_ldif.analytics import (
        ChangeTracker,
        LDIFAnalyzer,
        LDIFInsights,
    )
    from flext_dbt_ldif.models import (
        AnalyticsModel,
        DimensionModel,
        ModelGenerator,
    )


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
