# ruff: noqa: N802
import json
from pathlib import Path

import pytest

from .models import AddressGroup, AddressObject, SecurityRule


def load_json(name: str):
    """Loads JSON file from the data folder and return it."""
    file_path = Path(__file__).parent.parent / "data" / f"{name}.json"
    with open(file_path, encoding="utf-8") as f:
        return json.loads(f.read())


@pytest.mark.parametrize(
    "file_name,cls",
    [
        ("security_rules", SecurityRule),
        ("address_objects", AddressObject),
        ("address_groups", AddressGroup),
    ],
)
def test_models(file_name, cls):
    data = load_json(file_name)
    load_method = cls.load_many
    objects = load_method(data)
    print(objects)
    assert [isinstance(obj, cls) for obj in objects]
