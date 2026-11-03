# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/_protocols/dbt
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

from flext_dbt_ldif import t


class FlextDbtLdifProtocolsDbt:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class DbtModel(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def name(self) -> t.StrippedStr:
            """DBT model name."""
            ...

        @property
        def dbt_model_type(self) -> str:
            """DBT model category."""
            ...

        @property
        def ldif_source(self) -> t.StrippedStr:
            """LDIF source identifier."""
            ...

        @property
        def materialization(self) -> str:
            """DBT materialization strategy."""
            ...

        @property
        def sql_content(self) -> t.StrippedStr:
            """Rendered SQL for the DBT model."""
            ...

        @property
        def description(self) -> str:
            """Human-readable model description."""
            ...

        @property
        def columns(self) -> Sequence[t.JsonMapping]:
            """Column metadata for the DBT model."""
            ...

        @property
        def dependencies(self) -> Sequence[str]:
            """Upstream model dependencies."""
            ...

    @runtime_checkable
    class LdifValidationResult(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def total_entries(self) -> int:
            """Total LDIF entries validated."""
            ...

        @property
        def quality_score(self) -> float:
            """Aggregate LDIF quality score."""
            ...

        @property
        def validation_status(self) -> str:
            """Validation lifecycle status."""
            ...

    @runtime_checkable
    class DbtTransformationResult(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def records(self) -> int:
            """Number of transformed records."""
            ...

        @property
        def models(self) -> Sequence[str]:
            """Names of models produced by the transformation."""
            ...

        @property
        def status(self) -> str:
            """Transformation lifecycle status."""
            ...

    @runtime_checkable
    class ModelGenerationResult(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def models_generated(self) -> int:
            """Number of generated DBT models."""
            ...

        @property
        def model_names(self) -> Sequence[str]:
            """Names of generated DBT models."""
            ...

    @runtime_checkable
    class ParseValidationResult(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def entry_count(self) -> int:
            """Number of parsed LDIF entries."""
            ...

        @property
        def quality_score(self) -> float:
            """Validation quality score."""
            ...

        @property
        def validation_status(self) -> str:
            """Validation lifecycle status."""
            ...

    @runtime_checkable
    class WorkflowResult(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def ldif_file(self) -> str:
            """Input LDIF file path."""
            ...

        @property
        def entry_count(self) -> int:
            """Processed LDIF entry count."""
            ...

        @property
        def validation_status(self) -> str:
            """Validation lifecycle status."""
            ...

        @property
        def models_generated(self) -> int:
            """Number of generated DBT models."""
            ...

        @property
        def transformation_status(self) -> str:
            """Transformation lifecycle status."""
            ...

        @property
        def workflow_status(self) -> str:
            """Overall workflow status."""
            ...

    @runtime_checkable
    class DbtConnectionProfile(FlextMeltanoProtocols.Model, Protocol):
        """Structural data contract projected from the owning model."""

        @property
        def type(self) -> str:
            """Dbt adapter type."""
            ...

        @property
        def path(self) -> str:
            """LDIF source file path."""
            ...

        @property
        def project(self) -> str:
            """Dbt project name."""
            ...


__all__: list[str] = [
    "FlextDbtLdifProtocolsDbt",
]
