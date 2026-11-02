import pytest

from yini_parser import YiniParseError, loads


def _document(value: str, *, strict: bool) -> str:
    marker = "@yini\n" if strict else ""
    terminator = "/END\n" if strict else ""
    return f"{marker}^ App\nscript = {value}\n{terminator}"


@pytest.mark.parametrize("strict", [False, True])
def test_command_string_removes_structural_indentation(strict: bool) -> None:
    value = (
        'command"""\n'
        "    npm install\n"
        "      --verbose\n"
        '    echo \\\\n and """ quotes\n'
        '"""'
    )

    result = loads(_document(value, strict=strict), strict=strict)

    assert result["App"]["script"] == (
        'npm install\n  --verbose\necho \\\\n and """ quotes'
    )


@pytest.mark.parametrize("strict", [False, True])
def test_command_string_preserves_blank_and_space_only_lines(strict: bool) -> None:
    value = 'command"""\n    first\n\n      \n    last\n"""'

    result = loads(_document(value, strict=strict), strict=strict)

    assert result["App"]["script"] == "first\n\n  \nlast"


@pytest.mark.parametrize("strict", [False, True])
def test_command_string_can_be_empty_and_end_at_eof(strict: bool) -> None:
    value = 'command"""\n"""'
    source = _document(value, strict=strict).rstrip("\n")

    result = loads(source, strict=strict)

    assert result["App"]["script"] == ""


@pytest.mark.parametrize("strict", [False, True])
def test_command_string_in_list_and_concatenation(strict: bool) -> None:
    marker = "@yini\n" if strict else ""
    terminator = "/END\n" if strict else ""
    source = (
        f'{marker}^ App\nitems = ["two", command"""\n  one\n"""\n]\n'
        'combined = "start:" + command"""\n  end\n"""\n'
        f"{terminator}"
    )

    result = loads(source, strict=strict)

    assert result["App"]["items"] == ["two", "one"]
    assert result["App"]["combined"] == "start:end"


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize("ending", ["\n", "\r\n", "\r"])
def test_command_string_preserves_line_endings(strict: bool, ending: str) -> None:
    value = ending.join(['command"""', "  one", "  two", '"""'])
    marker = f"@yini{ending}" if strict else ""
    terminator = f"/END{ending}" if strict else ""
    source = f"{marker}^ App{ending}script = {value}{ending}{terminator}"

    result = loads(source, strict=strict)

    assert result["App"]["script"] == f"one{ending}two"


@pytest.mark.parametrize("strict", [False, True])
@pytest.mark.parametrize(
    "value",
    [
        'command"""inline\n"""',
        'command"""\n    first\n  second\n"""',
        'command"""\n     \n    first\n"""',
        'command"""\n    first\n\t"""',
        'command"""\n    first\n"""tail',
        'command"""\n    first\n"""  ',
        'command"""\n    first\n""" #comment',
        'Command"""\n    first\n"""',
        'command"first"',
    ],
)
def test_rejects_invalid_command_string(value: str, strict: bool) -> None:
    with pytest.raises(YiniParseError):
        loads(_document(value, strict=strict), strict=strict)
