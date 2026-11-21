"""Test models for flext-dbt-ldif.

Provides TestsFlextDbtLdifModels, combining TestsFlextModels with
m for test-specific model definitions.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsModels

from tests import FlextDbtLdifModels


class TestsFlextDbtLdifModels(FlextTestsModels, FlextDbtLdifModels):
    """Test models combining TestsFlextModels with flext-dbt-ldif models."""

    class Tests(FlextTestsModels.Tests):
        """Project-specific test models."""


m = TestsFlextDbtLdifModels

__all__: list[str] = ["TestsFlextDbtLdifModels", "m"]
