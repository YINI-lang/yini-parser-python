# tests/test_sections.py
from __future__ import annotations

import pytest

from yini_parser.api.load import loads
from yini_parser.api.errors import YiniParseError


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


def test_parses_section_markers_with_underscore_separators() -> None:
    text = """
^ Root
name = "root"

^_^ Child
enabled = true

^_^_^ GrandChild
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


def test_parses_sibling_sections_with_underscore_marker_separators() -> None:
    text = """
^ Root
name = "root"

^_^ Api
host = "localhost"

^_^ Database
port = 5432
""".lstrip()

    result = loads(text)

    assert result == {
        "Root": {
            "name": "root",
            "Api": {
                "host": "localhost",
            },
            "Database": {
                "port": 5432,
            },
        },
    }


def test_parses_repeated_section_markers_up_to_level_9() -> None:
    text = """
^ L1
^^ L2
^^^ L3
^^^^ L4
^^^^^ L5
^^^^^^ L6
^^^^^^^ L7
^^^^^^^^ L8
^^^^^^^^^ L9
value = "deep"
""".lstrip()

    result = loads(text)

    assert (
        result["L1"]["L2"]["L3"]["L4"]["L5"]["L6"]["L7"]["L8"]["L9"]["value"] == "deep"
    )


def test_rejects_section_level_jump() -> None:
    text = """
^ Root
^^^ GrandChild
value = true
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


def test_rejects_starting_with_repeated_section_markers_at_level_10() -> None:
    text = """
^^^^^^^^^^ TooDeep
value = true
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


def test_rejects_repeated_section_markers_at_level_10() -> None:
    text = """
^ L1
^^ L2
^^^ L3
^^^^ L4
^^^^^ L5
^^^^^^ L6
^^^^^^^ L7
^^^^^^^^ L8
^^^^^^^^^ L9
^^^^^^^^^^ L10
value = true
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


def test_parses_numeric_section_level_10_shorthand() -> None:
    text = """
^ Root
^2 Two
^3 Three
^4 Four
^5 Five
^6 Six
^7 Seven
^8 Eight
^9 Nine
^10 Ten
value = true
""".lstrip()

    result = loads(text)

    current = result["Root"]
    for name in [
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
    ]:
        current = current[name]

    assert current["value"] is True
