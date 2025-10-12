"""Test exceptions for FLEXT DBT LDIF.

Tests the unified exception class with error codes following FLEXT patterns.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

import pytest
from flext_core import FlextCore

from flext_dbt_ldif import FlextDbtLdifError


class TestFlextDbtLdifErrorCodes:
    """Test error codes enumeration."""

    def test_error_codes_defined(self) -> None:
        """Test that all error codes are properly defined."""
        error_codes = FlextDbtLdifError.ErrorCode

        # General error codes
        assert error_codes.DBT_LDIF_ERROR == "DBT_LDIF_ERROR"
        assert error_codes.VALIDATION_ERROR == "DBT_LDIF_VALIDATION_ERROR"
        assert error_codes.CONFIGURATION_ERROR == "DBT_LDIF_CONFIGURATION_ERROR"
        assert error_codes.CONNECTION_ERROR == "DBT_LDIF_CONNECTION_ERROR"
        assert error_codes.PROCESSING_ERROR == "DBT_LDIF_PROCESSING_ERROR"
        assert error_codes.AUTHENTICATION_ERROR == "DBT_LDIF_AUTHENTICATION_ERROR"
        assert error_codes.TIMEOUT_ERROR == "DBT_LDIF_TIMEOUT_ERROR"

        # Domain-specific error codes
        assert error_codes.PARSE_ERROR == "DBT_LDIF_PARSE_ERROR"
        assert error_codes.MODEL_ERROR == "DBT_LDIF_MODEL_ERROR"
        assert error_codes.TRANSFORMATION_ERROR == "DBT_LDIF_TRANSFORMATION_ERROR"
        assert error_codes.TEST_ERROR == "DBT_LDIF_TEST_ERROR"

    def test_error_codes_string_enum(self) -> None:
        """Test that error codes are string enums."""
        error_code = FlextDbtLdifError.ErrorCode.VALIDATION_ERROR
        assert isinstance(error_code, str)
        assert error_code == "DBT_LDIF_VALIDATION_ERROR"


class TestFlextDbtLdifError:
    """Test unified LDIF DBT exception class."""

    def test_basic_exception_creation(self) -> None:
        """Test basic exception creation with default error code."""
        error = FlextDbtLdifError("Test message")

        assert str(error) == "Test message"
        assert error.error_code == FlextDbtLdifError.ErrorCode.DBT_LDIF_ERROR
        assert hasattr(error, "context")

    def test_exception_with_explicit_error_code(self) -> None:
        """Test exception creation with explicit error code."""
        error = FlextDbtLdifError(
            "Validation failed",
            error_code=FlextDbtLdifError.ErrorCode.VALIDATION_ERROR,
        )

        assert str(error) == "Validation failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.VALIDATION_ERROR

    def test_exception_with_context(self) -> None:
        """Test exception creation with context data."""
        error = FlextDbtLdifError(
            "Processing failed",
            error_code=FlextDbtLdifError.ErrorCode.PROCESSING_ERROR,
            file_path="/test/file.ldif",
            line_number=42,
        )

        assert str(error) == "Processing failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.PROCESSING_ERROR
        # Context is stored in the parent exception class
        assert hasattr(error, "context")

    def test_exception_inheritance(self) -> None:
        """Test that FlextDbtLdifError inherits from flext-core FlextCore.Exceptions."""
        error = FlextDbtLdifError("Test message")

        # Should inherit from FlextCore.Exceptions (from flext-core)
        assert isinstance(error, FlextCore.Exceptions)
        assert isinstance(error, Exception)


class TestFlextDbtLdifErrorFactoryMethods:
    """Test factory methods for creating specific error types."""

    def test_validation_error_factory(self) -> None:
        """Test validation error factory method."""
        error = FlextDbtLdifError.validation_error("Data validation failed")

        assert str(error) == "Data validation failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.VALIDATION_ERROR

    def test_validation_error_factory_with_default_message(self) -> None:
        """Test validation error factory with default message."""
        error = FlextDbtLdifError.validation_error()

        assert str(error) == "LDIF data validation failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.VALIDATION_ERROR

    def test_configuration_error_factory(self) -> None:
        """Test configuration error factory method."""
        error = FlextDbtLdifError.configuration_error(
            "Missing required config",
            config_field="database_url",
        )

        assert str(error) == "Missing required config"
        assert error.error_code == FlextDbtLdifError.ErrorCode.CONFIGURATION_ERROR

    def test_connection_error_factory(self) -> None:
        """Test connection error factory method."""
        error = FlextDbtLdifError.connection_error(
            "Database connection failed",
            host="localhost",
            port=5432,
        )

        assert str(error) == "Database connection failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.CONNECTION_ERROR

    def test_processing_error_factory(self) -> None:
        """Test processing error factory method."""
        error = FlextDbtLdifError.processing_error("LDIF processing failed")

        assert str(error) == "LDIF processing failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.PROCESSING_ERROR

    def test_authentication_error_factory(self) -> None:
        """Test authentication error factory method."""
        error = FlextDbtLdifError.authentication_error(
            "LDAP authentication failed",
            username="testuser",
        )

        assert str(error) == "LDAP authentication failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.AUTHENTICATION_ERROR

    def test_timeout_error_factory(self) -> None:
        """Test timeout error factory method."""
        error = FlextDbtLdifError.timeout_error(
            "Operation timed out",
            timeout_seconds=30,
        )

        assert str(error) == "Operation timed out"
        assert error.error_code == FlextDbtLdifError.ErrorCode.TIMEOUT_ERROR

    def test_parse_error_factory(self) -> None:
        """Test parse error factory method with LDIF-specific context."""
        error = FlextDbtLdifError.parse_error(
            "LDIF parsing failed",
            line_number=10,
            entry_dn="cn=user,dc=example,dc=com",
        )

        assert str(error) == "LDIF parsing failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.PARSE_ERROR

    def test_model_error_factory(self) -> None:
        """Test model error factory method with dbt context."""
        error = FlextDbtLdifError.model_error(
            "Model compilation failed",
            model_name="dim_ldif_entries",
            model_type="dimension",
        )

        assert str(error) == "Model compilation failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.MODEL_ERROR

    def test_transformation_error_factory(self) -> None:
        """Test transformation error factory method."""
        error = FlextDbtLdifError.transformation_error(
            "Transformation failed",
            transformation_type="analytics",
            model_name="fact_ldif_changes",
        )

        assert str(error) == "Transformation failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.TRANSFORMATION_ERROR

    def test_test_error_factory(self) -> None:
        """Test test error factory method with test context."""
        error = FlextDbtLdifError.test_error(
            "Test validation failed",
            test_name="unique_dn_test",
            model_name="dim_ldif_entries",
        )

        assert str(error) == "Test validation failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.TEST_ERROR


class TestFlextDbtLdifErrorWithContext:
    """Test error creation with various context combinations."""

    def test_parse_error_with_full_context(self) -> None:
        """Test parse error with complete LDIF parsing context."""
        error = FlextDbtLdifError.parse_error(
            "Invalid LDIF entry",
            line_number=42,
            entry_dn="cn=invalid,dc=test,dc=com",
            file_path="/data/input.ldif",
            encoding="utf-8",
        )

        assert str(error) == "Invalid LDIF entry"
        assert error.error_code == FlextDbtLdifError.ErrorCode.PARSE_ERROR

    def test_model_error_with_full_context(self) -> None:
        """Test model error with complete dbt model context."""
        error = FlextDbtLdifError.model_error(
            "Model execution failed",
            model_name="staging_ldif_entries",
            model_type="staging",
            dbt_project_dir="/dbt/ldif_analytics",
            target="dev",
        )

        assert str(error) == "Model execution failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.MODEL_ERROR

    def test_transformation_error_with_analytics_context(self) -> None:
        """Test transformation error with analytics context."""
        error = FlextDbtLdifError.transformation_error(
            "Analytics model failed",
            transformation_type="anomaly_detection",
            model_name="ldif_anomaly_detection",
            risk_threshold=0.8,
            batch_size=1000,
        )

        assert str(error) == "Analytics model failed"
        assert error.error_code == FlextDbtLdifError.ErrorCode.TRANSFORMATION_ERROR


class TestFlextDbtLdifErrorChecking:
    """Test error type checking methods."""

    def test_is_validation_error(self) -> None:
        """Test validation error checking."""
        validation_error = FlextDbtLdifError.validation_error("Validation failed")
        processing_error = FlextDbtLdifError.processing_error("Processing failed")

        assert validation_error.is_validation_error() is True
        assert processing_error.is_validation_error() is False

    def test_is_configuration_error(self) -> None:
        """Test configuration error checking."""
        config_error = FlextDbtLdifError.configuration_error("Config missing")
        validation_error = FlextDbtLdifError.validation_error("Validation failed")

        assert config_error.is_configuration_error() is True
        assert validation_error.is_configuration_error() is False

    def test_is_processing_error(self) -> None:
        """Test processing error checking (includes domain-specific errors)."""
        processing_error = FlextDbtLdifError.processing_error("Processing failed")
        parse_error = FlextDbtLdifError.parse_error("Parse failed")
        model_error = FlextDbtLdifError.model_error("Model failed")
        transformation_error = FlextDbtLdifError.transformation_error(
            "Transform failed",
        )
        validation_error = FlextDbtLdifError.validation_error("Validation failed")

        # All processing-related errors should return True
        assert processing_error.is_processing_error() is True
        assert parse_error.is_processing_error() is True
        assert model_error.is_processing_error() is True
        assert transformation_error.is_processing_error() is True

        # Non-processing errors should return False
        assert validation_error.is_processing_error() is False


class TestFlextDbtLdifErrorIntegration:
    """Integration tests for LDIF DBT error handling."""

    def test_error_raising_and_catching(self) -> None:
        """Test raising and catching LDIF DBT errors."""
        error_message = "Test parse error"
        with pytest.raises(FlextDbtLdifError) as exc_info:
            raise FlextDbtLdifError.parse_error(error_message)

        error = exc_info.value
        assert str(error) == "Test parse error"
        assert error.error_code == FlextDbtLdifError.ErrorCode.PARSE_ERROR

    def test_error_chain_handling(self) -> None:
        """Test error chaining with different error types."""
        config_error_message = "Config error"
        processing_error_message = "Processing error"

        # First create and test the cause error
        config_error = FlextDbtLdifError.configuration_error(config_error_message)
        assert (
            config_error.error_code == FlextDbtLdifError.ErrorCode.CONFIGURATION_ERROR
        )

        # Then test the chained error
        with pytest.raises(FlextDbtLdifError) as processing_exc_info:
            raise FlextDbtLdifError.processing_error(
                processing_error_message,
            ) from config_error

        processing_error = processing_exc_info.value
        assert (
            processing_error.error_code == FlextDbtLdifError.ErrorCode.PROCESSING_ERROR
        )
        assert processing_error.__cause__ is config_error

    def test_factory_methods_produce_consistent_errors(self) -> None:
        """Test that factory methods produce consistent error instances."""
        error1 = FlextDbtLdifError.validation_error("Test validation")
        error2 = FlextDbtLdifError(
            "Test validation",
            error_code=FlextDbtLdifError.ErrorCode.VALIDATION_ERROR,
        )

        # Both should have the same error code and message
        assert error1.error_code == error2.error_code
        assert str(error1) == str(error2)
        assert type(error1) is type(error2)
