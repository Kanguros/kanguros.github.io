import json
import logging
from pathlib import Path
from typing import Union

logger = logging.getLogger(__name__)


def load_json(file_path: Union[str, Path]):
    """Loads JSON file from given file_path and return it."""
    with open(file_path, encoding="utf-8") as f:
        return json.loads(f.read())
