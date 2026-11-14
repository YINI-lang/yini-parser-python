# tests/test_parser_mode.py
from __future__ import annotations

import pytest

from yini_parser.api.errors import YiniParseError
from yini_parser.api.load import loads
from yini_parser.api.warnings import YiniParseWarning


@pytest.mark.parametrize("strict", [False, True])
def test_reserved_include_directive_is_rejected(strict: bool) -> None:
    with pytest.raises(YiniParseError, match="@include directive is reserved"):
        loads('@include "base.yini"\n^ App\nvalue = true\n/END\n', strict=strict)


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


def test_yini_lenient_declaration_warns_in_strict_parser_mode() -> None:
    text = """
@yini lenient

^ App
name = "Demo App"

/END
""".lstrip()

    with pytest.warns(
        YiniParseWarning,
        match="declares '@yini lenient'.*strict mode",
    ) as captured:
        result = loads(text, strict=True)

    assert result == {"App": {"name": "Demo App"}}
    warning = captured[0].message
    assert isinstance(warning, YiniParseWarning)
    assert (warning.code, warning.line, warning.column) == ("mode-mismatch", 1, 7)


def test_yini_lenient_declaration_still_requires_strict_terminator() -> None:
    text = """
@yini lenient

^ App
name = "Demo App"

""".lstrip()

    with pytest.warns(YiniParseWarning, match="declares '@yini lenient'"):
        with pytest.raises(
            YiniParseError, match="requires exactly one document terminator"
        ):
            loads(text, strict=True)


def test_yini_lenient_declaration_still_rejects_strict_trailing_comma() -> None:
    with pytest.warns(YiniParseWarning, match="declares '@yini lenient'"):
        with pytest.raises(YiniParseError, match="Trailing commas"):
            loads("@yini lenient\n^ App\nvalues = [1,]\n/END\n", strict=True)


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
