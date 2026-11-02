# tests/test_values.py
from __future__ import annotations

import pytest

from yini_parser.api.errors import YiniParseError
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
    text = r"""
^ App
name = "Demo App"
single = 'hello'
path = "\home\user\docs\report.docx"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "single": "hello",
            "path": r"\home\user\docs\report.docx",
        },
    }


def test_parses_classic_octal_escape() -> None:
    text = r"""
^ App
letter = C"\o141"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "letter": "a",
        },
    }


@pytest.mark.parametrize("strict", [False, True])
def test_escaped_prefixes_and_escapes(strict: bool) -> None:
    text = (
        ("@yini\n" if strict else "")
        + "^ App\nupper = E\"a\\nb\"\nlower = e'\\x41\\o7\\?\\/\\`\\0'\n"
        + 'legacy = c"a\\nb"\ntriple = e"""one\\ntwo"""\n'
        + ("/END\n" if strict else "")
    )

    result = loads(text, strict=strict)

    assert result["App"] == {
        "upper": "a\nb",
        "lower": "A\x07?/`\0",
        "legacy": "a\nb",
        "triple": "one\ntwo",
    }


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize("escape", [r"\z", r"\x1", r"\uD800", r"\U00110000", r"\o400"])
def test_rejects_invalid_escaped_string_escape(strict: bool, escape: str) -> None:
    text = (
        ("@yini\n" if strict else "")
        + f'^ App\nbad = E"{escape}"\n'
        + ("/END\n" if strict else "")
    )

    with pytest.raises(YiniParseError):
        loads(text, strict=strict)


def test_rejects_invalid_classic_octal_escape() -> None:
    text = r"""
^ App
bad = C"\o378"
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


@pytest.mark.parametrize("strict", [False, True])
def test_preserves_literal_tabs_in_single_line_strings(strict: bool) -> None:
    text = (
        ("@yini\n" if strict else "")
        + '^ App\nraw = "alpha\tbeta"\nescaped = E"one\ttwo"\n'
        + ("/END\n" if strict else "")
    )

    result = loads(text, strict=strict)

    assert result["App"] == {"raw": "alpha\tbeta", "escaped": "one\ttwo"}


def test_rejects_literal_control_character_in_string() -> None:
    text = '^ App\nbad = "alpha\x01beta"\n'

    with pytest.raises(YiniParseError):
        loads(text)


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


def test_parses_decimal_numbers_with_digit_separators() -> None:
    text = """
^ App
maxUsers = 1_000_000
negativeOffset = -1_250
ratio = 1_000.25
sampleRate = 1e-3
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "maxUsers": 1_000_000,
            "negativeOffset": -1_250,
            "ratio": 1000.25,
            "sampleRate": 1e-3,
        },
    }


def test_parses_base_notation_numbers_with_digit_separators() -> None:
    text = """
^ App
binaryMask = 0b_1010_1100
binaryMaskAlt = %_1010_1100
octalMode = 0o_755
hexColor = 0x_FF_AA_00
hexColorAlt = hex:FF_AA_00
duodecimalValue = 0z_1x_e
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "binaryMask": 0b10101100,
            "binaryMaskAlt": 0b10101100,
            "octalMode": 0o755,
            "hexColor": 0xFFAA00,
            "hexColorAlt": 0xFFAA00,
            "duodecimalValue": 1 * 12 * 12 + 10 * 12 + 11,
        },
    }


@pytest.mark.parametrize("strict", [False, True])
def test_accepts_signed_64_bit_integer_boundaries(strict: bool) -> None:
    text = (
        ("@yini\n" if strict else "")
        + "^ App\nmax = 9223372036854775807\nmin = -9223372036854775808\n"
        + ("/END\n" if strict else "")
    )

    result = loads(text, strict=strict)

    assert result["App"] == {
        "max": 9223372036854775807,
        "min": -9223372036854775808,
    }


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize(
    "number",
    [
        "9223372036854775808",
        "-9223372036854775809",
        "0x8000000000000000",
        "1e400",
        "1e-400",
    ],
)
def test_rejects_number_outside_supported_range(strict: bool, number: str) -> None:
    text = (
        ("@yini\n" if strict else "")
        + f"^ App\nvalue = {number}\n"
        + ("/END\n" if strict else "")
    )

    with pytest.raises(YiniParseError):
        loads(text, strict=strict)
