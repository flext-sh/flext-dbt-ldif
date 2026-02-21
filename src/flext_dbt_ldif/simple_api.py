"""Public API facade for DBT LDIF workflows."""

from __future__ import annotations

from pathlib import Path

from flext_core import FlextResult, FlextService, t

from .dbt_services import FlextDbtLdifService
from .settings import FlextDbtLdifSettings


class FlextDbtLdif(FlextService[FlextDbtLdifSettings]):
    """Facade class that exposes primary DBT LDIF operations."""

    def __init__(self, config: FlextDbtLdifSettings | None = None) -> None:
        """Initialize facade with optional settings override."""
        super().__init__()
        self._config = config or FlextDbtLdifSettings.get_global_instance()
        self._service = FlextDbtLdifService(config=self._config)

    def execute(self) -> FlextResult[FlextDbtLdifSettings]:
        """Return current settings payload for service contracts."""
        if isinstance(self._config, FlextDbtLdifSettings):
            return FlextResult[FlextDbtLdifSettings].ok(self._config)
        return FlextResult[FlextDbtLdifSettings].fail("Invalid DBT LDIF settings")

    @property
    def service(self) -> FlextDbtLdifService:
        """Return bound workflow service."""
        return self._service

    def process_ldif_file(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Execute end-to-end LDIF workflow."""
        _ = project_dir
        return self.service.run_complete_workflow(
            ldif_file=ldif_file,
            generate_models=generate_models,
            run_transformations=run_transformations,
        )

    def validate_ldif_quality(
        self,
        ldif_file: Path | str,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Run quality-focused workflow."""
        return self.service.run_data_quality_assessment(ldif_file)

    def generate_ldif_models(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        overwrite: bool = False,
    ) -> FlextResult[dict[str, t.GeneralValueType]]:
        """Generate DBT model metadata from LDIF input."""
        _ = project_dir
        parsed = self.service.parse_and_validate_ldif(ldif_file)
        if parsed.is_failure or parsed.value is None:
            return FlextResult[dict[str, t.GeneralValueType]].fail(
                parsed.error or "Parsing failed",
            )
        entries_raw = parsed.value.get("entries", [])
        entries_payload = entries_raw if isinstance(entries_raw, list) else []
        entries = [entry for entry in entries_payload if isinstance(entry, dict)]
        return self.service.generate_and_write_models(entries, overwrite=overwrite)


__all__ = ["FlextDbtLdif"]
