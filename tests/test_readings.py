import io
import unittest

from telemetry.readings import Reading, latest_values, read_csv


class ReadingsTests(unittest.TestCase):
    def test_converts_csv_fields(self):
        source = io.StringIO("machine,timestamp,value\npress,10,2.5\n")
        self.assertEqual(read_csv(source), [Reading("press", 10, 2.5)])

    def test_latest_across_machines(self):
        rows = [Reading("b", 1, 8), Reading("a", 2, 1), Reading("a", 3, 4)]
        self.assertEqual(latest_values(rows), {"a": 4, "b": 8})

    def test_empty_summary(self):
        self.assertEqual(latest_values([]), {})
