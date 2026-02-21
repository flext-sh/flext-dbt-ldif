"""Unit tests for DBT services functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

import pytest
from flext_dbt_ldif import t
from flext_core import FlextResult

from flext_dbt_ldif import FlextDbtLdifModels, FlextDbtLdifService


@pytest.fixture
def svc(tmp_path: Path) -> FlextDbtLdifService:
    """Create a test service."""
    return FlextDbtLdifService(project_dir=tmp_path)


def test_run_complete_workflow_all(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test complete workflow with all entities."""
    entries: list[t.GeneralValueType] = [object(), object()]

    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: FlextResult[list[t.GeneralValueType]].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: FlextResult[dict[str, t.GeneralValueType]].ok({
            "quality_score": 0.9
        }),
    )
    monkeypatch.setattr(
        svc.client,
        "transform_with_dbt",
        lambda _e, _m: FlextResult[dict[str, t.GeneralValueType]].ok({"ran": True}),
    )

    # Model generator behavior
    staging_model: t.GeneralValueType = FlextDbtLdifModels("stg_persons", "d", [])
    analytics_model: t.GeneralValueType = FlextDbtLdifModels(
        "analytics_ldif_insights",
        "d",
        [],
    )

    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextResult[list[t.GeneralValueType]].ok([staging_model]),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_analytics_models",
        lambda _m: FlextResult[list[t.GeneralValueType]].ok([analytics_model]),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "write_models_to_disk",
        lambda _models, *, _overwrite=False: FlextResult[dict[str, str | list[str]]].ok(
            {"written_files": ["a.sql"], "output_dir": str(tmp_path)},
        ),
    )

    result = svc.run_complete_workflow(
        tmp_path / "f.ldif",
        generate_models=True,
        run_transformations=True,
        model_names=["m1"],
    )
    assert result.is_success
    data = result.value or {}
    # Allow completed pipeline via workflow_status key
    assert data.get("workflow_status") == "completed"


def test_run_data_quality_assessment(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test data quality assessment."""
    entries: list[t.GeneralValueType] = [object()]
    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: FlextResult[list[t.GeneralValueType]].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: FlextResult[dict[str, t.GeneralValueType]].ok({
            "quality_score": 0.88
        }),
    )

    # analyze_ldif_schema + generate_staging_models paths
    staging_model3: t.GeneralValueType = FlextDbtLdifModels("stg_persons", "d", [])

    monkeypatch.setattr(
        svc.model_generator,
        "analyze_ldif_schema",
        lambda _e: FlextResult[dict[str, t.GeneralValueType]].ok({"total_entries": 1}),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextResult[list[t.GeneralValueType]].ok([staging_model3]),
    )

    result = svc.run_data_quality_assessment(tmp_path / "f.ldif")
    assert result.is_success
    summary = (result.value or {}).get("quality_summary", {})
    assert isinstance(summary, dict)


def test_generate_model_documentation(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifService,
) -> None:
    """Test model documentation generation."""
    staging_model4: t.GeneralValueType = FlextDbtLdifModels("stg_persons", "d", [])

    monkeypatch.setattr(
        svc.model_generator,
        "analyze_ldif_schema",
        lambda _e: FlextResult[dict[str, t.GeneralValueType]].ok({"total_entries": 0}),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextResult[list[t.GeneralValueType]].ok([staging_model4]),
    )

    result = svc.generate_model_documentation([])
    assert result.is_success
    doc = result.value or {}
    assert "project_info" in doc
