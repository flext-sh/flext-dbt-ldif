# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_tests import FlextTestsConstants, d, e, h, r, td, tf, tk, tm, tv, x

    from . import unit as unit
    from .base import TestsFlextDbtLdifServiceBase, TestsFlextDbtLdifServiceBase as s
    from .conftest import set_test_environment
    from .constants import TestsFlextDbtLdifConstants, TestsFlextDbtLdifConstants as c
    from .models import TestsFlextDbtLdifModels, TestsFlextDbtLdifModels as m
    from .protocols import TestsFlextDbtLdifProtocols, TestsFlextDbtLdifProtocols as p
    from .settings import TestsFlextDbtLdifSettings
    from .typings import TestsFlextDbtLdifTypes, TestsFlextDbtLdifTypes as t
    from .utilities import TestsFlextDbtLdifUtilities, TestsFlextDbtLdifUtilities as u
__all__: tuple[str, ...] = (
    "FlextTestsConstants",
    "TestsFlextDbtLdifConstants",
    "TestsFlextDbtLdifModels",
    "TestsFlextDbtLdifProtocols",
    "TestsFlextDbtLdifServiceBase",
    "TestsFlextDbtLdifSettings",
    "TestsFlextDbtLdifTypes",
    "TestsFlextDbtLdifUtilities",
    "c",
    "d",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "set_test_environment",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextDbtLdifServiceBase", "s"),
            ".conftest": ("set_test_environment",),
            ".constants": ("TestsFlextDbtLdifConstants", "c"),
            ".models": ("TestsFlextDbtLdifModels", "m"),
            ".protocols": ("TestsFlextDbtLdifProtocols", "p"),
            ".settings": ("TestsFlextDbtLdifSettings",),
            ".typings": ("TestsFlextDbtLdifTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtLdifUtilities", "u"),
            "flext_tests": (
                "FlextTestsConstants",
                "d",
                "e",
                "h",
                "r",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
                "x",
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
