"""Test protocol definitions for flext-dbt-ldif.

Provides TestsFlextDbtLdifProtocols, combining p with
FlextDbtLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import p

from flext_dbt_ldif import FlextDbtLdifProtocols


class TestsFlextDbtLdifProtocols(p, FlextDbtLdifProtocols):
    """Test protocols combining p and FlextDbtLdifProtocols.

    Provides access to:
    - p.Tests.* (from p)
    - p.DbtLdif.* (from FlextDbtLdifProtocols)
    - p.DbtLdif.Tests.* (project test protocols)
    """

    class DbtLdif(FlextDbtLdifProtocols.DbtLdif):
        """DbtLdif test protocols namespace."""

        class Tests:
            """Project-specific test protocols."""


__all__ = ["TestsFlextDbtLdifProtocols", "p"]

p = TestsFlextDbtLdifProtocols
