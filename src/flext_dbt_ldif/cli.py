"""CLI entrypoint for flext-dbt-ldif — dispatches through the meltano dbt base.

Copyright (c) 2026 FLEXT Team. All rights reserved.
src/flext_dbt_ldif/cli
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from collections.abc import Sequence

from flext_dbt_ldif import FlextDbtLdifServiceBase


def main(args: Sequence[str] | None = None) -> int:
    """Run the flext-dbt-ldif console-script entry point.

    Delegates to the inherited dbt ``cli_main`` dispatcher.

    Args:
        args: Command-line arguments; defaults to ``sys.argv[1:]`` when
            omitted.

    Returns:
        Process exit code from the dispatched dbt command.

    """
    return FlextDbtLdifServiceBase().cli_main(args)


__all__: list[str] = ["main"]
