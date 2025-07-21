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
        assert result.exit_code == 0
        assert "FLEXT dbt LDIF" in result.output
        assert "Advanced LDAP Data Analytics" in result.output

    def test_cli_version(self) -> None:
        """Test CLI version command."""
        result = self.runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert __version__ in result.output

    def test_cli_verbose_flag(self) -> None:
        """Test CLI verbose flag."""
        result = self.runner.invoke(cli, ["--verbose", "--help"])
        assert result.exit_code == 0

    def test_info_command(self) -> None:
        """Test info command."""
        result = self.runner.invoke(cli, ["info"])
        assert result.exit_code == 0
        assert "FLEXT dbt LDIF" in result.output
        assert __version__ in result.output
        assert "Programmatic dbt model generation" in result.output

    def test_generate_command(self) -> None:
        """Test generate command."""
        result = self.runner.invoke(cli, ["generate"])
        assert result.exit_code == 0
        assert "Model generation functionality coming soon!" in result.output

    def test_validate_command(self) -> None:
        """Test validate command."""
        result = self.runner.invoke(cli, ["validate"])
        assert result.exit_code == 0
        assert "Model validation functionality coming soon!" in result.output

    def test_main_keyboard_interrupt(self) -> None:
        """Test main function with KeyboardInterrupt."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.side_effect = KeyboardInterrupt()

            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_runtime_error(self) -> None:
        """Test main function with RuntimeError."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.side_effect = RuntimeError("Test error")

            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 1

    def test_main_success(self) -> None:
        """Test main function successful execution."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.return_value = None

            with pytest.raises(SystemExit) as exc_info:
                main()

            assert exc_info.value.code == 0
