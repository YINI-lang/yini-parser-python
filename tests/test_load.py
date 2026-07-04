# tests/test_load.py
from __future__ import annotations

import pytest

from yini_parser.api.load import load, loads
from yini_parser.api.warnings import YiniParseWarning


def test_loads_parses_basic_document() -> None:
    text = """
^ App
name = "Demo App"
version = 1.2
features = ["search", "logs"]
debug = false
pageSize = 25

^^ Server
host = "localhost"
port = 8080
useTLS = off
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "version": 1.2,
            "features": ["search", "logs"],
            "debug": False,
            "pageSize": 25,
            "Server": {
                "host": "localhost",
                "port": 8080,
                "useTLS": False,
            },
        },
    }


def test_load_parses_sample_basic_file() -> None:
    result = load("sample/basic.yini")

    assert result == {
        "App": {
            "name": "Demo App",
            "version": 1.2,
            "features": ["search", "logs"],
            "debug": False,
            "pageSize": 25,
            "Server": {
                "host": "localhost",
                "port": 8080,
                "useTLS": False,
            },
        },
    }


def test_loads_parses_empty_value_as_none() -> None:
    text = """
^ App
name =
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": None,
        },
    }


def test_loads_parses_empty_object_and_list() -> None:
    text = """
^ App
meta = {}
items = []
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "meta": {},
            "items": [],
        },
    }


def test_loads_accepts_section_without_final_newline() -> None:
    # Arrange.
    source = "^ App"

    # Act.
    result = loads(source)

    # Assert.
    assert result == {"App": {}}


def test_loads_accepts_assignment_without_final_newline() -> None:
    # Arrange.
    source = '^ App\nname = "demo"'

    # Act.
    result = loads(source)

    # Assert.
    assert result == {"App": {"name": "demo"}}


def test_load_accepts_file_without_final_newline(tmp_path) -> None:
    # Arrange.
    path = tmp_path / "config.yini"
    path.write_text('^ App\nname = "demo"', encoding="utf-8")

    # Act.
    result = load(path)

    # Assert.
    assert result == {"App": {"name": "demo"}}


def test_loads_accepts_utf8_bom_in_lenient_mode_with_warning() -> None:
    source = '\ufeff@yini\n\n^ Encoding\nname = "utf8-bom"\naccepted = true\n'

    with pytest.warns(YiniParseWarning, match="BOM"):
        result = loads(source)

    assert result == {
        "Encoding": {
            "name": "utf8-bom",
            "accepted": True,
        },
    }


def test_load_accepts_utf8_bom_in_lenient_mode_with_warning(tmp_path) -> None:
    path = tmp_path / "bom.yini"
    path.write_bytes(
        b'\xef\xbb\xbf@yini\n\n^ Encoding\nname = "utf8-bom"\naccepted = true\n'
    )

    with pytest.warns(YiniParseWarning, match="BOM"):
        result = load(path)

    assert result == {
        "Encoding": {
            "name": "utf8-bom",
            "accepted": True,
        },
    }


def test_loads_accepts_utf8_bom_in_strict_mode() -> None:
    source = (
        '\ufeff@yini strict\n\n^ Encoding\nname = "utf8-bom"\naccepted = true\n\n/END\n'
    )

    result = loads(source, strict=True)

    assert result == {
        "Encoding": {
            "name": "utf8-bom",
            "accepted": True,
        },
    }
