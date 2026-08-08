"""
Read basic.

Run from the repository root with:
    python examples/example1.py
"""

from pathlib import Path

from yini_parser import load


def main() -> None:
    config = load(Path(__file__).with_name("basic.yini"))
    app = config["App"]

    print(f"{app['name']} v{app['version']}")
    print(f"Listening on port {app['port']}")
    print(f"Debug mode: {app['debug']}")


if __name__ == "__main__":
    main()
