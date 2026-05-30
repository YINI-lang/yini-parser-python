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


def test_strict_mode_rejects_empty_member_value() -> None:
    text = """
@yini

^ App
name =

/END
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_strict_mode_rejects_trailing_comma_in_list() -> None:
    text = """
@yini

^ App
items = [1, 2, ]

/END
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_strict_mode_rejects_trailing_comma_in_inline_object() -> None:
    text = """
@yini

^ App
obj = { a: 1, }

/END
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)


def test_strict_mode_rejects_orphan_root_member() -> None:
    text = """
@yini strict

name = "orphan-member-example"

^ Package
version = "0.1.0"

/END
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text, strict=True)
