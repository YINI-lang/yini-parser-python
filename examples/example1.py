"""
Read a basic YINI file.

Run from the repository root with:
    python examples/example1.py
"""

from pathlib import Path

from yini_parser import load


def main() -> None:
    # Load the YINI file beside this script, regardless of
    # the current directory.
    config = load(Path(__file__).with_name("basic.yini"))
    app = config["App"]

    print("Basic configuration")
    print("-------------------")
    print(f"Name:    {app['name']}")
    print(f"Version: {app['version']}")
    print(f"Port:    {app['port']}")
    print(f"Debug:   {app['debug']}")


if __name__ == "__main__":
    main()
