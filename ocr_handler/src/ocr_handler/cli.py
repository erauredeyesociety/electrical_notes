"""Command line interface. Placeholder until emit.py lands."""

import typer

app = typer.Typer()


@app.command()
def version():
    """Print the version."""
    typer.echo("ocr-handler 0.1.0")
