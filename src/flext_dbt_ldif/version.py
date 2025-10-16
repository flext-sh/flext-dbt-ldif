"""FLEXT DBT LDIF - Version information with Flextpatterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any as FlextProjectMetadata, Final

from flext_core import FlextResult, FlextTypes

if TYPE_CHECKING:
    from typing import Any as FlextProjectPerson


class FlextDbtLdifVersion:
    """Version information for flext-dbt-ldif package."""

    def __init__(self, metadata: FlextProjectMetadata) -> None:
        """Initialize version from metadata.

        Args:
            metadata: Project metadata from flext-core

        """
        self.metadata = metadata

    @property
    def version(self) -> str:
        """Get version string."""
        return self.metadata.version

    @property
    def version_info(self) -> tuple[int | str, ...]:
        """Get version info tuple."""
        return self.metadata.version_info

    @property
    def version_tuple(self) -> tuple[int | str, ...]:
        """Alias for version_info."""
        return self.version_info

    @property
    def author(self) -> FlextProjectPerson | None:
        """Get primary author."""
        return self.metadata.authors[0] if self.metadata.authors else None

    @property
    def maintainer(self) -> FlextProjectPerson | None:
        """Get primary maintainer."""
        return self.metadata.maintainers[0] if self.metadata.maintainers else None

    @property
    def author_name(self) -> str | None:
        """Get author name."""
        return self.author.name if self.author else None

    @property
    def maintainer_name(self) -> str | None:
        """Get maintainer name."""
        return self.maintainer.name if self.maintainer else None

    @property
    def authors(self) -> list[FlextProjectPerson]:
        """Get all authors."""
        return self.metadata.authors

    @property
    def maintainers(self) -> list[FlextProjectPerson]:
        """Get all maintainers."""
        return self.metadata.maintainers

    @property
    def urls(self) -> FlextTypes.Mapping:
        """Get project URLs."""
        return self.metadata.urls


def _create_version() -> FlextResult[FlextDbtLdifVersion]:
    """Create version instance from package metadata.

    Returns:
        FlextResult[FlextDbtLdifVersion]: Version instance or error

    """
    try:
        metadata_result = FlextProjectMetadata.from_package("flext-dbt-ldif")
        if metadata_result.is_failure:
            return FlextResult[FlextDbtLdifVersion].fail(
                f"Failed to load metadata: {metadata_result.error}"
            )

        version = FlextDbtLdifVersion(metadata_result.unwrap())
        return FlextResult[FlextDbtLdifVersion].ok(version)

    except Exception as e:
        return FlextResult[FlextDbtLdifVersion].fail(f"Version creation failed: {e}")


# Global version instance
_version_result = _create_version()
if _version_result.is_failure:
    error_msg = f"Failed to initialize version: {_version_result.error}"
    raise RuntimeError(error_msg)

VERSION: Final[FlextDbtLdifVersion] = _version_result.unwrap()

__all__ = [
    "VERSION",
    "FlextDbtLdifVersion",
]
