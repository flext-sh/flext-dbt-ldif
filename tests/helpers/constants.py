"""Test constants for flext-dbt-ldif tests.

Centralized constants for test fixtures, factories, and test data.
Does NOT duplicate src/flext_dbt_ldif/constants.py - only test-specific constants.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_dbt_ldif.constants import FlextDbtLdifConstants


class TestsConstants(FlextDbtLdifConstants):
    """Centralized test constants following flext-core nested class pattern."""

    class Paths:
        """Test path constants."""

        TEST_INPUT_DIR: Final[str] = "tests/fixtures/data/input"
        TEST_OUTPUT_DIR: Final[str] = "tests/fixtures/data/output"
        TEST_TEMP_PREFIX: Final[str] = "flext_dbt_ldif_test_"
        TEST_PROFILES_DIR: Final[str] = "tests/fixtures/profiles"
        TEST_LDIF_FILE: Final[str] = "tests/fixtures/data/sample.ldif"

    class Dbt:
        """DBT test constants."""

        TEST_TARGET: Final[str] = "dev"
        TEST_PROFILE: Final[str] = "test_profile"
        TEST_PROJECT_DIR: Final[str] = "tests/fixtures/dbt_project"
        TEST_MODEL_NAME: Final[str] = "test_model"
        TEST_SCHEMA: Final[str] = "ldif_analytics"

    class Ldif:
        """LDIF test constants."""

        TEST_BASE_DN: Final[str] = "dc=test,dc=com"
        TEST_ENTRY_DN: Final[str] = "cn=test,dc=test,dc=com"
        TEST_ATTRIBUTE: Final[str] = "cn"
        TEST_ATTRIBUTE_VALUE: Final[str] = "test_value"

    class Transformation:
        """Transformation test constants."""

        TEST_SCHEMA_MAPPING: Final[dict[str, str]] = {
            "persons": "stg_persons",
            "groups": "stg_groups",
        }
        TEST_BATCH_SIZE: Final[int] = 1000
        TEST_OUTPUT_FORMAT: Final[str] = "postgresql"


# Standardized short name for use in tests
c = TestsConstants
__all__ = ["TestsConstants", "c"]
