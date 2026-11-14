# tests/test_load.py
from __future__ import annotations

import pytest

from yini_parser.api.load import load, loads
from yini_parser.api.errors import YiniParseError
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

    with pytest.warns(YiniParseWarning, match="empty value"):
        result = loads(text)

    assert result == {
        "App": {
            "name": None,
        },
    }


@pytest.mark.parametrize("section", ["", "^ App\n"])
@pytest.mark.parametrize("comment", ["", "# note", "// note", "/* note */"])
def test_empty_values_warn_with_member_location(section: str, comment: str) -> None:
    with pytest.warns(YiniParseWarning, match="empty value") as caught:
        result = loads(f"{section}value = {comment}\n")

    members = result["App"] if section else result
    assert members == {"value": None}
    assert len(caught) == 1
    assert caught[0].message.line == (2 if section else 1)
    assert caught[0].message.column == 1


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


@pytest.mark.parametrize("ending", ["\r\n", "\r"])
def test_load_normalizes_string_line_endings(tmp_path, ending: str) -> None:
    path = tmp_path / "line-endings.yini"
    source = ending.join(["^ App", 'text = """one', 'two"""', ""])
    path.write_bytes(source.encode("utf-8"))

    result = load(path)

    assert result["App"]["text"] == "one\ntwo"


def test_strict_mode_rejects_mixed_line_endings() -> None:
    source = "@yini strict\r\n^ App\nvalue = true\r\n/END\r\n"

    with pytest.raises(YiniParseError, match="Mixed line endings"):
        loads(source, strict=True)


def test_lenient_mode_warns_once_for_mixed_source_line_endings() -> None:
    source = '^ App\r\ntext = """one\rtwo\nthree"""\r\n'

    with pytest.warns(YiniParseWarning, match="mixed-line-endings") as caught:
        result = loads(source)

    assert result == {"App": {"text": "one\ntwo\nthree"}}
    assert len(caught) == 1


@pytest.mark.parametrize("strict", [False, True])
def test_escaped_line_endings_do_not_count_as_mixed_source_endings(
    strict: bool,
) -> None:
    result = loads('^ App\ntext = E"one\\r\\ntwo"\n/END\n', strict=strict)

    assert result == {"App": {"text": "one\r\ntwo"}}


@pytest.mark.parametrize("ending", ["\r\n", "\r"])
def test_final_newline_added_by_parser_does_not_trigger_mixed_ending_warning(
    ending: str,
) -> None:
    result = loads(f"^ App{ending}value = 1")

    assert result == {"App": {"value": 1}}


def test_strict_mode_rejects_shebang_with_leading_whitespace() -> None:
    source = " #!/usr/bin/env yini\n^ App\nvalue = true\n/END\n"

    with pytest.raises(YiniParseError, match="shebang must start at column 1"):
        loads(source, strict=True)


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
