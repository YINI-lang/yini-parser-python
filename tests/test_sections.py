# tests/test_sections.py
from __future__ import annotations

from yini_parser.api.load import loads


def test_parses_single_top_level_section() -> None:
    text = """
^ App
name = "Demo App"
version = 1.0
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "version": 1.0,
        },
    }


def test_parses_nested_sections() -> None:
    text = """
^ App
name = "Demo App"

^^ Server
host = "localhost"
port = 8080
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "Server": {
                "host": "localhost",
                "port": 8080,
            },
        },
    }


def test_parses_multiple_sibling_sections() -> None:
    text = """
^ App
name = "Demo App"

^ User
name = "Marko"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
        },
        "User": {
            "name": "Marko",
        },
    }


def test_returns_from_deeper_section_to_shallower_section() -> None:
    text = """
^ Root
name = "root"

^^ Child
enabled = true

^ Sibling
active = false
""".lstrip()

    result = loads(text)

    assert result == {
        "Root": {
            "name": "root",
            "Child": {
                "enabled": True,
            },
        },
        "Sibling": {
            "active": False,
        },
    }


def test_parses_backticked_section_names() -> None:
    text = """
^ `DB Config`
host = "db.internal"

^^ `Connection Pool`
size = 10
""".lstrip()

    result = loads(text)

    assert result == {
        "DB Config": {
            "host": "db.internal",
            "Connection Pool": {
                "size": 10,
            },
        },
    }


def test_parses_numeric_section_level_shorthand() -> None:
    text = """
^ Root
name = "root"

^2 Child
enabled = true

^3 GrandChild
value = 42
""".lstrip()

    result = loads(text)

    assert result == {
        "Root": {
            "name": "root",
            "Child": {
                "enabled": True,
                "GrandChild": {
                    "value": 42,
                },
            },
        },
    }


def test_parses_mixed_section_depth_transitions() -> None:
    text = """
^ Root
rootValue = 1

^^ ChildA
childAValue = 2

^^ ChildB
childBValue = 3

^^^ GrandChild
grandChildValue = 4

^ AnotherRoot
anotherRootValue = 5
""".lstrip()

    result = loads(text)

    assert result == {
        "Root": {
            "rootValue": 1,
            "ChildA": {
                "childAValue": 2,
            },
            "ChildB": {
                "childBValue": 3,
                "GrandChild": {
                    "grandChildValue": 4,
                },
            },
        },
        "AnotherRoot": {
            "anotherRootValue": 5,
        },
    }
