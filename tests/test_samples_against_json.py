from __future__ import annotations

import json
from pathlib import Path

import pytest

from api.load import load

FIXTURES_DIR = Path("tests/fixtures/smoke-fixtures")


def _yini_files() -> list[Path]:
    return sorted(FIXTURES_DIR.glob("*.yini"))


def _fixture_pairs() -> list[tuple[Path, Path]]:
    return [(yini_path, yini_path.with_suffix(".json")) for yini_path in _yini_files()]


@pytest.mark.parametrize("yini_path", _yini_files(), ids=lambda p: p.name)
def test_sample_yini_parses_without_crashing(yini_path: Path) -> None:
    result = load(str(yini_path))
    assert isinstance(result, dict)


@pytest.mark.parametrize(
    ("yini_path", "json_path"),
    _fixture_pairs(),
    ids=lambda value: value.name if isinstance(value, Path) else str(value),
)
def test_sample_yini_matches_expected_json(yini_path: Path, json_path: Path) -> None:
    if not json_path.exists():
        pytest.skip(f"No expected JSON fixture yet for {yini_path.name}")

    actual = load(str(yini_path))

    with json_path.open("r", encoding="utf-8") as f:
        expected = json.load(f)

    assert actual == expected, (
        f"Parsed output did not match expected JSON for {yini_path.name}.\n"
        f"YINI file: {yini_path}\n"
        f"JSON file: {json_path}"
    )
