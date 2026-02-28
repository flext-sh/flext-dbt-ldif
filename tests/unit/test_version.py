"""Version metadata tests for flext-dbt-ldif."""

from __future__ import annotations

from flext_dbt_ldif import __version__, __version_info__
from flext_dbt_ldif.version import VERSION


def test_dunder_alignment() -> None:
    """Dunder version exports map to the canonical VERSION constant."""
    assert __version__ == VERSION
    assert __version_info__ == tuple(
        int(part) if part.isdigit() else part for part in VERSION.split(".")
    )


def test_version_is_string() -> None:
    """Ensure VERSION is a string constant."""
    assert isinstance(VERSION, str)
    assert VERSION
