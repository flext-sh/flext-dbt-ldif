"""Unit tests for version module."""

from __future__ import annotations

from flext_dbt_ldif.__version__ import VERSION


class TestVersion:
    """Test cases for version module."""

    def test_version_is_string(self) -> None:
        """Test that VERSION is a string."""
        assert isinstance(VERSION, str)

    def test_version_format(self) -> None:
        """Test that VERSION follows semantic versioning format."""
        # Basic check for semantic versioning pattern (major.minor.patch)
        parts = VERSION.split(".")
        assert len(parts) >= 3
        assert all(part.isdigit() for part in parts[:3])

    def test_version_not_empty(self) -> None:
        """Test that VERSION is not empty."""
        assert VERSION.strip() != ""
