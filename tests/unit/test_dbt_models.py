"""Test DBT models functionality.

This module tests the DBT models functionality of flext-dbt-ldif.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

from pathlib import Path

from flext_dbt_ldif import (
    FlextDbtLdifConfig,
    FlextDbtLdifModelGenerator,
    FlextLdifDbtModel,
)


def test_write_models_and_sql_generation(tmp_path: Path) -> None:
    """Test writing models and generating SQL."""
    gen = FlextDbtLdifModelGenerator(FlextDbtLdifConfig(), project_dir=tmp_path)
    # Create a simple staging model and analytics models
    stg = FlextLdifDbtModel(
      name="stg_persons",
      description="staging",
      columns=[{"name": "dn"}, {"name": "object_class"}],
      materialization="view",
    )
    an_insights = FlextLdifDbtModel(
      name="analytics_ldif_insights",
      description="insights",
      columns=[{"name": "analysis_date"}],
      materialization="table",
    )
    an_hier = FlextLdifDbtModel(
      name="analytics_ldif_hierarchy",
      description="hier",
      columns=[{"name": "dn_path"}],
      materialization="table",
    )
    result = gen.write_models_to_disk([stg, an_insights, an_hier], overwrite=True)
    assert result.success
    data = result.data or {}
    written = data.get("written_files", [])
    assert any(str(p).endswith("stg_persons.sql") for p in written)
    assert any(str(p).endswith("analytics_ldif_insights.sql") for p in written)
    assert any(str(p).endswith("analytics_ldif_hierarchy.sql") for p in written)


def test_generate_analytics_models() -> None:
    """Test generating analytics models."""
    gen = FlextDbtLdifModelGenerator(FlextDbtLdifConfig())
    res = gen.generate_analytics_models([])
    assert res.success
    models = res.data or []
    assert any(m.name.startswith("analytics_") for m in models)
