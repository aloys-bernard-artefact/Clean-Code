# Standard library
import logging
# Third party imports (need to be added to pyproject.toml)
import click

logger = logging.getLogger(__name__)

@click.command()
@click.option(
    "--name",
    help="The person to greet.",
)
def hello(name):
    """Say hello to NAME."""
    click.echo(f"Hello {name}!")
    logger.log(logging.INFO,"✅ Hello executed.")


if __name__ == "__main__":
    hello()