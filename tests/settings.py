"""Runtime settings for flext-dbt-ldif tests."""

from __future__ import annotations

from flext_tests import FlextTestsSettings

from flext_dbt_ldif import FlextDbtLdifSettings


class TestsFlextDbtLdifSettings(FlextDbtLdifSettings, FlextTestsSettings):
    """DBT LDIF settings extended with the shared test namespace."""


__all__: list[str] = ["TestsFlextDbtLdifSettings"]
