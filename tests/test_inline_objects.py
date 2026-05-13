import pytest

from yini_parser import loads, YiniParseError


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
