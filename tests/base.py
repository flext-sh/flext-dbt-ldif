"""Service base for flext-dbt-ldif tests."""

from __future__ import annotations

from typing import override

from flext_tests import s as tests_s

from flext_dbt_ldif import m
from tests.settings import TestsFlextDbtLdifSettings


class TestsFlextDbtLdifServiceBase(tests_s):
    """DBT LDIF test service base with source and test settings namespaces."""

    # NOTE (multi-agent, bead mro-wfc8): fetch_settings is delivered by the flext_tests
    # base via MRO (resolves TestsFlextDbtLdifSettings from _runtime_bootstrap_options).
    # The prior override returned the FlextDbtLdifSettings production singleton — a
    # type mismatch (bad-return) and a settings atravessador.
    @classmethod
    @override
    def _runtime_bootstrap_options(cls) -> m.RuntimeBootstrapOptions:
        return m.RuntimeBootstrapOptions(settings_type=TestsFlextDbtLdifSettings)


s = TestsFlextDbtLdifServiceBase

__all__: list[str] = ["TestsFlextDbtLdifServiceBase", "s"]
