"""Simple API for LDIF DBT operations.

Provides simplified interface for common LDIF-to-DBT operations.
Follows the same pattern as flext-dbt-ldap for consistency.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextLogger, FlextResult

from .dbt_services import FlextDbtLdifService

logger = FlextLogger(__name__)


def process_ldif_file(
    ldif_file: Path | str,
    project_dir: Path | str | None = None,
    *,
    generate_models: bool = True,
    run_transformations: bool = False,
) -> FlextResult[dict[str, object]]:
    """Simple function to process an LDIF file with DBT.

    Args:
      ldif_file: Path to LDIF file
      project_dir: DBT project directory (optional)
      generate_models: Whether to generate DBT models
      run_transformations: Whether to run transformations

    Returns:
      FlextResult containing processing results

    """
    logger.info("Processing LDIF file with simple API: %s", ldif_file)

    proj_path = Path(project_dir) if project_dir else None
    service = FlextDbtLdifService(project_dir=proj_path)

    return service.run_complete_workflow(
        ldif_file=ldif_file,
        generate_models=generate_models,
        run_transformations=run_transformations,
    )


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
    """Simple function to generate DBT models from LDIF.

    Args:
      ldif_file: Path to LDIF file
      project_dir: DBT project directory (optional)
      overwrite: Whether to overwrite existing models

    Returns:
      FlextResult containing model generation results

    """
    logger.info("Generating LDIF models with simple API: %s", ldif_file)

    proj_path = Path(project_dir) if project_dir else None
    service = FlextDbtLdifService(project_dir=proj_path)

    # Parse file first
    parse_result = service.parse_and_validate_ldif(ldif_file)
    if not parse_result.success:
        return parse_result

    parse_data = parse_result.value or {}
    entries = parse_data.get("entries", [])
    if not isinstance(entries, list):
        return FlextResult[dict[str, object]].fail("Invalid entries data format")
    return service.generate_and_write_models(entries, overwrite=overwrite)


__all__: list[str] = [
    "generate_ldif_models",
    "process_ldif_file",
    "validate_ldif_quality",
]
