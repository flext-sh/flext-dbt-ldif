# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests package."""

from __future__ import annotations

from types import MappingProxyType
from typing import TYPE_CHECKING

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from flext_ldif import ldif, servers
    from flext_meltano import meltano
    from flext_tests import (
        api,
        cli,
        config,
        core,
        d,
        e,
        h,
        install_local_packages,
        lazy_attribute,
        load_infra_report,
        r,
        services,
        settings,
        td,
        tf,
        tk,
        tm,
        tv,
        x,
    )

    from flext_dbt_ldif import dbt_ldif, main

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
    "api",
    "c",
    "cli",
    "config",
    "core",
    "d",
    "dbt_ldif",
    "e",
    "h",
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
    "servers",
    "services",
    "settings",
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
            ".constants": ("TestsFlextDbtLdifConstants", "c"),
            ".models": ("TestsFlextDbtLdifModels", "m"),
            ".protocols": ("TestsFlextDbtLdifProtocols", "p"),
            ".settings": ("TestsFlextDbtLdifSettings",),
            ".typings": ("TestsFlextDbtLdifTypes", "t"),
            ".unit": ("unit",),
            ".utilities": ("TestsFlextDbtLdifUtilities", "u"),
            "flext_dbt_ldif": ("dbt_ldif", "main"),
            "flext_ldif": ("ldif", "servers"),
            "flext_meltano": ("meltano",),
            "flext_tests": (
                "api",
                "cli",
                "config",
                "core",
                "d",
                "e",
                "h",
                "install_local_packages",
                "lazy_attribute",
                "load_infra_report",
                "r",
                "services",
                "settings",
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
