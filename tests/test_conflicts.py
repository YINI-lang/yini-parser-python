# tests/test_conflicts.py
from __future__ import annotations

import pytest

from yini_parser.api.load import loads
from yini_parser.api.errors import YiniParseError
from yini_parser.api.warnings import YiniParseWarning

"""
These rules apply:

- In lenient mode, when duplicate keys occur, the FIRST definition always wins.
- Duplicate keys MUST NOT overwrite an earlier key. Later duplicate keys should emit warnings.
- Duplicate section names MUST produce an error in both modes.
- Member/section name collisions MUST result in an error in both modes.
- No merging of repeated sections is allowed.
- In strict mode, duplicate keys and duplicate section names MUST result in an error.
"""


def test_orphan_member_and_top_level_section_collision_is_an_error() -> None:
    text = "@yini\nitem = 1\n^ item\nvalue = 2\n"

    with pytest.raises(YiniParseError, match="Orphan member and top-level section"):
        loads(text)


def test_duplicate_key_first_value_wins_in_lenient_mode() -> None:
    text = """
^ App
name = "First"
name = "Second"
""".lstrip()

    with pytest.warns(YiniParseWarning, match="Duplicate key"):
        result = loads(text)

    assert result == {
        "App": {
            "name": "First",
        },
    }


def test_duplicate_scalar_key_first_value_wins_in_lenient_mode() -> None:
    text = """
^ App
pageSize = 10
pageSize = 25
""".lstrip()

    with pytest.warns(YiniParseWarning, match="Duplicate key"):
        result = loads(text)

    assert result == {
        "App": {
            "pageSize": 10,
        },
    }


def test_repeated_top_level_section_errors_in_lenient_mode() -> None:
    text = """
^ App
name = "Demo"

^ App
debug = true
""".lstrip()

    with pytest.raises(YiniParseError, match="Duplicate section"):
        loads(text)


@pytest.mark.parametrize("strict", [False, True])
def test_repeated_nested_section_errors_in_both_modes(strict: bool) -> None:
    text = """
^ App
^^ Server
host = "localhost"

^^ Server
port = 8080
""".lstrip()

    with pytest.raises(YiniParseError, match="Duplicate section"):
        loads(text + "/END\n", strict=strict)


def test_key_then_section_name_collision_errors_in_lenient_mode() -> None:
    text = """
^ App
Server = "localhost"

^^ Server
port = 8080
""".lstrip()

    with pytest.raises(YiniParseError, match="Name collision"):
        loads(text)


def test_duplicate_parent_section_errors_before_later_member_in_lenient_mode() -> None:
    text = """
^ App
^^ Server
port = 8080

^ App
Server = "localhost"
""".lstrip()

    with pytest.raises(YiniParseError, match="Duplicate section"):
        loads(text)


def test_duplicate_key_should_warn_in_lenient_mode() -> None:
    text = """
^ App
name = "First"
name = "Second"
""".lstrip()

    with pytest.warns(
        YiniParseWarning,
        match=r"Duplicate key 'name' ignored\. The first value is kept\.",
    ):
        loads(text)


def test_repeated_section_should_error_in_lenient_mode() -> None:
    text = """
^ App
name = "Demo"

^ App
debug = true
""".lstrip()

    with pytest.raises(
        YiniParseError,
        match=r"Duplicate section 'App' is not allowed\.",
    ):
        loads(text)


def test_key_section_collision_should_error_in_lenient_mode() -> None:
    text = """
^ App
Server = "localhost"

^^ Server
port = 8080
""".lstrip()

    with pytest.raises(YiniParseError, match="Name collision for 'Server'"):
        loads(text)


def test_duplicate_key_should_error_in_strict_mode() -> None:
    text = """
^ App
name = "First"
name = "Second"
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_repeated_section_should_error_in_strict_mode() -> None:
    text = """
^ App
name = "Demo"

^ App
debug = true
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_key_then_section_name_collision_should_error_in_strict_mode() -> None:
    text = """
^ App
Server = "localhost"

^^ Server
port = 8080
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_duplicate_parent_section_should_error_in_strict_mode() -> None:
    text = """
^ App
^^ Server
port = 8080

^ App
Server = "localhost"
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)
