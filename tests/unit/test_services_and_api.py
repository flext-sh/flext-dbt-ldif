"""Behavior contract for FlextDbtLdif public API delegation.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from flext_tests import tm

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

        tm.ok(result)
        workflow = result.value
        tm.that(workflow.workflow_status, eq=c.DbtLdif.WORKFLOW_STATUS_COMPLETED)
        tm.that(workflow.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)
        tm.that(workflow.entry_count, eq=1)
        tm.that(workflow.ldif_file, eq=str(tmp_path / "f.ldif"))

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

        tm.ok(result)
        workflow = result.value
        tm.that(workflow.models_generated, eq=expected_models)
        tm.that(workflow.transformation_status, eq=expected_status)

    def test_validate_ldif_quality_reports_passing_metrics(
        self,
        tmp_path: Path,
    ) -> None:
        """validate_ldif_quality returns the parse/validation quality contract."""
        api = FlextDbtLdif()

        result = api.validate_ldif_quality(tmp_path / "f.ldif")

        tm.ok(result)
        report = result.value
        tm.that(report.entry_count, eq=1)
        tm.that(report.quality_score, eq=c.DbtLdif.DEFAULT_QUALITY_SCORE)
        tm.that(report.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)

    def test_generate_ldif_models_produces_staging_and_analytics(
        self,
        tmp_path: Path,
    ) -> None:
        """generate_ldif_models emits the staging and analytics model names."""
        api = FlextDbtLdif()

        result = api.generate_ldif_models(tmp_path / "f.ldif")

        tm.ok(result)
        generation = result.value
        tm.that(generation.models_generated, eq=2)
        tm.that(
            list(generation.model_names),
            eq=[
                c.DbtLdif.STAGING_MODEL_NAME,
                c.DbtLdif.ANALYTICS_MODEL_NAME,
            ],
        )

    def test_generate_ldif_models_dump_exposes_public_state(
        self,
        tmp_path: Path,
    ) -> None:
        """The generation result serializes its public fields via model_dump."""
        api = FlextDbtLdif()

        dumped = api.generate_ldif_models(tmp_path / "f.ldif").value.model_dump()

        tm.that(dumped["models_generated"], eq=2)
        tm.that(dumped["model_names"], has=c.DbtLdif.STAGING_MODEL_NAME)

    def test_execute_returns_configured_settings(self) -> None:
        """Execute surfaces the settings the facade was constructed with."""
        # NOTE (multi-agent, bead mro-d421): DbtLdif is the typed _DbtLdif model, not a raw
        # dict (U18: config/settings values are validated models, no model-less payload).
        settings = FlextDbtLdifSettings(
            DbtLdif=FlextDbtLdifSettings._DbtLdif(min_quality_threshold=0.5),
        )
        api = FlextDbtLdif(settings=settings)

        result = api.execute()

        tm.ok(result)
        tm.that(result.value, is_=FlextDbtLdifSettings)
        tm.that(result.value.DbtLdif.min_quality_threshold, eq=pytest.approx(0.5))

    def test_service_property_exposes_workflow_service(self) -> None:
        """The service property exposes the bound workflow Service."""
        api = FlextDbtLdif()

        tm.that(api.service, is_=FlextDbtLdifServiceMixin.Service)

    def test_fetch_instance_returns_shared_singleton(self) -> None:
        """fetch_instance returns the same facade instance on repeated calls."""
        first = FlextDbtLdif.fetch_instance()
        second = FlextDbtLdif.fetch_instance()

        assert first is second
