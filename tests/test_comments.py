from __future__ import annotations

import pytest

from yini_parser.api.errors import YiniParseError
from yini_parser.api.load import loads
from yini_parser.api.warnings import YiniParseWarning


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize("ending", ["\n", "\r\n", "\r"])
@pytest.mark.parametrize(
    "member",
    [
        "value = /*{ending}*/ [1]",
        "value = /*{ending}*/ {{a: 1}}",
        "value /*{ending}*/ = 1",
        'value = "a" /*{ending}*/ + "b"',
        "value = {{a: /*{ending}*/ 1}}",
    ],
)
def test_block_comments_preserve_same_logical_line_requirements(
    strict: bool, ending: str, member: str
) -> None:
    source = ending.join(["^ App", member.format(ending=ending), "/END", ""])

    with pytest.raises(YiniParseError, match="same logical line"):
        loads(source, strict=strict)


@pytest.mark.parametrize("strict", [False, True])
def test_block_comment_line_breaks_are_valid_inside_collections(strict: bool) -> None:
    source = '^ App\nvalue = [1, /*\n*/ 2]\ntext = "a" + /*\n*/ "b"\n/END\n'

    result = loads(source, strict=strict)

    assert result == {"App": {"value": [1, 2], "text": "ab"}}


@pytest.mark.parametrize(
    "source",
    [
        " #! misplaced\n^ App\n/END\n",
        "\n#! misplaced\n^ App\n/END\n",
        "// comment\n#! misplaced\n^ App\n/END\n",
        "^ App #! misplaced\n/END\n",
        "^ App\nvalue = 1 #! misplaced\n/END\n",
    ],
)
def test_misplaced_shebang_warns_in_lenient_mode_and_errors_in_strict_mode(
    source: str,
) -> None:
    with pytest.warns(YiniParseWarning, match="misplaced-shebang") as caught:
        result = loads(source)
    assert "App" in result
    assert len(caught) == 1

    with pytest.raises(YiniParseError, match="misplaced-shebang"):
        loads(source, strict=True)


@pytest.mark.parametrize("strict", [False, True])
def test_shebang_text_in_literals_and_other_comments_is_not_diagnosed(
    strict: bool,
) -> None:
    source = (
        "#!/usr/bin/env yini\n"
        "^ `#! section` /* #! block comment */\n"
        'text = "#! string" // #! line comment\n'
        'multi = """#! first\n#! second"""\n'
        "`#! key` = 1\n; #! semicolon comment\n-- #! disabled\n/END\n"
    )

    result = loads(source, strict=strict)

    assert result["#! section"]["text"] == "#! string"


def test_only_first_misplaced_shebang_is_reported() -> None:
    with pytest.warns(YiniParseWarning, match="misplaced-shebang") as caught:
        loads("\n#! first\n#! second\n^ App\n")

    assert len(caught) == 1
    assert caught[0].message.line == 2


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

    with pytest.warns(YiniParseWarning, match="empty value"):
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


def test_shebang_after_yini_directive_is_treated_as_comment() -> None:
    text = """
@yini
#!/usr/bin/env yini

^ App
name = "Demo App"
""".lstrip()

    with pytest.warns(YiniParseWarning, match="misplaced-shebang"):
        result = loads(text)

    assert result == {
        "App": {
            "name": "Demo App",
        },
    }


def test_rejects_unterminated_block_comment() -> None:
    text = """
@yini

^ App
name = "Demo App"
/* This block comment never closes.
""".lstrip()

    with pytest.raises(YiniParseError):
        loads(text)
