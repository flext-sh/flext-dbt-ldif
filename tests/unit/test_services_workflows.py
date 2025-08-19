"""Test services workflows.

This module tests the services workflows of flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path
from typing import Any, cast

import pytest
from flext_core import FlextResult

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
    entries: list[object] = [object(), object()]

    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: FlextResult[None].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: FlextResult[None].ok({"quality_score": 0.9}),
    )
    monkeypatch.setattr(
        svc.client,
        "transform_with_dbt",
        lambda _e, _m: FlextResult[None].ok({"ran": True}),
    )

    # Model generator behavior
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextResult[None].ok(
            [cast("Any", FlextLdifDbtModel("stg_persons", "d", []))],
        ),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_analytics_models",
        lambda _m: FlextResult[None].ok(
            [cast("Any", FlextLdifDbtModel("analytics_ldif_insights", "d", []))],
        ),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "write_models_to_disk",
        lambda _models, *, _overwrite=False: FlextResult[None].ok(
            {"written_files": ["a.sql"], "output_dir": str(tmp_path)},
        ),
    )

    result = svc.run_complete_workflow(
        tmp_path / "f.ldif",
        generate_models=True,
        run_transformations=True,
        model_names=["m1"],
    )
    assert result.success
    data = result.data or {}
    # Allow completed pipeline via workflow_status key
    assert data.get("workflow_status") == "completed"


def test_run_data_quality_assessment(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test data quality assessment."""
    entries: list[object] = [object()]
    monkeypatch.setattr(
        svc.client,
        "parse_ldif_file",
        lambda _fp: FlextResult[None].ok(entries),
    )
    monkeypatch.setattr(
        svc.client,
        "validate_ldif_data",
        lambda _e: FlextResult[None].ok({"quality_score": 0.88}),
    )

    # analyze_ldif_schema + generate_staging_models paths
    monkeypatch.setattr(
        svc.model_generator,
        "analyze_ldif_schema",
        lambda _e: FlextResult[None].ok({"total_entries": 1}),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextResult[None].ok(
            [cast("Any", FlextLdifDbtModel("stg_persons", "d", []))],
        ),
    )

    result = svc.run_data_quality_assessment(tmp_path / "f.ldif")
    assert result.success
    summary = (result.data or {}).get("quality_summary", {})
    assert isinstance(summary, dict)


def test_generate_model_documentation(
    monkeypatch: pytest.MonkeyPatch,
    svc: FlextDbtLdifService,
) -> None:
    """Test model documentation generation."""
    monkeypatch.setattr(
        svc.model_generator,
        "analyze_ldif_schema",
        lambda _e: FlextResult[None].ok({"total_entries": 0}),
    )
    monkeypatch.setattr(
        svc.model_generator,
        "generate_staging_models",
        lambda _e: FlextResult[None].ok(
            [cast("Any", FlextLdifDbtModel("stg_persons", "d", []))],
        ),
    )

    result = svc.generate_model_documentation([])
    assert result.success
    doc = result.data or {}
    assert "project_info" in doc
