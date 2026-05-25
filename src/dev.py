# src/dev.py
"""
For development, playground, and local manual testing/debugging.
"""

from pprint import pprint

from yini_parser.api import load, loads


def main() -> None:
    print("*** dev run ***\n")

    print("--- data: --------------------------------------------")
    data = load("sample/basic.yini")
    pprint(data)
    print("------------------------------------------------------\n")

    print("--- text2: --------------------------------------------")
    text2 = """
^ App
name = "This is a test-name."
debug = true
isDebug = YES
object = { x: 3, y: 3, content: {env: "dev", log: ['aa', 'bb', 'cc']}}
"""
    config2 = loads(text2)
    pprint(config2)
    print()

    print(f"isDebug = {config2['App']['isDebug']}")
    print(f"xxx = {config2['App']['object']['x']}")
    print(f"xxx = {config2['App']['object']['content']}")
    print(f"xxx = {config2['App']['object']['content']['log'][1]}")

    print("------------------------------------------------------\n")

    print("--- text3: --------------------------------------------")
    text3 = """
^ Title
name = "This is a test-name."
debug = true
isDebug = YES
^ Title
name2 = 'name2data'
"""
    config3 = loads(text3)
    pprint(config3)
    print()

    print("------------------------------------------------------\n")


if __name__ == "__main__":
    main()
