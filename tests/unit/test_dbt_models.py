"""Test DBT models for FLEXT DBT LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from pathlib import Path

from flext_core import FlextTypes

from flext_dbt_ldif import FlextDbtLdifSettings, FlextDbtLdifUnifiedService
from flext_dbt_ldif.models import FlextDbtLdifModels


class TestFlextDbtLdifUnifiedService:
    """Test cases for FlextDbtLdifUnifiedService."""

    def test_initialization(self, tmp_path: Path) -> None:
        """Test service initialization with project dir."""
        gen = FlextDbtLdifUnifiedService(
            config=FlextDbtLdifSettings.get_global(), project_dir=tmp_path
        )
        assert gen.project_dir == tmp_path
        assert gen.name == "ldif_generator"

    def test_execute(self) -> None:
        """Test execute returns metadata payload."""
        gen = FlextDbtLdifUnifiedService(config=FlextDbtLdifSettings.get_global())
        result = gen.execute()
        assert result.is_success
        data = result.value or {}
        assert data["name"] == "ldif_generator"
        assert data["status"] == "ready"

    def test_generate_staging_models_with_entries(self) -> None:
        """Test staging model generation with entries."""
        gen = FlextDbtLdifUnifiedService(config=FlextDbtLdifSettings.get_global())
        entries: Sequence[Mapping[str, FlextTypes.Scalar]] = [
            {"dn": "cn=test,dc=example,dc=org"}
        ]
        result = gen.generate_staging_models(entries)
        assert result.is_success
        models = result.value or []
        assert len(models) == 1
        assert models[0].name == "stg_ldif_entries"
        assert models[0].dbt_model_type == "staging"
        assert models[0].materialization == "view"

    def test_generate_staging_models_empty(self) -> None:
        """Test staging model generation with empty entries."""
        gen = FlextDbtLdifUnifiedService(config=FlextDbtLdifSettings.get_global())
        result = gen.generate_staging_models([])
        assert result.is_success
        models = result.value or []
        assert len(models) == 0

    def test_generate_analytics_models_with_staging(self) -> None:
        """Test analytics model generation from staging models."""
        gen = FlextDbtLdifUnifiedService(config=FlextDbtLdifSettings.get_global())
        staging_model = FlextDbtLdifModels.DbtLdif.DbtModel(
            name="stg_ldif_entries",
            dbt_model_type="staging",
            ldif_source="ldif_entries",
            sql_content="select * from raw",
            columns=[],
            dependencies=[],
        )
        result = gen.generate_analytics_models([staging_model])
        assert result.is_success
        models = result.value or []
        assert len(models) == 1
        assert models[0].name == "analytics_ldif_insights"
        assert models[0].dbt_model_type == "analytics"
        assert models[0].materialization == "table"

    def test_generate_analytics_models_empty(self) -> None:
        """Test analytics model generation with empty staging."""
        gen = FlextDbtLdifUnifiedService(config=FlextDbtLdifSettings.get_global())
        result = gen.generate_analytics_models([])
        assert result.is_success
        models = result.value or []
        assert len(models) == 0


class TestDbtModel:
    """Test cases for FlextDbtLdifModels.DbtLdif.DbtModel."""

    def test_create_model(self) -> None:
        """Test creating a DbtModel instance."""
        model = FlextDbtLdifModels.DbtLdif.DbtModel(
            name="test_model",
            dbt_model_type="staging",
            ldif_source="ldif_entries",
            sql_content="select 1",
            columns=[],
            dependencies=[],
        )
        assert model.name == "test_model"
        assert model.materialization == "view"
        assert model.description == ""
        assert model.columns == []
        assert model.dependencies == []

    def test_validate_business_rules_ok(self) -> None:
        """Test business rules pass for valid model."""
        model = FlextDbtLdifModels.DbtLdif.DbtModel(
            name="test_model",
            dbt_model_type="staging",
            ldif_source="ldif_entries",
            sql_content="select 1",
            columns=[],
            dependencies=[],
        )
        result = model.validate_business_rules()
        assert result.is_success
        assert result.value is True

    def test_validate_business_rules_empty_name(self) -> None:
        """Test business rules fail for empty name."""
        model = FlextDbtLdifModels.DbtLdif.DbtModel(
            name="  ",
            dbt_model_type="staging",
            ldif_source="ldif_entries",
            sql_content="select 1",
            columns=[],
            dependencies=[],
        )
        result = model.validate_business_rules()
        assert result.is_failure

    def test_validate_business_rules_empty_source(self) -> None:
        """Test business rules fail for empty ldif_source."""
        model = FlextDbtLdifModels.DbtLdif.DbtModel(
            name="test_model",
            dbt_model_type="staging",
            ldif_source="  ",
            sql_content="select 1",
            columns=[],
            dependencies=[],
        )
        result = model.validate_business_rules()
        assert result.is_failure

    def test_validate_business_rules_empty_sql(self) -> None:
        """Test business rules fail for empty sql_content."""
        model = FlextDbtLdifModels.DbtLdif.DbtModel(
            name="test_model",
            dbt_model_type="staging",
            ldif_source="ldif_entries",
            sql_content="  ",
            columns=[],
            dependencies=[],
        )
        result = model.validate_business_rules()
        assert result.is_failure
