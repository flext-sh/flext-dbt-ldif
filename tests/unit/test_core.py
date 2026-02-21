"""Unit tests for core functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations
from flext_dbt_ldif import t

from pathlib import Path

from flext_dbt_ldif.dbt_models import FlextDbtLdifUnifiedService

# Constants
EXPECTED_BULK_SIZE = 2


class TestFlextDbtLdifUnifiedService:
    """Test cases for FlextDbtLdifUnifiedService class."""

    def test_initialization(self, tmp_path: Path) -> None:
        """Test FlextDbtLdifUnifiedService initialization."""
        generator = FlextDbtLdifUnifiedService(project_dir=tmp_path)
        if generator.project_dir != tmp_path:
            msg: str = f"Expected {tmp_path}, got {generator.project_dir}"
            raise AssertionError(msg)

    def test_staging_model_generation(self, tmp_path: Path) -> None:
        """Test staging model generation."""
        generator = FlextDbtLdifUnifiedService(project_dir=tmp_path)
        models = generator.generate_staging_models()

        assert isinstance(models, list)
        assert len(models) > 0

        # Check the stg_ldif_entries model
        stg_model = next((m for m in models if m["name"] == "stg_ldif_entries"), None)
        assert stg_model is not None
        if stg_model["materialization"] != "view":
            raise AssertionError(f"Expected view, got {stg_model['materialization']}")
        if "columns" not in stg_model:
            raise AssertionError(f"Expected columns in {stg_model}")

    def test_analytics_model_generation(self, tmp_path: Path) -> None:
        """Test analytics model generation."""
        generator = FlextDbtLdifUnifiedService(project_dir=tmp_path)
        models = generator.generate_analytics_models()

        assert isinstance(models, list)
        assert len(models) > 0

        # Check the analytics model
        analytics_model = next(
            (m for m in models if m["name"] == "analytics_ldif_insights"),
            None,
        )
        assert analytics_model is not None
        if analytics_model["materialization"] != "table":
            raise AssertionError(
                f"Expected table, got {analytics_model['materialization']}",
            )
        if "features" not in analytics_model:
            raise AssertionError(f"Expected features in {analytics_model}")

    def test_analyze_entry_patterns_empty(self) -> None:
        """Test pattern analysis with empty data."""
        analytics = FlextDbtLdifUnifiedService()
        result = analytics.analyze_entry_patterns([])
        assert result.is_success
        data = result.value or {}
        if data.get("total_entries") != 0:
            raise AssertionError(f"Expected 0, got {data.get('total_entries')}")

    def test_analyze_entry_patterns_with_data(self) -> None:
        """Test pattern analysis with sample data."""
        sample_data: list[dict[str, t.GeneralValueType]] = [
            {
                "dn": "cn=user1,ou=users,dc=example,dc=com",
                "objectClass": ["inetOrgPerson"],
            },
            {
                "dn": "cn=user2,ou=users,dc=example,dc=com",
                "objectClass": ["inetOrgPerson"],
            },
        ]

        analytics = FlextDbtLdifUnifiedService()
        result = analytics.analyze_entry_patterns(sample_data)
        assert result.is_success
        data = result.value or {}
        if data.get("total_entries") != EXPECTED_BULK_SIZE:
            raise AssertionError(
                f"Expected {EXPECTED_BULK_SIZE}, got {data.get('total_entries')}",
            )
        if "unique_object_classes" not in data:
            msg: str = "Expected unique_object_classes in result"
            raise AssertionError(msg)
        assert "dn_depth_distribution" in data
        if "risk_assessment" not in data:
            msg: str = "Expected risk_assessment in result"
            raise AssertionError(msg)

    def test_generate_quality_metrics_empty(self) -> None:
        """Test quality metrics with empty data."""
        analytics = FlextDbtLdifUnifiedService()
        result = analytics.generate_quality_metrics([])
        assert result.is_success
        data = result.value or {}
        if data.get("completeness") != 0.0:
            raise AssertionError(f"Expected 0.0, got {data.get('completeness')}")
        assert data.get("validity") == 0.0
        if data.get("consistency") != 0.0:
            raise AssertionError(f"Expected 0.0, got {data.get('consistency')}")

    def test_generate_quality_metrics_with_data(self) -> None:
        """Test quality metrics with sample data."""
        sample_entries: list[dict[str, t.GeneralValueType]] = [
            {"dn": "test", "objectClass": ["top"]},
        ]
        analytics = FlextDbtLdifUnifiedService()
        result = analytics.generate_quality_metrics(sample_entries)
        assert result.is_success
        data = result.value or {}
        if "completeness" not in data:
            msg: str = "Expected completeness in result"
            raise AssertionError(msg)
        assert "validity" in data
        if "consistency" not in data:
            msg: str = "Expected consistency in result"
            raise AssertionError(msg)
        assert all(isinstance(v, (int, float)) for v in data.values())
