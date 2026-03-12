"""Unit tests for DBT services functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_core import r

from flext_dbt_ldif import FlextDbtLdifService, t
from flext_dbt_ldif.models import FlextDbtLdifModels


@pytest.fixture
def svc(tmp_path: Path) -> FlextDbtLdifService:
    """Create a test service."""
    return FlextDbtLdifService(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch, svc: FlextDbtLdifService, tmp_path: Path
) -> None:
    """Test parsing and validating LDIF succeeds."""
    entries: list[dict[str, object]] = [{"dn": "cn=test,dc=example,dc=org"}]
    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: r[list[t.ConfigurationMapping]].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: r[t.ConfigurationMapping].ok({"quality_score": 0.9}),
    )
    result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")
    assert result.is_success
    data = result.value or {}
    assert data["entry_count"] == 1
    assert data["entries"] == entries


def test_parse_and_validate_ldif_parse_fails(
    monkeypatch: pytest.MonkeyPatch, svc: FlextDbtLdifService, tmp_path: Path
) -> None:
    """Test parse failure propagates."""
    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: r[list[t.ConfigurationMapping]].fail("Parse error"),
    )
    result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")
    assert result.is_failure


def test_generate_and_write_models_ok(
    monkeypatch: pytest.MonkeyPatch, svc: FlextDbtLdifService
) -> None:
    """Test model generation succeeds."""
    staging_model = FlextDbtLdifModels.DbtModel(
        name="stg_ldif_entries",
        dbt_model_type="staging",
        ldif_source="ldif_entries",
        sql_content="select * from raw",
    )
    analytics_model = FlextDbtLdifModels.DbtModel(
        name="analytics_ldif_insights",
        dbt_model_type="analytics",
        ldif_source="ldif_entries",
        sql_content="select * from stg",
    )
    gen = svc.model_generator
    object.__setattr__(
        gen,
        "generate_staging_models",
        lambda _e: r[list[FlextDbtLdifModels.DbtModel]].ok([staging_model]),
    )
    object.__setattr__(
        gen,
        "generate_analytics_models",
        lambda _m: r[list[FlextDbtLdifModels.DbtModel]].ok([analytics_model]),
    )
    entries: list[dict[str, object]] = [{"dn": "cn=test,dc=example,dc=org"}]
    result = svc.generate_and_write_models(entries)
    assert result.is_success
    data = result.value or {}
    assert data["models_generated"] == 2
    model_names = data["model_names"]
    assert isinstance(model_names, list)
    assert "stg_ldif_entries" in model_names
    assert "analytics_ldif_insights" in model_names


def test_run_complete_workflow_all(
    monkeypatch: pytest.MonkeyPatch, svc: FlextDbtLdifService, tmp_path: Path
) -> None:
    """Test complete workflow with all stages."""
    entries: list[dict[str, object]] = [{"dn": "cn=test,dc=example,dc=org"}]
    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: r[list[t.ConfigurationMapping]].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: r[t.ConfigurationMapping].ok({"quality_score": 0.9}),
    )
    monkeypatch.setattr(
        svc.client,
        "transform_with_dbt",
        lambda _e, _m: r[t.ConfigurationMapping].ok({"ran": True}),
    )
    staging_model = FlextDbtLdifModels.DbtModel(
        name="stg_ldif_entries",
        dbt_model_type="staging",
        ldif_source="ldif_entries",
        sql_content="select * from raw",
    )
    analytics_model = FlextDbtLdifModels.DbtModel(
        name="analytics_ldif_insights",
        dbt_model_type="analytics",
        ldif_source="ldif_entries",
        sql_content="select * from stg",
    )
    gen = svc.model_generator
    object.__setattr__(
        gen,
        "generate_staging_models",
        lambda _e: r[list[FlextDbtLdifModels.DbtModel]].ok([staging_model]),
    )
    object.__setattr__(
        gen,
        "generate_analytics_models",
        lambda _m: r[list[FlextDbtLdifModels.DbtModel]].ok([analytics_model]),
    )
    result = svc.run_complete_workflow(
        tmp_path / "f.ldif",
        generate_models=True,
        run_transformations=True,
        model_names=["m1"],
    )
    assert result.is_success
    data = result.value or {}
    assert data.get("workflow_status") == "completed"


def test_run_data_quality_assessment(
    monkeypatch: pytest.MonkeyPatch, svc: FlextDbtLdifService, tmp_path: Path
) -> None:
    """Test data quality assessment delegates to parse_and_validate."""
    entries: list[dict[str, object]] = [{"dn": "cn=test,dc=example,dc=org"}]
    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: r[list[t.ConfigurationMapping]].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: r[t.ConfigurationMapping].ok({"quality_score": 0.88}),
    )
    result = svc.run_data_quality_assessment(tmp_path / "f.ldif")
    assert result.is_success
    data = result.value or {}
    assert "entries" in data
    assert "entry_count" in data
