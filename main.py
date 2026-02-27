import argparse
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="tamir",
        description="Tamir CLI",
    )
    # Add subcommands or arguments here
    parser.add_argument("--version", action="version", version="0.1.0")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("Hello from tamir!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
