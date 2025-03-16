import logging
from pathlib import Path

import rich
import rich_click as click
from click.types import Path as ClickPath
from rich.logging import RichHandler

from .check import DEFAULT_CHECKS
from .lookup import resolve_rules_addresses
from .models import AddressGroup, AddressObject, SecurityRule
from .shadower import run_checks_on_rules

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


@click.command(add_help_option=True)
@click.option(
    "--security-rules",
    "-sr",
    "security_rules_file",
    type=ClickPath(exists=True, dir_okay=False, path_type=Path),
    default=Path("./data/security_rules.json"),
    show_default=True,
    help="Path to JSON file with Security Rules",
)
@click.option(
    "--address-groups",
    "-ag",
    "address_groups_file",
    type=ClickPath(exists=True, dir_okay=False, path_type=Path),
    default=Path("./data/address_grups.json"),
    show_default=True,
    help="Path to JSON file with Address Groups",
)
@click.option(
    "--address-objects",
    "-ao",
    "address_objects_file",
    type=ClickPath(exists=True, dir_okay=False, path_type=Path),
    default=Path("./data/address_objects.json"),
    show_default=True,
    help="Path to JSON file with Address Objects",
)
def main(security_rules_file, address_objects_file, address_groups_file):
    """SRF stands for Shadowing Rules Finder"""
    security_rules = SecurityRule.load_from_json(security_rules_file)
    address_objects = AddressObject.load_from_json(address_objects_file)
    address_groups = AddressGroup.load_from_json(address_groups_file)

    security_rules = resolve_rules_addresses(
        security_rules, address_objects, address_groups
    )

    results = run_checks_on_rules(security_rules, DEFAULT_CHECKS)
    rich.print(results)


if __name__ == "__main__":
    main()
