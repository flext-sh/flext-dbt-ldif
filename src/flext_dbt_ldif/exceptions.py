"""LDIF DBT exception hierarchy using flext-core patterns.

Copyright (c) 2025 FLEXT Contributors
SPDX-License-Identifier: MIT

Domain-specific exceptions for LDIF DBT operations inheriting from flext-core.
"""

from __future__ import annotations

from flext_core.exceptions import (
    FlextConfigurationError,
    FlextError,
    FlextProcessingError,
    FlextValidationError,
)


class FlextDbtLdifError(FlextError):
    """Base exception for LDIF DBT operations."""

    def __init__(
        self,
        message: str = "LDIF DBT error",
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(message, error_code="LDIF_DBT_ERROR", context=context)


class FlextDbtLdifConfigurationError(FlextConfigurationError):
    """LDIF DBT configuration errors."""

    def __init__(
        self,
        message: str = "LDIF DBT configuration error",
        config_key: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT configuration error with context."""
        context = kwargs.copy()
        if config_key is not None:
            context["config_key"] = config_key

        super().__init__(f"LDIF DBT config: {message}", **context)


class FlextDbtLdifValidationError(FlextValidationError):
    """LDIF DBT validation errors."""

    def __init__(
        self,
        message: str = "LDIF DBT validation failed",
        field: str | None = None,
        value: object = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT validation error with context."""
        validation_details: dict[str, object] = {}
        if field is not None:
            validation_details["field"] = field
        if value is not None:
            validation_details["value"] = str(value)[:100]  # Truncate long values

        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(
            f"LDIF DBT validation: {message}",
            validation_details=validation_details,
            context=context,
        )


class FlextDbtLdifProcessingError(FlextProcessingError):
    """LDIF DBT processing errors."""

    def __init__(
        self,
        message: str = "LDIF DBT processing failed",
        model_name: str | None = None,
        stage: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT processing error with context."""
        context = kwargs.copy()
        if model_name is not None:
            context["model_name"] = model_name
        if stage is not None:
            context["stage"] = stage

        super().__init__(f"LDIF DBT processing: {message}", **context)


class FlextDbtLdifParseError(FlextProcessingError):
    """LDIF DBT parsing errors."""

    def __init__(
        self,
        message: str = "LDIF DBT parsing failed",
        line_number: int | None = None,
        entry_dn: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT parsing error with context."""
        context = kwargs.copy()
        if line_number is not None:
            context["line_number"] = line_number
        if entry_dn is not None:
            context["entry_dn"] = entry_dn

        super().__init__(f"LDIF DBT parse: {message}", **context)


class FlextDbtLdifModelError(FlextDbtLdifError):
    """LDIF DBT model-specific errors."""

    def __init__(
        self,
        message: str = "LDIF DBT model error",
        model_name: str | None = None,
        model_type: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT model error with context."""
        context = kwargs.copy()
        if model_type is not None:
            context["model_type"] = model_type

        super().__init__(f"LDIF DBT model: {message}", model_name=model_name, **context)


class FlextDbtLdifTransformationError(FlextProcessingError):
    """LDIF DBT transformation errors."""

    def __init__(
        self,
        message: str = "LDIF DBT transformation failed",
        transformation_type: str | None = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT transformation error with context."""
        context = kwargs.copy()
        if transformation_type is not None:
            context["transformation_type"] = transformation_type
        if model_name is not None:
            context["model_name"] = model_name

        super().__init__(f"LDIF DBT transformation: {message}", **context)


class FlextDbtLdifTestError(FlextDbtLdifError):
    """LDIF DBT test errors."""

    def __init__(
        self,
        message: str = "LDIF DBT test failed",
        test_name: str | None = None,
        model_name: str | None = None,
        **kwargs: object,
    ) -> None:
        """Initialize LDIF DBT test error with context."""
        context = kwargs.copy()
        if test_name is not None:
            context["test_name"] = test_name

        super().__init__(f"LDIF DBT test: {message}", model_name=model_name, **context)


__all__ = [
    "FlextDbtLdifConfigurationError",
    "FlextDbtLdifError",
    "FlextDbtLdifModelError",
    "FlextDbtLdifParseError",
    "FlextDbtLdifProcessingError",
    "FlextDbtLdifTestError",
    "FlextDbtLdifTransformationError",
    "FlextDbtLdifValidationError",
]
