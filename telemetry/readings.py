import csv
from dataclasses import dataclass
from typing import Iterable, TextIO


@dataclass(frozen=True)
class Reading:
    machine: str
    timestamp: int
    value: float


def read_csv(stream: TextIO) -> list[Reading]:
    readings = []
    for row in csv.DictReader(stream):
        readings.append(Reading(row["machine"], int(row["timestamp"]), float(row["value"])))
    return readings


def latest_values(readings: Iterable[Reading]) -> dict[str, float]:
    """Return the most recent value for each machine."""
    values = {}
    for reading in readings:
        values[reading.machine] = reading.value
    return values
