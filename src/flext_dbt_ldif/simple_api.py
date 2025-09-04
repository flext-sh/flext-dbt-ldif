"""Simple API for LDIF DBT operations.

Provides simplified interface for common LDIF-to-DBT operations.
Follows the same pattern as flext-dbt-ldap for consistency.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult

from .dbt_exceptions import (
    FlextDbtLdifError,
    FlextDbtLdifModelError,
    FlextDbtLdifProcessingError,
    FlextDbtLdifValidationError,
)
from .dbt_services import FlextDbtLdifService

logger = FlextLogger(__name__)


def process_ldif_file(
    ldif_file: Path | str,
    project_dir: Path | str | None = None,
    *,
    generate_models: bool = True,
    run_transformations: bool = False,
) -> FlextResult[dict[str, object]]:
    """Simple function to process an LDIF file with DBT using flext-core patterns.

    Args:
      ldif_file: Path to LDIF file
      project_dir: DBT project directory (optional)
      generate_models: Whether to generate DBT models
      run_transformations: Whether to run transformations

    Returns:
      FlextResult containing processing results

    """
    logger.info("Processing LDIF file with simple API: %s", ldif_file)

    try:
        proj_path = Path(project_dir) if project_dir else None
        service = FlextDbtLdifService(project_dir=proj_path)

        return service.run_complete_workflow(
            ldif_file=ldif_file,
            generate_models=generate_models,
            run_transformations=run_transformations,
        )
    except FlextDbtLdifError as e:
        logger.error("LDIF processing failed: %s", e)
        return FlextResult[dict[str, object]].fail(f"Processing failed: {e}")
    except Exception as e:
        logger.exception("Unexpected error in simple API")
        return FlextResult[dict[str, object]].fail(f"Unexpected error: {e}")


def validate_ldif_quality(
    ldif_file: Path | str,
) -> FlextResult[dict[str, object]]:
    """Simple function to validate LDIF data quality.

    Args:
      ldif_file: Path to LDIF file

    Returns:
      FlextResult containing quality assessment

    """
    logger.info("Validating LDIF quality with simple API: %s", ldif_file)

    service = FlextDbtLdifService()
    return service.run_data_quality_assessment(ldif_file)


def generate_ldif_models(
    ldif_file: Path | str,
    project_dir: Path | str | None = None,
    *,
    overwrite: bool = False,
) -> FlextResult[dict[str, object]]:
    """Simple function to generate DBT models from LDIF using flext-core patterns.

    Args:
      ldif_file: Path to LDIF file
      project_dir: DBT project directory (optional)
      overwrite: Whether to overwrite existing models

    Returns:
      FlextResult containing model generation results

    """
    logger.info("Generating LDIF models with simple API: %s", ldif_file)

    try:
        proj_path = Path(project_dir) if project_dir else None
        service = FlextDbtLdifService(project_dir=proj_path)

        # Parse file first - this now raises exceptions
        parse_data = service.parse_and_validate_ldif(ldif_file)
        entries = parse_data.get("entries", [])
        
        if not isinstance(entries, list):
            return FlextResult[dict[str, object]].fail("Invalid entries data format")
            
        # Generate models - this now raises exceptions  
        model_data = service.generate_and_write_models(entries, overwrite=overwrite)
        return FlextResult[dict[str, object]].ok(model_data)
        
    except (
        FlextDbtLdifProcessingError,
        FlextDbtLdifValidationError,
        FlextDbtLdifModelError,
    ) as e:
        logger.error("Model generation failed: %s", e)
        return FlextResult[dict[str, object]].fail(f"Model generation failed: {e}")
    except Exception as e:
        logger.exception("Unexpected error in model generation")
        return FlextResult[dict[str, object]].fail(f"Unexpected error: {e}")


__all__: list[str] = [
    "generate_ldif_models",
    "process_ldif_file",
    "validate_ldif_quality",
]
