import logging
from pathlib import Path

import rich_click as click
from click.types import File
from rich.logging import RichHandler

LOG_FORMAT = "%(message)s"
LOG_DEFAULT_LEVEL = "INFO"
logging.basicConfig(
    level=LOG_DEFAULT_LEVEL,
    format=LOG_FORMAT,
    datefmt="[%X]",
    handlers=[
        RichHandler(
            rich_tracebacks=True, tracebacks_suppress=[click], show_path=False
        )
    ],
)

log = logging.getLogger(__name__)


@click.group(add_help_option=True)
@click.option(
    "--security-rules",
    "-sr",
    "security_rules",
    type=File(),
    default=Path("./data/security_rules.json"),
    show_default=True,
    help="Path to JSON file with Security Rules",
)
@click.option(
    "--address-groups",
    "-ag",
    "address_groups",
    type=File(),
    default=Path("./data/address_groups.json"),
    show_default=True,
    help="Path to JSON file with Address Groups",
)
@click.option(
    "--address-objects",
    "-ao",
    "address_objects",
    type=File(),
    default=Path("./data/address_objects.json"),
    show_default=True,
    help="Path to JSON file with Address Objects",
)
def main(security_rules, address_groups, address_objects):
    """SRF stands for Shadowing Rules Finder"""


@main.command("find")
@click.argument("names", metavar="NAME", nargs=-1, default=None, required=False)
def main_find(names):
    if names:
        log.info(f"Looking for shadowing rules of rules: {', '.join(names)}")
    log.info("Looking for all shadowing rules")


if __name__ == "__main__":
    main()
