import json
from pathlib import Path

import pytest

from .models import SecurityRule


def load_json(name: str):
    """Loads JSON file from the data folder and return it."""
    file_path = Path(__file__).parent.parent / "data" / f"{name}.json"
    with open(file_path, encoding="utf-8") as f:
        return json.loads(f.read())


@pytest.mark.parametrize("data", load_json("security_rules"))
def test_load_entry(data):
    rule = SecurityRule.from_entry(data)
    print(rule)
    assert isinstance(rule, SecurityRule)
