"""Unit tests for core functionality.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

from flext_dbt_ldif import FlextDbtLdifCore


class TestModelGenerator:
    """Test cases for FlextDbtLdifCore.Core.ModelGenerator."""

    def test_initialization_default(self) -> None:
        """Test ModelGenerator default initialization."""
        gen = FlextDbtLdifCore.Core.ModelGenerator()
        assert gen.project_dir == Path.cwd()

    def test_initialization_custom_dir(self, tmp_path: Path) -> None:
        """Test ModelGenerator with custom project_dir."""
        gen = FlextDbtLdifCore.Core.ModelGenerator(project_dir=tmp_path)
        assert gen.project_dir == tmp_path

    def test_generate_staging_models(self) -> None:
        """Test staging model generation returns expected structure."""
        gen = FlextDbtLdifCore.Core.ModelGenerator()
        models = gen.generate_staging_models()
        assert isinstance(models, list)
        assert models
        stg = models[0]
        assert stg["name"] == "stg_ldif_entries"
        assert "description" in stg

    def test_generate_analytics_models(self) -> None:
        """Test analytics model generation returns expected structure."""
        gen = FlextDbtLdifCore.Core.ModelGenerator()
        models = gen.generate_analytics_models()
        assert isinstance(models, list)
        assert models
        analytics = models[0]
        assert analytics["name"] == "analytics_ldif_insights"
        assert "description" in analytics


class TestAnalytics:
    """Test cases for FlextDbtLdifCore.Core.Analytics."""

    def test_analyze_entry_patterns_empty(self) -> None:
        """Test pattern analysis with empty data."""
        analytics = FlextDbtLdifCore.Core.Analytics()
        result = analytics.analyze_entry_patterns([])
        assert result.success
        data = result.value or {}
        assert data["total_entries"] == 0
        assert data["unique_dns"] == 0

    def test_analyze_entry_patterns_with_data(self) -> None:
        """Test pattern analysis with sample data."""
        sample_data = [
            {"dn": "cn=user1,ou=users,dc=example,dc=com"},
            {"dn": "cn=user2,ou=users,dc=example,dc=com"},
        ]
        analytics = FlextDbtLdifCore.Core.Analytics()
        result = analytics.analyze_entry_patterns(sample_data)
        assert result.success
        data = result.value or {}
        assert data["total_entries"] == 2
        assert data["unique_dns"] == 2

    def test_analyze_entry_patterns_duplicates(self) -> None:
        """Test pattern analysis with duplicate DNs."""
        sample_data = [
            {"dn": "cn=user1,dc=example,dc=com"},
            {"dn": "cn=user1,dc=example,dc=com"},
        ]
        analytics = FlextDbtLdifCore.Core.Analytics()
        result = analytics.analyze_entry_patterns(sample_data)
        assert result.success
        data = result.value or {}
        assert data["total_entries"] == 2
        assert data["unique_dns"] == 1
