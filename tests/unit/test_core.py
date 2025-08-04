"""Unit tests for core functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import LDIFAnalytics, Path

from flext_dbt_ldif.core import DBTModelGenerator

# Constants
EXPECTED_BULK_SIZE = 2


class TestDBTModelGenerator:
    """Test cases for DBTModelGenerator class."""

    def test_init(self, tmp_path: Path) -> None:
        """Test DBTModelGenerator initialization."""
        generator = DBTModelGenerator(tmp_path)
        if generator.project_dir != tmp_path:
            msg = f"Expected {tmp_path}, got {generator.project_dir}"
            raise AssertionError(msg)
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
        if stg_model["materialization"] != "view":
            msg = f"Expected {'view'}, got {stg_model['materialization']}"
            raise AssertionError(msg)
        if "columns" not in stg_model:
            msg = f"Expected {'columns'} in {stg_model}"
            raise AssertionError(msg)

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
        if analytics_model["materialization"] != "table":
            msg = f"Expected {'table'}, got {analytics_model['materialization']}"
            raise AssertionError(msg)
        if "features" not in analytics_model:
            msg = f"Expected {'features'} in {analytics_model}"
            raise AssertionError(msg)


class TestLDIFAnalytics:
    """Test cases for LDIFAnalytics class."""

    def test_analyze_entry_patterns_empty(self) -> None:
        """Test pattern analysis with empty data."""
        result = LDIFAnalytics.analyze_entry_patterns([])
        if result["total_entries"] != 0:
            msg = f"Expected {0}, got {result['total_entries']}"
            raise AssertionError(msg)

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
        if result["total_entries"] != EXPECTED_BULK_SIZE:
            msg = f"Expected {2}, got {result['total_entries']}"
            raise AssertionError(msg)
        if "unique_object_classes" not in result:
            msg = f"Expected {'unique_object_classes'} in {result}"
            raise AssertionError(msg)
        assert "dn_depth_distribution" in result
        if "risk_assessment" not in result:
            msg = f"Expected {'risk_assessment'} in {result}"
            raise AssertionError(msg)

    def test_generate_quality_metrics_empty(self) -> None:
        """Test quality metrics with empty data."""
        result = LDIFAnalytics.generate_quality_metrics([])
        if result["completeness"] != 0.0:
            msg = f"Expected {0.0}, got {result['completeness']}"
            raise AssertionError(msg)
        assert result["validity"] == 0.0
        if result["consistency"] != 0.0:
            msg = f"Expected {0.0}, got {result['consistency']}"
            raise AssertionError(msg)

    def test_generate_quality_metrics_with_data(self) -> None:
        """Test quality metrics with sample data."""
        sample_entries = [{"dn": "test", "objectClass": ["top"]}]
        result = LDIFAnalytics.generate_quality_metrics(sample_entries)

        if "completeness" not in result:
            msg = f"Expected {'completeness'} in {result}"
            raise AssertionError(msg)
        assert "validity" in result
        if "consistency" not in result:
            msg = f"Expected {'consistency'} in {result}"
            raise AssertionError(msg)
        assert all(isinstance(v, (int, float)) for v in result.values())
