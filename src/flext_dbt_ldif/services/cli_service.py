"""CliService mixin for dbt-ldif utilities."""

from __future__ import annotations

import sys

from flext_core import FlextLogger, r
from flext_dbt_ldif import FlextDbtLdifServiceMixin, c

logger = FlextLogger(__name__)


class FlextDbtLdifCliService:
    """Mixin providing CliService for dbt-ldif utilities."""

    class CliService:
        """FLEXT dbt LDIF CLI service using flext-cli foundation exclusively."""

        def display_generate_message(self) -> r[str]:
            """Generate dbt models from LDIF schema definitions."""
            try:
                service = FlextDbtLdifServiceMixin.Service()
                result = service.generate_and_write_models([])
                if result.failure:
                    return r[str].fail(result.error or "Model generation failed")
                logger.info(
                    "Model generation completed: %s",
                    result.value,
                )
                return r[str].ok("Generate message displayed")
            except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
                return r[str].fail(f"Generate message display failed: {exc}")

        def display_info(self) -> r[str]:
            """Display package info using flext-cli."""
            info_data = {
                "name": "FLEXT dbt LDIF",
                "version": "__version__",
                "description": ("Advanced LDAP Data Analytics and Transformations"),
                "features": (
                    "Programmatic dbt model generation, "
                    "LDIF data processing and analytics, "
                    "Advanced SQL pattern generation, "
                    "PostgreSQL optimized transformations"
                ),
            }
            try:
                logger.info(str(info_data))
                return r[str].ok("Package information displayed successfully")
            except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
                return r[str].fail(f"Package info display failed: {exc}")

        def display_validate_message(self) -> r[str]:
            """Validate dbt models and configurations."""
            try:
                service = FlextDbtLdifServiceMixin.Service()
                result = service.run_data_quality_assessment("")
                if result.failure:
                    return r[str].fail(result.error or "Validation failed")
                logger.info(
                    "Validation completed: %s",
                    result.value,
                )
                return r[str].ok("Validate message displayed")
            except c.Meltano.SINGER_SAFE_EXCEPTIONS as exc:
                return r[str].fail(f"Validate message display failed: {exc}")

        def generate(self) -> None:
            """Generate dbt models from LDIF schema definitions."""
            result: r[str] = self.display_generate_message()
            if result.failure:
                logger.error("Generate command failed: %s", result.error)

        def info(self) -> None:
            """Show package information."""
            result = self.display_info()
            if result.failure:
                logger.error("Info command failed: %s", result.error)

        def main(self) -> int:
            """Main CLI entry point for flext-dbt-ldif."""
            try:
                if len(sys.argv) > 1:
                    command: str = sys.argv[1]
                    if command == c.DbtLdif.CLI_COMMAND_INFO:
                        self.info()
                    elif command == c.DbtLdif.CLI_COMMAND_GENERATE:
                        self.generate()
                    elif command == c.DbtLdif.CLI_COMMAND_VALIDATE:
                        self.validate()
                    else:
                        logger.error("Unknown command: %s", command)
                        return c.DbtLdif.EXIT_CODE_FAILURE
                return c.DbtLdif.EXIT_CODE_SUCCESS
            except KeyboardInterrupt:
                logger.info("Interrupted by user")
                return c.DbtLdif.EXIT_CODE_FAILURE
            except c.Meltano.SINGER_SAFE_EXCEPTIONS:
                logger.exception("CLI error")
                return c.DbtLdif.EXIT_CODE_FAILURE

        def validate(self) -> None:
            """Validate dbt models and configurations."""
            result: r[str] = self.display_validate_message()
            if result.failure:
                logger.error("Validate command failed: %s", result.error)
