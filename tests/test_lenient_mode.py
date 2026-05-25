# tests/test_lenient_mode.py
from __future__ import annotations

from yini_parser.api.load import loads


def test_lenient_mode_accepts_document_terminator() -> None:
    text = """
@yini

^ App
name = "Demo"

/End
""".lstrip()

    result = loads(text, strict=True)

    assert result["App"]["name"] == "Demo"


def test_lenient_mode_accepts_empty_member_value_as_null() -> None:
    text = """
^ App
name =
""".lstrip()

    result = loads(text)

    assert result["App"]["name"] is None


def test_lenient_mode_accepts_trailing_comma_in_list() -> None:
    text = """
@yini

^ App
items = [10, 20, ]

/END
""".lstrip()

    result = loads(text, strict=False)

    items = result["App"]["items"]

    assert len(items) == 2
    assert items == [10, 20]


def test_lenient_mode_accepts_trailing_comma_in_inline_object() -> None:
    text = """
@yini

^ App
obj = { a: 10, }

/END
""".lstrip()

    result = loads(text, strict=False)

    obj = result["App"]["obj"]

    assert len(obj) == 1
    assert obj == {"a": 10}
