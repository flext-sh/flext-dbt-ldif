"""Module skeleton for TestsFlextDbtLdifTypes.

Test type aliases for flextdbtldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsTypes

from flext_dbt_ldif import FlextDbtLdifTypes


class TestsFlextDbtLdifTypes(FlextTestsTypes, FlextDbtLdifTypes):
    """Test type aliases for flextdbtldif."""


t = TestsFlextDbtLdifTypes

__all__ = [
    "TestsFlextDbtLdifTypes",
    "t",
]
