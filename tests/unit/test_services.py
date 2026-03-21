"""Unit tests for DBT services functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_core import r
from flext_core.typings import FlextTypes

from flext_dbt_ldif import FlextDbtLdifService
from flext_dbt_ldif.models import FlextDbtLdifModels


@pytest.fixture
def svc(tmp_path: Path) -> FlextDbtLdifService:
    """Create a test service."""
    return FlextDbtLdifService(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test parsing and validating LDIF succeeds."""
    entries: list[dict[str, FlextTypes.ContainerValue]] = [
        {"dn": "cn=test,dc=example,dc=org"}
    ]

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[list[dict[str, FlextTypes.ContainerValue]]]:
        return r[list[dict[str, FlextTypes.ContainerValue]]].ok(entries)

    def _validate_ldif_data(
        _entries: list[dict[str, FlextTypes.ContainerValue]],
    ) -> r[FlextDbtLdifModels.DbtLdif.LdifValidationResult]:
        return r[FlextDbtLdifModels.DbtLdif.LdifValidationResult].ok(
            FlextDbtLdifModels.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.9,
                validation_status="passed",
            )
        )

    monkeypatch.setattr(svc.client, "parse_ldif_file", _parse_ldif_file)
    monkeypatch.setattr(svc.client, "validate_ldif_data", _validate_ldif_data)

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
    svc: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test parse failure propagates."""

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[list[dict[str, FlextTypes.ContainerValue]]]:
        return r[list[dict[str, FlextTypes.ContainerValue]]].fail("Parse error")

    monkeypatch.setattr(svc.client, "parse_ldif_file", _parse_ldif_file)
    result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")
    assert result.is_failure


def test_generate_and_write_models_ok(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifService,
) -> None:
    """Test model generation succeeds."""
    staging_model = FlextDbtLdifModels.DbtLdif.DbtModel(
        name="stg_ldif_entries",
        dbt_model_type="staging",
        ldif_source="ldif_entries",
        sql_content="select * from raw",
        columns=[],
        dependencies=[],
    )
    analytics_model = FlextDbtLdifModels.DbtLdif.DbtModel(
        name="analytics_ldif_insights",
        dbt_model_type="analytics",
        ldif_source="ldif_entries",
        sql_content="select * from stg",
        columns=[],
        dependencies=["stg_ldif_entries"],
    )

    def _generate_staging_models(
        _entries: list[dict[str, FlextTypes.ContainerValue]],
    ) -> r[list[FlextDbtLdifModels.DbtLdif.DbtModel]]:
        return r[list[FlextDbtLdifModels.DbtLdif.DbtModel]].ok([staging_model])

    def _generate_analytics_models(
        _models: list[FlextDbtLdifModels.DbtLdif.DbtModel],
    ) -> r[list[FlextDbtLdifModels.DbtLdif.DbtModel]]:
        return r[list[FlextDbtLdifModels.DbtLdif.DbtModel]].ok([analytics_model])

    gen = svc.model_generator
    object.__setattr__(gen, "generate_staging_models", _generate_staging_models)
    object.__setattr__(gen, "generate_analytics_models", _generate_analytics_models)

    entries: list[dict[str, FlextTypes.ContainerValue]] = [
        {"dn": "cn=test,dc=example,dc=org"}
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
    svc: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test complete workflow with all stages."""
    entries: list[dict[str, FlextTypes.ContainerValue]] = [
        {"dn": "cn=test,dc=example,dc=org"}
    ]

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[list[dict[str, FlextTypes.ContainerValue]]]:
        return r[list[dict[str, FlextTypes.ContainerValue]]].ok(entries)

    def _validate_ldif_data(
        _entries: list[dict[str, FlextTypes.ContainerValue]],
    ) -> r[FlextDbtLdifModels.DbtLdif.LdifValidationResult]:
        return r[FlextDbtLdifModels.DbtLdif.LdifValidationResult].ok(
            FlextDbtLdifModels.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.9,
                validation_status="passed",
            )
        )

    def _transform_with_dbt(
        _entries: list[dict[str, FlextTypes.ContainerValue]],
        _model_names: list[str] | None,
    ) -> r[FlextDbtLdifModels.DbtLdif.DbtTransformationResult]:
        return r[FlextDbtLdifModels.DbtLdif.DbtTransformationResult].ok(
            FlextDbtLdifModels.DbtLdif.DbtTransformationResult(
                records=1,
                models=["m1"],
                status="success",
            )
        )

    staging_model = FlextDbtLdifModels.DbtLdif.DbtModel(
        name="stg_ldif_entries",
        dbt_model_type="staging",
        ldif_source="ldif_entries",
        sql_content="select * from raw",
        columns=[],
        dependencies=[],
    )
    analytics_model = FlextDbtLdifModels.DbtLdif.DbtModel(
        name="analytics_ldif_insights",
        dbt_model_type="analytics",
        ldif_source="ldif_entries",
        sql_content="select * from stg",
        columns=[],
        dependencies=["stg_ldif_entries"],
    )

    def _generate_staging_models(
        _entries: list[dict[str, FlextTypes.ContainerValue]],
    ) -> r[list[FlextDbtLdifModels.DbtLdif.DbtModel]]:
        return r[list[FlextDbtLdifModels.DbtLdif.DbtModel]].ok([staging_model])

    def _generate_analytics_models(
        _models: list[FlextDbtLdifModels.DbtLdif.DbtModel],
    ) -> r[list[FlextDbtLdifModels.DbtLdif.DbtModel]]:
        return r[list[FlextDbtLdifModels.DbtLdif.DbtModel]].ok([analytics_model])

    monkeypatch.setattr(svc.client, "parse_ldif_file", _parse_ldif_file)
    monkeypatch.setattr(svc.client, "validate_ldif_data", _validate_ldif_data)
    monkeypatch.setattr(svc.client, "transform_with_dbt", _transform_with_dbt)
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
    svc: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test data quality assessment delegates to parse_and_validate."""
    entries: list[dict[str, FlextTypes.ContainerValue]] = [
        {"dn": "cn=test,dc=example,dc=org"}
    ]

    def _parse_ldif_file(
        _fp: Path | str,
    ) -> r[list[dict[str, FlextTypes.ContainerValue]]]:
        return r[list[dict[str, FlextTypes.ContainerValue]]].ok(entries)

    def _validate_ldif_data(
        _entries: list[dict[str, FlextTypes.ContainerValue]],
    ) -> r[FlextDbtLdifModels.DbtLdif.LdifValidationResult]:
        return r[FlextDbtLdifModels.DbtLdif.LdifValidationResult].ok(
            FlextDbtLdifModels.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.88,
                validation_status="passed",
            )
        )

    monkeypatch.setattr(svc.client, "parse_ldif_file", _parse_ldif_file)
    monkeypatch.setattr(svc.client, "validate_ldif_data", _validate_ldif_data)

    result = svc.run_data_quality_assessment(tmp_path / "f.ldif")
    assert result.is_success
    data = result.value
    assert data is not None
    assert data.entry_count == 1
