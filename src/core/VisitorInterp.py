import sys
from antlr4 import *
from grammar.generated import YiniParserVisitor
from grammar.generated.YiniLexer import YiniLexer
from grammar.generated.YiniParser import YiniParser

class VisitorInterp(YiniParserVisitor):
    def visitAtom(self, ctx:YiniParser.AtomContext):
        return int(ctx.getText())

    def visitExpr(self, ctx:YiniParser.ExprContext):
        if ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == "(":
                return self.visit(ctx.getChild(1))
            op = ctx.getChild(1).getText()
            v1 = self.visit(ctx.getChild(0))
            v2 = self.visit(ctx.getChild(2))
            if op == "+":
                return v1 + v2
            if op == "-":
                return v1 - v2
            if op == "*":
                return v1 * v2
            if op == "/":
                return v1 / v2
            return 0
        if ctx.getChildCount() == 2:
            opc = ctx.getChild(0).getText()
            if opc == "+":
                return self.visit(ctx.getChild(1))
            if opc == "-":
                return - self.visit(ctx.getChild(1))
            return 0
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return 0

    def visitStart_(self, ctx:YiniParser.Start_Context):
        for i in range(0, ctx.getChildCount(), 2):
            print(self.visit(ctx.getChild(i)))
        return 0
