from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import NoReturn


def _configure_stdio() -> None:
    """
    The yini-test-suite reads adapter output as UTF-8 JSON. On some Windows
    setups, Python may encode piped stdout/stderr with the active locale unless
    we make the encoding explicit.
    """

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")


def _ensure_local_src_on_path() -> None:
    """
    Allows this adapter to run directly from the repository root without
    requiring the package to be installed first.

    If the package is already installed, this is harmless.
    """
    repo_root = Path(__file__).resolve().parents[1]
    src_dir = repo_root / "src"

    if src_dir.exists():
        sys.path.insert(0, str(src_dir))


def _fail(message: str, exit_code: int = 1) -> NoReturn:
    print(message, file=sys.stderr)
    raise SystemExit(exit_code)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="yini-test adapter for yini-parser-python.",
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the .yini input file.",
    )

    parser.add_argument(
        "--mode",
        choices=("lenient", "strict"),
        default="lenient",
        help="Parser mode to use. Defaults to lenient.",
    )

    return parser.parse_args()


def main() -> int:
    _configure_stdio()
    _ensure_local_src_on_path()

    from yini_parser.api.errors import YiniParseError
    from yini_parser.api.load import load

    args = _parse_args()

    input_path = Path(args.input)

    if not input_path.exists():
        _fail(f"Input file does not exist: {input_path}")

    if not input_path.is_file():
        _fail(f"Input path is not a file: {input_path}")

    strict = args.mode == "strict"

    try:
        result = load(str(input_path), strict=strict)

    except YiniParseError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    except Exception as exc:
        print(f"Unexpected adapter error: {exc}", file=sys.stderr)
        return 1

    json.dump(
        result,
        sys.stdout,
        ensure_ascii=False,
        separators=(",", ":"),
    )
    sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
