"""Unit tests for DBT services functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import pytest

from flext_core import r
from flext_dbt_ldif import FlextDbtLdifServiceMixin
from tests import m, t


@pytest.fixture
def svc(tmp_path: Path) -> FlextDbtLdifServiceMixin.Service:
    """Create a test service."""
    return FlextDbtLdifServiceMixin.Service(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifServiceMixin.Service,
    tmp_path: Path,
) -> None:
    """Test parsing and validating LDIF succeeds."""
    entries: Sequence[t.ContainerValueMapping] = [
        {"dn": "cn=test,dc=example,dc=org"},
    ]

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[Sequence[t.ContainerValueMapping]]:
        return r[Sequence[t.ContainerValueMapping]].ok(entries)

    def _validate_ldif_data(
        _entries: Sequence[t.ContainerValueMapping],
    ) -> r[m.DbtLdif.LdifValidationResult]:
        return r[m.DbtLdif.LdifValidationResult].ok(
            m.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.9,
                validation_status="passed",
            ),
        )


    result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")
    assert result.is_success
    data = result.value
    assert data is not None
    assert data.entry_count == 1
    quality_score = data.quality_score
    assert isinstance(quality_score, float)
    assert 0.89 < quality_score < 0.91
    assert data.validation_status == "passed"


def test_parse_and_validate_ldif_parse_fails(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifServiceMixin.Service,
    tmp_path: Path,
) -> None:
    """Test parse failure propagates."""

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[Sequence[t.ContainerValueMapping]]:
        return r[Sequence[t.ContainerValueMapping]].fail("Parse error")

    result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")
    assert result.is_failure


def test_generate_and_write_models_ok(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifServiceMixin.Service,
) -> None:
    """Test model generation succeeds."""
    staging_model = m.DbtLdif.DbtModel(
        name="stg_ldif_entries",
        dbt_model_type="staging",
        ldif_source="ldif_entries",
        sql_content="select * from raw",
        columns=[],
        dependencies=[],
    )
    analytics_model = m.DbtLdif.DbtModel(
        name="analytics_ldif_insights",
        dbt_model_type="analytics",
        ldif_source="ldif_entries",
        sql_content="select * from stg",
        columns=[],
        dependencies=["stg_ldif_entries"],
    )

    def _generate_staging_models(
        _entries: Sequence[t.ContainerValueMapping],
    ) -> r[Sequence[m.DbtLdif.DbtModel]]:
        return r[Sequence[m.DbtLdif.DbtModel]].ok([staging_model])

    def _generate_analytics_models(
        _models: Sequence[m.DbtLdif.DbtModel],
    ) -> r[Sequence[m.DbtLdif.DbtModel]]:
        return r[Sequence[m.DbtLdif.DbtModel]].ok([analytics_model])

    gen = svc.model_generator
    object.__setattr__(gen, "generate_staging_models", _generate_staging_models)
    object.__setattr__(gen, "generate_analytics_models", _generate_analytics_models)

    entries: Sequence[t.ContainerValueMapping] = [
        {"dn": "cn=test,dc=example,dc=org"},
    ]
    result = svc.generate_and_write_models(entries)
    assert result.is_success
    data = result.value
    assert data is not None
    assert data.models_generated == 2
    assert "stg_ldif_entries" in data.model_names
    assert "analytics_ldif_insights" in data.model_names


def test_run_complete_workflow_all(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifServiceMixin.Service,
    tmp_path: Path,
) -> None:
    """Test complete workflow with all stages."""
    entries: Sequence[t.ContainerValueMapping] = [
        {"dn": "cn=test,dc=example,dc=org"},
    ]

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[Sequence[t.ContainerValueMapping]]:
        return r[Sequence[t.ContainerValueMapping]].ok(entries)

    def _validate_ldif_data(
        _entries: Sequence[t.ContainerValueMapping],
    ) -> r[m.DbtLdif.LdifValidationResult]:
        return r[m.DbtLdif.LdifValidationResult].ok(
            m.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.9,
                validation_status="passed",
            ),
        )

    def _transform_with_dbt(
        _entries: Sequence[t.ContainerValueMapping],
        _model_names: t.StrSequence | None,
    ) -> r[m.DbtLdif.DbtTransformationResult]:
        return r[m.DbtLdif.DbtTransformationResult].ok(
            m.DbtLdif.DbtTransformationResult(
                records=1,
                models=["m1"],
                status="success",
            ),
        )

    staging_model = m.DbtLdif.DbtModel(
        name="stg_ldif_entries",
        dbt_model_type="staging",
        ldif_source="ldif_entries",
        sql_content="select * from raw",
        columns=[],
        dependencies=[],
    )
    analytics_model = m.DbtLdif.DbtModel(
        name="analytics_ldif_insights",
        dbt_model_type="analytics",
        ldif_source="ldif_entries",
        sql_content="select * from stg",
        columns=[],
        dependencies=["stg_ldif_entries"],
    )

    def _generate_staging_models(
        _entries: Sequence[t.ContainerValueMapping],
    ) -> r[Sequence[m.DbtLdif.DbtModel]]:
        return r[Sequence[m.DbtLdif.DbtModel]].ok([staging_model])

    def _generate_analytics_models(
        _models: Sequence[m.DbtLdif.DbtModel],
    ) -> r[Sequence[m.DbtLdif.DbtModel]]:
        return r[Sequence[m.DbtLdif.DbtModel]].ok([analytics_model])

    gen = svc.model_generator
    object.__setattr__(gen, "generate_staging_models", _generate_staging_models)
    object.__setattr__(gen, "generate_analytics_models", _generate_analytics_models)

    result = svc.run_complete_workflow(
        tmp_path / "f.ldif",
        generate_models=True,
        run_transformations=True,
        model_names=["m1"],
    )
    assert result.is_success
    data = result.value
    assert data is not None
    assert data.workflow_status == "completed"


def test_run_data_quality_assessment(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifServiceMixin.Service,
    tmp_path: Path,
) -> None:
    """Test data quality assessment delegates to parse_and_validate."""
    entries: Sequence[t.ContainerValueMapping] = [
        {"dn": "cn=test,dc=example,dc=org"},
    ]

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[Sequence[t.ContainerValueMapping]]:
        return r[Sequence[t.ContainerValueMapping]].ok(entries)

    def _validate_ldif_data(
        _entries: Sequence[t.ContainerValueMapping],
    ) -> r[m.DbtLdif.LdifValidationResult]:
        return r[m.DbtLdif.LdifValidationResult].ok(
            m.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.88,
                validation_status="passed",
            ),
        )


    result = svc.run_data_quality_assessment(tmp_path / "f.ldif")
    assert result.is_success
    data = result.value
    assert data is not None
    assert data.entry_count == 1
