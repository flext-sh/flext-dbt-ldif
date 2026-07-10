"""Behavior contract for FlextDbtLdif public API delegation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flext_dbt_ldif import FlextDbtLdif, FlextDbtLdifSettings, c
from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin

if TYPE_CHECKING:
    from pathlib import Path

__all__: list[str] = ["TestsFlextDbtLdifServicesAndApi"]


class TestsFlextDbtLdifServicesAndApi:
    """Observable behavior of the FlextDbtLdif facade public methods."""

    def test_process_ldif_file_returns_completed_workflow(
        self,
        tmp_path: Path,
    ) -> None:
        """process_ldif_file yields a completed, validated workflow result."""
        api = FlextDbtLdif()

        result = api.process_ldif_file(tmp_path / "f.ldif")

        assert result.success
        workflow = result.value
        assert workflow.workflow_status == c.DbtLdif.WORKFLOW_STATUS_COMPLETED
        assert workflow.validation_status == c.DbtLdif.VALIDATION_STATUS_PASSED
        assert workflow.entry_count == 1
        assert workflow.ldif_file == str(tmp_path / "f.ldif")

    @pytest.mark.parametrize(
        (
            "generate_models",
            "run_transformations",
            "expected_models",
            "expected_status",
        ),
        [
            (True, False, 2, ""),
            (False, False, 0, ""),
            (True, True, 2, c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS),
            (False, True, 0, c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS),
        ],
    )
    def test_process_ldif_file_honors_generation_and_transformation_flags(
        self,
        tmp_path: Path,
        *,
        generate_models: bool,
        run_transformations: bool,
        expected_models: int,
        expected_status: str,
    ) -> None:
        """Model generation and transformation flags drive the workflow result."""
        api = FlextDbtLdif()

        result = api.process_ldif_file(
            tmp_path / "f.ldif",
            generate_models=generate_models,
            run_transformations=run_transformations,
        )

        assert result.success
        workflow = result.value
        assert workflow.models_generated == expected_models
        assert workflow.transformation_status == expected_status

    def test_validate_ldif_quality_reports_passing_metrics(
        self,
        tmp_path: Path,
    ) -> None:
        """validate_ldif_quality returns the parse/validation quality contract."""
        api = FlextDbtLdif()

        result = api.validate_ldif_quality(tmp_path / "f.ldif")

        assert result.success
        report = result.value
        assert report.entry_count == 1
        assert report.quality_score == c.DbtLdif.DEFAULT_QUALITY_SCORE
        assert report.validation_status == c.DbtLdif.VALIDATION_STATUS_PASSED

    def test_generate_ldif_models_produces_staging_and_analytics(
        self,
        tmp_path: Path,
    ) -> None:
        """generate_ldif_models emits the staging and analytics model names."""
        api = FlextDbtLdif()

        result = api.generate_ldif_models(tmp_path / "f.ldif")

        assert result.success
        generation = result.value
        assert generation.models_generated == 2
        assert list(generation.model_names) == [
            c.DbtLdif.STAGING_MODEL_NAME,
            c.DbtLdif.ANALYTICS_MODEL_NAME,
        ]

    def test_generate_ldif_models_dump_exposes_public_state(
        self,
        tmp_path: Path,
    ) -> None:
        """The generation result serializes its public fields via model_dump."""
        api = FlextDbtLdif()

        dumped = api.generate_ldif_models(tmp_path / "f.ldif").value.model_dump()

        assert dumped["models_generated"] == 2
        assert c.DbtLdif.STAGING_MODEL_NAME in dumped["model_names"]

    def test_execute_returns_configured_settings(self) -> None:
        """Execute surfaces the settings the facade was constructed with."""
        # NOTE (multi-agent): mro-rn88 — project fields nest under the DbtLdif namespace.
        settings = FlextDbtLdifSettings(DbtLdif={"min_quality_threshold": 0.5})
        api = FlextDbtLdif(settings=settings)

        result = api.execute()

        assert result.success
        assert isinstance(result.value, FlextDbtLdifSettings)
        assert result.value.DbtLdif.min_quality_threshold == pytest.approx(0.5)

    def test_service_property_exposes_workflow_service(self) -> None:
        """The service property exposes the bound workflow Service."""
        api = FlextDbtLdif()

        assert isinstance(api.service, FlextDbtLdifServiceMixin.Service)

    def test_fetch_instance_returns_shared_singleton(self) -> None:
        """fetch_instance returns the same facade instance on repeated calls."""
        first = FlextDbtLdif.fetch_instance()
        second = FlextDbtLdif.fetch_instance()

        assert first is second
