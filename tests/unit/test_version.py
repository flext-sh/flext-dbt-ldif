"""Version metadata behavioral contract for flext-dbt-ldif."""

from __future__ import annotations

from flext_dbt_ldif import (
from flext_tests import tm
    __version__,
    __version__ as version,
    __version_info__,
)

__all__ = ["TestsFlextDbtLdifVersion"]


class TestsFlextDbtLdifVersion:
    """Public contract of the package version metadata exports."""

    def test_version_is_non_empty_string(self) -> None:
        """`__version__` is exposed as a non-empty string."""
        tm.that(__version__, is_=str)
        assert __version__

    def test_version_alias_matches_canonical(self) -> None:
        """The `version` alias export is identical to `__version__`."""
        tm.that(version, eq=__version__)

    def test_version_info_is_tuple(self) -> None:
        """`__version_info__` is exposed as a tuple."""
        tm.that(__version_info__, is_=tuple)
        assert __version_info__

    def test_version_info_derives_from_version_string(self) -> None:
        """`__version_info__` is the parsed component view of `__version__`."""
        expected = tuple(
            int(part) if part.isdigit() else part for part in __version__.split(".")
        )
        tm.that(__version_info__, eq=expected)

    def test_version_info_components_are_int_or_str(self) -> None:
        """Every version component is either a numeric int or a string label."""
        assert all(isinstance(component, (int, str)) for component in __version_info__)

    def test_version_string_reassembles_from_info(self) -> None:
        """Joining string forms of the components reproduces the version string."""
        tm.that(
            ".".join(str(component) for component in __version_info__), eq=__version__
        )

    def test_version_info_leading_component_is_numeric(self) -> None:
        """The leading version component is a non-negative integer (major)."""
        major = __version_info__[0]
        tm.that(major, is_=int)
        assert major >= 0
