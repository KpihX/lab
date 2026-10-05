from __future__ import annotations

import typer

from lab.kit import Context

app = typer.Typer(help="KπX-Labs CLI environment diagnostic and utilities.", no_args_is_help=True)


@app.callback()
def lab() -> None:
    """KπX-Labs CLI environment diagnostic and utilities."""


@app.command()
def context() -> None:
    """Print the sovereign environment context side-by-side with the KπX logo."""
    Context.display()


if __name__ == "__main__":
    app()
