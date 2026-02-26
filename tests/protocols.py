"""Test protocol definitions for flext-dbt-ldif.

Provides TestsFlextDbtLdifProtocols, combining FlextTestsProtocols with
FlextDbtLdifProtocols for test-specific protocol definitions.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_dbt_ldif.protocols import FlextDbtLdifProtocols
from flext_tests.protocols import FlextTestsProtocols


class TestsFlextDbtLdifProtocols(FlextTestsProtocols, FlextDbtLdifProtocols):
    """Test protocols combining FlextTestsProtocols and FlextDbtLdifProtocols.

    Provides access to:
    - p.Tests.Docker.* (from FlextTestsProtocols)
    - p.Tests.Factory.* (from FlextTestsProtocols)
    - p.DbtLdif.* (from FlextDbtLdifProtocols)
    """



# Runtime aliases
p = TestsFlextDbtLdifProtocols
p = TestsFlextDbtLdifProtocols

__all__ = ["TestsFlextDbtLdifProtocols", "p"]
