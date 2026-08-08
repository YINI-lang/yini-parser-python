"""
Inspect nested.

Run from the repository root with:
    python examples/example2.py
"""

from pathlib import Path

from yini_parser import load


def main() -> None:
    # Load the YINI file beside this script, regardless of the
    # current directory.
    config = load(Path(__file__).with_name("nested.yini"))

    # Nested YINI sections become nested Python dictionaries.
    project = config["Project"]
    database = project["Database"]
    logging = project["Logging"]

    # Build an application-friendly value from individual config fields.
    database_address = f"{database['host']}:{database['port']}/{database['name']}"

    print("Project")
    print(f"|-- name: {project['name']}")
    print(f"|-- environment: {project['environment']}")
    print("|-- Database")
    print(f"|   |-- address: \"{database_address}\"")
    print(f"|   `-- ssl: {database['ssl']}")
    print("`-- Logging")
    print(f"    |-- level: {logging['level']}")
    print(f"    `-- file: \"{logging['file']}\"")


if __name__ == "__main__":
    main()
