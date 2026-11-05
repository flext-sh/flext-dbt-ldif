# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_core.lazy import install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import api, d, e, h, r, td, tf, tk, tm, x

    from flext_dbt_ldif import (
        FlextDbtLdif,
        FlextDbtLdifConfig,
        FlextDbtLdifConstants,
        FlextDbtLdifConstantsBase,
        FlextDbtLdifModels,
        FlextDbtLdifProtocols,
        FlextDbtLdifServiceBase,
        FlextDbtLdifSettings,
        FlextDbtLdifTypes,
        FlextDbtLdifUtilities,
        FlextDbtLdifVersion,
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
        config,
        dbt_ldif,
        main,
        settings,
    )
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
    "FlextDbtLdif",
    "FlextDbtLdifConfig",
    "FlextDbtLdifConstants",
    "FlextDbtLdifConstantsBase",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifServiceBase",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
    "FlextDbtLdifUtilities",
    "FlextDbtLdifVersion",
    "TestsFlextDbtLdifConstants",
    "TestsFlextDbtLdifModels",
    "TestsFlextDbtLdifProtocols",
    "TestsFlextDbtLdifServiceBase",
    "TestsFlextDbtLdifSettings",
    "TestsFlextDbtLdifTypes",
    "TestsFlextDbtLdifUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "api",
    "c",
    "config",
    "d",
    "dbt_ldif",
    "e",
    "h",
    "m",
    "main",
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
    {
        "FlextDbtLdif": "flext_dbt_ldif",
        "FlextDbtLdifConfig": "flext_dbt_ldif",
        "FlextDbtLdifConstants": "flext_dbt_ldif",
        "FlextDbtLdifConstantsBase": "flext_dbt_ldif",
        "FlextDbtLdifModels": "flext_dbt_ldif",
        "FlextDbtLdifProtocols": "flext_dbt_ldif",
        "FlextDbtLdifServiceBase": "flext_dbt_ldif",
        "FlextDbtLdifSettings": "flext_dbt_ldif",
        "FlextDbtLdifTypes": "flext_dbt_ldif",
        "FlextDbtLdifUtilities": "flext_dbt_ldif",
        "FlextDbtLdifVersion": "flext_dbt_ldif",
        "TestsFlextDbtLdifConstants": ".constants",
        "TestsFlextDbtLdifModels": ".models",
        "TestsFlextDbtLdifProtocols": ".protocols",
        "TestsFlextDbtLdifServiceBase": ".base",
        "TestsFlextDbtLdifSettings": ".settings",
        "TestsFlextDbtLdifTypes": ".typings",
        "TestsFlextDbtLdifUtilities": ".utilities",
        "__author__": "flext_dbt_ldif",
        "__author_email__": "flext_dbt_ldif",
        "__description__": "flext_dbt_ldif",
        "__license__": "flext_dbt_ldif",
        "__title__": "flext_dbt_ldif",
        "__url__": "flext_dbt_ldif",
        "__version__": "flext_dbt_ldif",
        "__version_info__": "flext_dbt_ldif",
        "api": "flext_tests",
        "c": ".constants",
        "config": "flext_dbt_ldif",
        "d": "flext_tests",
        "dbt_ldif": "flext_dbt_ldif",
        "e": "flext_tests",
        "h": "flext_tests",
        "m": ".models",
        "main": "flext_dbt_ldif",
        "p": ".protocols",
        "pytest_runtest_setup": ".conftest",
        "pytest_runtest_teardown": ".conftest",
        "r": "flext_tests",
        "s": ".base",
        "set_test_environment": ".conftest",
        "settings": "flext_dbt_ldif",
        "t": ".typings",
        "td": "flext_tests",
        "tf": "flext_tests",
        "tk": "flext_tests",
        "tm": "flext_tests",
        "u": ".utilities",
        "x": "flext_tests",
    },
    public_exports=__all__,
)
