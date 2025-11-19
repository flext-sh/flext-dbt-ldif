"""Version metadata tests for flext-dbt-ldif."""

from __future__ import annotations

from flext_dbt_ldif import __version__, __version_info__
from flext_dbt_ldif.version import VERSION, FlextDbtLdifVersion


def test_dunder_alignment() -> None:
    """Dunder version exports map to the canonical VERSION object."""
    assert __version__ == VERSION.version
    assert __version_info__ == VERSION.version_info


def test_metadata_payload() -> None:
    """Ensure VERSION carries the pyproject metadata."""
    assert isinstance(VERSION, FlextDbtLdifVersion)
    assert VERSION.version
    assert VERSION.version_info
    assert VERSION.version_tuple == VERSION.version_info


def test_contact_details() -> None:
    """Primary author and maintainer information is exposed."""
    assert isinstance(VERSION.author, str)
    assert VERSION.author
    assert VERSION.author_email


def test_metadata_passthrough() -> None:
    """Author information is accessible."""
    assert VERSION.author
    assert VERSION.name
    assert VERSION.description
