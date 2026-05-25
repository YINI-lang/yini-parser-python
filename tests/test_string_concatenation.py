import pytest

from yini_parser import loads, YiniParseError


def test_string_concatenation_uses_explicit_line_end_plus() -> None:
    text = """
^ App
message = "Hello" + " " + "there!"
""".lstrip()

    result = loads(text)

    assert result["App"]["message"] == "Hello there!"


def test_parses_string_concatenation() -> None:
    text = """
^ App
message = "hello" +
    " " +
    "world"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "message": "hello world",
        },
    }


# ---------
# Test lenient string concatenation.
# ---------


def test_lenient_string_concatenation_allows_scalar_tail_operands() -> None:
    text = """
^ App
label = "port-" + 5432
enabledLabel = "enabled-" + true
emptyLabel = "value-" + null
""".lstrip()

    result = loads(text)

    assert result["App"]["label"] == "port-5432"
    assert result["App"]["enabledLabel"] == "enabled-true"
    assert result["App"]["emptyLabel"] == "value-null"


def test_lenient_concatenation_requires_first_operand_to_be_string() -> None:
    text = """
^ App
value = 1 + 2 + "3"
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)


def test_lenient_concatenation_converts_scalar_tail_operands_canonically() -> None:
    text = """
^ App
hexLabel = "hex-" + 0xFF
boolLabel = "enabled-" + YES
nullLabel = "value-" + NULL
plusNumber = "n-" + +100
""".lstrip()

    result = loads(text)

    assert result["App"]["hexLabel"] == "hex-255"
    assert result["App"]["boolLabel"] == "enabled-true"
    assert result["App"]["nullLabel"] == "value-null"
    assert result["App"]["plusNumber"] == "n-100"


# ---------
# Test strict string concatenation.
# ---------


def test_strict_string_concatenation_rejects_non_string_tail_operands() -> None:
    text = """
@yini

^ App
label = "port-" + 5432

/END
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)
