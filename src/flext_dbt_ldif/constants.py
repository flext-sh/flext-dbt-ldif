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

from flext_core import FlextConstants


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
    DEFAULT_BATCH_SIZE: int = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
    """Default batch size for LDIF processing."""
    MAX_BATCH_SIZE: int = FlextConstants.Performance.BatchProcessing.MAX_ITEMS
    """Maximum batch size for LDIF processing."""

    # =========================================================================
    # DBT CONFIGURATION CONSTANTS
    # =========================================================================

    # DBT profiles directory
    DEFAULT_DBT_PROFILES_DIR: str = "./profiles"
    """Default DBT profiles directory path."""

    # DBT target environment (will be set after enum definition)
    DEFAULT_DBT_TARGET: str = "dev"
    """Default DBT target environment."""

    # =========================================================================
    # LDIF DBT MODEL CONFIGURATION CONSTANTS
    # =========================================================================

    # Default schema name
    DEFAULT_SCHEMA: str = "ldif_analytics"
    """Default DBT schema name for LDIF analytics."""

    # Default output format (will be set after enum definition)
    DEFAULT_OUTPUT_FORMAT: str = "postgresql"
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
        """LDIF operation types using StrEnum for type safety."""

        ADD = "add"
        MODIFY = "modify"
        DELETE = "delete"
        REPLACE = "replace"

    class OutputFormats(StrEnum):
        """Supported output formats using StrEnum for type safety."""

        POSTGRESQL = "postgresql"
        DUCKDB = "duckdb"
        PARQUET = "parquet"

    class DbtTargets(StrEnum):
        """DBT target environments using StrEnum for type safety."""

        DEV = "dev"
        STAGING = "staging"
        PROD = "prod"

    class DbtLogLevels(StrEnum):
        """DBT log levels using StrEnum for type safety."""

        DEBUG = "debug"
        INFO = "info"
        WARN = "warn"
        ERROR = "error"
        NONE = "none"

    # =========================================================================
    # TYPE-SAFE LITERALS - PEP 695 syntax for type checking
    # =========================================================================

    class Literals:
        """Type-safe string literals for DBT LDIF operations.

        Uses Python 3.13+ PEP 695 type syntax for better type checking.
        All literals match corresponding StrEnum values for consistency.
        """

        # DBT log level literal - matches DbtLogLevels StrEnum
        type DbtLogLevelLiteral = Literal[
            "debug",
            "info",
            "warn",
            "error",
            "none",
        ]
        """DBT log level literal type."""

        # DBT target literal - matches DbtTargets StrEnum
        type DbtTargetLiteral = Literal[
            "dev",
            "staging",
            "prod",
        ]
        """DBT target literal type."""

        # Output format literal - matches OutputFormats StrEnum
        type OutputFormatLiteral = Literal[
            "postgresql",
            "duckdb",
            "parquet",
        ]
        """Output format literal type."""

        # LDIF operation literal - matches LdifOperations StrEnum
        type LdifOperationLiteral = Literal[
            "add",
            "modify",
            "delete",
            "replace",
        ]
        """LDIF operation literal type."""

    # =========================================================================
    # MAPPING CONSTANTS - Type-safe mappings for configuration
    # =========================================================================

    class Mappings:
        """Type-safe mapping constants for DBT LDIF operations.

        Uses Mapping type for read-only configuration mappings.
        """

        # DBT allowed targets mapping - using string values for compatibility
        DBT_ALLOWED_TARGETS: ClassVar[list[str]] = [
            "dev",
            "staging",
            "prod",
        ]
        """List of allowed DBT target environment names."""

        # Supported output formats mapping - using string values for compatibility
        SUPPORTED_OUTPUT_FORMATS: ClassVar[list[str]] = [
            "postgresql",
            "duckdb",
            "parquet",
        ]
        """List of supported output format names."""

        # LDIF operations mapping - using string values for compatibility
        LDIF_OPERATIONS: ClassVar[list[str]] = [
            "add",
            "modify",
            "delete",
            "replace",
        ]
        """List of LDIF operation names."""

        # DBT log levels mapping - using string values for compatibility
        DBT_LOG_LEVELS: ClassVar[list[str]] = [
            "debug",
            "info",
            "warn",
            "error",
            "none",
        ]
        """List of DBT log level names."""


# =============================================================================
# PUBLIC API EXPORTS
# =============================================================================

__all__: list[str] = [
    "FlextDbtLdifConstants",
]
