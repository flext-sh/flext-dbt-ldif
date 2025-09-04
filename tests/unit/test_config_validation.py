"""Test configuration validation improvements.

This module tests the enhanced configuration validation using flext-core patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import pytest

from flext_dbt_ldif import FlextDbtLdifConfig


class TestFlextDbtLdifConfigValidation:
    """Test cases for configuration validation improvements."""

    def test_valid_config_passes_validation(self) -> None:
        """Test that a valid configuration passes validation."""
        config = FlextDbtLdifConfig(
            ldif_max_file_size=1024 * 1024,  # 1MB
            max_dn_depth=5,
            min_quality_threshold=0.8,
            dbt_threads=4,
            dbt_log_level="info",
        )
        
        result = config.validate_config()
        assert result.success
        assert result.value is True

    def test_invalid_max_file_size_fails_validation(self) -> None:
        """Test that invalid max file size fails validation."""
        config = FlextDbtLdifConfig(ldif_max_file_size=-1)
        
        result = config.validate_config()
        assert not result.success
        assert "ldif_max_file_size must be positive" in result.error

    def test_invalid_quality_threshold_fails_validation(self) -> None:
        """Test that invalid quality threshold fails validation."""
        config = FlextDbtLdifConfig(min_quality_threshold=1.5)  # > 1.0
        
        result = config.validate_config()
        assert not result.success
        assert "min_quality_threshold must be between 0.0 and 1.0" in result.error

    def test_invalid_log_level_fails_validation(self) -> None:
        """Test that invalid log level fails validation."""
        config = FlextDbtLdifConfig(dbt_log_level="invalid")
        
        result = config.validate_config()
        assert not result.success
        assert "dbt_log_level must be debug, info, warn, or error" in result.error

    def test_to_dict_serialization(self) -> None:
        """Test configuration serialization to dictionary."""
        config = FlextDbtLdifConfig(
            ldif_file_path="/test/file.ldif",
            dbt_target="test",
            min_quality_threshold=0.9,
        )
        
        config_dict = config.to_dict()
        
        assert config_dict["ldif_file_path"] == "/test/file.ldif"
        assert config_dict["dbt_target"] == "test"
        assert config_dict["min_quality_threshold"] == 0.9
        assert "ldif_schema_mapping" in config_dict
        assert isinstance(config_dict["ldif_schema_mapping"], dict)

    def test_enhanced_meltano_config_generation(self) -> None:
        """Test enhanced Meltano configuration generation."""
        config = FlextDbtLdifConfig(
            dbt_project_dir="/project",
            dbt_profiles_dir="/profiles",
            dbt_target="prod",
            dbt_threads=8,
            dbt_log_level="debug",
        )
        
        meltano_config = config.get_meltano_config()
        
        assert meltano_config.dbt_project_dir == "/project"
        assert meltano_config.dbt_profiles_dir == "/profiles"
        assert meltano_config.dbt_target == "prod"
        assert meltano_config.dbt_threads == 8
        assert meltano_config.log_level == "debug"