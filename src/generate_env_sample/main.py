import typer

app = typer.Typer(
    help="A CLI tool to generate .env.sample files from .env files.",
    invoke_without_command=True,
)


@app.callback()
def main() -> None:
    """Generate a .env.sample file from the existing .env file."""
    typer.echo("Generating .env.sample from .env...")


if __name__ == "__main__":
    app()
