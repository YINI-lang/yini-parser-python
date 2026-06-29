from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_adapter_writes_utf8_json_for_unicode_strings(tmp_path: Path) -> None:
    input_path = tmp_path / "unicode.yini"
    input_path.write_text(
        """
@yini

^ Strings
quote = "She said “hello” and left."
""".lstrip(),
        encoding="utf-8",
    )

    completed = subprocess.run(
        [
            sys.executable,
            "tools/yini_parser_adapter.py",
            "--input",
            str(input_path),
            "--mode",
            "lenient",
        ],
        check=True,
        capture_output=True,
    )

    stdout = completed.stdout.decode("utf-8")

    assert json.loads(stdout) == {
        "Strings": {
            "quote": "She said “hello” and left.",
        },
    }
