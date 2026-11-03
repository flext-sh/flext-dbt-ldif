# AUTO-GENERATED FILE — Regenerate with: make gen
"""Source-derived structural model contracts.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/_protocols/dbt
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Protocol, runtime_checkable

from flext_meltano import FlextMeltanoProtocols

if TYPE_CHECKING:
    from flext_dbt_ldif import t


class FlextDbtLdifProtocolsDbt:
    """Own the structural contracts declared by its model source."""

    @runtime_checkable
    class DbtModel(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        name: t.StrippedStr
        dbt_model_type: str
        ldif_source: t.StrippedStr
        materialization: str
        sql_content: t.StrippedStr
        description: str
        columns: Sequence[t.JsonMapping]
        dependencies: Sequence[str]

    @runtime_checkable
    class LdifValidationResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        total_entries: int
        quality_score: float
        validation_status: str

    @runtime_checkable
    class DbtTransformationResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        records: int
        models: Sequence[str]
        status: str

    @runtime_checkable
    class ModelGenerationResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        models_generated: int
        model_names: Sequence[str]

    @runtime_checkable
    class ParseValidationResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        entry_count: int
        quality_score: float
        validation_status: str

    @runtime_checkable
    class WorkflowResult(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        ldif_file: str
        entry_count: int
        validation_status: str
        models_generated: int
        transformation_status: str
        workflow_status: str

    @runtime_checkable
    class DbtConnectionProfile(FlextMeltanoProtocols.BaseModel, Protocol):
        """Structural data contract projected from the owning model."""

        type: str
        path: str
        project: str


__all__: list[str] = [
    "FlextDbtLdifProtocolsDbt",
]
