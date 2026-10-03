"""CLI entrypoint for flext-dbt-ldif — dispatches through the meltano dbt base."""

from __future__ import annotations

from flext_dbt_ldif import FlextDbtLdifServiceBase, t


def main(args: t.StrSequence | None = None) -> int:
    """Console-script entry point delegating to the inherited dbt ``cli_main``."""
    return FlextDbtLdifServiceBase().cli_main(args)


__all__: list[str] = ["main"]
