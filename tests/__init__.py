# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports, merge_lazy_imports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
    from tests import conftest, constants, models, protocols, typings, unit, utilities
    from tests.constants import (
        TestsFlextDbtLdifConstants,
        TestsFlextDbtLdifConstants as c,
    )
    from tests.models import TestsFlextDbtLdifModels, TestsFlextDbtLdifModels as m
    from tests.protocols import (
        TestsFlextDbtLdifProtocols,
        TestsFlextDbtLdifProtocols as p,
    )
    from tests.typings import TestsFlextDbtLdifTypes, TestsFlextDbtLdifTypes as t
    from tests.utilities import (
        TestsFlextDbtLdifUtilities,
        TestsFlextDbtLdifUtilities as u,
    )
_LAZY_IMPORTS = merge_lazy_imports(
    ("tests.unit",),
    {
        "TestsFlextDbtLdifConstants": ("tests.constants", "TestsFlextDbtLdifConstants"),
        "TestsFlextDbtLdifModels": ("tests.models", "TestsFlextDbtLdifModels"),
        "TestsFlextDbtLdifProtocols": ("tests.protocols", "TestsFlextDbtLdifProtocols"),
        "TestsFlextDbtLdifTypes": ("tests.typings", "TestsFlextDbtLdifTypes"),
        "TestsFlextDbtLdifUtilities": ("tests.utilities", "TestsFlextDbtLdifUtilities"),
        "c": ("tests.constants", "TestsFlextDbtLdifConstants"),
        "conftest": "tests.conftest",
        "constants": "tests.constants",
        "d": ("flext_core.decorators", "FlextDecorators"),
        "e": ("flext_core.exceptions", "FlextExceptions"),
        "h": ("flext_core.handlers", "FlextHandlers"),
        "m": ("tests.models", "TestsFlextDbtLdifModels"),
        "models": "tests.models",
        "p": ("tests.protocols", "TestsFlextDbtLdifProtocols"),
        "protocols": "tests.protocols",
        "r": ("flext_core.result", "FlextResult"),
        "s": ("flext_core.service", "FlextService"),
        "t": ("tests.typings", "TestsFlextDbtLdifTypes"),
        "typings": "tests.typings",
        "u": ("tests.utilities", "TestsFlextDbtLdifUtilities"),
        "unit": "tests.unit",
        "utilities": "tests.utilities",
        "x": ("flext_core.mixins", "FlextMixins"),
    },
)
_ = _LAZY_IMPORTS.pop("cleanup_submodule_namespace", None)
_ = _LAZY_IMPORTS.pop("install_lazy_exports", None)
_ = _LAZY_IMPORTS.pop("lazy_getattr", None)
_ = _LAZY_IMPORTS.pop("logger", None)
_ = _LAZY_IMPORTS.pop("merge_lazy_imports", None)
_ = _LAZY_IMPORTS.pop("output", None)
_ = _LAZY_IMPORTS.pop("output_reporting", None)

__all__ = [
    "TestsFlextDbtLdifConstants",
    "TestsFlextDbtLdifModels",
    "TestsFlextDbtLdifProtocols",
    "TestsFlextDbtLdifTypes",
    "TestsFlextDbtLdifUtilities",
    "c",
    "conftest",
    "constants",
    "d",
    "e",
    "h",
    "m",
    "models",
    "p",
    "protocols",
    "r",
    "s",
    "t",
    "typings",
    "u",
    "unit",
    "utilities",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
