"""Unit tests for version module."""

from __future__ import annotations

from flext_dbt_ldif.__version__ import __version__


class TestVersion:
    """Test cases for version module."""

    def test_version_is_string(self) -> None:
        """Test that __version__ is a string."""
        assert isinstance(__version__, str)

    def test_version_format(self) -> None:
        """Test that __version__ follows semantic versioning format."""
        # Basic check for semantic versioning pattern (major.minor.patch)
        parts = __version__.split(".")
        assert len(parts) >= 3
        assert all(part.isdigit() for part in parts[:3])

    def test_version_not_empty(self) -> None:
        """Test that __version__ is not empty."""
        assert __version__.strip() != ""
