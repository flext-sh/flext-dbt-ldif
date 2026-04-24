"""Error mixin for dbt-ldif utilities."""

from __future__ import annotations

from typing import Self, override

from flext_dbt_ldif import c, e, t


class FlextDbtLdifError:
    """Mixin providing Error for dbt-ldif utilities."""

    class Error(e.BaseError):
        """Unified exception for all LDIF DBT operations with error codes.

        Single responsibility class that handles all LDIF DBT error scenarios
        through error codes instead of multiple exception classes.
        """

        @override
        def __init__(
            self,
            message: str,
            *,
            error_code: c.ErrorCode = c.ErrorCode.DBT_LDIF_ERROR,
            **context: t.Scalar,
        ) -> None:
            """Initialize LDIF DBT error with error code and context.

            Args:
                message: Human-readable error message
                error_code: Specific error code for this error type
                **context: Additional context information

            """
            context["error_code"] = error_code.value
            context["operation"] = context.get("operation", "ldif_dbt_operation")
            super().__init__(message)
            self.error_code = error_code

        @classmethod
        def authentication_error(
            cls,
            message: str = "LDIF DBT authentication failed",
            **context: t.Scalar,
        ) -> Self:
            """Create authentication error."""
            return cls(
                message,
                error_code=c.ErrorCode.AUTHENTICATION_ERROR,
                **context,
            )

        @classmethod
        def configuration_error(
            cls,
            message: str = "LDIF DBT configuration is invalid or missing",
            **context: t.Scalar,
        ) -> Self:
            """Create configuration error."""
            return cls(
                message,
                error_code=c.ErrorCode.CONFIGURATION_ERROR,
                **context,
            )

        @classmethod
        def connection_error(
            cls,
            message: str = "LDIF DBT database connection failed",
            **context: t.Scalar,
        ) -> Self:
            """Create connection error."""
            return cls(
                message,
                error_code=c.ErrorCode.CONNECTION_ERROR,
                **context,
            )

        @classmethod
        def model_error(
            cls,
            message: str = "LDIF DBT model error",
            *,
            model_name: str | None = None,
            model_type: str | None = None,
            **context: t.Scalar,
        ) -> Self:
            """Create LDIF DBT model error with dbt context."""
            context["operation"] = "dbt_model_processing"
            if model_name is not None:
                context["model_name"] = model_name
            if model_type is not None:
                context["model_type"] = model_type
            return cls(
                message,
                error_code=c.ErrorCode.MODEL_ERROR,
                **context,
            )

        @classmethod
        def parse_error(
            cls,
            message: str = "LDIF DBT parsing failed",
            *,
            line_number: int | None = None,
            entry_dn: str | None = None,
            **context: t.Scalar,
        ) -> Self:
            """Create LDIF parsing error with parse context."""
            context["operation"] = "ldif_parsing"
            if line_number is not None:
                context["line_number"] = line_number
            if entry_dn is not None:
                context["entry_dn"] = entry_dn
            return cls(
                message,
                error_code=c.ErrorCode.PARSE_ERROR,
                **context,
            )

        @classmethod
        def processing_error(
            cls,
            message: str = "LDIF processing operations failed",
            **context: t.Scalar,
        ) -> Self:
            """Create processing error."""
            return cls(
                message,
                error_code=c.ErrorCode.PROCESSING_ERROR,
                **context,
            )

        @classmethod
        def test_error(
            cls,
            message: str = "LDIF DBT test failed",
            *,
            test_name: str | None = None,
            model_name: str | None = None,
            **context: t.Scalar,
        ) -> Self:
            """Create LDIF DBT test error with test validation context."""
            context["operation"] = "dbt_test_validation"
            if test_name is not None:
                context["test_name"] = test_name
            if model_name is not None:
                context["model_name"] = model_name
            return cls(
                message,
                error_code=c.ErrorCode.TEST_ERROR,
                **context,
            )

        @classmethod
        def timeout_error(
            cls,
            message: str = "LDIF DBT operation timeout",
            **context: t.Scalar,
        ) -> Self:
            """Create timeout error."""
            return cls(
                message,
                error_code=c.ErrorCode.TIMEOUT_ERROR,
                **context,
            )

        @classmethod
        def transformation_error(
            cls,
            message: str = "LDIF DBT transformation failed",
            *,
            transformation_type: str | None = None,
            model_name: str | None = None,
            **context: t.Scalar,
        ) -> Self:
            """Create LDIF DBT transformation error with transformation context."""
            context["operation"] = "ldif_transformation"
            if transformation_type is not None:
                context["transformation_type"] = transformation_type
            if model_name is not None:
                context["model_name"] = model_name
            return cls(
                message,
                error_code=c.ErrorCode.TRANSFORMATION_ERROR,
                **context,
            )

        @classmethod
        def validation_error(
            cls,
            message: str = "LDIF data validation failed",
            **context: t.Scalar,
        ) -> Self:
            """Create validation error."""
            return cls(
                message,
                error_code=c.ErrorCode.VALIDATION_ERROR,
                **context,
            )

        def is_configuration_error(self) -> bool:
            """Check if this is a configuration error."""
            return self.error_code == c.ErrorCode.CONFIGURATION_ERROR

        def is_processing_error(self) -> bool:
            """Check if this is a processing error."""
            return self.error_code in {
                c.ErrorCode.PROCESSING_ERROR,
                c.ErrorCode.PARSE_ERROR,
                c.ErrorCode.MODEL_ERROR,
                c.ErrorCode.TRANSFORMATION_ERROR,
            }

        def is_validation_error(self) -> bool:
            """Check if this is a validation error."""
            return self.error_code == c.ErrorCode.VALIDATION_ERROR
