"""Constants for flext-dbt-ldif tests.

Provides TestsFlextDbtLdifConstants, extending FlextTestsConstants with flext-dbt-ldif-specific
constants using COMPOSITION INHERITANCE.

Inheritance hierarchy:
- FlextTestsConstants (flext_tests) - Provides .Tests.* namespace
- FlextDbtLdifConstants (production) - Provides .DbtLdif.* namespace

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final

from flext_dbt_ldif.constants import FlextDbtLdifConstants
from flext_tests.constants import FlextTestsConstants


class TestsFlextDbtLdifConstants(FlextTestsConstants, FlextDbtLdifConstants):
    """Constants for flext-dbt-ldif tests using COMPOSITION INHERITANCE.

    MANDATORY: Inherits from BOTH:
    1. FlextTestsConstants - for test infrastructure (.Tests.*)
    2. FlextDbtLdifConstants - for domain constants (.DbtLdif.*)

    Access patterns:
    - c.Tests.Docker.* (container testing)
    - c.Tests.Matcher.* (assertion messages)
    - c.Tests.Factory.* (test data generation)
    - c.DbtLdif.* (domain constants from production)
    - c.TestDbt.* (project-specific test data)

    Rules:
    - NEVER duplicate constants from FlextTestsConstants or FlextDbtLdifConstants
    - Only flext-dbt-ldif-specific test constants allowed
    - All generic constants come from FlextTestsConstants
    - All production constants come from FlextDbtLdifConstants
    """

    class Paths:
        """Test path constants."""

        TEST_INPUT_DIR: Final[str] = "tests/fixtures/data/input"
        TEST_OUTPUT_DIR: Final[str] = "tests/fixtures/data/output"
        TEST_TEMP_PREFIX: Final[str] = "flext_dbt_ldif_test_"
        TEST_PROFILES_DIR: Final[str] = "tests/fixtures/profiles"
        TEST_LDIF_FILE: Final[str] = "tests/fixtures/data/sample.ldif"

    class TestDbt:
        """DBT test constants."""

        TEST_TARGET: Final[str] = "dev"
        TEST_PROFILE: Final[str] = "test_profile"
        TEST_PROJECT_DIR: Final[str] = "tests/fixtures/dbt_project"
        TEST_MODEL_NAME: Final[str] = "test_model"
        TEST_SCHEMA: Final[str] = "ldif_analytics"

    class TestLdif:
        """LDIF test constants."""

        TEST_BASE_DN: Final[str] = "dc=test,dc=com"
        TEST_ENTRY_DN: Final[str] = "cn=test,dc=test,dc=com"
        TEST_ATTRIBUTE: Final[str] = "cn"
        TEST_ATTRIBUTE_VALUE: Final[str] = "test_value"

    class TestTransformation:
        """Transformation test constants."""

        TEST_SCHEMA_MAPPING: Final[dict[str, str]] = {
            "persons": "stg_persons",
            "groups": "stg_groups",
        }
        TEST_BATCH_SIZE: Final[int] = 1000
        TEST_OUTPUT_FORMAT: Final[str] = "postgresql"


# Short aliases per FLEXT convention
tc = TestsFlextDbtLdifConstants  # Primary test constants alias
c = TestsFlextDbtLdifConstants  # Alternative alias for compatibility

__all__ = [
    "TestsFlextDbtLdifConstants",
    "c",
    "tc",
]
