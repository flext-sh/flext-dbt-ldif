"""Service base for flext-dbt-ldif tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_dbt_ldif import m
from tests.settings import TestsFlextDbtLdifSettings


class TestsFlextDbtLdifServiceBase(tests_s):
    """DBT LDIF test service base with source and test settings namespaces."""

    @classmethod
    @override
    def fetch_settings(cls) -> TestsFlextDbtLdifSettings:
        """Return the typed DBT LDIF+Tests settings singleton."""
        return settings

    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtLdifSettings)


s = TestsFlextDbtLdifServiceBase

__all__: list[str] = ["TestsFlextDbtLdifServiceBase", "s"]
