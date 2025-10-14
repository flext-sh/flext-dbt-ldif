"""FLEXT DBT LDIF Types - Domain-specific DBT LDIF type definitions.

This module provides DBT LDIF-specific type definitions extending FlextCore.Types.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextCore.Types properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextCore

# =============================================================================
# DBT LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDIF operations
# =============================================================================


# DBT LDIF domain TypeVars
class FlextDbtLdifTypes(FlextCore.Types):
    """DBT LDIF-specific type definitions extending FlextCore.Types.

    Domain-specific type system for DBT LDIF data transformation operations.
    Contains ONLY complex DBT LDIF-specific types, no simple aliases.
    Uses Python 3.13+ type syntax and patterns.
    """

    # =========================================================================
    # LDIF DATA TYPES - LDIF file format and record types
    # =========================================================================

    class LdifData:
        """LDIF data complex types."""

        type LdifRecord = dict[
            str,
            str
            | FlextCore.Types.StringList
            | bytes
            | dict[str, FlextCore.Types.JsonValue],
        ]
        type LdifEntry = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.StringList
        ]
        type LdifChangeRecord = dict[
            str, str | list[dict[str, FlextCore.Types.JsonValue]]
        ]
        type LdifAttributes = dict[str, str | FlextCore.Types.StringList | bytes]
        type LdifModification = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type LdifOperation = dict[str, str | FlextCore.Types.Dict]

    # =========================================================================
    # DBT LDIF TRANSFORMATION TYPES - LDIF to analytical data transformation
    # =========================================================================

    class DbtLdifTransformation:
        """DBT LDIF transformation complex types."""

        type TransformationConfig = dict[
            str, FlextCore.Types.JsonValue | FlextCore.Types.Dict
        ]
        type LdifToTableMapping = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type AttributeMapping = dict[
            str, str | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type DataNormalization = dict[
            str, str | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type SchemaGeneration = dict[str, str | list[FlextCore.Types.Dict]]
        type OutputConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]

    # =========================================================================
    # LDIF PARSING TYPES - LDIF file parsing and validation types
    # =========================================================================

    class LdifParsing:
        """LDIF parsing complex types."""

        type ParserConfiguration = dict[str, bool | str | int | FlextCore.Types.Dict]
        type ValidationRules = dict[
            str,
            bool | FlextCore.Types.StringList | dict[str, FlextCore.Types.JsonValue],
        ]
        type ErrorHandling = dict[str, str | bool | FlextCore.Types.Dict]
        type ParsedData = dict[str, list[dict[str, FlextCore.Types.JsonValue]]]
        type ParsingMetrics = dict[str, int | float | str | FlextCore.Types.Dict]
        type FileProcessing = dict[str, str | int | bool | FlextCore.Types.Dict]

    # =========================================================================
    # DBT MODEL TYPES - DBT model generation for LDIF data
    # =========================================================================

    class DbtLdifModel:
        """DBT LDIF model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type LdifModelConfig = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type DimensionalModel = dict[
            str, str | list[dict[str, FlextCore.Types.JsonValue]]
        ]
        type FactModel = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type StagingModel = dict[str, str | FlextCore.Types.Dict]
        type ModelDocumentation = dict[str, str | dict[str, FlextCore.Types.JsonValue]]

    # =========================================================================
    # LDIF PROCESSING TYPES - File processing and pipeline types
    # =========================================================================

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingPipeline = dict[
            str, list[dict[str, FlextCore.Types.JsonValue]] | FlextCore.Types.Dict
        ]
        type BatchProcessing = dict[str, int | str | bool | FlextCore.Types.Dict]
        type StreamProcessing = dict[
            str, int | bool | dict[str, FlextCore.Types.JsonValue]
        ]
        type ErrorRecovery = dict[
            str, str | bool | FlextCore.Types.StringList | FlextCore.Types.Dict
        ]
        type QualityValidation = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type ProcessingMetrics = dict[str, int | float | FlextCore.Types.Dict]

    # =========================================================================
    # LDIF EXPORT TYPES - Data export and output types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types."""

        type ExportConfiguration = dict[
            str, FlextCore.Types.ConfigValue | FlextCore.Types.Dict
        ]
        type OutputFormat = dict[str, str | dict[str, FlextCore.Types.JsonValue]]
        type DataSerialization = dict[str, str | FlextCore.Types.Dict]
        type CompressionSettings = dict[str, str | bool | int | FlextCore.Types.Dict]
        type ExportValidation = dict[
            str, bool | str | dict[str, FlextCore.Types.JsonValue]
        ]
        type DeliveryConfiguration = dict[str, str | FlextCore.Types.Dict]

    # =========================================================================
    # DBT LDIF PROJECT TYPES - Domain-specific project types extending FlextCore.Types
    # =========================================================================

    class Project(FlextCore.Types.Project):
        """DBT LDIF-specific project types extending FlextCore.Types.Project.

        Adds DBT LDIF analytics-specific project types while inheriting
        generic types from FlextCore.Types. Follows domain separation principle:
        DBT LDIF domain owns LDIF analytics and transformation-specific types.
        """

        # DBT LDIF-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextCore.Types.Project
            "library",
            "application",
            "service",
            # DBT LDIF-specific types
            "dbt-ldif",
            "ldif-analytics",
            "ldif-transform",
            "ldif-dbt-models",
            "dbt-ldif-project",
            "ldif-dimensional",
            "ldif-warehouse",
            "ldif-etl",
            "dbt-ldif-pipeline",
            "ldif-reporting",
            "ldif-dbt",
            "ldif-data-warehouse",
            "ldif-anomaly-detection",
            "ldif-change-analytics",
            "ldif-parser",
            "ldif-validator",
        ]

        # DBT LDIF-specific project configurations
        type DbtLdifProjectConfig = dict[str, FlextCore.Types.ConfigValue | object]
        type LdifAnalyticsConfig = dict[
            str, str | int | bool | FlextCore.Types.StringList
        ]
        type LdifTransformConfig = dict[str, bool | str | FlextCore.Types.Dict]
        type DbtLdifPipelineConfig = dict[str, FlextCore.Types.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT LDIF TypeVars and types
# =============================================================================

__all__: FlextCore.Types.StringList = [
    "FlextDbtLdifTypes",
]
