"""Snippets for handling csv files in Python."""
import csv
from pathlib import Path
from typing import Any, Iterable


def read_csv(path: str) -> list[list[str]]:
    """Reads a csv file.

    :param path: The path to the file
    """
    with Path(path).open(newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        return list(reader)


def write_csv(
    path: str, data: Iterable[Iterable[Any]], header: Iterable[Any]
) -> None:
    """Write csv file.

    :param path: The path to the file
    :param data: The data to write
    :param header: The header for the csv file
    """
    with Path(path).open("w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
