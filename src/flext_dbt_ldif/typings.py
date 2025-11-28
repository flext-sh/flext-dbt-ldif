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
        """LDIF data complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        LdifRecord: type = dict[
            str,
            str | list[str] | bytes | dict[str, FlextTypes.JsonValue],
        ]
        """LDIF record type."""
        LdifEntry: type = dict[str, FlextTypes.JsonValue | list[str]]
        """LDIF entry type."""
        LdifChangeRecord: type = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        """LDIF change record type."""
        LdifAttributes: type = dict[str, str | list[str] | bytes]
        """LDIF attributes type."""
        LdifModification: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """LDIF modification type."""
        LdifOperation: type = dict[str, str | dict[str, object]]
        """LDIF operation type."""

    # =========================================================================
    # DBT LDIF TRANSFORMATION TYPES - LDIF to analytical data transformation
    # =========================================================================

    class DbtLdifTransformation:
        """DBT LDIF transformation complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        TransformationConfig: type = dict[str, FlextTypes.JsonValue | dict[str, object]]
        """DBT LDIF transformation configuration type."""
        LdifToTableMapping: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """LDIF to table mapping type."""
        AttributeMapping: type = dict[str, str | list[str] | dict[str, object]]
        """Attribute mapping type."""
        DataNormalization: type = dict[
            str, str | bool | dict[str, FlextTypes.JsonValue]
        ]
        """Data normalization type."""
        SchemaGeneration: type = dict[str, str | list[dict[str, object]]]
        """Schema generation type."""
        OutputConfiguration: type = dict[str, object | dict[str, object]]
        """Output configuration type."""

    # =========================================================================
    # LDIF PARSING TYPES - LDIF file parsing and validation types
    # =========================================================================

    class LdifParsing:
        """LDIF parsing complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ParserConfiguration: type = dict[str, bool | str | int | dict[str, object]]
        """LDIF parser configuration type."""
        ValidationRules: type = dict[
            str,
            bool | list[str] | dict[str, FlextTypes.JsonValue],
        ]
        """LDIF validation rules type."""
        ErrorHandling: type = dict[str, str | bool | dict[str, object]]
        """LDIF error handling type."""
        ParsedData: type = dict[str, list[dict[str, FlextTypes.JsonValue]]]
        """LDIF parsed data type."""
        ParsingMetrics: type = dict[str, int | float | str | dict[str, object]]
        """LDIF parsing metrics type."""
        FileProcessing: type = dict[str, str | int | bool | dict[str, object]]
        """LDIF file processing type."""

    # =========================================================================
    # DBT MODEL TYPES - DBT model generation for LDIF data
    # =========================================================================

    class DbtLdifModel:
        """DBT LDIF model complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ModelDefinition: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT LDIF model definition type."""
        LdifModelConfig: type = dict[str, object | dict[str, object]]
        """LDIF model configuration type."""
        DimensionalModel: type = dict[str, str | list[dict[str, FlextTypes.JsonValue]]]
        """DBT dimensional model type."""
        FactModel: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT fact model type."""
        StagingModel: type = dict[str, str | dict[str, object]]
        """DBT staging model type."""
        ModelDocumentation: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """DBT model documentation type."""

    # =========================================================================
    # LDIF PROCESSING TYPES - File processing and pipeline types
    # =========================================================================

    class LdifProcessing:
        """LDIF processing complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ProcessingPipeline: type = dict[
            str, list[dict[str, FlextTypes.JsonValue]] | dict[str, object]
        ]
        """LDIF processing pipeline type."""
        BatchProcessing: type = dict[str, int | str | bool | dict[str, object]]
        """LDIF batch processing type."""
        StreamProcessing: type = dict[str, int | bool | dict[str, FlextTypes.JsonValue]]
        """LDIF stream processing type."""
        ErrorRecovery: type = dict[str, str | bool | list[str] | dict[str, object]]
        """LDIF error recovery type."""
        QualityValidation: type = dict[
            str, bool | str | dict[str, FlextTypes.JsonValue]
        ]
        """LDIF quality validation type."""
        ProcessingMetrics: type = dict[str, int | float | dict[str, object]]
        """LDIF processing metrics type."""

    # =========================================================================
    # LDIF EXPORT TYPES - Data export and output types
    # =========================================================================

    class LdifExport:
        """LDIF export complex types.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        ExportConfiguration: type = dict[str, object | dict[str, object]]
        """LDIF export configuration type."""
        OutputFormat: type = dict[str, str | dict[str, FlextTypes.JsonValue]]
        """LDIF output format type."""
        DataSerialization: type = dict[str, str | dict[str, object]]
        """LDIF data serialization type."""
        CompressionSettings: type = dict[str, str | bool | int | dict[str, object]]
        """LDIF compression settings type."""
        ExportValidation: type = dict[str, bool | str | dict[str, FlextTypes.JsonValue]]
        """LDIF export validation type."""
        DeliveryConfiguration: type = dict[str, str | dict[str, object]]
        """LDIF delivery configuration type."""

    # =========================================================================
    # DBT LDIF PROJECT TYPES - Domain-specific project types extending FlextTypes
    # =========================================================================

    class Project(FlextTypes):
        """DBT LDIF-specific project types extending FlextTypes.

        Adds DBT LDIF analytics-specific project types while inheriting
        generic types from FlextTypes. Follows domain separation principle:
        DBT LDIF domain owns LDIF analytics and transformation-specific types.
        """

        # DBT LDIF-specific project types extending the generic ones
        # Python 3.13+ best practice: Use TypeAlias for better type checking
        ProjectType: type = Literal[
            # Generic types inherited from FlextTypes
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
        DbtLdifProjectConfig: type = dict[str, object]
        """DBT LDIF project configuration type."""
        LdifAnalyticsConfig: type = dict[str, str | int | bool | list[str]]
        """LDIF analytics configuration type."""
        LdifTransformConfig: type = dict[str, bool | str | dict[str, object]]
        """LDIF transformation configuration type."""
        DbtLdifPipelineConfig: type = dict[str, object]
        """DBT LDIF pipeline configuration type."""


# =============================================================================
# PUBLIC API EXPORTS - DBT LDIF TypeVars and types
# =============================================================================

__all__: list[str] = [
    "FlextDbtLdifTypes",
]
