"""Version metadata tests for flext-dbt-ldif."""

from __future__ import annotations

from collections.abc import Mapping

from flext_dbt_ldif import __version__, __version_info__
from flext_dbt_ldif.version import VERSION, FlextDbtLdifVersion


def test_dunder_alignment() -> None:
    """Dunder version exports map to the canonical VERSION object."""
    assert __version__ == VERSION.version
    assert __version_info__ == VERSION.version_info


def test_metadata_payload() -> None:
    """Ensure VERSION carries the pyproject metadata."""
    assert isinstance(VERSION, FlextDbtLdifVersion)
    assert isinstance(VERSION.metadata, FlextProjectMetadata)
    assert isinstance(VERSION.urls, Mapping)
    assert VERSION.version_tuple == VERSION.version_info


def test_contact_details() -> None:
    """Primary author and maintainer information is exposed."""
    assert isinstance(VERSION.author, FlextProjectPerson)
    assert isinstance(VERSION.maintainer, FlextProjectPerson)
    assert VERSION.author_name
    assert VERSION.maintainer_name


def test_metadata_passthrough() -> None:
    """Author and maintainer collections match metadata."""
    assert VERSION.authors == VERSION.metadata.authors
    assert VERSION.maintainers == VERSION.metadata.maintainers
