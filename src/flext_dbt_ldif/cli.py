"""Command-line interface for FLEXT dbt LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import sys
from typing import NoReturn, override

from flext_cli import FlextCli, FlextCliModels
from flext_core import FlextCore

logger = FlextCore.Logger(__name__)


class FlextDbtLdifCliService:
    """FLEXT dbt LDIF CLI service using flext-cli foundation exclusively."""

    @override
    def __init__(self: object) -> None:
        """Initialize CLI service with flext-cli patterns."""
        self._cli_api = FlextCli()
        self._config: FlextCore.Types.Dict = FlextCliModels.FlextCliConfig()

    class _CommandHandlers:
        """Nested helper class for command handling operations."""

        @staticmethod
        def handle_info_command(service_instance: FlextDbtLdifCliService) -> None:
            """Handle info command execution."""
            result: FlextCore.Result[object] = service_instance.display_info()
            if result.is_failure:
                logger.error(f"Info command failed: {result.error}")

        @staticmethod
        def handle_generate_command(service_instance: FlextDbtLdifCliService) -> None:
            """Handle generate command execution."""
            result: FlextCore.Result[object] = (
                service_instance.display_generate_message()
            )
            if result.is_failure:
                logger.error(f"Generate command failed: {result.error}")

        @staticmethod
        def handle_validate_command(service_instance: FlextDbtLdifCliService) -> None:
            """Handle validate command execution."""
            result: FlextCore.Result[object] = (
                service_instance.display_validate_message()
            )
            if result.is_failure:
                logger.error(f"Validate command failed: {result.error}")

    class _MainEntry:
        """Nested helper class for main entry point operations."""

        @staticmethod
        def run_main_cli(service_instance: FlextDbtLdifCliService) -> NoReturn:
            """Execute main CLI entry point logic."""
            try:
                if len(sys.argv) > 1:
                    command = sys.argv[1]
                    if command == "info":
                        service_instance._CommandHandlers.handle_info_command(
                            service_instance,
                        )
                    elif command == "generate":
                        service_instance._CommandHandlers.handle_generate_command(
                            service_instance,
                        )
                    elif command == "validate":
                        service_instance._CommandHandlers.handle_validate_command(
                            service_instance,
                        )
                    else:
                        logger.error(f"Unknown command: {command}")
                        sys.exit(1)

                sys.exit(0)

            except KeyboardInterrupt:
                logger.info("Interrupted by user")
                sys.exit(1)
            except (OSError, RuntimeError, ValueError):
                logger.exception("CLI error")
                sys.exit(1)

    def display_info(self: object) -> FlextCore.Result[str]:
        """Display package info using flext-cli."""
        info_data = {
            "name": "FLEXT dbt LDIF",
            "version": "__version__",
            "description": "Advanced LDAP Data Analytics and Transformations",
            "features": [
                "Programmatic dbt model generation",
                "LDIF data processing and analytics",
                "Advanced SQL pattern generation",
                "PostgreSQL optimized transformations",
            ],
        }

        # Use flext-cli to format and display data
        try:
            formatted_data: FlextCore.Types.Dict = self._cli_api.format_data(
                info_data, "json"
            )
            if formatted_data.is_success:
                return FlextCore.Result[str].ok(
                    "Package information displayed successfully"
                )
            return FlextCore.Result[str].fail("Package information display failed")
        except Exception as e:
            return FlextCore.Result[str].fail(f"Package info display failed: {e}")

    def display_generate_message(self: object) -> FlextCore.Result[str]:
        """Display generate message using flext-cli."""
        try:
            self._cli_api.format_data(
                {"message": "Model generation functionality coming soon!"},
                "json",
            )
            return FlextCore.Result[str].ok("Generate message displayed")
        except Exception as e:
            return FlextCore.Result[str].fail(f"Generate message display failed: {e}")

    def display_validate_message(self: object) -> FlextCore.Result[str]:
        """Display validate message using flext-cli."""
        try:
            self._cli_api.format_data(
                {"message": "Model validation functionality coming soon!"},
                "json",
            )
            return FlextCore.Result[str].ok("Validate message displayed")
        except Exception as e:
            return FlextCore.Result[str].fail(f"Validate message display failed: {e}")

    def info(self: object) -> None:
        """Show package information."""
        self._CommandHandlers.handle_info_command(self)

    def generate(self: object) -> None:
        """Generate dbt models from LDIF schema definitions."""
        self._CommandHandlers.handle_generate_command(self)

    @override
    def validate(self: object) -> None:
        """Validate dbt models and configurations."""
        self._CommandHandlers.handle_validate_command(self)

    def main(self: object) -> NoReturn:
        """Main CLI entry point for flext-dbt-ldif."""
        self._MainEntry.run_main_cli(self)


# Module-level entry point for backwards compatibility
def main() -> NoReturn:
    """Module-level main entry point - delegates to service."""
    service = FlextDbtLdifCliService()
    service.main()


if __name__ == "__main__":
    main()
