import pytest

from yini_parser import loads, YiniParseError


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize("key", ["hex", "HEX", "HeX"])
@pytest.mark.parametrize(
    ("value", "expected"),
    [("10", 10), ("1.5", 1.5), ("1e+3", 1000.0), ("0xFF", 255), ("hex:FF", 255)],
)
def test_hex_key_without_separator_whitespace(
    strict: bool, key: str, value: str, expected: int | float
) -> None:
    text = f"^ App\nobj = {{ nested: {{ {key}:{value} }} }}\n/END\n"

    assert loads(text, strict=strict)["App"]["obj"] == {"nested": {key: expected}}


@pytest.mark.parametrize("strict", [False, True])
def test_hex_key_after_collection_values_and_trivia(strict: bool) -> None:
    text = (
        "^ App\nobj = { values: [hex:10, {hex:20}], /* gap */\n"
        "# Comment.\n-- Disabled.\n; Comment.\n"
        "hex:30, other: hex:40 }\n/END\n"
    )

    assert loads(text, strict=strict)["App"]["obj"] == {
        "values": [16, {"hex": 20}],
        "hex": 30,
        "other": 64,
    }


@pytest.mark.parametrize("strict", [False, True])
def test_hex_key_keeps_invalid_decimal_value_invalid(strict: bool) -> None:
    with pytest.raises(YiniParseError):
        loads("^ App\nobj = {hex:01}\n/END\n", strict=strict)


@pytest.mark.parametrize("strict", [False, True])
def test_hex_key_error_preserves_source_location(strict: bool) -> None:
    with pytest.raises(YiniParseError) as error:
        loads("^ App\nobj = {hex:1e9999}\n/END\n", strict=strict)

    assert (error.value.line, error.value.column) == (2, 12)


def test_inline_object_equal_separator_is_allowed_in_lenient_mode() -> None:
    text = """
^ App
cache = { enabled = true, maxMb = 256 }
""".lstrip()

    result = loads(text)

    assert result["App"]["cache"] == {
        "enabled": True,
        "maxMb": 256,
    }


def test_inline_object_equal_separator_is_rejected_in_strict_mode() -> None:
    text = """
@yini

^ App
cache = { enabled = true, maxMb = 256 }

/END
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_inline_object_colon_separator_is_allowed_in_strict_mode() -> None:
    text = """
@yini

^ App
cache = { enabled: true, maxMb: 256 }

/END
""".lstrip()

    result = loads(text, strict=True)

    assert result["App"]["cache"] == {
        "enabled": True,
        "maxMb": 256,
    }


def test_inline_object_member_value_must_begin_on_same_line_as_separator() -> None:
    text = """
^ App
obj = {
    a:
        1
}
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


def test_lenient_inline_object_equal_separator_value_must_begin_on_same_line() -> None:
    text = """
^ App
obj = {
    a =
        1
}
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


def test_inline_object_member_rejects_hash_prefixed_missing_value() -> None:
    text = """
^ App
palette = { primary: #FF0000 }
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)
