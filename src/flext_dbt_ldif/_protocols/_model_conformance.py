# AUTO-GENERATED FILE — Regenerate with: make gen
"""Static instance-to-protocol evidence required by candidate admission.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/_protocols/_model_conformance
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flext_dbt_ldif import FlextDbtLdifModels, FlextDbtLdifProtocols

    def model_protocol_1(
        value: (FlextDbtLdifModels.DbtLdif.DbtConnectionProfile),
    ) -> FlextDbtLdifProtocols.DbtLdif.DbtConnectionProfile:
        return value

    def model_protocol_2(
        value: (FlextDbtLdifModels.DbtLdif.DbtModel),
    ) -> FlextDbtLdifProtocols.DbtLdif.DbtModel:
        return value

    def model_protocol_3(
        value: (FlextDbtLdifModels.DbtLdif.DbtTransformationResult),
    ) -> FlextDbtLdifProtocols.DbtLdif.DbtTransformationResult:
        return value

    def model_protocol_4(
        value: (FlextDbtLdifModels.DbtLdif.LdifValidationResult),
    ) -> FlextDbtLdifProtocols.DbtLdif.LdifValidationResult:
        return value

    def model_protocol_5(
        value: (FlextDbtLdifModels.DbtLdif.ModelGenerationResult),
    ) -> FlextDbtLdifProtocols.DbtLdif.ModelGenerationResult:
        return value

    def model_protocol_6(
        value: (FlextDbtLdifModels.DbtLdif.ParseValidationResult),
    ) -> FlextDbtLdifProtocols.DbtLdif.ParseValidationResult:
        return value

    def model_protocol_7(
        value: (FlextDbtLdifModels.DbtLdif.WorkflowResult),
    ) -> FlextDbtLdifProtocols.DbtLdif.WorkflowResult:
        return value
