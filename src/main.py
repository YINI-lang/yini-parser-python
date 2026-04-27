"""
  Usage:
    from yini_parser import load

    data = load("sample/basic.yini")
    print(data["App"]["name"])
"""


# src/main.py
import sys
from pprint import pprint

from api.load import load


def main(argv):
    if len(argv) < 2:
        print("Usage: python src/main.py sample/basic.yini")
        sys.exit(1)

    data = load(argv[1])
    pprint(data)


if __name__ == "__main__":
    main(sys.argv)
