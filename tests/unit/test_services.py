"""Unit tests for DBT services functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import cast

import pytest
from flext_core import FlextCore

from flext_dbt_ldif import FlextDbtLdifService, FlextLdifDbtModel


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
    entries: FlextCore.Types.List = [object(), object()]

    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: FlextCore.Result[FlextCore.Types.List].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: FlextCore.Result[FlextCore.Types.Dict].ok({"quality_score": 0.9}),
    )
    monkeypatch.setattr(
        svc.client,
        "transform_with_dbt",
        lambda _e, _m: FlextCore.Result[FlextCore.Types.Dict].ok({"ran": True}),
    )

    # Model generator behavior
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextCore.Result[FlextCore.Types.List].ok(
            [cast("object", FlextLdifDbtModel("stg_persons", "d", []))],
        ),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_analytics_models",
        lambda _m: FlextCore.Result[FlextCore.Types.List].ok(
            [cast("object", FlextLdifDbtModel("analytics_ldif_insights", "d", []))],
        ),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "write_models_to_disk",
        lambda _models, *, _overwrite=False: FlextCore.Result[
            dict[str, str | FlextCore.Types.StringList]
        ].ok(
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
    entries: FlextCore.Types.List = [object()]
    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: FlextCore.Result[FlextCore.Types.List].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: FlextCore.Result[FlextCore.Types.Dict].ok({"quality_score": 0.88}),
    )

    # analyze_ldif_schema + generate_staging_models paths
    monkeypatch.setattr(
        svc.model_generator,
        "analyze_ldif_schema",
        lambda _e: FlextCore.Result[FlextCore.Types.Dict].ok({"total_entries": 1}),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextCore.Result[FlextCore.Types.List].ok(
            [cast("object", FlextLdifDbtModel("stg_persons", "d", []))],
        ),
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
    monkeypatch.setattr(
        svc.model_generator,
        "analyze_ldif_schema",
        lambda _e: FlextCore.Result[FlextCore.Types.Dict].ok({"total_entries": 0}),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextCore.Result[FlextCore.Types.List].ok(
            [cast("object", FlextLdifDbtModel("stg_persons", "d", []))],
        ),
    )

    result = svc.generate_model_documentation([])
    assert result.is_success
    doc = result.value or {}
    assert "project_info" in doc
