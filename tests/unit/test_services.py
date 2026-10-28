"""Behavior contract for FlextDbtLdifService services — public API only.

Copyright (c) 2026 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from pathlib import Path

import pytest

from flext_dbt_ldif.services.service import FlextDbtLdifService
from tests import c, t, tm


@pytest.fixture
def svc(tmp_path: Path) -> FlextDbtLdifService.Service:
    """Create a service backed by a real project directory.

    Returns:
        The resulting ``FlextDbtLdifService.Service``.

    """
    return FlextDbtLdifService.Service(project_dir=tmp_path)


@pytest.fixture
def entries() -> t.SequenceOf[t.JsonMapping]:
    """Provide a minimal LDIF entry payload accepted by the public API.

    Returns:
        The resulting ``t.SequenceOf[t.JsonMapping]``.

    """
    return [{"dn": "cn=test,dc=example,dc=org"}]


class TestsFlextDbtLdifServices:
    """Behavior contract for FlextDbtLdifService.Service workflows."""

    @staticmethod
    def test_run_data_quality_assessment(
        svc: FlextDbtLdifService.Service,
        tmp_path: Path,
    ) -> None:
        """Data quality assessment parses, validates, and reports entry metrics."""
        target = tmp_path / "f.ldif"
        target.write_text(
            "dn: cn=test,dc=example,dc=org\nobjectClass: top\n\n",
            encoding="utf-8",
        )

        result = svc.run_data_quality_assessment(target)

        tm.ok(result)
        data = result.unwrap()
        tm.that(data, none=False)
        tm.that(data.entry_count, eq=1)
        tm.that(data.quality_score, eq=c.DbtLdif.DEFAULT_QUALITY_SCORE)
        tm.that(data.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)

    @staticmethod
    def test_parse_and_validate_ldif_returns_quality_metrics(
        svc: FlextDbtLdifService.Service,
        tmp_path: Path,
    ) -> None:
        """A valid LDIF path yields a passed validation with a quality score."""
        result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")

        tm.ok(result)
        data = result.unwrap()
        tm.that(data.entry_count, eq=1)
        tm.that(data.quality_score, eq=c.DbtLdif.DEFAULT_QUALITY_SCORE)
        tm.that(data.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)

    @staticmethod
    def test_parse_and_validate_ldif_is_idempotent(
        svc: FlextDbtLdifService.Service,
        tmp_path: Path,
    ) -> None:
        """Repeated calls with the same input return equal public state."""
        target = tmp_path / "f.ldif"

        first = svc.parse_and_validate_ldif(target)
        second = svc.parse_and_validate_ldif(target)

        tm.ok(first)
        tm.ok(second)
        tm.that(first.unwrap().model_dump(), eq=second.unwrap().model_dump())

    @staticmethod
    def test_parse_and_validate_ldif_empty_path_fails(
        svc: FlextDbtLdifService.Service,
    ) -> None:
        """An empty path surfaces a required-path failure via the result channel."""
        result = svc.parse_and_validate_ldif("")

        error = tm.fail(result)
        tm.that(error.lower(), has="required")

    @staticmethod
    def test_run_data_quality_assessment_equals_parse_and_validate(
        svc: FlextDbtLdifService.Service,
        tmp_path: Path,
    ) -> None:
        """Quality assessment exposes the same contract as parse+validate."""
        target = tmp_path / "f.ldif"

        assessed = svc.run_data_quality_assessment(target)
        parsed = svc.parse_and_validate_ldif(target)

        tm.ok(assessed)
        tm.ok(parsed)
        tm.that(assessed.unwrap().model_dump(), eq=parsed.unwrap().model_dump())

    @staticmethod
    def test_generate_and_write_models_produces_staging_and_analytics(
        svc: FlextDbtLdifService.Service,
        entries: t.SequenceOf[t.JsonMapping],
    ) -> None:
        """Model generation yields one staging and one analytics model."""
        result = svc.generate_and_write_models(entries)

        tm.ok(result)
        data = result.unwrap()
        tm.that(data.models_generated, eq=2)
        tm.that(data.model_names, has=c.DbtLdif.STAGING_MODEL_NAME)
        tm.that(data.model_names, has=c.DbtLdif.ANALYTICS_MODEL_NAME)

    @staticmethod
    def test_generate_and_write_models_empty_entries_yields_no_models(
        svc: FlextDbtLdifService.Service,
    ) -> None:
        """No entries produce an empty, well-formed generation result."""
        result = svc.generate_and_write_models([])

        tm.ok(result)
        data = result.unwrap()
        tm.that(data.models_generated, eq=0)
        tm.that(data.model_names, eq=[])

    @staticmethod
    def test_run_complete_workflow_all_stages_completes(
        svc: FlextDbtLdifService.Service,
        tmp_path: Path,
    ) -> None:
        """The full workflow reports completion with model and transform state."""
        result = svc.run_complete_workflow(
            tmp_path / "f.ldif",
            generate_models=True,
            run_transformations=True,
        )

        tm.ok(result)
        data = result.unwrap()
        tm.that(data.workflow_status, eq=c.DbtLdif.WORKFLOW_STATUS_COMPLETED)
        tm.that(data.entry_count, eq=1)
        tm.that(data.validation_status, eq=c.DbtLdif.VALIDATION_STATUS_PASSED)
        tm.that(data.models_generated, eq=2)
        tm.that(data.transformation_status, eq=c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS)

    @staticmethod
    @pytest.mark.parametrize(
        ("generate_models", "run_transformations", "expected_models"),
        [(True, False, 2), (False, True, 0), (False, False, 0)],
    )
    def test_run_complete_workflow_honors_stage_flags(
        svc: FlextDbtLdifService.Service,
        tmp_path: Path,
        *,
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

        tm.ok(result)
        data = result.unwrap()
        tm.that(data.workflow_status, eq=c.DbtLdif.WORKFLOW_STATUS_COMPLETED)
        tm.that(data.models_generated, eq=expected_models)
        expected_status = (
            c.DbtLdif.TRANSFORMATION_STATUS_SUCCESS if run_transformations else ""
        )
        tm.that(data.transformation_status, eq=expected_status)

    @staticmethod
    def test_run_complete_workflow_records_source_file(
        svc: FlextDbtLdifService.Service,
        tmp_path: Path,
    ) -> None:
        """The workflow result echoes the LDIF source path it processed."""
        target = tmp_path / "source.ldif"

        result = svc.run_complete_workflow(target)

        tm.ok(result)
        tm.that(result.unwrap().ldif_file, eq=str(target))
