"""FLEXT DBT LDIF - Version information with Flext patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from importlib.metadata import metadata

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


# Simplified version class for backward compatibility
class FlextDbtLdifVersion:
    """Version information for flext-dbt-ldif package."""

    @property
    def version(self) -> str:
        """Get version string."""
        return __version__

    @property
    def version_info(self) -> tuple[int | str, ...]:
        """Get version info tuple."""
        return __version_info__

    @property
    def version_tuple(self) -> tuple[int | str, ...]:
        """Alias for version_info."""
        return __version_info__

    @property
    def author(self) -> str:
        """Get primary author."""
        return __author__

    @property
    def author_email(self) -> str:
        """Get primary author email."""
        return __author_email__

    @property
    def description(self) -> str:
        """Get package description."""
        return __description__

    @property
    def license(self) -> str:
        """Get package license."""
        return __license__

    @property
    def url(self) -> str:
        """Get package URL."""
        return __url__

    @property
    def name(self) -> str:
        """Get package name."""
        return __title__


# Global version instance
VERSION = FlextDbtLdifVersion()

__all__ = [
    "VERSION",
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
