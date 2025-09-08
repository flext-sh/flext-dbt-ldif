"""Unit tests for CLI functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from unittest.mock import patch

import pytest
from click.testing import CliRunner

from flext_dbt_ldif import __version__, cli, main


class TestCLI:
    """Test cases for CLI functionality."""

    def setup_method(self) -> None:
        """Set up test fixtures."""
        self.runner = CliRunner()

    def test_cli_help(self) -> None:
        """Test CLI help command."""
        result = self.runner.invoke(cli, ["--help"])
        if result.exit_code != 0:
            raise AssertionError(f"Expected 0, got {result.exit_code}")
        if "FLEXT dbt LDIF" not in result.output:
            msg: str = "Expected 'FLEXT dbt LDIF' in output"
            raise AssertionError(msg)
        assert "Advanced LDAP Data Analytics" in result.output

    def test_cli_version(self) -> None:
        """Test CLI version command."""
        result = self.runner.invoke(cli, ["--version"])
        if result.exit_code != 0:
            raise AssertionError(f"Expected 0, got {result.exit_code}")
        if __version__ not in result.output:
            msg: str = f"Expected {__version__} in output"
            raise AssertionError(msg)

    def test_cli_verbose_flag(self) -> None:
        """Test CLI verbose flag."""
        result = self.runner.invoke(cli, ["--verbose", "--help"])
        if result.exit_code != 0:
            raise AssertionError(f"Expected 0, got {result.exit_code}")

    def test_info_command(self) -> None:
        """Test info command."""
        result = self.runner.invoke(cli, ["info"])
        if result.exit_code != 0:
            raise AssertionError(f"Expected 0, got {result.exit_code}")
        if "FLEXT dbt LDIF" not in result.output:
            msg: str = "Expected 'FLEXT dbt LDIF' in output"
            raise AssertionError(msg)
        assert __version__ in result.output
        if "Programmatic dbt model generation" not in result.output:
            msg: str = "Expected 'Programmatic dbt model generation' in output"
            raise AssertionError(msg)

    def test_generate_command(self) -> None:
        """Test generate command."""
        result = self.runner.invoke(cli, ["generate"])
        if result.exit_code != 0:
            raise AssertionError(f"Expected 0, got {result.exit_code}")
        if "Model generation functionality coming soon!" not in result.output:
            msg: str = (
                "Expected 'Model generation functionality coming soon!' in output"
            )
            raise AssertionError(msg)

    def test_validate_command(self) -> None:
        """Test validate command."""
        result = self.runner.invoke(cli, ["validate"])
        if result.exit_code != 0:
            raise AssertionError(f"Expected 0, got {result.exit_code}")
        if "Model validation functionality coming soon!" not in result.output:
            msg: str = (
                "Expected 'Model validation functionality coming soon!' in output"
            )
            raise AssertionError(msg)

    def test_main_keyboard_interrupt(self) -> None:
        """Test main function with KeyboardInterrupt."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.side_effect = KeyboardInterrupt()

            with pytest.raises(SystemExit) as exc_info:
                main()

            if exc_info.value.code != 1:
                raise AssertionError(f"Expected 1, got {exc_info.value.code}")

    def test_main_runtime_error(self) -> None:
        """Test main function with RuntimeError."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.side_effect = RuntimeError("Test error")

            with pytest.raises(SystemExit) as exc_info:
                main()

            if exc_info.value.code != 1:
                raise AssertionError(f"Expected 1, got {exc_info.value.code}")

    def test_main_success(self) -> None:
        """Test main function successful execution."""
        with patch("flext_dbt_ldif.cli.cli") as mock_cli:
            mock_cli.return_value = None

            with pytest.raises(SystemExit) as exc_info:
                main()

            if exc_info.value.code != 0:
                raise AssertionError(f"Expected 0, got {exc_info.value.code}")
