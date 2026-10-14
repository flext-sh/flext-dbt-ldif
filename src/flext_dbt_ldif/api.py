"""Public API facade for DBT LDIF workflows.

MRO facade composing all service mixins per AGENTS.md §2.5.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path
from typing import ClassVar, Self

from flext_dbt_ldif import FlextDbtLdifSettings, c, m, p, r, u
from flext_dbt_ldif.services.client import FlextDbtLdifClient
from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService


class FlextDbtLdif(
    FlextDbtLdifClient,
    FlextDbtLdifServiceMixin,
    FlextDbtLdifUnifiedService,
):
    """MRO facade for all DBT LDIF operations.

    All domain behavior comes from service mixins via MRO.
    """

    _instance: ClassVar[Self | None] = None

    def __init__(self, settings: FlextDbtLdifSettings | None = None) -> None:
        """Initialize facade with optional settings override."""
        # NOTE (multi-agent): mro-rn88 — resolve effective settings from the injected
        # override or the global singleton; Service reads the global internally.
        self._settings = settings or FlextDbtLdifSettings.fetch_global()
        self._service = self.Service()

    @classmethod
    def fetch_global(cls) -> Self:
        """Return the shared facade singleton, creating it on first call."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def service(self) -> FlextDbtLdifServiceMixin.Service:
        """The bound workflow service."""
        return self._service

    def execute(self) -> p.Result[FlextDbtLdifSettings]:
        """Return the current settings payload for service contracts."""
        return r[FlextDbtLdifSettings].ok(self._settings)

    def generate_ldif_models(
        self,
        ldif_file: Path | str,
        *,
        overwrite: bool = False,
    ) -> p.Result[m.DbtLdif.ModelGenerationResult]:
        """Generate DBT model metadata from LDIF input.

        Parses the LDIF file and produces staging and analytics model
        definitions for the parsed entries.

        Args:
            ldif_file: Path to the LDIF file to process.
            overwrite: Whether to overwrite existing generated artifacts.

        Returns:
            Result wrapping the generation summary, or a failure when
            parsing or generation fails.

        """
        parsed = self.service.client.parse_ldif_file(ldif_file)
        if parsed.failure:
            return r[m.DbtLdif.ModelGenerationResult].from_failure(parsed)
        entries_raw = parsed.value
        try:
            entries = u.json_mapping_sequence_adapter().validate_python(entries_raw)
        except c.ValidationError:
            return r[m.DbtLdif.ModelGenerationResult].fail(
                "Invalid parsed entries payload",
            )
        return self.service.generate_and_write_models(entries, overwrite=overwrite)

    def process_ldif_file(
        self,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> p.Result[m.DbtLdif.WorkflowResult]:
        """Execute end-to-end LDIF workflow.

        Runs parsing, validation, and optionally model generation and
        transformations according to the given flags.

        Args:
            ldif_file: Path to the LDIF file to process.
            generate_models: Whether to generate DBT models.
            run_transformations: Whether to run DBT transformations.

        Returns:
            Result wrapping the workflow summary, or a failure when any
            stage fails.

        """
        return self.service.run_complete_workflow(
            ldif_file=ldif_file,
            generate_models=generate_models,
            run_transformations=run_transformations,
        )

    def validate_ldif_quality(
        self,
        ldif_file: Path | str,
    ) -> p.Result[m.DbtLdif.ParseValidationResult]:
        """Run quality-focused workflow.

        Parses and validates the LDIF file and reports the resulting
        quality metrics.

        Args:
            ldif_file: Path to the LDIF file to assess.

        Returns:
            Result wrapping the parse and validation summary, or a
            failure when parsing or validation fails.

        """
        return self.service.run_data_quality_assessment(ldif_file)


dbt_ldif: FlextDbtLdif = FlextDbtLdif.fetch_global()
"""Shared ``FlextDbtLdif`` facade instance for DBT LDIF workflows."""

__all__: list[str] = ["FlextDbtLdif", "dbt_ldif"]
