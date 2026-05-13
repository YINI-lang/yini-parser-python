from __future__ import annotations

from yini_parser.api.load import loads


def test_parses_disable_line_as_ignored_lines() -> None:
    text = """
; This line is ignored.
-- This line is also ignored.

^ App
name = "Demo App"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }
