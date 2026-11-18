import argparse
import json

from .readings import latest_values, read_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Print latest machine readings")
    parser.add_argument("path")
    args = parser.parse_args()
    with open(args.path, encoding="utf-8", newline="") as stream:
        values = latest_values(read_csv(stream))
    print(json.dumps(values, sort_keys=True))


if __name__ == "__main__":
    main()
