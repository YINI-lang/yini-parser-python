# tests/test_parser_mode.py
from __future__ import annotations

import pytest

from yini_parser.api.errors import YiniParseError
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


def test_yini_lenient_declaration_rejects_strict_parser_mode() -> None:
    text = """
@yini lenient

^ App
name = "Demo App"

/END
""".lstrip()

    with pytest.raises(
        YiniParseError,
        match="declares '@yini lenient'.*strict mode",
    ):
        loads(text, strict=True)


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


def test_plain_yini_directive_allows_strict_parser_mode_when_document_is_strict_valid() -> None:
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
