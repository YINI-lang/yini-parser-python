# tests/test_parser_mode.py
from __future__ import annotations

import pytest

from yini_parser.api.errors import YiniParseError
from yini_parser.api.warnings import YiniParseWarning
from yini_parser.api.load import loads


def test_yini_strict_declaration_matches_strict_parser_mode() -> None:
    text = """
@yini strict

^ App
name = "Demo App"

/END
""".lstrip()

    result = loads(text, strict=True)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }


def test_yini_strict_declaration_rejects_lenient_parser_mode() -> None:
    text = """
@yini strict

^ App
name = "Demo App"

/END
""".lstrip()

    with pytest.raises(
        YiniParseError,
        match="declares '@yini strict'.*lenient mode",
    ):
        loads(text, strict=False)


def test_yini_lenient_declaration_matches_lenient_parser_mode() -> None:
    text = """
@yini lenient

^ App
name = "Demo App"
""".lstrip()

    result = loads(text, strict=False)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }


def test_yini_lenient_declaration_warns_in_strict_parser_mode_1() -> None:
    text = """
@yini lenient

^ App
name = "Demo App"

/END
""".lstrip()

    with pytest.warns(
        Warning,
        match="declares '@yini lenient'.*strict mode",
    ):
        result = loads(text, strict=True)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }


def test_yini_lenient_declaration_warns_in_strict_parser_mode_2() -> None:
    text = """
@yini lenient

^ App
name = "Demo App"

/END
""".lstrip()

    with pytest.warns(
        YiniParseWarning,
        match="declares '@yini lenient'.*strict mode",
    ):
        result = loads(text, strict=True)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }


def test_plain_yini_directive_allows_lenient_parser_mode() -> None:
    text = """
@yini

^ App
name = "Demo App"
""".lstrip()

    result = loads(text, strict=False)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }


def test_plain_yini_directive_allows_strict_parser_mode_when_document_is_strict_valid() -> (
    None
):
    text = """
@yini

^ App
name = "Demo App"

/END
""".lstrip()

    result = loads(text, strict=True)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }


def test_yini_mode_declaration_rejects_unknown_mode() -> None:
    text = """
@yini banana

^ App
name = "Demo"
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


def test_yini_directive_after_member_is_rejected() -> None:
    text = """
^ App
name = "Demo App"

@yini
""".lstrip()

    with pytest.raises(YiniParseError, match="@yini directives must appear"):
        loads(text)


def test_yini_directive_after_section_is_rejected() -> None:
    text = """
^ App

@yini

name = "Demo App"
""".lstrip()

    with pytest.raises(YiniParseError, match="@yini directives must appear"):
        loads(text)
