"""Command-line interface for FLEXT dbt LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import sys

from flext_cli import FlextCliOutput, FlextCliSettings
from flext_core import FlextLogger, r

from flext_dbt_ldif import FlextDbtLdifService, c

logger = FlextLogger(__name__)


class FlextDbtLdifCliService:
    """FLEXT dbt LDIF CLI service using flext-cli foundation exclusively."""

    def __init__(self) -> None:
        """Initialize CLI service with flext-cli patterns."""
        self._output = FlextCliOutput()
        self._config = FlextCliSettings.get_global()

    class _CommandHandlers:
        """Nested helper class for command handling operations."""

        @staticmethod
        def handle_generate_command(service_instance: FlextDbtLdifCliService) -> None:
            """Handle generate command execution."""
            result: r[str] = service_instance.display_generate_message()
            if result.is_failure:
                logger.error(f"Generate command failed: {result.error}")

        @staticmethod
        def handle_info_command(service_instance: FlextDbtLdifCliService) -> None:
            """Handle info command execution."""
            result = service_instance.display_info()
            if result.is_failure:
                logger.error(f"Info command failed: {result.error}")

        @staticmethod
        def handle_validate_command(service_instance: FlextDbtLdifCliService) -> None:
            """Handle validate command execution."""
            result: r[str] = service_instance.display_validate_message()
            if result.is_failure:
                logger.error(f"Validate command failed: {result.error}")

    class _MainEntry:
        """Nested helper class for main entry point operations."""

        @staticmethod
        def run_main_cli(service_instance: FlextDbtLdifCliService) -> int:
            """Execute main CLI entry point logic."""
            try:
                if len(sys.argv) > 1:
                    command: str = sys.argv[1]
                    if command == c.DbtLdif.CLI_COMMAND_INFO:
                        service_instance._CommandHandlers.handle_info_command(
                            service_instance,
                        )
                    elif command == c.DbtLdif.CLI_COMMAND_GENERATE:
                        service_instance._CommandHandlers.handle_generate_command(
                            service_instance,
                        )
                    elif command == c.DbtLdif.CLI_COMMAND_VALIDATE:
                        service_instance._CommandHandlers.handle_validate_command(
                            service_instance,
                        )
                    else:
                        logger.error("Unknown command: %s", command)
                        return c.DbtLdif.EXIT_CODE_FAILURE
                return c.DbtLdif.EXIT_CODE_SUCCESS
            except KeyboardInterrupt:
                logger.info("Interrupted by user")
                return c.DbtLdif.EXIT_CODE_FAILURE
            except (OSError, RuntimeError, ValueError):
                logger.exception("CLI error")
                return c.DbtLdif.EXIT_CODE_FAILURE

    def display_generate_message(self) -> r[str]:
        """Generate dbt models from LDIF schema definitions."""
        try:
            service = FlextDbtLdifService()
            result = service.generate_and_write_models([])
            if result.is_failure:
                return r[str].fail(result.error or "Model generation failed")
            self._output.display_text(
                f"Model generation completed: {result.value}",
            )
            return r[str].ok("Generate message displayed")
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[str].fail(f"Generate message display failed: {e}")

    def display_info(self) -> r[str]:
        """Display package info using flext-cli."""
        info_data = {
            "name": "FLEXT dbt LDIF",
            "version": "__version__",
            "description": "Advanced LDAP Data Analytics and Transformations",
            "features": "Programmatic dbt model generation, LDIF data processing and analytics, Advanced SQL pattern generation, PostgreSQL optimized transformations",
        }
        try:
            self._output.display_text(str(info_data))
            return r[str].ok("Package information displayed successfully")
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[str].fail(f"Package info display failed: {e}")

    def display_validate_message(self) -> r[str]:
        """Validate dbt models and configurations."""
        try:
            service = FlextDbtLdifService()
            result = service.run_data_quality_assessment("")
            if result.is_failure:
                return r[str].fail(result.error or "Validation failed")
            self._output.display_text(
                f"Validation completed: {result.value}",
            )
            return r[str].ok("Validate message displayed")
        except (
            ValueError,
            TypeError,
            KeyError,
            AttributeError,
            OSError,
            RuntimeError,
            ImportError,
        ) as e:
            return r[str].fail(f"Validate message display failed: {e}")

    def generate(self) -> None:
        """Generate dbt models from LDIF schema definitions."""
        self._CommandHandlers.handle_generate_command(self)

    def info(self) -> None:
        """Show package information."""
        self._CommandHandlers.handle_info_command(self)

    def main(self) -> int:
        """Main CLI entry point for flext-dbt-ldif."""
        return self._MainEntry.run_main_cli(self)

    def validate(self) -> None:
        """Validate dbt models and configurations."""
        self._CommandHandlers.handle_validate_command(self)


if __name__ == "__main__":
    sys.exit(FlextDbtLdifCliService().main())


__all__ = ["FlextDbtLdifCliService"]
