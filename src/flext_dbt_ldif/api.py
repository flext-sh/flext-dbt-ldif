"""Public API facade for DBT LDIF workflows.

MRO facade composing all service mixins per AGENTS.md §2.5.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import ClassVar, Self

from flext_core import FlextTypes, r
from flext_dbt_ldif import (
    FlextDbtLdifClient,
    FlextDbtLdifCliService,
    FlextDbtLdifCore,
    FlextDbtLdifError as FlextDbtLdifErrorMixin,
    FlextDbtLdifServiceMixin,
    FlextDbtLdifSettings,
    FlextDbtLdifUnifiedService,
    c,
    m,
    u,
)


class FlextDbtLdif(
    FlextDbtLdifCliService,
    FlextDbtLdifClient,
    FlextDbtLdifCore,
    FlextDbtLdifErrorMixin,
    FlextDbtLdifServiceMixin,
    FlextDbtLdifUnifiedService,
):
    """MRO facade for all DBT LDIF operations.

    All domain behavior comes from service mixins via MRO.
    """

    class _EntryListAdapter(
        m.RootModel[Sequence[FlextTypes.ContainerValueMapping]],
    ):
        """Adapter for parsed-entry lists."""

        root: Sequence[FlextTypes.ContainerValueMapping]

    _instance: ClassVar[Self | None] = None

    def __init__(self, settings: FlextDbtLdifSettings | None = None) -> None:
        """Initialize facade with optional settings override."""
        self._config = (
            settings if settings is not None else FlextDbtLdifSettings.fetch_global()
        )
        self._service = self.Service(settings=self._config)

    @classmethod
    def get_instance(cls) -> Self:
        """Return the shared facade instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def service(self) -> FlextDbtLdifServiceMixin.Service:
        """Return bound workflow service."""
        return self._service

    def execute(self) -> p.Result[FlextDbtLdifSettings]:
        """Return current settings payload for service contracts."""
        current_config = self._config
        return u.try_(
            lambda: FlextDbtLdifSettings.model_validate(current_config.model_dump()),
            catch=c.ValidationError,
        ).map_error(lambda _: "Invalid DBT LDIF settings")

    def generate_ldif_models(
        self,
        ldif_file: Path | str,
        *,
        overwrite: bool = False,
    ) -> p.Result[m.DbtLdif.ModelGenerationResult]:
        """Generate DBT model metadata from LDIF input."""
        parsed = self.service.client.parse_ldif_file(ldif_file)
        if parsed.failure:
            return r[m.DbtLdif.ModelGenerationResult].fail(
                parsed.error or "Parsing failed",
            )
        entries_raw = parsed.value
        try:
            entries = self._EntryListAdapter.model_validate(entries_raw).root
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
        """Execute end-to-end LDIF workflow."""
        return self.service.run_complete_workflow(
            ldif_file=ldif_file,
            generate_models=generate_models,
            run_transformations=run_transformations,
        )

    def validate_ldif_quality(
        self,
        ldif_file: Path | str,
    ) -> p.Result[m.DbtLdif.ParseValidationResult]:
        """Run quality-focused workflow."""
        return self.service.run_data_quality_assessment(ldif_file)


dbt_ldif = FlextDbtLdif

__all__: list[str] = ["FlextDbtLdif", "dbt_ldif"]
