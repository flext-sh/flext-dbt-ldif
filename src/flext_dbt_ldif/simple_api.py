"""FLEXT DBT LDIF API - Unified facade for DBT LDIF operations.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

Unified facade for FLEXT DBT LDIF operations with complete FLEXT integration.
"""

from __future__ import annotations

from pathlib import Path

from flext_core import (
    FlextContainer,
    FlextContext,
    FlextLogger,
    FlextResult,
    FlextService,
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
    """

    def __init__(self, config: FlextDbtLdifConfig | None = None) -> None:
        """Initialize the unified DBT LDIF service."""
        super().__init__()
        self._config = config or FlextDbtLdifConfig()
        self._service: FlextDbtLdifService | None = None

        # Complete FLEXT ecosystem integration
        self._container = FlextContainer.get_global().clear()().get_or_create()
        self._context = FlextContext()
        self.logger = FlextLogger(__name__)

    @classmethod
    def create(cls) -> FlextDbtLdif:
        """Create a new FlextDbtLdif instance (factory method)."""
        return cls()

    @property
    def service(self) -> FlextDbtLdifService:
        """Get the DBT LDIF service instance."""
        if self._service is None:
            self._service = FlextDbtLdifService(project_dir=self._config.project_dir)
        return self._service

    @property
    def config(self) -> FlextDbtLdifConfig:
        """Get the current configuration."""
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
    ) -> FlextResult[dict[str, object]]:
        """Process an LDIF file with DBT using railway pattern.

        Args:
        ldif_file: Path to LDIF file
        project_dir: DBT project directory (optional)
        generate_models: Whether to generate DBT models
        run_transformations: Whether to run transformations

        Returns:
        FlextResult containing processing results

        """
        try:
            self.logger.info("Processing LDIF file: %s", ldif_file)

            # Use provided project_dir or fall back to config
            proj_path = Path(project_dir) if project_dir else self._config.project_dir
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
            return FlextResult[dict[str, object]].fail(f"LDIF processing failed: {e}")

    def validate_ldif_quality(
        self, ldif_file: Path | str
    ) -> FlextResult[dict[str, object]]:
        """Validate LDIF data quality using railway pattern.

        Args:
        ldif_file: Path to LDIF file

        Returns:
        FlextResult containing quality assessment

        """
        try:
            self.logger.info("Validating LDIF quality: %s", ldif_file)
            return self.service.run_data_quality_assessment(ldif_file)
        except Exception as e:
            return FlextResult[dict[str, object]].fail(
                f"LDIF quality validation failed: {e}"
            )

    def generate_ldif_models(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        overwrite: bool = False,
    ) -> FlextResult[dict[str, object]]:
        """Generate DBT models from LDIF using railway pattern.

        Args:
        ldif_file: Path to LDIF file
        project_dir: DBT project directory (optional)
        overwrite: Whether to overwrite existing models

        Returns:
        FlextResult containing model generation results

        """
        try:
            self.logger.info("Generating LDIF models: %s", ldif_file)

            # Use provided project_dir or fall back to config
            proj_path = Path(project_dir) if project_dir else self._config.project_dir
            if proj_path:
                service = FlextDbtLdifService(project_dir=proj_path)
            else:
                service = self.service

            # Parse file first
            parse_result = service.parse_and_validate_ldif(ldif_file)
            if not parse_result.success:
                return FlextResult[dict[str, object]].fail(
                    f"LDIF parsing failed: {parse_result.error}"
                )

            parse_data = parse_result.value or {}
            entries: list[object] = parse_data.get("entries", [])
            if not isinstance(entries, list):
                return FlextResult[dict[str, object]].fail(
                    "Invalid entries data format"
                )

            return service.generate_and_write_models(entries, overwrite=overwrite)
        except Exception as e:
            return FlextResult[dict[str, object]].fail(f"Model generation failed: {e}")


# Backward compatibility aliases
FlextDbtLdifAPI = FlextDbtLdif


# Legacy function wrappers for backward compatibility
def process_ldif_file(
    ldif_file: Path | str,
    project_dir: Path | str | None = None,
    *,
    generate_models: bool = True,
    run_transformations: bool = False,
) -> FlextResult[dict[str, object]]:
    """Legacy function wrapper - use FlextDbtLdif.process_ldif_file() instead."""
    api = FlextDbtLdif()
    return api.process_ldif_file(
        ldif_file,
        project_dir,
        generate_models=generate_models,
        run_transformations=run_transformations,
    )


def validate_ldif_quality(
    ldif_file: Path | str,
) -> FlextResult[dict[str, object]]:
    """Legacy function wrapper - use FlextDbtLdif.validate_ldif_quality() instead."""
    api = FlextDbtLdif()
    return api.validate_ldif_quality(ldif_file)


def generate_ldif_models(
    ldif_file: Path | str,
    project_dir: Path | str | None = None,
    *,
    overwrite: bool = False,
) -> FlextResult[dict[str, object]]:
    """Legacy function wrapper - use FlextDbtLdif.generate_ldif_models() instead."""
    api = FlextDbtLdif()
    return api.generate_ldif_models(ldif_file, project_dir, overwrite=overwrite)


__all__ = [
    "FlextDbtLdif",
    "FlextDbtLdifAPI",
    "generate_ldif_models",  # Backward compatibility
    "process_ldif_file",  # Backward compatibility
    "validate_ldif_quality",  # Backward compatibility
]
