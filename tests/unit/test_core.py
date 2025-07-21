"""Unit tests for core functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING

from flext_dbt_ldif.core import DBTModelGenerator, LDIFAnalytics

if TYPE_CHECKING:
    from pathlib import Path


class TestDBTModelGenerator:
    """Test cases for DBTModelGenerator class."""

    def test_init(self, tmp_path: Path) -> None:
        """Test DBTModelGenerator initialization."""
        generator = DBTModelGenerator(tmp_path)
        assert generator.project_dir == tmp_path
        assert generator.models_dir == tmp_path / "models"

    def test_generate_staging_models(self, tmp_path: Path) -> None:
        """Test staging model generation."""
        generator = DBTModelGenerator(tmp_path)
        models = generator.generate_staging_models()

        assert isinstance(models, list)
        assert len(models) > 0

        # Check the stg_ldif_entries model
        stg_model = next((m for m in models if m["name"] == "stg_ldif_entries"), None)
        assert stg_model is not None
        assert stg_model["materialization"] == "view"
        assert "columns" in stg_model

    def test_generate_analytics_models(self, tmp_path: Path) -> None:
        """Test analytics model generation."""
        generator = DBTModelGenerator(tmp_path)
        models = generator.generate_analytics_models()

        assert isinstance(models, list)
        assert len(models) > 0

        # Check the analytics model
        analytics_model = next(
            (m for m in models if m["name"] == "analytics_ldif_insights"),
            None,
        )
        assert analytics_model is not None
        assert analytics_model["materialization"] == "table"
        assert "features" in analytics_model


class TestLDIFAnalytics:
    """Test cases for LDIFAnalytics class."""

    def test_analyze_entry_patterns_empty(self) -> None:
        """Test pattern analysis with empty data."""
        result = LDIFAnalytics.analyze_entry_patterns([])
        assert result["total_entries"] == 0

    def test_analyze_entry_patterns_with_data(self) -> None:
        """Test pattern analysis with sample data."""
        sample_data = [
            {
                "dn": "cn=user1,ou=users,dc=example,dc=com",
                "objectClass": ["inetOrgPerson"],
            },
            {
                "dn": "cn=user2,ou=users,dc=example,dc=com",
                "objectClass": ["inetOrgPerson"],
            },
        ]

        result = LDIFAnalytics.analyze_entry_patterns(sample_data)
        assert result["total_entries"] == 2
        assert "unique_object_classes" in result
        assert "dn_depth_distribution" in result
        assert "risk_assessment" in result

    def test_generate_quality_metrics_empty(self) -> None:
        """Test quality metrics with empty data."""
        result = LDIFAnalytics.generate_quality_metrics([])
        assert result["completeness"] == 0.0
        assert result["validity"] == 0.0
        assert result["consistency"] == 0.0

    def test_generate_quality_metrics_with_data(self) -> None:
        """Test quality metrics with sample data."""
        sample_entries = [{"dn": "test", "objectClass": ["top"]}]
        result = LDIFAnalytics.generate_quality_metrics(sample_entries)

        assert "completeness" in result
        assert "validity" in result
        assert "consistency" in result
        assert all(isinstance(v, (int, float)) for v in result.values())
