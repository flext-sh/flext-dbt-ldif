"""Command-line interface for FLEXT dbt LDIF.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT

"""

from __future__ import annotations

import sys
from typing import NoReturn

import click
from rich.console import Console

from flext_dbt_ldif import __version__

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="flext-data.dbt.flext-dbt-ldif")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.pass_context
def cli(ctx: click.Context, *, verbose: bool) -> None:
    """FLEXT dbt LDIF - Advanced LDAP Data Analytics and Transformations."""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


@cli.command()
def info() -> None:
    """Show package information."""
    console.print(f"[bold blue]FLEXT dbt LDIF[/bold blue] v{__version__}")
    console.print("Advanced LDAP Data Analytics and Transformations")
    console.print("")
    console.print("[bold]Features:[/bold]")
    console.print("• Programmatic dbt model generation")
    console.print("• LDIF data processing and analytics")
    console.print("• Advanced SQL pattern generation")
    console.print("• PostgreSQL optimized transformations")


@cli.command()
def generate() -> None:
    """Generate dbt models from LDIF schema definitions."""
    console.print(
        "[bold yellow]Model generation functionality coming soon![/bold yellow]",
    )
    console.print("This will generate dbt models programmatically.")


@cli.command()
def validate() -> None:
    """Validate dbt models and configurations."""
    console.print(
        "[bold yellow]Model validation functionality coming soon![/bold yellow]",
    )
    console.print("This will validate generated dbt models.")


def main() -> NoReturn:
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted by user[/bold red]")
        sys.exit(1)
    except (OSError, RuntimeError, ValueError) as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
