import pytest

from yini_parser import loads, YiniParseError


def test_strict_mode_requires_document_terminator() -> None:
    text = """
@yini

^ App
name = "Demo"
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_strict_mode_accepts_case_variant_document_terminator() -> None:
    text = """
@yini

^ App
name = "Demo"

/End
""".lstrip()

    result = loads(text, strict=True)

    assert result["App"]["name"] == "Demo"
