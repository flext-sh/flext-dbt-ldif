"""Version metadata behavioral contract for flext-dbt-ldif.

Copyright (c) 2026 FLEXT Team. All rights reserved.
tests/unit/test_version
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from flext_tests import tm
from packaging.version import Version

from flext_dbt_ldif import __version__, __version__ as version, __version_info__


class TestsFlextDbtLdifVersion:
    """Public contract of the package version metadata exports."""

    @staticmethod
    def test_version_is_non_empty_string() -> None:
        """`__version__` is exposed as a non-empty string."""
        tm.that(__version__, is_=str)
        assert __version__

    @staticmethod
    def test_version_alias_matches_canonical() -> None:
        """The `version` alias export is identical to `__version__`."""
        tm.that(version, eq=__version__)

    @staticmethod
    def test_version_info_is_release_triple() -> None:
        """`__version_info__` is exposed as a three-integer release tuple."""
        tm.that(__version_info__, is_=tuple)
        tm.that(len(__version_info__), eq=3)
        assert all(isinstance(component, int) for component in __version_info__)

    @staticmethod
    def test_version_info_derives_from_version_string() -> None:
        """`__version_info__` is the exact PEP 440 release triple."""
        tm.that(__version_info__, eq=Version(__version__).release)

    @staticmethod
    def test_version_info_leading_component_is_numeric() -> None:
        """The leading version component is a non-negative integer (major)."""
        major = __version_info__[0]
        assert isinstance(major, int)
        assert major >= 0
