"""
Utility helpers for ChatGPT-generated lab report tooling.
"""

import json
from pathlib import Path
from typing import Any


def ensure_dir(path: str | Path) -> Path:
    """
    Create a directory if it does not already exist.
    """

    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_json(data: dict[str, Any], path: str | Path, indent: int = 2) -> Path:
    """
    Write a dictionary to JSON.
    """

    path = Path(path)
    ensure_dir(path.parent)

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)

    return path


def write_text(text: str, path: str | Path) -> Path:
    """
    Write text to a file.
    """

    path = Path(path)
    ensure_dir(path.parent)

    with path.open("w", encoding="utf-8") as f:
        f.write(text)

    return path
