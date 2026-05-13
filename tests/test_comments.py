from __future__ import annotations

from yini_parser.api.load import loads


def test_parses_hash_full_line_comments() -> None:
    text = """
# This is a full-line hash comment.
^ App
# This comment should be ignored.
name = "Demo App"
version = 1
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "version": 1,
        },
    }


def test_parses_slash_full_line_comments() -> None:
    text = """
// This is a full-line slash comment.
^ App
// This comment should be ignored.
name = "Demo App"
enabled = true
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "enabled": True,
        },
    }


def test_parses_hash_inline_comments_after_members() -> None:
    text = """
^ App
name = "Demo App" # Application name.
version = 1.2 # Application version.
enabled = true# No whitespace is required before a hash comment.
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "version": 1.2,
            "enabled": True,
        },
    }


def test_parses_slash_inline_comments_after_members() -> None:
    text = """
^ App
name = "Demo App" // Application name.
version = 1.2 // Application version.
enabled = true// No whitespace is required before a slash comment.
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "version": 1.2,
            "enabled": True,
        },
    }


def test_parses_comments_after_section_headers() -> None:
    text = """
^ App # Main application section.
name = "Demo App"

^^ Server // Nested server section.
host = "localhost"
port = 8080
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "Server": {
                "host": "localhost",
                "port": 8080,
            },
        },
    }


def test_parses_block_comments_between_statements() -> None:
    text = """
/*
 * This is a block comment before the first section.
 */

^ App
name = "Demo App"

/*
 * This block comment appears between members.
 */

enabled = true
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "enabled": True,
        },
    }


def test_parses_inline_block_comments_between_tokens() -> None:
    text = """
^ App
name = /* ignored */ "Demo App"
enabled = /* ignored */ true
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
            "enabled": True,
        },
    }


def test_parses_comments_inside_lists() -> None:
    text = """
^ App
features = [
    "search", // Search feature.
    "logs",   # Log feature.
    "metrics" # Metrics feature.
]
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "features": ["search", "logs", "metrics"],
        },
    }


def test_parses_comments_inside_inline_objects() -> None:
    text = """
^ App
cache = {
    enabled: true, # Cache is enabled.
    maxMb: 256,   // Cache size limit.
    timeoutSec: 30
}
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "cache": {
                "enabled": True,
                "maxMb": 256,
                "timeoutSec": 30,
            },
        },
    }


def test_comment_markers_inside_strings_are_preserved() -> None:
    text = """
^ App
hashText = "value # not a comment"
slashText = "value // not a comment"
blockText = "value /* not a comment */"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "hashText": "value # not a comment",
            "slashText": "value // not a comment",
            "blockText": "value /* not a comment */",
        },
    }


def test_hash_comment_after_empty_value_keeps_value_as_none() -> None:
    text = """
^ App
description = # Empty value before comment.
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "description": None,
        },
    }


def test_parses_full_line_semicolon_comment() -> None:
    text = """
; This line is ignored.

^ App
name = "Demo App"
""".lstrip()

    result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }
