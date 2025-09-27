"""FLEXT DBT LDIF Constants - LDIF DBT transformation constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import ClassVar

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
    DBT_ALLOWED_TARGETS: ClassVar[list[str]] = ["dev", "staging", "prod"]

    # LDIF DBT Model Configuration
    DEFAULT_SCHEMA = "ldif_analytics"
    DEFAULT_OUTPUT_FORMAT = "postgresql"
    SUPPORTED_OUTPUT_FORMATS: ClassVar[list[str]] = ["postgresql", "duckdb", "parquet"]

    # File Size Limits
    MIN_FILE_SIZE_KB = 1024  # 1KB minimum
    MAX_FILE_SIZE_GB = 1024 * 1024 * 1024  # 1GB maximum

    # Performance Thresholds
    PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND = 100
    PERFORMANCE_THRESHOLD_ENTRIES_PER_SECOND_MIN = 50
    PERFORMANCE_THRESHOLD_ENTRY_TIME_MS = 100
    PERFORMANCE_THRESHOLD_MODEL_RUNTIME_SECONDS = 60
    PERFORMANCE_THRESHOLD_MODEL_COUNT_INCREMENTAL = 20
    PERFORMANCE_THRESHOLD_MODEL_RUNTIME_PARTITIONING = 300


__all__ = ["FlextDbtLdifConstants"]
