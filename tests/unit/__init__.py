# AUTO-GENERATED FILE — Regenerate with: make gen
"""Tests.unit package."""

from __future__ import annotations

from typing import TYPE_CHECKING

from types import MappingProxyType

from flext_core.lazy import build_lazy_import_map, install_lazy_exports

if TYPE_CHECKING:
    from . import _services_parts as _services_parts
    from flext_tests import c, d, e, h, m, p, r, s, t, td, tf, tk, tm, tv, u, x

    from ._services_parts.data_quality import TestsFlextDbtLdifServicesDataQuality
    from .test_api_surface import TestsFlextDbtLdifApiSurface
    from .test_cli import TestsFlextDbtLdifCli
    from .test_connection_profile import (
        test_connection_profile_returns_typed_ldif_wire_shape,
    )
    from .test_core import TestsFlextDbtLdifCore
    from .test_dbt_client import TestsFlextDbtLdifClient
    from .test_dbt_models import TestsFlextDbtLdifDbtModels
    from .test_services import TestsFlextDbtLdifServices
    from .test_services_and_api import TestsFlextDbtLdifServicesAndApi
    from .test_version import TestsFlextDbtLdifVersion
__all__: tuple[str, ...] = (
    "TestsFlextDbtLdifApiSurface",
    "TestsFlextDbtLdifCli",
    "TestsFlextDbtLdifClient",
    "TestsFlextDbtLdifCore",
    "TestsFlextDbtLdifDbtModels",
    "TestsFlextDbtLdifServices",
    "TestsFlextDbtLdifServicesAndApi",
    "TestsFlextDbtLdifServicesDataQuality",
    "TestsFlextDbtLdifVersion",
    "_services_parts",
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
    "test_connection_profile_returns_typed_ldif_wire_shape",
    "tf",
    "tk",
    "tm",
    "tv",
    "u",
    "x",
)

_LAZY_IMPORTS = MappingProxyType(
    build_lazy_import_map(
        MappingProxyType({
            "._services_parts": ("_services_parts",),
            "._services_parts.data_quality": ("TestsFlextDbtLdifServicesDataQuality",),
            ".test_api_surface": ("TestsFlextDbtLdifApiSurface",),
            ".test_cli": ("TestsFlextDbtLdifCli",),
            ".test_connection_profile": (
                "test_connection_profile_returns_typed_ldif_wire_shape",
            ),
            ".test_core": ("TestsFlextDbtLdifCore",),
            ".test_dbt_client": ("TestsFlextDbtLdifClient",),
            ".test_dbt_models": ("TestsFlextDbtLdifDbtModels",),
            ".test_services": ("TestsFlextDbtLdifServices",),
            ".test_services_and_api": ("TestsFlextDbtLdifServicesAndApi",),
            ".test_version": ("TestsFlextDbtLdifVersion",),
            "flext_tests": (
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
            ),
        }),
        alias_groups=MappingProxyType({}),
        sort_keys=False,
    )
)

install_lazy_exports(__name__, globals(), _LAZY_IMPORTS, public_exports=__all__)
