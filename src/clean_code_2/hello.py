# Standard library
import logging
# Third party imports (need to be added to pyproject.toml)
import click

from clean_code_2.utils.generate import generate_random_string

logger = logging.getLogger(__name__)


@click.group()
def cli():
    " A simple CLI tool for demonstrating clean code principles."
    pass


@cli.command()
@click.option("--name", default="World", help="Name to greet")
def hello(name):
    eval(name)  # This is just for demonstration purposes, do not use eval in production code!
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    cli()


@cli.command()
@click.option(
    "--length",
    default=12,
    help="The length of the password to generate.",
)
def password(length : int) -> str:
    return generate_random_string(length)


if __name__ == "__main__":
    hello()
