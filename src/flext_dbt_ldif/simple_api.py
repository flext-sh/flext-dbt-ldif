"""Public API facade for DBT LDIF workflows."""

from __future__ import annotations

from pathlib import Path
from typing import override

from flext_core import r, t, u
from pydantic import TypeAdapter, ValidationError

from flext_dbt_ldif import FlextDbtLdifSettings, m, s

_ENTRY_LIST_ADAPTER = TypeAdapter(list[dict[str, t.ContainerValue]])


class FlextDbtLdif(s[FlextDbtLdifSettings]):
    """Facade class that exposes primary DBT LDIF operations."""

    def __init__(self, config: FlextDbtLdifSettings | None = None) -> None:
        """Initialize facade with optional settings override."""
        super().__init__(
            config_type=None,
            config_overrides=None,
            initial_context=None,
        )
        self._config = (
            config if config is not None else FlextDbtLdifSettings.get_global()
        )
        self._service = s(config=self._config)

    @property
    def service(self) -> s:
        """Return bound workflow service."""
        return self._service

    @override
    def execute(self) -> r[FlextDbtLdifSettings]:
        """Return current settings payload for service contracts."""
        current_config = (
            self._config
            if self._config is not None
            else FlextDbtLdifSettings.get_global()
        )
        return u.DbtLdif.try_(
            lambda: FlextDbtLdifSettings.model_validate(current_config.model_dump()),
            catch=ValidationError,
        ).map_error(lambda _: "Invalid DBT LDIF settings")

    def generate_ldif_models(
        self,
        ldif_file: Path | str,
        project_dir: Path | str | None = None,
        *,
        overwrite: bool = False,
    ) -> r[m.DbtLdif.ModelGenerationResult]:
        """Generate DBT model metadata from LDIF input."""
        _ = project_dir
        parsed = self.service.client.parse_ldif_file(ldif_file)
        if parsed.is_failure:
            return r[m.DbtLdif.ModelGenerationResult].fail(
                parsed.error or "Parsing failed"
            )
        entries_raw = parsed.value
        try:
            entries = _ENTRY_LIST_ADAPTER.validate_python(entries_raw)
        except ValidationError:
            return r[m.DbtLdif.ModelGenerationResult].fail(
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
    ) -> r[m.DbtLdif.WorkflowResult]:
        """Execute end-to-end LDIF workflow."""
        _ = project_dir
        return self.service.run_complete_workflow(
            ldif_file=ldif_file,
            generate_models=generate_models,
            run_transformations=run_transformations,
        )

    def validate_ldif_quality(
        self, ldif_file: Path | str
    ) -> r[m.DbtLdif.ParseValidationResult]:
        """Run quality-focused workflow."""
        return self.service.run_data_quality_assessment(ldif_file)


__all__ = ["FlextDbtLdif"]
