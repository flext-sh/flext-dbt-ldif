"""FLEXT DBT LDIF Constants - LDIF DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from enum import StrEnum
from typing import ClassVar, Literal

from flext_core import FlextConstants


class FlextDbtLdifConstants(FlextConstants):
    """LDIF DBT transformation-specific constants following flext-core patterns."""

    # LDIF Configuration
    DEFAULT_LDIF_ENCODING = "utf-8"
    DEFAULT_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.DEFAULT_SIZE
    MAX_BATCH_SIZE = FlextConstants.Performance.BatchProcessing.MAX_ITEMS

    # DBT Configuration
    DEFAULT_DBT_PROFILES_DIR = "./profiles"
    DEFAULT_DBT_TARGET = "dev"
    DBT_ALLOWED_TARGETS: ClassVar[list[str]] = [
        "dev",
        "staging",
        "prod",
    ]

    # LDIF DBT Model Configuration
    DEFAULT_SCHEMA = "ldif_analytics"
    DEFAULT_OUTPUT_FORMAT = "postgresql"
    SUPPORTED_OUTPUT_FORMATS: ClassVar[list[str]] = [
        "postgresql",
        "duckdb",
        "parquet",
    ]

    # File Size Limits
    MIN_FILE_SIZE_KB = 1024  # 1KB minimum
    MAX_FILE_SIZE_GB = 1024 * 1024 * 1024  # 1GB maximum

    # Performance Thresholds
    # Schema Analysis Limits
    MAX_SAMPLE_VALUES = 5  # Maximum sample values to display

    # Entry Count Thresholds
    LARGE_DATASET_THRESHOLD = 1000000  # 1M entries threshold for optimizations

    class LdifOperations(StrEnum):
        """LDIF operation types."""

        ADD = "add"
        MODIFY = "modify"
        DELETE = "delete"
        REPLACE = "replace"

    class OutputFormats(StrEnum):
        """Supported output formats."""

        POSTGRESQL = "postgresql"
        DUCKDB = "duckdb"
        PARQUET = "parquet"

    class DbtTargets(StrEnum):
        """DBT target environments."""

        DEV = "dev"
        STAGING = "staging"
        PROD = "prod"

    # Size Thresholds
    LARGE_ENTRY_SIZE_BYTES = 10240  # 10KB per entry threshold

    # Performance Thresholds
    PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND = 100
    PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND_MIN = 50
    PERFORMANCE_THRESHOLD_ENTRY_TIME_MS = 100
    PERFORMANCE_THRESHOLD_MODEL_RUNTIME_SECONDS = 60
    PERFORMANCE_THRESHOLD_MODEL_COUNT_INCREMENTAL = 20
    PERFORMANCE_THRESHOLD_MODEL_RUNTIME_PARTITIONING = 300

    class Literals:
        """Type-safe string literals for DBT LDIF operations.

        Python 3.13+ best practice: Use TypeAlias for better type checking.
        """

        # DBT log level literal - matches DBT log levels
        type DbtLogLevelLiteral = Literal["debug", "info", "warn", "error", "none"]
        """DBT log level literal."""

        # DBT target literal - matches DBT_ALLOWED_TARGETS
        type DbtTargetLiteral = Literal["dev", "staging", "prod"]
        """DBT target literal."""

        # Output format literal - matches SUPPORTED_OUTPUT_FORMATS
        type OutputFormatLiteral = Literal["postgresql", "duckdb", "parquet"]
        """Output format literal."""

        # LDIF operation literal - matches LdifOperations StrEnum
        type LdifOperationLiteral = Literal["add", "modify", "delete", "replace"]
        """LDIF operation literal."""


__all__ = ["FlextDbtLdifConstants"]
