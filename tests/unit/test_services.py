"""Behavior contract for FlextDbtLdifServiceMixin services — public API only.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flext_dbt_ldif import c
from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
from tests import t
from tests.unit._services_parts.data_quality import (
    TestsFlextDbtLdifServicesDataQuality,
)

if TYPE_CHECKING:
    from pathlib import Path


@pytest.fixture
def svc(tmp_path: Path) -> FlextDbtLdifServiceMixin.Service:
    """Create a service backed by a real project directory."""
    return FlextDbtLdifServiceMixin.Service(project_dir=tmp_path)


@pytest.fixture
def entries() -> t.SequenceOf[t.JsonMapping]:
    """Provide a minimal LDIF entry payload accepted by the public API."""
    return [{"dn": "cn=test,dc=example,dc=org"}]


class TestsFlextDbtLdifServices(TestsFlextDbtLdifServicesDataQuality):
    """Behavior contract for FlextDbtLdifServiceMixin.Service workflows."""

    def test_parse_and_validate_ldif_returns_quality_metrics(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """A valid LDIF path yields a passed validation with a quality score."""
        result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")

        assert result.success
        data = result.unwrap()
        assert data.entry_count == 1
        assert data.quality_score == c.DbtLdif.DEFAULT_QUALITY_SCORE
        assert data.validation_status == c.DbtLdif.VALIDATION_STATUS_PASSED

    def test_parse_and_validate_ldif_is_idempotent(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """Repeated calls with the same input return equal public state."""
        target = tmp_path / "f.ldif"

        first = svc.parse_and_validate_ldif(target)
        second = svc.parse_and_validate_ldif(target)

        assert first.success and second.success
        assert first.unwrap().model_dump() == second.unwrap().model_dump()

    def test_parse_and_validate_ldif_empty_path_fails(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
    ) -> None:
        """An empty path surfaces a required-path failure via the result channel."""
        result = svc.parse_and_validate_ldif("")

        assert result.failure
        assert result.error is not None
        assert "required" in result.error.lower()

    def test_run_data_quality_assessment_equals_parse_and_validate(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """Quality assessment exposes the same contract as parse+validate."""
        target = tmp_path / "f.ldif"

        assessed = svc.run_data_quality_assessment(target)
        parsed = svc.parse_and_validate_ldif(target)

        assert assessed.success and parsed.success
        assert assessed.unwrap().model_dump() == parsed.unwrap().model_dump()

    def test_generate_and_write_models_produces_staging_and_analytics(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
        entries: t.SequenceOf[t.JsonMapping],
    ) -> None:
        """Model generation yields one staging and one analytics model."""
        result = svc.generate_and_write_models(entries)

        assert result.success
        data = result.unwrap()
        assert data.models_generated == 2
        assert c.DbtLdif.STAGING_MODEL_NAME in data.model_names
        assert c.DbtLdif.ANALYTICS_MODEL_NAME in data.model_names

    def test_generate_and_write_models_empty_entries_yields_no_models(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
    ) -> None:
        """No entries produce an empty, well-formed generation result."""
        result = svc.generate_and_write_models([])

        assert result.success
        data = result.unwrap()
        assert data.models_generated == 0
        assert data.model_names == []

    def test_run_complete_workflow_all_stages_completes(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """The full workflow reports completion with model and transform state."""
        result = svc.run_complete_workflow(
            tmp_path / "f.ldif",
            generate_models=True,
            run_transformations=True,
        )

        assert result.success
        data = result.unwrap()
        assert data.workflow_status == c.DbtLdif.WORKFLOW_STATUS_COMPLETED
        assert data.entry_count == 1
        assert data.validation_status == c.DbtLdif.VALIDATION_STATUS_PASSED
        assert data.models_generated == 2
        assert data.transformation_status == c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS

    @pytest.mark.parametrize(
        ("generate_models", "run_transformations", "expected_models"),
        [
            (True, False, 2),
            (False, True, 0),
            (False, False, 0),
        ],
    )
    def test_run_complete_workflow_honors_stage_flags(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
        generate_models: bool,
        run_transformations: bool,
        expected_models: int,
    ) -> None:
        """Optional stages are skipped when their flags are disabled."""
        result = svc.run_complete_workflow(
            tmp_path / "f.ldif",
            generate_models=generate_models,
            run_transformations=run_transformations,
        )

        assert result.success
        data = result.unwrap()
        assert data.workflow_status == c.DbtLdif.WORKFLOW_STATUS_COMPLETED
        assert data.models_generated == expected_models
        expected_status = (
            c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS if run_transformations else ""
        )
        assert data.transformation_status == expected_status

    def test_run_complete_workflow_records_source_file(
        self,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """The workflow result echoes the LDIF source path it processed."""
        target = tmp_path / "source.ldif"

        result = svc.run_complete_workflow(target)

        assert result.success
        assert result.unwrap().ldif_file == str(target)


__all__: list[str] = ["TestsFlextDbtLdifServices"]
