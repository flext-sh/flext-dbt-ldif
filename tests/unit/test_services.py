"""Behavior contract for FlextDbtLdifServiceMixin services — public API only.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

import pytest
from flext_tests import r

from flext_dbt_ldif.services.service import FlextDbtLdifServiceMixin
from tests.models import m
from tests.protocols import p
from tests.typings import t
from tests.unit._services_parts.data_quality import (
    TestsFlextDbtLdifServicesDataQuality,
)


@pytest.fixture
def svc(tmp_path: Path) -> FlextDbtLdifServiceMixin.Service:
    """Create a test service."""
    return FlextDbtLdifServiceMixin.Service(project_dir=tmp_path)


class TestsFlextDbtLdifServices(TestsFlextDbtLdifServicesDataQuality):
    """Behavior contract for FlextDbtLdifServiceMixin.Service workflows."""

    def test_parse_and_validate_ldif_ok(
        self,
        monkeypatch: pytest.MonkeyPatch,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """Test parsing and validating LDIF succeeds."""
        entries: t.SequenceOf[t.JsonMapping] = [
            {"dn": "cn=test,dc=example,dc=org"},
        ]

        def _parse_ldif_file(
            _fp: Path | str,
        ) -> p.Result[Sequence[t.JsonMapping]]:
            return r[Sequence[t.JsonMapping]].ok(entries)

        def _validate_ldif_data(
            entries: t.SequenceOf[t.JsonMapping],
        ) -> p.Result[m.DbtLdif.LdifValidationResult]:
            return r[m.DbtLdif.LdifValidationResult].ok(
                m.DbtLdif.LdifValidationResult(
                    total_entries=1,
                    quality_score=0.9,
                    validation_status="passed",
                ),
            )

        monkeypatch.setattr(svc.client, "parse_ldif_file", _parse_ldif_file)
        monkeypatch.setattr(svc.client, "validate_ldif_data", _validate_ldif_data)

        result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")
        assert result.success
        data = result.value
        assert data is not None
        assert data.entry_count == 1
        quality_score = data.quality_score
        assert isinstance(quality_score, float)
        assert 0.89 < quality_score < 0.91
        assert data.validation_status == "passed"

    def test_parse_and_validate_ldif_parse_fails(
        self,
        monkeypatch: pytest.MonkeyPatch,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """Test parse failure propagates."""

        def _parse_ldif_file(
            _fp: Path | str,
        ) -> p.Result[Sequence[t.JsonMapping]]:
            return r[Sequence[t.JsonMapping]].fail("Parse error")

        monkeypatch.setattr(svc.client, "parse_ldif_file", _parse_ldif_file)

        result = svc.parse_and_validate_ldif(tmp_path / "f.ldif")
        assert result.failure

    def test_generate_and_write_models_ok(
        self,
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
            entries: t.SequenceOf[t.JsonMapping],
        ) -> p.Result[Sequence[m.DbtLdif.DbtModel]]:
            return r[Sequence[m.DbtLdif.DbtModel]].ok([staging_model])

        def _generate_analytics_models(
            models: t.SequenceOf[m.DbtLdif.DbtModel],
        ) -> p.Result[Sequence[m.DbtLdif.DbtModel]]:
            return r[Sequence[m.DbtLdif.DbtModel]].ok([analytics_model])

        gen = svc.model_generator
        object.__setattr__(gen, "generate_staging_models", _generate_staging_models)
        object.__setattr__(gen, "generate_analytics_models", _generate_analytics_models)

        entries: t.SequenceOf[t.JsonMapping] = [
            {"dn": "cn=test,dc=example,dc=org"},
        ]
        result = svc.generate_and_write_models(entries)
        assert result.success
        data = result.value
        assert data is not None
        assert data.models_generated == 2
        assert "stg_ldif_entries" in data.model_names
        assert "analytics_ldif_insights" in data.model_names

    def test_run_complete_workflow_all(
        self,
        monkeypatch: pytest.MonkeyPatch,
        svc: FlextDbtLdifServiceMixin.Service,
        tmp_path: Path,
    ) -> None:
        """Test complete workflow with all stages."""
        entries: t.SequenceOf[t.JsonMapping] = [
            {"dn": "cn=test,dc=example,dc=org"},
        ]

        def _parse_ldif_file(
            _fp: Path | str,
        ) -> p.Result[Sequence[t.JsonMapping]]:
            return r[Sequence[t.JsonMapping]].ok(entries)

        def _validate_ldif_data(
            entries: t.SequenceOf[t.JsonMapping],
        ) -> p.Result[m.DbtLdif.LdifValidationResult]:
            return r[m.DbtLdif.LdifValidationResult].ok(
                m.DbtLdif.LdifValidationResult(
                    total_entries=1,
                    quality_score=0.9,
                    validation_status="passed",
                ),
            )

        def _transform_with_dbt(
            entries: t.SequenceOf[t.JsonMapping],
            _model_names: t.StrSequence | None,
        ) -> p.Result[m.DbtLdif.DbtTransformationResult]:
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
            entries: t.SequenceOf[t.JsonMapping],
        ) -> p.Result[Sequence[m.DbtLdif.DbtModel]]:
            return r[Sequence[m.DbtLdif.DbtModel]].ok([staging_model])

        def _generate_analytics_models(
            models: t.SequenceOf[m.DbtLdif.DbtModel],
        ) -> p.Result[Sequence[m.DbtLdif.DbtModel]]:
            return r[Sequence[m.DbtLdif.DbtModel]].ok([analytics_model])

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
        assert result.success
        data = result.value
        assert data is not None
        assert data.workflow_status == "completed"
