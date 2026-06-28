from __future__ import annotations

import pytest

from yini_parser.api.errors import YiniParseError
from yini_parser.api.load import loads


def test_backticked_member_keys_decode_to_inner_text() -> None:
    text = """
^ Keys
`Description of Project` = "val"
`Amanda's Project` = "owned"
`Owner Team` = "Core"
""".lstrip()

    result = loads(text)

    assert result == {
        "Keys": {
            "Description of Project": "val",
            "Amanda's Project": "owned",
            "Owner Team": "Core",
        },
    }


def test_empty_backticked_member_key_is_allowed() -> None:
    text = """
^ Keys
`` = "val"
name = "empty backticked key"
""".lstrip()

    result = loads(text)

    assert result == {
        "Keys": {
            "": "val",
            "name": "empty backticked key",
        },
    }


def test_backticked_inline_object_keys_decode_to_inner_text() -> None:
    text = """
^ App
labels = { `Display Name`: "Demo", `Owner Team`: "Core" }
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "labels": {
                "Display Name": "Demo",
                "Owner Team": "Core",
            },
        },
    }


def test_rejects_plain_key_starting_with_digit() -> None:
    text = """
^ Keys
1key = "val"
""".lstrip()

    with pytest.raises(YiniParseError, match="Invalid key"):
        loads(text)


def test_rejects_plain_key_with_dot() -> None:
    text = """
^ Keys
my.key = "val"
""".lstrip()

    with pytest.raises(YiniParseError, match="Invalid key"):
        loads(text)
