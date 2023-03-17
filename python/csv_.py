"""Snippets for handling csv files in Python."""
import csv
from typing import Any, Iterable


def read_csv(path: str) -> None:
    """Read csv file.

    :param path: The path to the file
    """
    with open(path, newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # skip header
        for row in reader:
            print(row)


def write_csv(path: str, data: Iterable[Iterable[Any]], header: Iterable[Any]) -> None:
    """Write csv file.

    :param path: The path to the file
    :param data: The data to write
    :param header: The header for the csv file
    """
    with open(path, "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
