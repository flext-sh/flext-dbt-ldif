# AUTO-GENERATED FILE — Regenerate with: make gen
"""Flext Dbt Ldif package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import (
    build_lazy_import_map,
    install_lazy_exports,
    merge_lazy_imports,
)

if _t.TYPE_CHECKING:
    from flext_dbt_ldif.__version__ import (
        __author__,
        __author_email__,
        __description__,
        __license__,
        __title__,
        __url__,
        __version__,
        __version_info__,
    )
    from flext_dbt_ldif.api import FlextDbtLdif, dbt_ldif
    from flext_dbt_ldif.constants import FlextDbtLdifConstants, c
    from flext_dbt_ldif.models import FlextDbtLdifModels, m
    from flext_dbt_ldif.protocols import FlextDbtLdifProtocols, p
    from flext_dbt_ldif.services.client import FlextDbtLdifClient
    from flext_dbt_ldif.services.core import FlextDbtLdifCore
    from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
    from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService
    from flext_dbt_ldif.settings import FlextDbtLdifSettings
    from flext_dbt_ldif.typings import FlextDbtLdifTypes, t
    from flext_dbt_ldif.utilities import FlextDbtLdifUtilities, u
    from flext_meltano import d, e, h, r, s, x
_LAZY_IMPORTS = merge_lazy_imports(
    (".services",),
    build_lazy_import_map(
        {
            ".__version__": (
                "__author__",
                "__author_email__",
                "__description__",
                "__license__",
                "__title__",
                "__url__",
                "__version__",
                "__version_info__",
            ),
            ".api": (
                "FlextDbtLdif",
                "dbt_ldif",
            ),
            ".constants": (
                "FlextDbtLdifConstants",
                "c",
            ),
            ".models": (
                "FlextDbtLdifModels",
                "m",
            ),
            ".protocols": (
                "FlextDbtLdifProtocols",
                "p",
            ),
            ".services.client": ("FlextDbtLdifClient",),
            ".services.core": ("FlextDbtLdifCore",),
            ".services.service": ("FlextDbtLdifServiceMixin",),
            ".services.unified_service": ("FlextDbtLdifUnifiedService",),
            ".settings": ("FlextDbtLdifSettings",),
            ".typings": (
                "FlextDbtLdifTypes",
                "t",
            ),
            ".utilities": (
                "FlextDbtLdifUtilities",
                "u",
            ),
            "flext_meltano": (
                "d",
                "e",
                "h",
                "r",
                "s",
                "x",
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
        "pytest_addoption",
        "pytest_collect_file",
        "pytest_collection_modifyitems",
        "pytest_configure",
        "pytest_runtest_setup",
        "pytest_runtest_teardown",
        "pytest_sessionfinish",
        "pytest_sessionstart",
        "pytest_terminal_summary",
        "pytest_warning_recorded",
    ),
    module_name=__name__,
)


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)

__all__: list[str] = [
    "FlextDbtLdif",
    "FlextDbtLdifClient",
    "FlextDbtLdifConstants",
    "FlextDbtLdifCore",
    "FlextDbtLdifModels",
    "FlextDbtLdifProtocols",
    "FlextDbtLdifServiceMixin",
    "FlextDbtLdifSettings",
    "FlextDbtLdifTypes",
    "FlextDbtLdifUnifiedService",
    "FlextDbtLdifUtilities",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
    "c",
    "d",
    "dbt_ldif",
    "e",
    "h",
    "m",
    "p",
    "r",
    "s",
    "t",
    "u",
    "x",
]
