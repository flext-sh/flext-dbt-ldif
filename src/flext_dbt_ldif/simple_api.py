"""Public API facade for DBT LDIF workflows."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import override

from flext_core import FlextResult, FlextService, t
from pydantic import TypeAdapter, ValidationError

from .dbt_services import FlextDbtLdifService
from .settings import FlextDbtLdifSettings

_ENTRY_LIST_ADAPTER = TypeAdapter(list[t.ConfigurationMapping])


class FlextDbtLdif(FlextService[FlextDbtLdifSettings]):
    """Facade class that exposes primary DBT LDIF operations."""

    def __init__(self, config: FlextDbtLdifSettings | None = None) -> None:
        """Initialize facade with optional settings override."""
        super().__init__()
        self._config = config or FlextDbtLdifSettings.get_global_instance()
        self._service = FlextDbtLdifService(config=self._config)

    @property
    def service(self) -> FlextDbtLdifService:
        """Return bound workflow service."""
        return self._service

    @override
    def execute(self) -> FlextResult[FlextDbtLdifSettings]:
        """Return current settings payload for service contracts."""
        try:
            return FlextResult[FlextDbtLdifSettings].ok(
                FlextDbtLdifSettings.model_validate(self._config)
            )
        except ValidationError:
            return FlextResult[FlextDbtLdifSettings].fail("Invalid DBT LDIF settings")

    def generate_ldif_models(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        overwrite: bool = False,
    ) -> FlextResult[Mapping[str, t.ContainerValue]]:
        """Generate DBT model metadata from LDIF input."""
        _ = project_dir
        parsed = self.service.parse_and_validate_ldif(ldif_file)
        if parsed.is_failure or parsed.value is None:
            return FlextResult[t.ConfigurationMapping].fail(
                parsed.error or "Parsing failed"
            )
        entries_raw = parsed.value.get("entries", [])
        try:
            entries = _ENTRY_LIST_ADAPTER.validate_python(entries_raw)
        except ValidationError:
            return FlextResult[t.ConfigurationMapping].fail(
                "Invalid parsed entries payload"
            )
        return self.service.generate_and_write_models(entries, overwrite=overwrite)

    def process_ldif_file(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> FlextResult[Mapping[str, t.ContainerValue]]:
        """Execute end-to-end LDIF workflow."""
        _ = project_dir
        return self.service.run_complete_workflow(
            ldif_file=ldif_file,
            generate_models=generate_models,
            run_transformations=run_transformations,
        )

    def validate_ldif_quality(
        self, ldif_file: Path | str
    ) -> FlextResult[Mapping[str, t.ContainerValue]]:
        """Run quality-focused workflow."""
        return self.service.run_data_quality_assessment(ldif_file)


__all__ = ["FlextDbtLdif"]
