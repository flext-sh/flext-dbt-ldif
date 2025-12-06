"""FLEXT DBT LDIF API - Unified facade for DBT LDIF operations.

This module provides unified facade for DBT LDIF operations.
Uses types from typings.py and t, no dict[str, object].
Uses Python 3.13+ PEP 695 syntax and direct API calls.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

from flext_core import (
    FlextContainer,
    FlextContext,
    FlextLogger,
    FlextResult,
    FlextService,
    t,
)

from flext_dbt_ldif.config import FlextDbtLdifConfig
from flext_dbt_ldif.dbt_services import FlextDbtLdifService


class FlextDbtLdif(FlextService[FlextDbtLdifConfig]):
    """Unified DBT LDIF facade with complete FLEXT ecosystem integration.

    This is the single unified class for the flext-dbt-ldif domain providing
    access to all DBT LDIF domain functionality with centralized patterns.

    UNIFIED CLASS PATTERN: One class per module with nested helpers only.
    CENTRALIZED APPROACH: All operations follow centralized patterns:
    - FlextDbtLdif.* for DBT LDIF-specific operations
    - Centralized validation through FlextDbtLdifService
    - No wrappers, aliases, or fallbacks
    - Direct use of flext-core centralized services

    FLEXT INTEGRATION: Complete integration with flext-core patterns:
    - FlextContainer for dependency injection
    - FlextContext for operation context
    - FlextLogger for structured logging
    - FlextResult for railway-oriented error handling

    PYTHON 3.13+ COMPATIBILITY: Uses modern patterns and latest type features.
    Uses types from typings.py - no dict[str, object].
    """

    def __init__(self, config: FlextDbtLdifConfig | None = None) -> None:
        """Initialize the unified DBT LDIF service.

        Args:
            config: Optional configuration instance

        """
        super().__init__()
        self._config = config or FlextDbtLdifConfig.get_instance()
        self._service: FlextDbtLdifService | None = None

        # Complete FLEXT ecosystem integration
        self._container = FlextContainer.get_global().clear()().get_or_create()
        self._context = FlextContext()
        self.logger = FlextLogger(__name__)

    @classmethod
    def create(cls) -> FlextDbtLdif:
        """Create a new FlextDbtLdif instance (factory method).

        Returns:
            FlextDbtLdif: New instance

        """
        return cls()

    @property
    def service(self) -> FlextDbtLdifService:
        """Get the DBT LDIF service instance.

        Returns:
            FlextDbtLdifService: Service instance

        """
        if self._service is None:
            self._service = FlextDbtLdifService(
                project_dir=self._config.dbt_project_dir,
            )
        return self._service

    @property
    def config(self) -> FlextDbtLdifConfig:
        """Get the current configuration.

        Returns:
            FlextDbtLdifConfig: Current configuration

        """
        return self._config

    # =============================================================================
    # MAIN OPERATIONS - Enhanced with FlextResult error handling
    # =============================================================================

    def process_ldif_file(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> FlextResult[t.JsonDict]:
        """Process an LDIF file with DBT using railway pattern.

        Args:
            ldif_file: Path to LDIF file
            project_dir: DBT project directory (optional)
            generate_models: Whether to generate DBT models
            run_transformations: Whether to run transformations

        Returns:
            FlextResult[t.JsonDict]: Processing results

        """
        try:
            self.logger.info("Processing LDIF file: %s", ldif_file)

            # Use provided project_dir or fall back to config
            proj_path = (
                Path(project_dir) if project_dir else Path(self._config.dbt_project_dir)
            )
            if proj_path:
                service = FlextDbtLdifService(project_dir=proj_path)
            else:
                service = self.service

            return service.run_complete_workflow(
                ldif_file=ldif_file,
                generate_models=generate_models,
                run_transformations=run_transformations,
            )
        except Exception as e:
            return FlextResult[t.JsonDict].fail(f"LDIF processing failed: {e}")

    def validate_ldif_quality(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[t.JsonDict]:
        """Validate LDIF data quality using railway pattern.

        Args:
            ldif_file: Path to LDIF file

        Returns:
            FlextResult[t.JsonDict]: Quality assessment

        """
        try:
            self.logger.info("Validating LDIF quality: %s", ldif_file)
            return self.service.run_data_quality_assessment(ldif_file)
        except Exception as e:
            return FlextResult[t.JsonDict].fail(f"LDIF quality validation failed: {e}")

    def generate_ldif_models(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        overwrite: bool = False,
    ) -> FlextResult[t.JsonDict]:
        """Generate DBT models from LDIF using railway pattern.

        Args:
            ldif_file: Path to LDIF file
            project_dir: DBT project directory (optional)
            overwrite: Whether to overwrite existing models

        Returns:
            FlextResult[t.JsonDict]: Model generation results

        """
        try:
            self.logger.info("Generating LDIF models: %s", ldif_file)

            # Use provided project_dir or fall back to config
            proj_path = (
                Path(project_dir) if project_dir else Path(self._config.dbt_project_dir)
            )
            if proj_path:
                service = FlextDbtLdifService(project_dir=proj_path)
            else:
                service = self.service

            # Parse file first
            parse_result = service.parse_and_validate_ldif(ldif_file)
            if not parse_result.success:
                return FlextResult[t.JsonDict].fail(
                    f"LDIF parsing failed: {parse_result.error}",
                )

            parse_data = parse_result.value or {}
            entries = parse_data.get("entries", [])
            if not isinstance(entries, list):
                return FlextResult[t.JsonDict].fail("Invalid entries data format")

            return service.generate_and_write_models(entries, overwrite=overwrite)
        except Exception as e:
            return FlextResult[t.JsonDict].fail(f"Model generation failed: {e}")


# Backward compatibility aliases
FlextDbtLdifAPI = FlextDbtLdif


# Legacy function wrappers for backward compatibility
def process_ldif_file(
    ldif_file: Path | str,
    project_dir: Path | str | None = None,
    *,
    generate_models: bool = True,
    run_transformations: bool = False,
) -> FlextResult[t.JsonDict]:
    """Legacy function wrapper - use FlextDbtLdif.process_ldif_file() instead.

    Args:
        ldif_file: Path to LDIF file
        project_dir: DBT project directory (optional)
        generate_models: Whether to generate DBT models
        run_transformations: Whether to run transformations

    Returns:
        FlextResult[t.JsonDict]: Processing results

    """
    api = FlextDbtLdif()
    return api.process_ldif_file(
        ldif_file,
        project_dir,
        generate_models=generate_models,
        run_transformations=run_transformations,
    )


def validate_ldif_quality(
    ldif_file: Path | str,
) -> FlextResult[t.JsonDict]:
    """Legacy function wrapper - use FlextDbtLdif.validate_ldif_quality() instead.

    Args:
        ldif_file: Path to LDIF file

    Returns:
        FlextResult[t.JsonDict]: Quality assessment

    """
    api = FlextDbtLdif()
    return api.validate_ldif_quality(ldif_file)


def generate_ldif_models(
    ldif_file: Path | str,
    project_dir: Path | str | None = None,
    *,
    overwrite: bool = False,
) -> FlextResult[t.JsonDict]:
    """Legacy function wrapper - use FlextDbtLdif.generate_ldif_models() instead.

    Args:
        ldif_file: Path to LDIF file
        project_dir: DBT project directory (optional)
        overwrite: Whether to overwrite existing models

    Returns:
        FlextResult[t.JsonDict]: Model generation results

    """
    api = FlextDbtLdif()
    return api.generate_ldif_models(ldif_file, project_dir, overwrite=overwrite)


__all__: list[str] = [
    "FlextDbtLdif",
    "FlextDbtLdifAPI",
    "generate_ldif_models",  # Backward compatibility
    "process_ldif_file",  # Backward compatibility
    "validate_ldif_quality",  # Backward compatibility
]
