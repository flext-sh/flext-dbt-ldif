"""LDIF DBT Exception Hierarchy.

Exception hierarchy following FLEXT patterns using factory pattern from flext-core.
Eliminates code duplication by using create_module_exception_classes() factory.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from flext_core import FlextError

# Note: This module is intentionally simple. Runtime-focused code paths
# are covered by service and client tests; exception classes are thin wrappers.


# Base LDIF DBT error hierarchy using standard inheritance
class FlextDbtLdifError(FlextError):
    """Base exception for all LDIF DBT operations."""


class FlextDbtLdifValidationError(FlextDbtLdifError):
    """Raised when LDIF data validation fails."""


class FlextDbtLdifConfigurationError(FlextDbtLdifError):
    """Raised when configuration is invalid or missing."""


class FlextDbtLdifConnectionError(FlextDbtLdifError):
    """Raised when database connection fails."""


class FlextDbtLdifProcessingError(FlextDbtLdifError):
    """Raised when LDIF processing operations fail."""


class FlextDbtLdifAuthenticationError(FlextDbtLdifError):
    """Raised when authentication to LDAP/database fails."""


class FlextDbtLdifTimeoutError(FlextDbtLdifError):
    """Raised when operations timeout."""


# Domain-specific exceptions for LDIF DBT business logic
class FlextDbtLdifParseError(FlextDbtLdifProcessingError):
    """LDIF DBT parsing errors with LDIF parse context."""

    def __init__(
      self,
      message: str = "LDIF DBT parsing failed",
      *,
      line_number: int | None = None,
      entry_dn: str | None = None,
      error_code: str | None = None,
      **kwargs: object,
    ) -> None:
      """Initialize LDIF DBT parsing error with parse context."""
      context = dict(kwargs)
      context["operation"] = "ldif_parsing"
      if line_number is not None:
          context["line_number"] = line_number
      if entry_dn is not None:
          context["entry_dn"] = entry_dn

      super().__init__(message, error_code=error_code, context=context)


class FlextDbtLdifModelError(FlextDbtLdifProcessingError):
    """LDIF DBT model-specific errors with dbt model context."""

    def __init__(
      self,
      message: str = "LDIF DBT model error",
      *,
      model_name: str | None = None,
      model_type: str | None = None,
      error_code: str | None = None,
      **kwargs: object,
    ) -> None:
      """Initialize LDIF DBT model error with dbt context."""
      context = dict(kwargs)
      context["operation"] = "dbt_model_processing"
      if model_name is not None:
          context["model_name"] = model_name
      if model_type is not None:
          context["model_type"] = model_type

      super().__init__(message, error_code=error_code, context=context)


class FlextDbtLdifTransformationError(FlextDbtLdifProcessingError):
    """LDIF DBT transformation errors with transformation context."""

    def __init__(
      self,
      message: str = "LDIF DBT transformation failed",
      *,
      transformation_type: str | None = None,
      model_name: str | None = None,
      error_code: str | None = None,
      **kwargs: object,
    ) -> None:
      """Initialize LDIF DBT transformation error with transformation context."""
      context = dict(kwargs)
      context["operation"] = "ldif_transformation"
      if transformation_type is not None:
          context["transformation_type"] = transformation_type
      if model_name is not None:
          context["model_name"] = model_name

      super().__init__(message, error_code=error_code, context=context)


class FlextDbtLdifTestError(FlextDbtLdifValidationError):
    """LDIF DBT test errors with test validation context."""

    def __init__(
      self,
      message: str = "LDIF DBT test failed",
      *,
      test_name: str | None = None,
      model_name: str | None = None,
      error_code: str | None = None,
      **kwargs: object,
    ) -> None:
      """Initialize LDIF DBT test error with test context."""
      context = dict(kwargs)
      context["operation"] = "dbt_test_validation"
      if test_name is not None:
          context["test_name"] = test_name
      if model_name is not None:
          context["model_name"] = model_name

      super().__init__(message, error_code=error_code, context=context)


__all__: list[str] = [
    "FlextDbtLdifConfigurationError",
    "FlextDbtLdifError",
    "FlextDbtLdifModelError",
    "FlextDbtLdifParseError",
    "FlextDbtLdifProcessingError",
    "FlextDbtLdifTestError",
    "FlextDbtLdifTransformationError",
    "FlextDbtLdifValidationError",
]
