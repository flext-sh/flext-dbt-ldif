# AUTO-GENERATED FILE — Regenerate with: make gen
"""Package version and metadata for flext-dbt-ldif.

Subclass of ``FlextVersion`` — overrides only ``_metadata``.
All derived attributes (``__version__``, ``__title__``, etc.) are
computed automatically via ``FlextVersion.__init_subclass__``.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from importlib.metadata import PackageMetadata, metadata

from flext_core import FlextVersion


class FlextDbtLdifVersion(FlextVersion):
    """flext-dbt-ldif version — MRO-derived from FlextVersion."""

    _metadata: PackageMetadata = metadata("flext-dbt-ldif")


__version__ = FlextDbtLdifVersion.__version__
__version_info__ = FlextDbtLdifVersion.__version_info__
__title__ = FlextDbtLdifVersion.__title__
__description__ = FlextDbtLdifVersion.__description__
__author__ = FlextDbtLdifVersion.__author__
__author_email__ = FlextDbtLdifVersion.__author_email__
__license__ = FlextDbtLdifVersion.__license__
__url__ = FlextDbtLdifVersion.__url__
__all__: list[str] = [
    "FlextDbtLdifVersion",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
]
