import sys
from antlr4 import *
from grammar.generated.YiniLexer import YiniLexer
from grammar.generated.YiniParser import YiniParser
from core.VisitorInterp import VisitorInterp

print("start")

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = YiniLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = YiniParser(stream)
    tree = parser.start_()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        vinterp = VisitorInterp()
        vinterp.visit(tree)

if __name__ == '__main__':
    main(sys.argv)
