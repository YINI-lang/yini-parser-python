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


def test_strict_string_concatenation_rejects_non_string_tail_operands() -> None:
    text = """
@yini

^ App
label = "port-" + 5432

/END
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)
