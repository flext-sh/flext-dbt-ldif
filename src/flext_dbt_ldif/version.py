"""FLEXT DBT LDIF - Version information with Flext patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from importlib.metadata import metadata
from typing import Final

# Extract metadata from package
_metadata = metadata("flext-dbt-ldif")

# Version information
__version__ = _metadata["Version"]
__version_info__ = tuple(
    int(part) if part.isdigit() else part for part in __version__.split(".")
)

# Package metadata
__title__ = _metadata["Name"]
__description__ = _metadata.get("Summary", "")
__author__ = _metadata.get("Author", "")
__author_email__ = _metadata.get("Author-Email", "")
__license__ = _metadata.get("License", "")
__url__ = _metadata.get("Home-Page", "")


# Global version instance
VERSION: Final[str] = __version__
PROJECT_VERSION: Final[str] = __version__

__all__ = [
    "PROJECT_VERSION",
    "VERSION",
    "__author__",
    "__author_email__",
    "__description__",
    "__license__",
    "__title__",
    "__url__",
    "__version__",
    "__version_info__",
]
