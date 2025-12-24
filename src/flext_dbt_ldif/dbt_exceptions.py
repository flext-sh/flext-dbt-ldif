"""FLEXT DBT LDIF Exceptions Module.

Single unified exception class with error codes following FLEXT patterns.
Eliminates multiple exception hierarchies in favor of single class with error codes.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from typing import override

from flext import FlextExceptions
from flext_dbt_ldif.constants import c

# Alias for backward compatibility - ErrorCode is now centralized in constants.py
ErrorCode = c.ErrorCode


class FlextDbtLdifError(FlextExceptions.BaseError):
    """Unified exception for all LDIF DBT operations with error codes.

    Single responsibility class that handles all LDIF DBT error scenarios
    through error codes instead of multiple exception classes.
    """

    # Class-level reference to ErrorCode for internal usage
    ErrorCode = c.ErrorCode

    @override
    def __init__(
        self,
        message: str,
        *,
        error_code: ErrorCode = ErrorCode.DBT_LDIF_ERROR,
        **context: object,
    ) -> None:
        """Initialize LDIF DBT error with error code and context.

        Args:
        message: Human-readable error message
        error_code: Specific error code for this error type
        **context: Additional context information

        """
        # Add error code to context
        context["error_code"] = error_code.value
        context["operation"] = context.get("operation", "ldif_dbt_operation")

        super().__init__(message)
        self.error_code = error_code

    # Factory methods for common error scenarios
    @classmethod
    def validation_error(
        cls,
        message: str = "LDIF data validation failed",
        **context: object,
    ) -> FlextDbtLdifError:
        """Create validation error."""
        return cls(message, error_code=cls.ErrorCode.VALIDATION_ERROR, **context)

    @classmethod
    def configuration_error(
        cls,
        message: str = "LDIF DBT configuration is invalid or missing",
        **context: object,
    ) -> FlextDbtLdifError:
        """Create configuration error."""
        return cls(message, error_code=cls.ErrorCode.CONFIGURATION_ERROR, **context)

    @classmethod
    def connection_error(
        cls,
        message: str = "LDIF DBT database connection failed",
        **context: object,
    ) -> FlextDbtLdifError:
        """Create connection error."""
        return cls(message, error_code=cls.ErrorCode.CONNECTION_ERROR, **context)

    @classmethod
    def processing_error(
        cls,
        message: str = "LDIF processing operations failed",
        **context: object,
    ) -> FlextDbtLdifError:
        """Create processing error."""
        return cls(message, error_code=cls.ErrorCode.PROCESSING_ERROR, **context)

    @classmethod
    def authentication_error(
        cls,
        message: str = "LDIF DBT authentication failed",
        **context: object,
    ) -> FlextDbtLdifError:
        """Create authentication error."""
        return cls(message, error_code=cls.ErrorCode.AUTHENTICATION_ERROR, **context)

    @classmethod
    def timeout_error(
        cls,
        message: str = "LDIF DBT operation timeout",
        **context: object,
    ) -> FlextDbtLdifError:
        """Create timeout error."""
        return cls(message, error_code=cls.ErrorCode.TIMEOUT_ERROR, **context)

    @classmethod
    def parse_error(
        cls,
        message: str = "LDIF DBT parsing failed",
        *,
        line_number: int | None = None,
        entry_dn: str | None = None,
        **context: object,
    ) -> FlextDbtLdifError:
        """Create LDIF parsing error with parse context."""
        context["operation"] = "ldif_parsing"
        if line_number is not None:
            context["line_number"] = line_number
        if entry_dn is not None:
            context["entry_dn"] = entry_dn
        return cls(message, error_code=cls.ErrorCode.PARSE_ERROR, **context)

    @classmethod
    def model_error(
        cls,
        message: str = "LDIF DBT model error",
        *,
        model_name: str | None = None,
        model_type: str | None = None,
        **context: object,
    ) -> FlextDbtLdifError:
        """Create LDIF DBT model error with dbt context."""
        context["operation"] = "dbt_model_processing"
        if model_name is not None:
            context["model_name"] = model_name
        if model_type is not None:
            context["model_type"] = model_type
        return cls(message, error_code=cls.ErrorCode.MODEL_ERROR, **context)

    @classmethod
    def transformation_error(
        cls,
        message: str = "LDIF DBT transformation failed",
        *,
        transformation_type: str | None = None,
        model_name: str | None = None,
        **context: object,
    ) -> FlextDbtLdifError:
        """Create LDIF DBT transformation error with transformation context."""
        context["operation"] = "ldif_transformation"
        if transformation_type is not None:
            context["transformation_type"] = transformation_type
        if model_name is not None:
            context["model_name"] = model_name
        return cls(message, error_code=cls.ErrorCode.TRANSFORMATION_ERROR, **context)

    @classmethod
    def test_error(
        cls,
        message: str = "LDIF DBT test failed",
        *,
        test_name: str | None = None,
        model_name: str | None = None,
        **context: object,
    ) -> FlextDbtLdifError:
        """Create LDIF DBT test error with test validation context."""
        context["operation"] = "dbt_test_validation"
        if test_name is not None:
            context["test_name"] = test_name
        if model_name is not None:
            context["model_name"] = model_name
        return cls(message, error_code=cls.ErrorCode.TEST_ERROR, **context)

    def is_validation_error(self: object) -> bool:
        """Check if this is a validation error."""
        return self.error_code == self.ErrorCode.VALIDATION_ERROR

    def is_configuration_error(self: object) -> bool:
        """Check if this is a configuration error."""
        return self.error_code == self.ErrorCode.CONFIGURATION_ERROR

    def is_processing_error(self: object) -> bool:
        """Check if this is a processing error."""
        return self.error_code in {
            self.ErrorCode.PROCESSING_ERROR,
            self.ErrorCode.PARSE_ERROR,
            self.ErrorCode.MODEL_ERROR,
            self.ErrorCode.TRANSFORMATION_ERROR,
        }


__all__: list[str] = [
    "FlextDbtLdifError",
]
