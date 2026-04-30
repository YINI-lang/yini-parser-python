# yini-parser-python

from yini_parser import load

data = load("sample/basic.yini")
print(data["App"]["name"])

## Tests

In the dir `tests` contains some small but focused implementation-local test suite, with:

- Tests for the public API.
- Some few key semantic tests.
- Some smoke/golden tests.
