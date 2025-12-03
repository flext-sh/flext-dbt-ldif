"""FLEXT DBT LDIF Types - Domain-specific DBT LDIF type definitions.

This module provides DBT LDIF-specific type definitions extending t.
Follows FLEXT standards:
- Domain-specific complex types only
- No simple aliases to primitive types
- Python 3.13+ PEP 695 syntax
- Extends t properly
- Uses Mapping instead of dict for read-only interfaces
- No dict[str, object] or Any types

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Literal

from flext_core import t

# =============================================================================
# DBT LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDIF operations
# =============================================================================


# DBT LDIF domain TypeVars
class FlextDbtLdifTypes(t):
    """DBT LDIF-specific type definitions extending t.

    Domain-specific type system for DBT LDIF data transformation operations.
    Contains ONLY complex DBT LDIF-specific types, no simple aliases.
    Uses Python 3.13+ PEP 695 type syntax and patterns.
    All types use t.GeneralValueType as base for consistency.
    """

    # =========================================================================
    # CORE TYPE ALIASES - Reusable base types for DBT LDIF domain
    # =========================================================================

    # String list type - commonly used for LDIF attributes (defined at class level)
    type StringList = Sequence[str]
    """Sequence of strings for multi-valued LDIF attributes."""

    class Core:
        """Core DBT LDIF type aliases using t as foundation."""

        # Attribute value type - single or multi-valued
        type AttributeValue = str | FlextDbtLdifTypes.StringList | bytes
        """LDIF attribute value: single string, list of strings, or bytes."""

        # Entry attributes mapping
        type AttributesMapping = Mapping[str, AttributeValue]
        """Mapping of attribute names to values."""

    # =========================================================================
    # LDIF DATA TYPES - LDIF file format and record types
    # =========================================================================

    class LdifData:
        """LDIF data complex types using PEP 695 syntax."""

        # LDIF record - complete LDIF entry with DN and attributes
        type LdifRecord = Mapping[
            str,
            str | FlextDbtLdifTypes.StringList | bytes | Mapping[str, t.JsonValue],
        ]
        """LDIF record type: DN and attributes mapping."""

        # LDIF entry - structured entry data
        type LdifEntry = Mapping[str, t.JsonValue | FlextDbtLdifTypes.StringList]
        """LDIF entry type: structured entry data."""

        # LDIF change record - modification operations
        type LdifChangeRecord = Mapping[
            str,
            str | Sequence[Mapping[str, t.JsonValue]],
        ]
        """LDIF change record type: modification operations."""

        # LDIF attributes - attribute name to value mapping
        type LdifAttributes = Mapping[str, str | FlextDbtLdifTypes.StringList | bytes]
        """LDIF attributes type: attribute name to value mapping."""

        # LDIF modification - single modification operation
        type LdifModification = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """LDIF modification type: single modification operation."""

        # LDIF operation - complete operation with metadata
        type LdifOperation = Mapping[
            str,
            str | Mapping[str, t.GeneralValueType],
        ]
        """LDIF operation type: complete operation with metadata."""

    # =========================================================================
    # DBT LDIF TRANSFORMATION TYPES - LDIF to analytical data transformation
    # =========================================================================

    class DbtLdifTransformation:
        """DBT LDIF transformation complex types using PEP 695 syntax."""

        # Transformation configuration
        type TransformationConfig = Mapping[
            str,
            t.JsonValue | Mapping[str, t.GeneralValueType],
        ]
        """DBT LDIF transformation configuration type."""

        # LDIF to table mapping
        type LdifToTableMapping = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """LDIF to table mapping type."""

        # Attribute mapping configuration
        type AttributeMapping = Mapping[
            str,
            str | FlextDbtLdifTypes.StringList | Mapping[str, t.GeneralValueType],
        ]
        """Attribute mapping type."""

        # Data normalization configuration
        type DataNormalization = Mapping[
            str,
            str | bool | Mapping[str, t.JsonValue],
        ]
        """Data normalization type."""

        # Schema generation configuration
        type SchemaGeneration = Mapping[
            str,
            str | Sequence[Mapping[str, t.GeneralValueType]],
        ]
        """Schema generation type."""

        # Output configuration
        type OutputConfiguration = Mapping[
            str,
            t.GeneralValueType | Mapping[str, t.GeneralValueType],
        ]
        """Output configuration type."""

    # =========================================================================
    # LDIF PARSING TYPES - LDIF file parsing and validation types
    # =========================================================================

    class LdifParsing:
        """LDIF parsing complex types using PEP 695 syntax."""

        # Parser configuration
        type ParserConfiguration = Mapping[
            str,
            bool | str | int | Mapping[str, t.GeneralValueType],
        ]
        """LDIF parser configuration type."""

        # Validation rules
        type ValidationRules = Mapping[
            str,
            bool | FlextDbtLdifTypes.StringList | Mapping[str, t.JsonValue],
        ]
        """LDIF validation rules type."""

        # Error handling configuration
        type ErrorHandling = Mapping[
            str,
            str | bool | Mapping[str, t.GeneralValueType],
        ]
        """LDIF error handling type."""

        # Parsed data structure
        type ParsedData = Mapping[
            str,
            Sequence[Mapping[str, t.JsonValue]],
        ]
        """LDIF parsed data type."""

        # Parsing metrics
        type ParsingMetrics = Mapping[
            str,
            int | float | str | Mapping[str, t.GeneralValueType],
        ]
        """LDIF parsing metrics type."""

        # File processing configuration
        type FileProcessing = Mapping[
            str,
            str | int | bool | Mapping[str, t.GeneralValueType],
        ]
        """LDIF file processing type."""

    # =========================================================================
    # DBT MODEL TYPES - DBT model generation for LDIF data
    # =========================================================================

    class DbtLdifModel:
        """DBT LDIF model complex types using PEP 695 syntax."""

        # Model definition
        type ModelDefinition = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """DBT LDIF model definition type."""

        # LDIF model configuration
        type LdifModelConfig = Mapping[
            str,
            t.GeneralValueType | Mapping[str, t.GeneralValueType],
        ]
        """LDIF model configuration type."""

        # Dimensional model
        type DimensionalModel = Mapping[
            str,
            str | Sequence[Mapping[str, t.JsonValue]],
        ]
        """DBT dimensional model type."""

        # Fact model
        type FactModel = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """DBT fact model type."""

        # Staging model
        type StagingModel = Mapping[
            str,
            str | Mapping[str, t.GeneralValueType],
        ]
        """DBT staging model type."""

        # Model documentation
        type ModelDocumentation = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """DBT model documentation type."""

    # =========================================================================
    # LDIF PROCESSING TYPES - File processing and pipeline types
    # =========================================================================

    class LdifProcessing:
        """LDIF processing complex types using PEP 695 syntax."""

        # Processing pipeline configuration
        type ProcessingPipeline = Mapping[
            str,
            Sequence[Mapping[str, t.JsonValue]] | Mapping[str, t.GeneralValueType],
        ]
        """LDIF processing pipeline type."""

        # Batch processing configuration
        type BatchProcessing = Mapping[
            str,
            int | str | bool | Mapping[str, t.GeneralValueType],
        ]
        """LDIF batch processing type."""

        # Stream processing configuration
        type StreamProcessing = Mapping[
            str,
            int | bool | Mapping[str, t.JsonValue],
        ]
        """LDIF stream processing type."""

        # Error recovery configuration
        type ErrorRecovery = Mapping[
            str,
            str
            | bool
            | FlextDbtLdifTypes.StringList
            | Mapping[str, t.GeneralValueType],
        ]
        """LDIF error recovery type."""

        # Quality validation configuration
        type QualityValidation = Mapping[
            str,
            bool | str | Mapping[str, t.JsonValue],
        ]
        """LDIF quality validation type."""

        # Processing metrics
        type ProcessingMetrics = Mapping[
            str,
            int | float | Mapping[str, t.GeneralValueType],
        ]
        """LDIF processing metrics type."""

    # =========================================================================
    # LDIF EXPORT TYPES - Data export and output types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types using PEP 695 syntax."""

        # Export configuration
        type ExportConfiguration = Mapping[
            str,
            t.GeneralValueType | Mapping[str, t.GeneralValueType],
        ]
        """LDIF export configuration type."""

        # Output format configuration
        type OutputFormat = Mapping[
            str,
            str | Mapping[str, t.JsonValue],
        ]
        """LDIF output format type."""

        # Data serialization configuration
        type DataSerialization = Mapping[
            str,
            str | Mapping[str, t.GeneralValueType],
        ]
        """LDIF data serialization type."""

        # Compression settings
        type CompressionSettings = Mapping[
            str,
            str | bool | int | Mapping[str, t.GeneralValueType],
        ]
        """LDIF compression settings type."""

        # Export validation configuration
        type ExportValidation = Mapping[
            str,
            bool | str | Mapping[str, t.JsonValue],
        ]
        """LDIF export validation type."""

        # Delivery configuration
        type DeliveryConfiguration = Mapping[
            str,
            str | Mapping[str, t.GeneralValueType],
        ]
        """LDIF delivery configuration type."""

    # =========================================================================
    # DBT LDIF PROJECT TYPES - Domain-specific project types extending t
    # =========================================================================

    class Project:
        """DBT LDIF-specific project types extending t.

        Adds DBT LDIF analytics-specific project types while inheriting
        generic types from t. Follows domain separation principle:
        DBT LDIF domain owns LDIF analytics and transformation-specific types.
        """

        # DBT LDIF-specific project type literal
        type ProjectType = Literal[
            # Generic types inherited from t
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
        """DBT LDIF project type literal."""

        # DBT LDIF-specific project configurations
        type DbtLdifProjectConfig = Mapping[str, t.GeneralValueType]
        """DBT LDIF project configuration type."""

        type LdifAnalyticsConfig = Mapping[
            str, str | int | bool | FlextDbtLdifTypes.StringList
        ]
        """LDIF analytics configuration type."""

        type LdifTransformConfig = Mapping[
            str,
            bool | str | Mapping[str, t.GeneralValueType],
        ]
        """LDIF transformation configuration type."""

        type DbtLdifPipelineConfig = Mapping[str, t.GeneralValueType]
        """DBT LDIF pipeline configuration type."""


# =============================================================================
# PUBLIC API EXPORTS - DBT LDIF TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtLdifTypes",
]
