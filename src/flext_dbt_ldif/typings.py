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

from flext import FlextTypes

# =============================================================================
# DBT LDIF-SPECIFIC TYPE VARIABLES - Domain-specific TypeVars for DBT LDIF operations
# =============================================================================


# DBT LDIF domain TypeVars
class FlextDbtLdifTypes(FlextTypes):
    """DBT LDIF-specific type definitions extending t.

    Domain-specific type system for DBT LDIF data transformation operations.
    Contains ONLY complex DBT LDIF-specific types, no simple aliases.
    Uses Python 3.13+ PEP 695 type syntax and patterns.
    All types use FlextTypes.GeneralValueType as base for consistency.
    """

    # =========================================================================
    # CORE TYPE ALIASES - Reusable base types for DBT LDIF domain
    # =========================================================================

    # String list type - commonly used for LDIF attributes (defined at class level)
    type StringList = Sequence[str]
    """Sequence of strings for multi-valued LDIF attributes."""

    class DbtLdifCore:
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
            str
            | FlextDbtLdifTypes.StringList
            | bytes
            | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF record type: DN and attributes mapping."""

        # LDIF entry - structured entry data
        type LdifEntry = Mapping[
            str, FlextTypes.JsonValue | FlextDbtLdifTypes.StringList,
        ]
        """LDIF entry type: structured entry data."""

        # LDIF change record - modification operations
        type LdifChangeRecord = Mapping[
            str,
            str | Sequence[Mapping[str, FlextTypes.JsonValue]],
        ]
        """LDIF change record type: modification operations."""

        # LDIF attributes - attribute name to value mapping
        type Attributes = Mapping[str, str | FlextDbtLdifTypes.StringList | bytes]
        """LDIF attributes type: attribute name to value mapping."""

        # LDIF modification - single modification operation
        type LdifModification = Mapping[
            str,
            str | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF modification type: single modification operation."""

        # LDIF operation - complete operation with metadata
        type LdifOperation = Mapping[
            str,
            str | Mapping[str, FlextTypes.GeneralValueType],
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
            FlextTypes.JsonValue | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """DBT LDIF transformation configuration type."""

        # LDIF to table mapping
        type LdifToTableMapping = Mapping[
            str,
            str | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF to table mapping type."""

        # Attribute mapping configuration
        type AttributeMapping = Mapping[
            str,
            str
            | FlextDbtLdifTypes.StringList
            | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """Attribute mapping type."""

        # Data normalization configuration
        type DataNormalization = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.JsonValue],
        ]
        """Data normalization type."""

        # Schema generation configuration
        type SchemaGeneration = Mapping[
            str,
            str | Sequence[Mapping[str, FlextTypes.GeneralValueType]],
        ]
        """Schema generation type."""

        # Output configuration
        type OutputConfiguration = Mapping[
            str,
            FlextTypes.GeneralValueType | Mapping[str, FlextTypes.GeneralValueType],
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
            bool | str | int | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF parser configuration type."""

        # Validation rules
        type ValidationRules = Mapping[
            str,
            bool | FlextDbtLdifTypes.StringList | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF validation rules type."""

        # Error handling configuration
        type ErrorHandling = Mapping[
            str,
            str | bool | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF error handling type."""

        # Parsed data structure
        type ParsedData = Mapping[
            str,
            Sequence[Mapping[str, FlextTypes.JsonValue]],
        ]
        """LDIF parsed data type."""

        # Parsing metrics
        type ParsingMetrics = Mapping[
            str,
            int | float | str | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF parsing metrics type."""

        # File processing configuration
        type FileProcessing = Mapping[
            str,
            str | int | bool | Mapping[str, FlextTypes.GeneralValueType],
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
            str | Mapping[str, FlextTypes.JsonValue],
        ]
        """DBT LDIF model definition type."""

        # LDIF model configuration
        type LdifModelConfig = Mapping[
            str,
            FlextTypes.GeneralValueType | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF model configuration type."""

        # Dimensional model
        type DimensionalModel = Mapping[
            str,
            str | Sequence[Mapping[str, FlextTypes.JsonValue]],
        ]
        """DBT dimensional model type."""

        # Fact model
        type FactModel = Mapping[
            str,
            str | Mapping[str, FlextTypes.JsonValue],
        ]
        """DBT fact model type."""

        # Staging model
        type StagingModel = Mapping[
            str,
            str | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """DBT staging model type."""

        # Model documentation
        type ModelDocumentation = Mapping[
            str,
            str | Mapping[str, FlextTypes.JsonValue],
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
            Sequence[Mapping[str, FlextTypes.JsonValue]]
            | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF processing pipeline type."""

        # Batch processing configuration
        type BatchProcessing = Mapping[
            str,
            int | str | bool | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF batch processing type."""

        # Stream processing configuration
        type StreamProcessing = Mapping[
            str,
            int | bool | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF stream processing type."""

        # Error recovery configuration
        type ErrorRecovery = Mapping[
            str,
            str
            | bool
            | FlextDbtLdifTypes.StringList
            | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF error recovery type."""

        # Quality validation configuration
        type QualityValidation = Mapping[
            str,
            bool | str | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF quality validation type."""

        # Processing metrics
        type ProcessingMetrics = Mapping[
            str,
            int | float | Mapping[str, FlextTypes.GeneralValueType],
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
            FlextTypes.GeneralValueType | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF export configuration type."""

        # Output format configuration
        type OutputFormat = Mapping[
            str,
            str | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF output format type."""

        # Data serialization configuration
        type DataSerialization = Mapping[
            str,
            str | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF data serialization type."""

        # Compression settings
        type CompressionSettings = Mapping[
            str,
            str | bool | int | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF compression settings type."""

        # Export validation configuration
        type ExportValidation = Mapping[
            str,
            bool | str | Mapping[str, FlextTypes.JsonValue],
        ]
        """LDIF export validation type."""

        # Delivery configuration
        type DeliveryConfiguration = Mapping[
            str,
            str | Mapping[str, FlextTypes.GeneralValueType],
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
        type DbtLdifProjectConfig = Mapping[str, FlextTypes.GeneralValueType]
        """DBT LDIF project configuration type."""

        type LdifAnalyticsConfig = Mapping[
            str,
            str | int | bool | FlextDbtLdifTypes.StringList,
        ]
        """LDIF analytics configuration type."""

        type LdifTransformConfig = Mapping[
            str,
            bool | str | Mapping[str, FlextTypes.GeneralValueType],
        ]
        """LDIF transformation configuration type."""

        type DbtLdifPipelineConfig = Mapping[str, FlextTypes.GeneralValueType]
        """DBT LDIF pipeline configuration type."""

    class DbtLdif:
        """DBT LDIF types namespace for cross-project access.

        Provides organized access to all DBT LDIF types for other FLEXT projects.
        Usage: Other projects can reference `t.DbtLdif.LdifData.*`, `t.DbtLdif.Project.*`, etc.
        This enables consistent namespace patterns for cross-project type access.

        Examples:
            from flext_dbt_ldif.typings import t
            record: t.DbtLdif.LdifData.LdifRecord = ...
            config: t.DbtLdif.Project.DbtLdifProjectConfig = ...

        Note: Namespace composition via inheritance - no aliases needed.
        Access parent namespaces directly through inheritance.

        """


# Alias for simplified usage
t = FlextDbtLdifTypes

# Namespace composition via class inheritance
# DbtLdif namespace provides access to nested classes through inheritance
# Access patterns:
# - t.DbtLdif.* for DBT LDIF-specific types
# - t.Project.* for project types
# - t.Core.* for core types (inherited from parent)

__all__ = [
    "FlextDbtLdifTypes",
    "t",
]
