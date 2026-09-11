"""Test protocol definitions for flext-dbt-ldif.

Provides TestsFlextDbtLdifProtocols, combining TestsFlextProtocols with
p for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsProtocols

from flext_dbt_ldif import p


class TestsFlextDbtLdifProtocols(FlextTestsProtocols, p):
    """Test protocols combining TestsFlextProtocols and p."""

    class DbtLdif(p.DbtLdif):
        """DbtLdif test protocols namespace."""

        class Tests:
            """Project-specific test protocols."""


p = TestsFlextDbtLdifProtocols
__all__: list[str] = ["TestsFlextDbtLdifProtocols", "p"]
