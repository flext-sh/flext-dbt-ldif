# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_cli import cli
    from flext_infra import docs_main, infra, main
    from flext_ldif import ldif
    from flext_meltano import meltano
    from flext_tests import (
        active_rules,
        api,
        config,
        discover_repository_root,
        install_local_packages,
        load_infra_report,
        settings,
        split_csv,
        td,
        tf,
        tk,
        tm,
        tv,
    )
    from pydantic_core import from_json, to_json, to_jsonable_python

    from flext_core import core, d, e, h, lazy_attribute, r, x
    from flext_dbt_ldif import dbt_ldif

    from . import unit
    from .base import TestsFlextDbtLdifServiceBase, s
    from .constants import TestsFlextDbtLdifConstants, c
    from .models import TestsFlextDbtLdifModels, m
    from .protocols import TestsFlextDbtLdifProtocols, p
    from .settings import TestsFlextDbtLdifSettings
    from .typings import TestsFlextDbtLdifTypes, t
    from .utilities import TestsFlextDbtLdifUtilities, u
__all__: tuple[str, ...] = (
    "TestsFlextDbtLdifConstants",
    "TestsFlextDbtLdifModels",
    "TestsFlextDbtLdifProtocols",
    "TestsFlextDbtLdifServiceBase",
    "TestsFlextDbtLdifSettings",
    "TestsFlextDbtLdifTypes",
    "TestsFlextDbtLdifUtilities",
    "active_rules",
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "dbt_ldif",
    "discover_repository_root",
    "docs_main",
    "e",
    "from_json",
    "h",
    "infra",
    "install_local_packages",
    "lazy_attribute",
    "ldif",
    "load_infra_report",
    "m",
    "main",
    "meltano",
    "p",
    "r",
    "s",
    "settings",
    "split_csv",
    "t",
    "td",
    "tf",
    "tk",
    "tm",
    "to_json",
    "to_jsonable_python",
    "tv",
    "u",
    "unit",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            ".base": ("TestsFlextDbtLdifServiceBase", "s"),
            ".constants": ("TestsFlextDbtLdifConstants", "c"),
            ".models": ("TestsFlextDbtLdifModels", "m"),
            ".protocols": ("TestsFlextDbtLdifProtocols", "p"),
            ".settings": ("TestsFlextDbtLdifSettings",),
            ".typings": ("TestsFlextDbtLdifTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtLdifUtilities", "u"),
            "flext_cli": ("cli",),
            "flext_core": ("core", "d", "e", "h", "lazy_attribute", "r", "x"),
            "flext_dbt_ldif": ("dbt_ldif",),
            "flext_infra": ("docs_main", "infra", "main"),
            "flext_ldif": ("ldif",),
            "flext_meltano": ("meltano",),
            "flext_tests": (
                "active_rules",
                "api",
                "config",
                "discover_repository_root",
                "install_local_packages",
                "load_infra_report",
                "settings",
                "split_csv",
                "td",
                "tf",
                "tk",
                "tm",
                "tv",
            ),
            "pydantic_core": ("from_json", "to_json", "to_jsonable_python"),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
