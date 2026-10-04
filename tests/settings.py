"""Runtime settings for flext-dbt-ldif tests.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/settings
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_dbt_ldif import FlextDbtLdifSettings


class TestsFlextDbtLdifSettings(FlextDbtLdifSettings, FlextTestsSettings):
    """DBT LDIF settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtLdifSettings"]
