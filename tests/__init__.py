# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import (
        api,
        cli,
        config,
        d,
        e,
        h,
        install_local_packages,
        main,
        r,
        settings,
        td,
        tf,
        tk,
        tm,
        x,
    )

    from flext_dbt_ldif import dbt_ldif, ldif, meltano
    from tests.base import TestsFlextDbtLdifServiceBase, s
    from tests.conftest import (
        pytest_runtest_setup,
        pytest_runtest_teardown,
        set_test_environment,
    )
    from tests.constants import TestsFlextDbtLdifConstants, c
    from tests.models import TestsFlextDbtLdifModels, m
    from tests.protocols import TestsFlextDbtLdifProtocols, p
    from tests.settings import TestsFlextDbtLdifSettings
    from tests.typings import TestsFlextDbtLdifTypes, t
    from tests.utilities import TestsFlextDbtLdifUtilities, u


__all__: tuple[str, ...] = (
    "TestsFlextDbtLdifConstants",
    "TestsFlextDbtLdifModels",
    "TestsFlextDbtLdifProtocols",
    "TestsFlextDbtLdifServiceBase",
    "TestsFlextDbtLdifSettings",
    "TestsFlextDbtLdifTypes",
    "TestsFlextDbtLdifUtilities",
    "api",
    "c",
    "cli",
    "config",
    "d",
    "dbt_ldif",
    "e",
    "h",
    "install_local_packages",
    "ldif",
    "m",
    "main",
    "meltano",
    "p",
    "pytest_runtest_setup",
    "pytest_runtest_teardown",
    "r",
    "s",
    "set_test_environment",
    "settings",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "u",
    "x",
)

install_lazy_exports(
    __name__,
    globals(),
    MappingProxyType({
        "TestsFlextDbtLdifConstants": ".constants",
        "TestsFlextDbtLdifModels": ".models",
        "TestsFlextDbtLdifProtocols": ".protocols",
        "TestsFlextDbtLdifServiceBase": ".base",
        "TestsFlextDbtLdifSettings": ".settings",
        "TestsFlextDbtLdifTypes": ".typings",
        "TestsFlextDbtLdifUtilities": ".utilities",
        "api": "flext_tests",
        "c": ".constants",
        "cli": "flext_tests",
        "config": "flext_tests",
        "d": "flext_tests",
        "dbt_ldif": "flext_dbt_ldif",
        "e": "flext_tests",
        "h": "flext_tests",
        "install_local_packages": "flext_tests",
        "ldif": "flext_dbt_ldif",
        "m": ".models",
        "main": "flext_tests",
        "meltano": "flext_dbt_ldif",
        "p": ".protocols",
        "pytest_runtest_setup": ".conftest",
        "pytest_runtest_teardown": ".conftest",
        "r": "flext_tests",
        "s": ".base",
        "set_test_environment": ".conftest",
        "settings": "flext_tests",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    }),
    public_exports=__all__,
)
