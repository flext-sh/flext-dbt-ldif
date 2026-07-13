"""Behavioral tests for FLEXT DBT LDIF unified service and model contract.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from flext_dbt_ldif import FlextDbtLdifSettings
from flext_dbt_ldif.services.unified_service import FlextDbtLdifUnifiedService
from tests import c, m

if TYPE_CHECKING:
    from pathlib import Path

    from tests import t

__all__ = ["TestsFlextDbtLdifDbtModels"]


class TestsFlextDbtLdifDbtModels:
    """Public-contract tests for FlextDbtLdifUnifiedService and DbtModel."""

    @pytest.fixture
    def service(self) -> FlextDbtLdifUnifiedService.UnifiedService:
        """Provide a service instance backed by global settings."""
        return FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(),
        )

    @staticmethod
    def _make_model(
        *,
        name: str = "test_model",
        ldif_source: str = "ldif_entries",
        sql_content: str = "select 1",
    ) -> m.DbtLdif.DbtModel:
        """Build a DbtModel via its public constructor."""
        return m.DbtLdif.DbtModel(
            name=name,
            dbt_model_type="staging",
            ldif_source=ldif_source,
            sql_content=sql_content,
            columns=[],
            dependencies=[],
        )

    # -- service construction -------------------------------------------------

    def test_service_exposes_configured_project_dir_and_default_name(
        self,
        tmp_path: Path,
    ) -> None:
        """Constructor arguments surface through public fields."""
        gen = FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(),
            project_dir=tmp_path,
        )
        assert gen.project_dir == tmp_path
        assert gen.name == "ldif_generator"

    # -- execute --------------------------------------------------------------

    def test_execute_returns_ready_metadata_payload(
        self,
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """Execute succeeds and reports the ready status contract."""
        result = service.execute()
        assert result.success
        data: t.JsonMapping = result.unwrap()
        assert data["name"] == "ldif_generator"
        assert data["status"] == "ready"

    def test_execute_metadata_reflects_project_dir(self, tmp_path: Path) -> None:
        """Execute payload echoes the configured project directory."""
        gen = FlextDbtLdifUnifiedService.UnifiedService(
            settings=FlextDbtLdifSettings.fetch_global(),
            project_dir=tmp_path,
        )
        data = gen.execute().unwrap()
        assert data["project_dir"] == str(tmp_path)

    # -- staging generation ---------------------------------------------------

    def test_generate_staging_models_emits_view_model_for_entries(
        self,
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """Non-empty entries yield exactly one staging view model."""
        entries: t.SequenceOf[t.JsonMapping] = [
            {"dn": "cn=test,dc=example,dc=org"},
        ]
        models = service.generate_staging_models(entries).unwrap()
        assert len(models) == 1
        model = models[0]
        assert model.name == "stg_ldif_entries"
        assert model.dbt_model_type == "staging"
        assert model.materialization == "view"

    def test_generate_staging_models_returns_empty_without_entries(
        self,
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """Empty entries yield an empty, successful result."""
        result = service.generate_staging_models([])
        assert result.success
        assert result.unwrap() == []

    # -- analytics generation -------------------------------------------------

    def test_generate_analytics_models_emits_table_model_from_staging(
        self,
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """A staging model produces one analytics table model."""
        staging_model = self._make_model(name="stg_ldif_entries")
        models = service.generate_analytics_models([staging_model]).unwrap()
        assert len(models) == 1
        model = models[0]
        assert model.name == "analytics_ldif_insights"
        assert model.dbt_model_type == "analytics"
        assert model.materialization == "table"

    def test_generate_analytics_models_returns_empty_without_staging(
        self,
        service: FlextDbtLdifUnifiedService.UnifiedService,
    ) -> None:
        """No staging models yields an empty, successful result."""
        result = service.generate_analytics_models([])
        assert result.success
        assert result.unwrap() == []

    # -- model contract -------------------------------------------------------

    def test_dbt_model_defaults_exposed_via_public_api(self) -> None:
        """Optional fields default to their documented values."""
        model = self._make_model()
        assert model.name == "test_model"
        assert model.materialization == "view"
        assert model.description == ""
        assert list(model.columns) == []
        assert list(model.dependencies) == []

    def test_complete_model_constructs_via_public_api(self) -> None:
        """A fully populated model constructs successfully through its public API."""
        model = self._make_model()
        assert model.name == "test_model"
        assert model.ldif_source == "ldif_entries"
        assert model.sql_content == "select 1"

    @pytest.mark.parametrize(
        ("field", "kwargs"),
        [
            ("name", {"name": "  "}),
            ("ldif_source", {"ldif_source": "  "}),
            ("sql_content", {"sql_content": "  "}),
        ],
    )
    def test_blank_required_field_rejected_at_construction(
        self,
        field: str,
        kwargs: dict[str, str],
    ) -> None:
        """Blank required fields (t.StrippedStr) fail validation naming the field."""
        with pytest.raises(c.ValidationError) as exc_info:
            self._make_model(**kwargs)
        assert field in str(exc_info.value)
