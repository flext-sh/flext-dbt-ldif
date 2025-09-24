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
    DEFAULT_BATCH_SIZE = 1000
    MAX_BATCH_SIZE = 10000

    # DBT Configuration
    DEFAULT_DBT_PROFILES_DIR = "./profiles"
    DEFAULT_DBT_TARGET = "dev"
    DBT_ALLOWED_TARGETS: ClassVar[list[str]] = ["dev", "staging", "prod"]

    # LDIF DBT Model Configuration
    DEFAULT_SCHEMA = "ldif_analytics"
    DEFAULT_OUTPUT_FORMAT = "postgresql"
    SUPPORTED_OUTPUT_FORMATS: ClassVar[list[str]] = ["postgresql", "duckdb", "parquet"]


__all__ = ["FlextDbtLdifConstants"]
