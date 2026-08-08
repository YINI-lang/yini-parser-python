"""
Inspect nested.

Run from the repository root with:
    python examples/example2.py
"""

from pathlib import Path

from yini_parser import load


def main() -> None:
    config = load(Path(__file__).with_name("nested.yini"))

    project = config["Project"]
    database = project["Database"]
    logging = project["Logging"]

    dsn = f"{database['host']}:{database['port']}/{database['name']}"

    print(f"Project: {project['name']}")
    print(f"Environment: {project['environment']}")
    print(f"Database: {dsn}")
    print(f"Logging: {logging['level']} -> {logging['file']}")


if __name__ == "__main__":
    main()
