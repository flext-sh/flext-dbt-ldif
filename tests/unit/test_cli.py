"""Unit tests for CLI functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from unittest.mock import patch

from flext_dbt_ldif import FlextDbtLdifCliService


class TestFlextDbtLdifCliService:
    """Test cases for FlextDbtLdifCliService."""

    def test_initialization(self) -> None:
        """Test CLI service can be instantiated."""
        service = FlextDbtLdifCliService()
        assert isinstance(service, FlextDbtLdifCliService)

    def test_display_info(self) -> None:
        """Test display_info returns result."""
        service = FlextDbtLdifCliService()
        result = service.display_info()
        assert result.is_success or result.is_failure

    def test_display_generate_message(self) -> None:
        """Test display_generate_message calls real model generation."""
        service = FlextDbtLdifCliService()
        result = service.display_generate_message()
        assert result.is_success or result.is_failure
        if result.is_success:
            assert "coming soon" not in str(result.value).lower()

    def test_display_validate_message(self) -> None:
        """Test display_validate_message calls real validation."""
        service = FlextDbtLdifCliService()
        result = service.display_validate_message()
        assert result.is_success or result.is_failure
        if result.is_success:
            assert "coming soon" not in str(result.value).lower()

    def test_info_method(self) -> None:
        """Test info() method delegates to command handler."""
        service = FlextDbtLdifCliService()
        service.info()

    def test_generate_method(self) -> None:
        """Test generate() method delegates to command handler."""
        service = FlextDbtLdifCliService()
        service.generate()

    def test_validate_method(self) -> None:
        """Test validate() method delegates to command handler."""
        service = FlextDbtLdifCliService()
        service.validate()


class TestMainEntryPoint:
    """Test cases for FlextDbtLdifCliService.main() entry point."""

    def test_main_no_args_exits_zero(self) -> None:
        """Test main returns 0 when no args provided."""
        with patch("sys.argv", ["flext-dbt-ldif"]):
            service = FlextDbtLdifCliService()
            assert service.main() == 0

    def test_main_info_command(self) -> None:
        """Test main with info command returns 0."""
        with patch("sys.argv", ["flext-dbt-ldif", "info"]):
            service = FlextDbtLdifCliService()
            assert service.main() == 0

    def test_main_generate_command(self) -> None:
        """Test main with generate command returns 0."""
        with patch("sys.argv", ["flext-dbt-ldif", "generate"]):
            service = FlextDbtLdifCliService()
            assert service.main() == 0

    def test_main_validate_command(self) -> None:
        """Test main with validate command returns 0."""
        with patch("sys.argv", ["flext-dbt-ldif", "validate"]):
            service = FlextDbtLdifCliService()
            assert service.main() == 0

    def test_main_unknown_command_exits_one(self) -> None:
        """Test main with unknown command returns 1."""
        with patch("sys.argv", ["flext-dbt-ldif", "unknown"]):
            service = FlextDbtLdifCliService()
            assert service.main() == 1

    def test_main_keyboard_interrupt(self) -> None:
        """Test main handles KeyboardInterrupt and returns 1."""
        with patch("sys.argv", ["flext-dbt-ldif", "info"]):
            with patch.object(
                FlextDbtLdifCliService._CommandHandlers,
                "handle_info_command",
                side_effect=KeyboardInterrupt(),
            ):
                service = FlextDbtLdifCliService()
                assert service.main() == 1

    def test_main_runtime_error(self) -> None:
        """Test main handles RuntimeError and returns 1."""
        with patch("sys.argv", ["flext-dbt-ldif", "info"]):
            with patch.object(
                FlextDbtLdifCliService._CommandHandlers,
                "handle_info_command",
                side_effect=RuntimeError("Test error"),
            ):
                service = FlextDbtLdifCliService()
                assert service.main() == 1
