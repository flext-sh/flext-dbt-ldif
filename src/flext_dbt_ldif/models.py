"""Compatibility facade: re-export dbt_models via models.py.

Standardizes imports to use flext_dbt_ldif.models across the codebase.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from .dbt_models import *
