# ruff: noqa: N802
import json
from pathlib import Path

from .models import AddressGroup, AddressObject, SecurityRule


def load_json(name: str):
    """Loads JSON file from the data folder and return it."""
    file_path = Path(__file__).parent.parent / "data" / f"{name}.json"
    with open(file_path, encoding="utf-8") as f:
        return json.loads(f.read())


def test_SecurityRule():
    data = load_json("security_rules")
    rules = SecurityRule.load_many(data)
    print(rules)
    assert [isinstance(rule, SecurityRule) for rule in rules]


def test_AddressObject():
    data = load_json("address_objects")
    address_objects = AddressObject.load_many(data)
    print(address_objects)
    assert [isinstance(ao, AddressObject) for ao in address_objects]


def test_AddressGroup():
    data = load_json("address_groups")
    address_groups = AddressGroup.load_many(data)
    print(address_groups)
    assert [isinstance(ag, AddressGroup) for ag in address_groups]
