# tests/test_values.py
from __future__ import annotations

from yini_parser.api.load import loads


"""
Keep:
- One responsibility per test.
- Readable assertions.
- Simple input documents.
"""


def test_parses_booleans() -> None:
    text = """
^ App
enabled = true
disabled = off
confirmed = yes
rejected = no
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "enabled": True,
            "disabled": False,
            "confirmed": True,
            "rejected": False,
        },
    }


def test_parses_null_and_empty_value_as_none() -> None:
    text = """
^ App
explicitNull = null
implicitNull =
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "explicitNull": None,
            "implicitNull": None,
        },
    }


def test_parses_numbers() -> None:
    text = """
^ App
intValue = 25
floatValue = 1.25
negativeInt = -7
negativeFloat = -0.5
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "intValue": 25,
            "floatValue": 1.25,
            "negativeInt": -7,
            "negativeFloat": -0.5,
        },
    }


def test_parses_basic_strings() -> None:
    text = r'''
^ App
name = "Demo App"
single = 'hello'
path = "\home\user\docs\report.docx"
'''.lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "single": "hello",
            "path": r"\home\user\docs\report.docx",
        },
    }


def test_parses_lists() -> None:
    text = """
^ App
items = ["search", "logs", "metrics"]
numbers = [1, 2, 3]
flags = [true, off, yes, no]
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "items": ["search", "logs", "metrics"],
            "numbers": [1, 2, 3],
            "flags": [True, False, True, False],
        },
    }


def test_parses_empty_list_and_empty_object() -> None:
    text = """
^ App
items = []
meta = {}
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "items": [],
            "meta": {},
        },
    }


def test_parses_inline_objects() -> None:
    text = """
^ App
cache = { maxMb: 256, maxHours: 0.5 }
db = { host: "localhost", port: 5432, enabled: true }
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "cache": {
                "maxMb": 256,
                "maxHours": 0.5,
            },
            "db": {
                "host": "localhost",
                "port": 5432,
                "enabled": True,
            },
        },
    }


def test_parses_nested_inline_objects_and_lists() -> None:
    text = """
^ App
config = {
    name: "demo",
    tags: ["alpha", "beta"],
    limits: { maxUsers: 10, timeoutSec: 30 }
}
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "config": {
                "name": "demo",
                "tags": ["alpha", "beta"],
                "limits": {
                    "maxUsers": 10,
                    "timeoutSec": 30,
                },
            },
        },
    }


def test_parses_string_concatenation() -> None:
    text = """
^ App
message = "hello"
    + " "
    + "world"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "message": "hello world",
        },
    }
