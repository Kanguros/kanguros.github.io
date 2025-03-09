from pathlib import Path

import click
from click.types import File


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


if __name__ == "__main__":
    main()
