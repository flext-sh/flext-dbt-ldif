"""Test services and API for FLEXT DBT LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

import pytest
from flext_core import FlextTypes, r

from flext_dbt_ldif import FlextDbtLdif, FlextDbtLdifService
from flext_dbt_ldif.models import FlextDbtLdifModels


@pytest.fixture
def service(tmp_path: Path) -> FlextDbtLdifService:
    """Create a test service."""
    return FlextDbtLdifService(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch, service: FlextDbtLdifService, tmp_path: Path
) -> None:
    """Test parsing and validating LDIF via service."""
    entries: Sequence[Mapping[str, FlextTypes.ContainerValue]] = [
        {"dn": "cn=test,dc=example,dc=org"}
    ]

    def _parse_ldif_file(
        _ldif_file: Path | str,
    ) -> r[Sequence[Mapping[str, FlextTypes.ContainerValue]]]:
        return r[Sequence[Mapping[str, FlextTypes.ContainerValue]]].ok(entries)

    def _validate_ldif_data(
        _entries: Sequence[Mapping[str, FlextTypes.ContainerValue]],
    ) -> r[FlextDbtLdifModels.DbtLdif.LdifValidationResult]:
        return r[FlextDbtLdifModels.DbtLdif.LdifValidationResult].ok(
            FlextDbtLdifModels.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.91,
                validation_status="passed",
            )
        )

    monkeypatch.setattr(
        service.client,
        "parse_ldif_file",
        _parse_ldif_file,
    )
    monkeypatch.setattr(
        service.client,
        "validate_ldif_data",
        _validate_ldif_data,
    )
    result = service.parse_and_validate_ldif(tmp_path / "x.ldif")
    assert result.is_success
    data = result.value
    assert data is not None
    assert data.entry_count == 1


def test_generate_and_write_models_ok(
    monkeypatch: pytest.MonkeyPatch, service: FlextDbtLdifService
) -> None:
    """Test generating and writing models via service."""
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
        _entries: Sequence[Mapping[str, FlextTypes.ContainerValue]],
    ) -> r[Sequence[FlextDbtLdifModels.DbtLdif.DbtModel]]:
        return r[Sequence[FlextDbtLdifModels.DbtLdif.DbtModel]].ok([staging_model])

    def _generate_analytics_models(
        _models: Sequence[FlextDbtLdifModels.DbtLdif.DbtModel],
    ) -> r[Sequence[FlextDbtLdifModels.DbtLdif.DbtModel]]:
        return r[Sequence[FlextDbtLdifModels.DbtLdif.DbtModel]].ok([analytics_model])

    gen = service.model_generator
    object.__setattr__(gen, "generate_staging_models", _generate_staging_models)
    object.__setattr__(gen, "generate_analytics_models", _generate_analytics_models)
    entries: Sequence[Mapping[str, FlextTypes.ContainerValue]] = [
        {"dn": "cn=test,dc=example,dc=org"}
    ]
    result = service.generate_and_write_models(entries)
    assert result.is_success
    data = result.value
    assert data is not None
    assert data.models_generated == 2


def test_api_process_ldif_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Test FlextDbtLdif.process_ldif_file delegates correctly."""

    def _run(
        _self: FlextDbtLdifService,
        ldif_file: Path | str,
        *,
        generate_models: bool = True,
        run_transformations: bool = False,
        model_names: Sequence[str] | None = None,
    ) -> r[FlextDbtLdifModels.DbtLdif.WorkflowResult]:
        return r[FlextDbtLdifModels.DbtLdif.WorkflowResult].ok(
            FlextDbtLdifModels.DbtLdif.WorkflowResult(
                ldif_file=str(ldif_file),
                entry_count=0,
                validation_status="passed",
                workflow_status="completed",
            )
        )

    monkeypatch.setattr(FlextDbtLdifService, "run_complete_workflow", _run)
    api = FlextDbtLdif()
    result = api.process_ldif_file(tmp_path / "f.ldif")
    assert result.is_success


def test_api_validate_ldif_quality(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Test FlextDbtLdif.validate_ldif_quality delegates correctly."""

    def _run_quality(
        _self: FlextDbtLdifService, _ldif_file: Path | str
    ) -> r[FlextDbtLdifModels.DbtLdif.ParseValidationResult]:
        return r[FlextDbtLdifModels.DbtLdif.ParseValidationResult].ok(
            FlextDbtLdifModels.DbtLdif.ParseValidationResult(
                entry_count=0,
                quality_score=1.0,
                validation_status="passed",
            )
        )

    monkeypatch.setattr(
        FlextDbtLdifService, "run_data_quality_assessment", _run_quality
    )
    api = FlextDbtLdif()
    assert api.validate_ldif_quality(tmp_path / "f.ldif").is_success


def test_api_generate_ldif_models(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """Test FlextDbtLdif.generate_ldif_models delegates correctly."""

    def _gen_models(
        _self: FlextDbtLdifService,
        _entries: Sequence[Mapping[str, FlextTypes.ContainerValue]],
        *,
        overwrite: bool = False,
    ) -> r[FlextDbtLdifModels.DbtLdif.ModelGenerationResult]:
        _ = overwrite
        return r[FlextDbtLdifModels.DbtLdif.ModelGenerationResult].ok(
            FlextDbtLdifModels.DbtLdif.ModelGenerationResult(
                models_generated=0, model_names=[]
            )
        )

    monkeypatch.setattr(FlextDbtLdifService, "generate_and_write_models", _gen_models)
    api = FlextDbtLdif()
    assert api.generate_ldif_models(tmp_path / "f.ldif").is_success
