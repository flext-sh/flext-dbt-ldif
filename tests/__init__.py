# AUTO-GENERATED FILE — DO NOT EDIT MANUALLY.
# Regenerate with: make gen
#
"""Tests package."""

from __future__ import annotations

import typing as _t

from flext_core.lazy import install_lazy_exports

if _t.TYPE_CHECKING:
    from flext_core.decorators import FlextDecorators as d
    from flext_core.exceptions import FlextExceptions as e
    from flext_core.handlers import FlextHandlers as h
    from flext_core.mixins import FlextMixins as x
    from flext_core.result import FlextResult as r
    from flext_core.service import FlextService as s
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
_LAZY_IMPORTS = {
    "TestsFlextDbtLdifConstants": ".constants",
    "TestsFlextDbtLdifModels": ".models",
    "TestsFlextDbtLdifProtocols": ".protocols",
    "TestsFlextDbtLdifTypes": ".typings",
    "TestsFlextDbtLdifUtilities": ".utilities",
    "c": (".constants", "TestsFlextDbtLdifConstants"),
    "d": ("flext_core.decorators", "FlextDecorators"),
    "e": ("flext_core.exceptions", "FlextExceptions"),
    "h": ("flext_core.handlers", "FlextHandlers"),
    "m": (".models", "TestsFlextDbtLdifModels"),
    "p": (".protocols", "TestsFlextDbtLdifProtocols"),
    "r": ("flext_core.result", "FlextResult"),
    "s": ("flext_core.service", "FlextService"),
    "t": (".typings", "TestsFlextDbtLdifTypes"),
    "u": (".utilities", "TestsFlextDbtLdifUtilities"),
    "x": ("flext_core.mixins", "FlextMixins"),
}

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
    "u",
    "x",
]


install_lazy_exports(__name__, globals(), _LAZY_IMPORTS)
