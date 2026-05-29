# tests/test_load.py
from __future__ import annotations

from yini_parser.api.load import load, loads


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
