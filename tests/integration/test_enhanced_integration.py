"""Integration test for improved flext_core and flext_meltano usage.

This module tests the enhanced integration patterns implemented.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from flext_dbt_ldif import FlextDbtLdifConfig
from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifConfigurationError


class TestEnhancedIntegration:
    """Test enhanced flext_core and flext_meltano integration."""

    def test_configuration_validation_integration(self) -> None:
        """Test that configuration validation is properly integrated."""
        # Valid config should work
        valid_config = FlextDbtLdifConfig(
            ldif_max_file_size=1024,
            min_quality_threshold=0.8,
            dbt_threads=2,
            dbt_log_level="info",
        )
        
        result = valid_config.validate_config()
        assert result.success

        # Invalid config should fail
        invalid_config = FlextDbtLdifConfig(ldif_max_file_size=-1)
        result = invalid_config.validate_config()
        assert not result.success

    def test_meltano_config_generation(self) -> None:
        """Test enhanced Meltano configuration generation."""
        config = FlextDbtLdifConfig(
            dbt_project_dir="/test/project",
            dbt_profiles_dir="/test/profiles",
            dbt_target="test",
            dbt_threads=4,
            dbt_log_level="debug",
        )
        
        meltano_config = config.get_meltano_config()
        
        assert meltano_config.dbt_project_dir == "/test/project"
        assert meltano_config.dbt_profiles_dir == "/test/profiles"
        assert meltano_config.dbt_target == "test"
        assert meltano_config.dbt_threads == 4
        assert meltano_config.log_level == "debug"

    def test_config_serialization(self) -> None:
        """Test configuration serialization works correctly."""
        config = FlextDbtLdifConfig(
            ldif_file_path="/test.ldif",
            min_quality_threshold=0.9,
            dbt_target="prod",
        )
        
        config_dict = config.to_dict()
        
        assert config_dict["ldif_file_path"] == "/test.ldif"
        assert config_dict["min_quality_threshold"] == 0.9
        assert config_dict["dbt_target"] == "prod"
        assert "ldif_schema_mapping" in config_dict
        assert isinstance(config_dict["ldif_schema_mapping"], dict)

    def test_exception_context_preservation(self) -> None:
        """Test that exception context is properly preserved."""
        from flext_dbt_ldif.dbt_exceptions import FlextDbtLdifParseError
        
        exc = FlextDbtLdifParseError(
            "Test error",
            line_number=42,
            entry_dn="cn=test",
            error_code="TEST_ERROR",
        )
        
        # The exception should maintain context
        assert "TEST_ERROR" in str(exc)
        assert "Test error" in str(exc)