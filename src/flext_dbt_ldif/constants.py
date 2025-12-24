"""FLEXT DBT LDIF Constants - LDIF DBT transformation constants.

This module provides DBT LDIF-specific constants following flext-core patterns.
Uses Python 3.13+ PEP 695 syntax, StrEnum, Literals, and Mappings.
All constants are centralized and follow SRP principles.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import ClassVar, Literal

from flext import FlextConstants


class FlextDbtLdifConstants(FlextConstants):
    """LDIF DBT transformation-specific constants following flext-core patterns.

    Uses Python 3.13+ PEP 695 syntax for type-safe constants.
    All constants are centralized and follow SRP principles.
    """

    # =========================================================================
    # LDIF CONFIGURATION CONSTANTS
    # =========================================================================

    # LDIF file encoding
    DEFAULT_LDIF_ENCODING: str = "utf-8"
    """Default LDIF file encoding."""

    # Batch processing configuration (reusing flext-core constants)
    # Note: DEFAULT_BATCH_SIZE inherited from FlextConstants (Final, cannot override)
    MAX_BATCH_SIZE: int = FlextConstants.Performance.BatchProcessing.MAX_ITEMS
    """Maximum batch size for LDIF processing."""

    # =========================================================================
    # DBT CONFIGURATION CONSTANTS
    # =========================================================================

    # DBT profiles directory
    DEFAULT_DBT_PROFILES_DIR: str = "./profiles"
    """Default DBT profiles directory path."""

    # DBT target environment (will be set after enum definition)
    DEFAULT_DBT_TARGET: ClassVar[str]
    """Default DBT target environment."""

    # =========================================================================
    # LDIF DBT MODEL CONFIGURATION CONSTANTS
    # =========================================================================

    # Default schema name
    DEFAULT_SCHEMA: str = "ldif_analytics"
    """Default DBT schema name for LDIF analytics."""

    # Default output format (will be set after enum definition)
    DEFAULT_OUTPUT_FORMAT: ClassVar[str]
    """Default output format for DBT models."""

    # =========================================================================
    # FILE SIZE LIMITS
    # =========================================================================

    # Minimum file size (1KB)
    MIN_FILE_SIZE_KB: int = 1024
    """Minimum LDIF file size in bytes (1KB)."""

    # Maximum file size (1GB)
    MAX_FILE_SIZE_GB: int = 1024 * 1024 * 1024
    """Maximum LDIF file size in bytes (1GB)."""

    # =========================================================================
    # PERFORMANCE THRESHOLDS
    # =========================================================================

    # Schema analysis limits
    MAX_SAMPLE_VALUES: int = 5
    """Maximum sample values to display in schema analysis."""

    # Entry count thresholds
    LARGE_DATASET_THRESHOLD: int = 1000000
    """Large dataset threshold (1M entries) for optimizations."""

    # Size thresholds
    LARGE_ENTRY_SIZE_BYTES: int = 10240
    """Large entry size threshold (10KB per entry)."""

    # Performance thresholds
    PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND: int = 100
    """Performance threshold: entries per second."""
    PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND_MIN: int = 50
    """Performance threshold: minimum entries per second."""
    PERFORMANCE_THRESHOLD_ENTRY_TIME_MS: int = 100
    """Performance threshold: entry processing time in milliseconds."""
    PERFORMANCE_THRESHOLD_MODEL_RUNTIME_SECONDS: int = 60
    """Performance threshold: model runtime in seconds."""
    PERFORMANCE_THRESHOLD_MODEL_COUNT_INCREMENTAL: int = 20
    """Performance threshold: model count for incremental processing."""
    PERFORMANCE_THRESHOLD_MODEL_RUNTIME_PARTITIONING: int = 300
    """Performance threshold: model runtime for partitioning (5 minutes)."""

    # =========================================================================
    # STRING ENUMS - Type-safe string constants
    # =========================================================================

    class LdifOperations(StrEnum):
        """LDIF operation types using StrEnum for type safety.

        DRY Pattern:
            StrEnum is the single source of truth. Use LdifOperations.ADD.value
            or LdifOperations.ADD directly - no base strings needed.
        """

        ADD = "add"
        MODIFY = "modify"
        DELETE = "delete"
        REPLACE = "replace"

    class OutputFormats(StrEnum):
        """Supported output formats using StrEnum for type safety.

        DRY Pattern:
            StrEnum is the single source of truth. Use OutputFormats.POSTGRESQL.value
            or OutputFormats.POSTGRESQL directly - no base strings needed.
        """

        POSTGRESQL = "postgresql"
        DUCKDB = "duckdb"
        PARQUET = "parquet"

    class DbtTargets(StrEnum):
        """DBT target environments using StrEnum for type safety.

        DRY Pattern:
            StrEnum is the single source of truth. Use DbtTargets.DEV.value
            or DbtTargets.DEV directly - no base strings needed.
        """

        DEV = "dev"
        STAGING = "staging"
        PROD = "prod"

    class DbtLogLevels(StrEnum):
        """DBT log levels using StrEnum for type safety.

        DRY Pattern:
            StrEnum is the single source of truth. Use DbtLogLevels.DEBUG.value
            or DbtLogLevels.DEBUG directly - no base strings needed.
        """

        DEBUG = "debug"
        INFO = "info"
        WARN = "warn"
        ERROR = "error"
        NONE = "none"

    class ErrorCode(StrEnum):
        """Error codes for LDIF DBT operations.

        DRY Pattern:
            StrEnum is the single source of truth. Use ErrorCode.DBT_LDIF_ERROR.value
            or ErrorCode.DBT_LDIF_ERROR directly - no base strings needed.
        """

        # General errors
        DBT_LDIF_ERROR = "DBT_LDIF_ERROR"
        VALIDATION_ERROR = "DBT_LDIF_VALIDATION_ERROR"
        CONFIGURATION_ERROR = "DBT_LDIF_CONFIGURATION_ERROR"
        CONNECTION_ERROR = "DBT_LDIF_CONNECTION_ERROR"
        PROCESSING_ERROR = "DBT_LDIF_PROCESSING_ERROR"
        AUTHENTICATION_ERROR = "DBT_LDIF_AUTHENTICATION_ERROR"
        TIMEOUT_ERROR = "DBT_LDIF_TIMEOUT_ERROR"

        # Domain-specific errors
        PARSE_ERROR = "DBT_LDIF_PARSE_ERROR"
        MODEL_ERROR = "DBT_LDIF_MODEL_ERROR"
        TRANSFORMATION_ERROR = "DBT_LDIF_TRANSFORMATION_ERROR"
        TEST_ERROR = "DBT_LDIF_TEST_ERROR"

    # =========================================================================
    # TYPE-SAFE LITERALS - PEP 695 syntax for type checking
    # =========================================================================
    # All Literal types reference StrEnum members - NO string duplication!
    # Note: These are defined at FlextDbtLdifConstants level to reference StrEnum classes

    type DbtLogLevelLiteral = Literal[
        DbtLogLevels.DEBUG,
        DbtLogLevels.INFO,
        DbtLogLevels.WARN,
        DbtLogLevels.ERROR,
        DbtLogLevels.NONE,
    ]
    """DBT log level literal - references DbtLogLevels StrEnum members."""

    type DbtTargetLiteral = Literal[
        DbtTargets.DEV,
        DbtTargets.STAGING,
        DbtTargets.PROD,
    ]
    """DBT target literal - references DbtTargets StrEnum members."""

    type OutputFormatLiteral = Literal[
        OutputFormats.POSTGRESQL,
        OutputFormats.DUCKDB,
        OutputFormats.PARQUET,
    ]
    """Output format literal - references OutputFormats StrEnum members."""

    type LdifOperationLiteral = Literal[
        LdifOperations.ADD,
        LdifOperations.MODIFY,
        LdifOperations.DELETE,
        LdifOperations.REPLACE,
    ]
    """LDIF operation literal - references LdifOperations StrEnum members."""

    # =========================================================================
    # MAPPING CONSTANTS - Type-safe mappings for configuration
    # =========================================================================

    class Mappings:
        """Type-safe mapping constants for DBT LDIF operations.

        Uses Mapping type for read-only configuration mappings.
        Generated from StrEnum members (DRY principle) - will be set after enum definitions.
        """

        # DBT allowed targets mapping - generated from DbtTargets StrEnum
        DBT_ALLOWED_TARGETS: ClassVar[list[str]]
        """List of allowed DBT target environment names - generated from DbtTargets StrEnum."""

        # Supported output formats mapping - generated from OutputFormats StrEnum
        SUPPORTED_OUTPUT_FORMATS: ClassVar[list[str]]
        """List of supported output format names - generated from OutputFormats StrEnum."""

        # LDIF operations mapping - generated from LdifOperations StrEnum
        LDIF_OPERATIONS: ClassVar[list[str]]
        """List of LDIF operation names - generated from LdifOperations StrEnum."""

        # DBT log levels mapping - generated from DbtLogLevels StrEnum
        DBT_LOG_LEVELS: ClassVar[list[str]]
        """List of DBT log level names - generated from DbtLogLevels StrEnum."""


# Set DEFAULT_DBT_TARGET and DEFAULT_OUTPUT_FORMAT after enum definitions
FlextDbtLdifConstants.DEFAULT_DBT_TARGET = FlextDbtLdifConstants.DbtTargets.DEV
"""Default DBT target environment - references DbtTargets.DEV."""

FlextDbtLdifConstants.DEFAULT_OUTPUT_FORMAT = (
    FlextDbtLdifConstants.OutputFormats.POSTGRESQL
)
"""Default output format - references OutputFormats.POSTGRESQL."""

# Generate Mappings from StrEnum members (DRY principle)
FlextDbtLdifConstants.Mappings.DBT_ALLOWED_TARGETS = [
    member.value for member in FlextDbtLdifConstants.DbtTargets.__members__.values()
]
"""List of allowed DBT target environment names - generated from DbtTargets StrEnum."""

FlextDbtLdifConstants.Mappings.SUPPORTED_OUTPUT_FORMATS = [
    member.value for member in FlextDbtLdifConstants.OutputFormats.__members__.values()
]
"""List of supported output format names - generated from OutputFormats StrEnum."""

FlextDbtLdifConstants.Mappings.LDIF_OPERATIONS = [
    member.value for member in FlextDbtLdifConstants.LdifOperations.__members__.values()
]
"""List of LDIF operation names - generated from LdifOperations StrEnum."""

FlextDbtLdifConstants.Mappings.DBT_LOG_LEVELS = [
    member.value for member in FlextDbtLdifConstants.DbtLogLevels.__members__.values()
]
"""List of DBT log level names - generated from DbtLogLevels StrEnum."""


# =============================================================================
# PUBLIC API EXPORTS
# =============================================================================

c = FlextDbtLdifConstants

__all__: list[str] = [
    "FlextDbtLdifConstants",
    "c",
]
