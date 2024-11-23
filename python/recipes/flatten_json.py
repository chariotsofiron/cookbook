"""Flatten json."""

from typing import Any


def flatten_json(y: dict[str, Any], prefix: str = "") -> dict[str, Any]:
    """Flattens json/dict containing inner dicts and lists."""
    out = {}

    def flatten(element: dict[str, Any], name: str = "") -> None:
        if isinstance(element, dict):
            for a, value in element.items():
                flatten(value, name + a + "_")
        elif isinstance(element, list):
            for i, a in enumerate(element):
                flatten(a, name + str(i) + "_")
        else:
            out[name[:-1]] = element

    flatten(y, prefix)
    return out
