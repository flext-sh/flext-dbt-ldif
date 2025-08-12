"""Unit tests for version module.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

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
        if len(parts) < 3:
            raise AssertionError(f"Expected at least 3 parts, got {len(parts)}")
        if not all(part.isdigit() for part in parts[:3]):
            non_digits = [part for part in parts[:3] if not part.isdigit()]
            raise AssertionError(
                f"Expected all parts to be digits, found non-digits: {non_digits}"
            )

    def test_version_not_empty(self) -> None:
        """Test that __version__ is not empty."""
        assert __version__.strip() != ""
