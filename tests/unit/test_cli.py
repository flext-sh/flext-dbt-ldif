"""Unit tests for CLI functionality."""

from __future__ import annotations

from unittest.mock import patch

import pytest
from click.testing import CliRunner

from flext_dbt_ldif import __version__
from flext_dbt_ldif.cli import cli, main


class TestCLI:
    """Test cases for CLI functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_help(self) -> None:
        """Test CLI help command."""
        result = self.runner.invoke(cli, ["--help"])
        if result.exit_code != 0:
            msg = f"Expected {0}, got {result.exit_code}"
            raise AssertionError(msg)
        if "FLEXT dbt LDIF" not in result.output:
            msg = f"Expected {"FLEXT dbt LDIF"} in {result.output}"
            raise AssertionError(msg)
        assert "Advanced LDAP Data Analytics" in result.output

    def test_cli_version(self) -> None:
        """Test CLI version command."""
        result = self.runner.invoke(cli, ["--version"])
        if result.exit_code != 0:
            msg = f"Expected {0}, got {result.exit_code}"
            raise AssertionError(msg)
        if __version__ not in result.output:
            msg = f"Expected {__version__} in {result.output}"
            raise AssertionError(msg)

    def test_cli_verbose_flag(self) -> None:
        """Test CLI verbose flag."""
        result = self.runner.invoke(cli, ["--verbose", "--help"])
        if result.exit_code != 0:
            msg = f"Expected {0}, got {result.exit_code}"
            raise AssertionError(msg)

    def test_info_command(self) -> None:
        """Test info command."""
        result = self.runner.invoke(cli, ["info"])
        if result.exit_code != 0:
            msg = f"Expected {0}, got {result.exit_code}"
            raise AssertionError(msg)
        if "FLEXT dbt LDIF" not in result.output:
            msg = f"Expected {"FLEXT dbt LDIF"} in {result.output}"
            raise AssertionError(msg)
        assert __version__ in result.output
        if "Programmatic dbt model generation" not in result.output:
            msg = f"Expected {"Programmatic dbt model generation"} in {result.output}"
            raise AssertionError(msg)

    def test_generate_command(self) -> None:
        """Test generate command."""
        result = self.runner.invoke(cli, ["generate"])
        if result.exit_code != 0:
            msg = f"Expected {0}, got {result.exit_code}"
            raise AssertionError(msg)
        if "Model generation functionality coming soon!" not in result.output:
            msg = f"Expected {"Model generation functionality coming soon!"} in {result.output}"
            raise AssertionError(msg)

    def test_validate_command(self) -> None:
        """Test validate command."""
        result = self.runner.invoke(cli, ["validate"])
        if result.exit_code != 0:
            msg = f"Expected {0}, got {result.exit_code}"
            raise AssertionError(msg)
        if "Model validation functionality coming soon!" not in result.output:
            msg = f"Expected {"Model validation functionality coming soon!"} in {result.output}"
            raise AssertionError(msg)

    def test_main_keyboard_interrupt(self) -> None:
        """Test main function with KeyboardInterrupt."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.side_effect = KeyboardInterrupt()

            with pytest.raises(SystemExit) as exc_info:
                main()

            if exc_info.value.code != 1:

                msg = f"Expected {1}, got {exc_info.value.code}"
                raise AssertionError(msg)

    def test_main_runtime_error(self) -> None:
        """Test main function with RuntimeError."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.side_effect = RuntimeError("Test error")

            with pytest.raises(SystemExit) as exc_info:
                main()

            if exc_info.value.code != 1:

                msg = f"Expected {1}, got {exc_info.value.code}"
                raise AssertionError(msg)

    def test_main_success(self) -> None:
        """Test main function successful execution."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.return_value = None

            with pytest.raises(SystemExit) as exc_info:
                main()

            if exc_info.value.code != 0:

                msg = f"Expected {0}, got {exc_info.value.code}"
                raise AssertionError(msg)
