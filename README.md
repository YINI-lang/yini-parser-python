# yini-parser-python

from yini_parser import load

data = load("sample/basic.yini")
print(data["App"]["name"])

