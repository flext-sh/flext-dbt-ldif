# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_tests import td, tf, tk, tm, tv

    from flext_dbt_ldif import d, e, h, r, s, x
    from tests.constants import TestsFlextDbtLdifConstants, c
    from tests.models import TestsFlextDbtLdifModels, m
    from tests.protocols import TestsFlextDbtLdifProtocols, p
    from tests.typings import TestsFlextDbtLdifTypes, t
    from tests.utilities import TestsFlextDbtLdifUtilities, u
_LAZY_IMPORTS = merge_lazy_imports(
    (".unit",),
    build_lazy_import_map(
        {
            ".constants": (
                "TestsFlextDbtLdifConstants",
                "c",
            ),
            ".models": (
                "TestsFlextDbtLdifModels",
                "m",
            ),
            ".protocols": (
                "TestsFlextDbtLdifProtocols",
                "p",
            ),
            ".typings": (
                "TestsFlextDbtLdifTypes",
                "t",
            ),
            ".utilities": (
                "TestsFlextDbtLdifUtilities",
                "u",
            ),
            "flext_dbt_ldif": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
            ),
            "flext_tests": (
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
        },
    ),
    exclude_names=(
        "cleanup_submodule_namespace",
        "install_lazy_exports",
        "lazy_getattr",
        "logger",
        "merge_lazy_imports",
        "output",
        "output_reporting",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__ = [
    "TestsFlextDbtLdifConstants",
    "TestsFlextDbtLdifModels",
    "TestsFlextDbtLdifProtocols",
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
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "x",
]
