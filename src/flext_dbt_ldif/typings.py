"""FLEXT DBT LDIF Types - Domain-specific DBT LDIF type definitions.

This module provides DBT LDIF-specific type definitions extending FlextTypes.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ syntax
- Extends FlextTypes properly

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Literal

from flext_core import FlextTypes

# =============================================================================
# DBT LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDIF operations
# =============================================================================


# DBT LDIF domain TypeVars
class FlextDbtLdifTypes(FlextTypes):
    """DBT LDIF-specific type definitions extending FlextTypes.

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
            str, str | FlextTypes.StringList | bytes | dict[str, FlextTypes.JsonValue]
        ]
        type LdifEntry = dict[str, FlextTypes.JsonValue | FlextTypes.StringList]
        type LdifChangeRecord = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type LdifAttributes = dict[str, str | FlextTypes.StringList | bytes]
        type LdifModification = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type LdifOperation = dict[str, str | FlextTypes.Dict]

    # =========================================================================
    # DBT LDIF TRANSFORMATION TYPES - LDIF to analytical data transformation
    # =========================================================================

    class DbtLdifTransformation:
        """DBT LDIF transformation complex types."""

        type TransformationConfig = dict[str, FlextTypes.JsonValue | FlextTypes.Dict]
        type LdifToTableMapping = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type AttributeMapping = dict[str, str | FlextTypes.StringList | FlextTypes.Dict]
        type DataNormalization = dict[str, str | bool | dict[str, FlextTypes.JsonValue]]
        type SchemaGeneration = dict[str, str | list[FlextTypes.Dict]]
        type OutputConfiguration = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]

    # =========================================================================
    # LDIF PARSING TYPES - LDIF file parsing and validation types
    # =========================================================================

    class LdifParsing:
        """LDIF parsing complex types."""

        type ParserConfiguration = dict[str, bool | str | int | FlextTypes.Dict]
        type ValidationRules = dict[
            str, bool | FlextTypes.StringList | dict[str, FlextTypes.JsonValue]
        ]
        type ErrorHandling = dict[str, str | bool | FlextTypes.Dict]
        type ParsedData = dict[str, list[dict[str, FlextTypes.JsonValue]]]
        type ParsingMetrics = dict[str, int | float | str | FlextTypes.Dict]
        type FileProcessing = dict[str, str | int | bool | FlextTypes.Dict]

    # =========================================================================
    # DBT MODEL TYPES - DBT model generation for LDIF data
    # =========================================================================

    class DbtLdifModel:
        """DBT LDIF model complex types."""

        type ModelDefinition = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type LdifModelConfig = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type DimensionalModel = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        type FactModel = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type StagingModel = dict[str, str | FlextTypes.Dict]
        type ModelDocumentation = dict[str, str | dict[str, FlextTypes.JsonValue]]

    # =========================================================================
    # LDIF PROCESSING TYPES - File processing and pipeline types
    # =========================================================================

    class LdifProcessing:
        """LDIF processing complex types."""

        type ProcessingPipeline = dict[
            str, list[dict[str, FlextTypes.JsonValue]] | FlextTypes.Dict
        ]
        type BatchProcessing = dict[str, int | str | bool | FlextTypes.Dict]
        type StreamProcessing = dict[str, int | bool | dict[str, FlextTypes.JsonValue]]
        type ErrorRecovery = dict[
            str, str | bool | FlextTypes.StringList | FlextTypes.Dict
        ]
        type QualityValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type ProcessingMetrics = dict[str, int | float | FlextTypes.Dict]

    # =========================================================================
    # LDIF EXPORT TYPES - Data export and output types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types."""

        type ExportConfiguration = dict[str, FlextTypes.ConfigValue | FlextTypes.Dict]
        type OutputFormat = dict[str, str | dict[str, FlextTypes.JsonValue]]
        type DataSerialization = dict[str, str | FlextTypes.Dict]
        type CompressionSettings = dict[str, str | bool | int | FlextTypes.Dict]
        type ExportValidation = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        type DeliveryConfiguration = dict[str, str | FlextTypes.Dict]

    # =========================================================================
    # DBT LDIF PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes.Project):
        """DBT LDIF-specific project types extending FlextTypes.Project.

        Adds DBT LDIF analytics-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        DBT LDIF domain owns LDIF analytics and transformation-specific types.
        """

        # DBT LDIF-specific project types extending the generic ones
        type ProjectType = Literal[
            # Generic types inherited from FlextTypes.Project
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
        type DbtLdifProjectConfig = dict[str, FlextTypes.ConfigValue | object]
        type LdifAnalyticsConfig = dict[str, str | int | bool | FlextTypes.StringList]
        type LdifTransformConfig = dict[str, bool | str | FlextTypes.Dict]
        type DbtLdifPipelineConfig = dict[str, FlextTypes.ConfigValue | object]


# =============================================================================
# PUBLIC API EXPORTS - DBT LDIF TypeVars and types
# =============================================================================

__all__: FlextTypes.StringList = [
    "FlextDbtLdifTypes",
]
