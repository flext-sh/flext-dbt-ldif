"""Version metadata tests for flext-dbt-ldif."""

from __future__ import annotations

from flext_dbt_ldif import __version__, __version__ as version, __version_info__


def test_dunder_alignment() -> None:
    """Dunder version exports map to the canonical VERSION constant."""
    assert __version__ == version
    assert __version_info__ == tuple(
        int(part) if part.isdigit() else part for part in version.split(".")
    )


def test_version_is_string() -> None:
    """Ensure VERSION is a string constant."""
    assert isinstance(version, str)
    assert version
