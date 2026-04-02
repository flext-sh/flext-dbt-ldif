"""Test services and API for FLEXT DBT LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import pytest

from flext_core import r
from flext_dbt_ldif import FlextDbtLdif, FlextDbtLdifServiceMixin
from tests import m, t

FlextDbtLdifService = FlextDbtLdifServiceMixin.Service


@pytest.fixture
def service(tmp_path: Path) -> FlextDbtLdifServiceMixin.Service:
    """Create a test service."""
    return FlextDbtLdifServiceMixin.Service(project_dir=tmp_path)


def test_parse_and_validate_ldif_ok(
    monkeypatch: pytest.MonkeyPatch,
    service: FlextDbtLdifService,
    tmp_path: Path,
) -> None:
    """Test parsing and validating LDIF via service."""
    entries: Sequence[t.ContainerValueMapping] = [
        {"dn": "cn=test,dc=example,dc=org"},
    ]

    def _parse_ldif_file(
        _ldif_file: Path | str,
    ) -> r[Sequence[t.ContainerValueMapping]]:
        return r[Sequence[t.ContainerValueMapping]].ok(entries)

    def _validate_ldif_data(
        _entries: Sequence[t.ContainerValueMapping],
    ) -> r[m.DbtLdif.LdifValidationResult]:
        return r[m.DbtLdif.LdifValidationResult].ok(
            m.DbtLdif.LdifValidationResult(
                total_entries=1,
                quality_score=0.91,
                validation_status="passed",
            ),
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
    monkeypatch: pytest.MonkeyPatch,
    service: FlextDbtLdifService,
) -> None:
    """Test generating and writing models via service."""
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

    gen = service.model_generator
    object.__setattr__(gen, "generate_staging_models", _generate_staging_models)
    object.__setattr__(gen, "generate_analytics_models", _generate_analytics_models)
    entries: Sequence[t.ContainerValueMapping] = [
        {"dn": "cn=test,dc=example,dc=org"},
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
        model_names: t.StrSequence | None = None,
    ) -> r[m.DbtLdif.WorkflowResult]:
        return r[m.DbtLdif.WorkflowResult].ok(
            m.DbtLdif.WorkflowResult(
                ldif_file=str(ldif_file),
                entry_count=0,
                validation_status="passed",
                workflow_status="completed",
            ),
        )

    monkeypatch.setattr(FlextDbtLdifService, "run_complete_workflow", _run)
    api = FlextDbtLdif()
    result = api.process_ldif_file(tmp_path / "f.ldif")
    assert result.is_success


def test_api_validate_ldif_quality(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Test FlextDbtLdif.validate_ldif_quality delegates correctly."""

    def _run_quality(
        _self: FlextDbtLdifService,
        _ldif_file: Path | str,
    ) -> r[m.DbtLdif.ParseValidationResult]:
        return r[m.DbtLdif.ParseValidationResult].ok(
            m.DbtLdif.ParseValidationResult(
                entry_count=0,
                quality_score=1.0,
                validation_status="passed",
            ),
        )

    monkeypatch.setattr(
        FlextDbtLdifService,
        "run_data_quality_assessment",
        _run_quality,
    )
    api = FlextDbtLdif()
    assert api.validate_ldif_quality(tmp_path / "f.ldif").is_success


def test_api_generate_ldif_models(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    """Test FlextDbtLdif.generate_ldif_models delegates correctly."""

    def _gen_models(
        _self: FlextDbtLdifService,
        _entries: Sequence[t.ContainerValueMapping],
        *,
        overwrite: bool = False,
    ) -> r[m.DbtLdif.ModelGenerationResult]:
        _ = overwrite
        return r[m.DbtLdif.ModelGenerationResult].ok(
            m.DbtLdif.ModelGenerationResult(
                models_generated=0,
                model_names=[],
            ),
        )

    monkeypatch.setattr(FlextDbtLdifService, "generate_and_write_models", _gen_models)
    api = FlextDbtLdif()
    assert api.generate_ldif_models(tmp_path / "f.ldif").is_success
