# Generated from ./grammar/v1.0.0-rc.5xx/YiniParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,42,308,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,3,0,60,8,0,1,0,5,0,63,8,0,10,0,12,0,66,9,
        0,1,0,3,0,69,8,0,1,0,1,0,1,1,1,1,5,1,75,8,1,10,1,12,1,78,9,1,1,1,
        4,1,81,8,1,11,1,12,1,82,3,1,85,8,1,1,2,1,2,5,2,89,8,2,10,2,12,2,
        92,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,100,8,3,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,3,5,109,8,5,1,6,1,6,3,6,113,8,6,1,6,1,6,1,6,3,6,118,8,6,1,
        6,3,6,121,8,6,1,7,1,7,1,8,1,8,1,8,1,9,4,9,129,8,9,11,9,12,9,130,
        1,10,1,10,1,10,1,11,1,11,1,11,3,11,139,8,11,1,12,1,12,1,12,1,12,
        3,12,145,8,12,1,13,1,13,1,13,1,13,3,13,151,8,13,1,14,1,14,4,14,155,
        8,14,11,14,12,14,156,1,15,1,15,5,15,161,8,15,10,15,12,15,164,9,15,
        1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,5,18,174,8,18,10,18,12,18,
        177,9,18,1,18,3,18,180,8,18,1,18,5,18,183,8,18,10,18,12,18,186,9,
        18,1,18,1,18,5,18,190,8,18,10,18,12,18,193,9,18,1,18,1,18,5,18,197,
        8,18,10,18,12,18,200,9,18,3,18,202,8,18,1,19,1,19,1,19,5,19,207,
        8,19,10,19,12,19,210,9,19,1,19,5,19,213,8,19,10,19,12,19,216,9,19,
        1,19,3,19,219,8,19,1,20,1,20,1,20,5,20,224,8,20,10,20,12,20,227,
        9,20,1,20,1,20,1,21,1,21,1,22,1,22,5,22,235,8,22,10,22,12,22,238,
        9,22,1,22,3,22,241,8,22,1,22,5,22,244,8,22,10,22,12,22,247,9,22,
        1,22,1,22,5,22,251,8,22,10,22,12,22,254,9,22,1,22,1,22,5,22,258,
        8,22,10,22,12,22,261,9,22,3,22,263,8,22,1,23,1,23,5,23,267,8,23,
        10,23,12,23,270,9,23,1,23,1,23,5,23,274,8,23,10,23,12,23,277,9,23,
        1,23,5,23,280,8,23,10,23,12,23,283,9,23,1,23,3,23,286,8,23,1,24,
        1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,3,28,298,8,28,1,28,
        1,28,1,28,3,28,303,8,28,1,28,3,28,306,8,28,1,28,0,0,29,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,0,3,3,0,8,10,13,13,17,17,2,0,22,22,24,24,1,0,8,9,329,0,59,
        1,0,0,0,2,84,1,0,0,0,4,86,1,0,0,0,6,99,1,0,0,0,8,101,1,0,0,0,10,
        108,1,0,0,0,12,120,1,0,0,0,14,122,1,0,0,0,16,124,1,0,0,0,18,128,
        1,0,0,0,20,132,1,0,0,0,22,135,1,0,0,0,24,144,1,0,0,0,26,150,1,0,
        0,0,28,152,1,0,0,0,30,158,1,0,0,0,32,167,1,0,0,0,34,169,1,0,0,0,
        36,201,1,0,0,0,38,203,1,0,0,0,40,220,1,0,0,0,42,230,1,0,0,0,44,262,
        1,0,0,0,46,264,1,0,0,0,48,287,1,0,0,0,50,289,1,0,0,0,52,291,1,0,
        0,0,54,293,1,0,0,0,56,297,1,0,0,0,58,60,3,2,1,0,59,58,1,0,0,0,59,
        60,1,0,0,0,60,64,1,0,0,0,61,63,3,6,3,0,62,61,1,0,0,0,63,66,1,0,0,
        0,64,62,1,0,0,0,64,65,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,67,69,
        3,4,2,0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,0,0,1,
        71,1,1,0,0,0,72,76,5,1,0,0,73,75,3,18,9,0,74,73,1,0,0,0,75,78,1,
        0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,85,1,0,0,0,78,76,1,0,0,0,79,
        81,3,18,9,0,80,79,1,0,0,0,81,82,1,0,0,0,82,80,1,0,0,0,82,83,1,0,
        0,0,83,85,1,0,0,0,84,72,1,0,0,0,84,80,1,0,0,0,85,3,1,0,0,0,86,90,
        5,5,0,0,87,89,3,18,9,0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,
        90,91,1,0,0,0,91,5,1,0,0,0,92,90,1,0,0,0,93,100,3,18,9,0,94,100,
        5,6,0,0,95,100,3,8,4,0,96,100,3,20,10,0,97,100,3,10,5,0,98,100,3,
        56,28,0,99,93,1,0,0,0,99,94,1,0,0,0,99,95,1,0,0,0,99,96,1,0,0,0,
        99,97,1,0,0,0,99,98,1,0,0,0,100,7,1,0,0,0,101,102,5,7,0,0,102,9,
        1,0,0,0,103,109,3,12,6,0,104,109,3,16,8,0,105,106,3,54,27,0,106,
        107,3,18,9,0,107,109,1,0,0,0,108,103,1,0,0,0,108,104,1,0,0,0,108,
        105,1,0,0,0,109,11,1,0,0,0,110,112,5,2,0,0,111,113,3,14,7,0,112,
        111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,121,3,18,9,0,115,
        117,5,3,0,0,116,118,3,34,17,0,117,116,1,0,0,0,117,118,1,0,0,0,118,
        119,1,0,0,0,119,121,3,18,9,0,120,110,1,0,0,0,120,115,1,0,0,0,121,
        13,1,0,0,0,122,123,5,39,0,0,123,15,1,0,0,0,124,125,5,4,0,0,125,126,
        3,18,9,0,126,17,1,0,0,0,127,129,5,34,0,0,128,127,1,0,0,0,129,130,
        1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,19,1,0,0,0,132,133,3,
        22,11,0,133,134,3,18,9,0,134,21,1,0,0,0,135,136,5,39,0,0,136,138,
        5,22,0,0,137,139,3,24,12,0,138,137,1,0,0,0,138,139,1,0,0,0,139,23,
        1,0,0,0,140,145,3,28,14,0,141,145,3,26,13,0,142,145,3,44,22,0,143,
        145,3,36,18,0,144,140,1,0,0,0,144,141,1,0,0,0,144,142,1,0,0,0,144,
        143,1,0,0,0,145,25,1,0,0,0,146,151,3,50,25,0,147,151,3,34,17,0,148,
        151,3,48,24,0,149,151,3,52,26,0,150,146,1,0,0,0,150,147,1,0,0,0,
        150,148,1,0,0,0,150,149,1,0,0,0,151,27,1,0,0,0,152,154,5,13,0,0,
        153,155,3,30,15,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,1,0,0,
        0,156,157,1,0,0,0,157,29,1,0,0,0,158,162,5,29,0,0,159,161,5,34,0,
        0,160,159,1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,
        0,163,165,1,0,0,0,164,162,1,0,0,0,165,166,3,32,16,0,166,31,1,0,0,
        0,167,168,7,0,0,0,168,33,1,0,0,0,169,170,5,13,0,0,170,35,1,0,0,0,
        171,175,5,27,0,0,172,174,5,34,0,0,173,172,1,0,0,0,174,177,1,0,0,
        0,175,173,1,0,0,0,175,176,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,
        0,178,180,3,38,19,0,179,178,1,0,0,0,179,180,1,0,0,0,180,184,1,0,
        0,0,181,183,5,34,0,0,182,181,1,0,0,0,183,186,1,0,0,0,184,182,1,0,
        0,0,184,185,1,0,0,0,185,187,1,0,0,0,186,184,1,0,0,0,187,191,5,28,
        0,0,188,190,5,34,0,0,189,188,1,0,0,0,190,193,1,0,0,0,191,189,1,0,
        0,0,191,192,1,0,0,0,192,202,1,0,0,0,193,191,1,0,0,0,194,198,5,11,
        0,0,195,197,5,34,0,0,196,195,1,0,0,0,197,200,1,0,0,0,198,196,1,0,
        0,0,198,199,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,201,171,1,0,
        0,0,201,194,1,0,0,0,202,37,1,0,0,0,203,214,3,40,20,0,204,208,5,23,
        0,0,205,207,5,34,0,0,206,205,1,0,0,0,207,210,1,0,0,0,208,206,1,0,
        0,0,208,209,1,0,0,0,209,211,1,0,0,0,210,208,1,0,0,0,211,213,3,40,
        20,0,212,204,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,
        0,0,215,218,1,0,0,0,216,214,1,0,0,0,217,219,5,23,0,0,218,217,1,0,
        0,0,218,219,1,0,0,0,219,39,1,0,0,0,220,221,5,39,0,0,221,225,3,42,
        21,0,222,224,5,34,0,0,223,222,1,0,0,0,224,227,1,0,0,0,225,223,1,
        0,0,0,225,226,1,0,0,0,226,228,1,0,0,0,227,225,1,0,0,0,228,229,3,
        24,12,0,229,41,1,0,0,0,230,231,7,1,0,0,231,43,1,0,0,0,232,236,5,
        25,0,0,233,235,5,34,0,0,234,233,1,0,0,0,235,238,1,0,0,0,236,234,
        1,0,0,0,236,237,1,0,0,0,237,240,1,0,0,0,238,236,1,0,0,0,239,241,
        3,46,23,0,240,239,1,0,0,0,240,241,1,0,0,0,241,245,1,0,0,0,242,244,
        5,34,0,0,243,242,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,
        1,0,0,0,246,248,1,0,0,0,247,245,1,0,0,0,248,252,5,26,0,0,249,251,
        5,34,0,0,250,249,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,0,252,253,
        1,0,0,0,253,263,1,0,0,0,254,252,1,0,0,0,255,259,5,12,0,0,256,258,
        5,34,0,0,257,256,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,
        1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,262,232,1,0,0,0,262,255,
        1,0,0,0,263,45,1,0,0,0,264,281,3,24,12,0,265,267,5,34,0,0,266,265,
        1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,271,
        1,0,0,0,270,268,1,0,0,0,271,275,5,23,0,0,272,274,5,34,0,0,273,272,
        1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,278,
        1,0,0,0,277,275,1,0,0,0,278,280,3,24,12,0,279,268,1,0,0,0,280,283,
        1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,285,1,0,0,0,283,281,
        1,0,0,0,284,286,5,23,0,0,285,284,1,0,0,0,285,286,1,0,0,0,286,47,
        1,0,0,0,287,288,5,17,0,0,288,49,1,0,0,0,289,290,5,10,0,0,290,51,
        1,0,0,0,291,292,7,2,0,0,292,53,1,0,0,0,293,294,5,42,0,0,294,55,1,
        0,0,0,295,298,5,41,0,0,296,298,3,24,12,0,297,295,1,0,0,0,297,296,
        1,0,0,0,297,298,1,0,0,0,298,299,1,0,0,0,299,302,5,22,0,0,300,303,
        3,24,12,0,301,303,5,41,0,0,302,300,1,0,0,0,302,301,1,0,0,0,303,305,
        1,0,0,0,304,306,3,18,9,0,305,304,1,0,0,0,305,306,1,0,0,0,306,57,
        1,0,0,0,41,59,64,68,76,82,84,90,99,108,112,117,120,130,138,144,150,
        156,162,175,179,184,191,198,201,208,214,218,225,236,240,245,252,
        259,262,268,275,281,285,297,302,305
    ]

class YiniParser ( Parser ):

    grammarFileName = "YiniParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{}'", "'[]'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\u00A7'", "'^'", "'>'", "'<'", "'='", 
                     "','", "':'", "'['", "']'", "'{'", "'}'", "'+'", "'$'", 
                     "'%'", "'@'", "';'" ]

    symbolicNames = [ "<INVALID>", "SHEBANG", "YINI_TOKEN", "INCLUDE_TOKEN", 
                      "DEPRECATED_TOKEN", "TERMINAL_TOKEN", "SECTION_HEAD", 
                      "INVALID_SECTION_HEAD", "BOOLEAN_FALSE", "BOOLEAN_TRUE", 
                      "NULL", "EMPTY_OBJECT", "EMPTY_LIST", "STRING", "TRIPLE_QUOTED_STRING", 
                      "SINGLE_OR_DOUBLE", "R_AND_C_STRING", "NUMBER", "SS", 
                      "CARET", "GT", "LT", "EQ", "COMMA", "COLON", "OB", 
                      "CB", "OC", "CC", "PLUS", "DOLLAR", "PC", "AT", "SEMICOLON", 
                      "NL", "WS", "BLOCK_COMMENT", "FULL_LINE_COMMENT", 
                      "INLINE_COMMENT", "KEY", "IDENT_INVALID", "REST", 
                      "META_INVALID" ]

    RULE_yini = 0
    RULE_prolog = 1
    RULE_terminal_stmt = 2
    RULE_stmt = 3
    RULE_invalid_section_stmt = 4
    RULE_meta_stmt = 5
    RULE_directive = 6
    RULE_yini_mode = 7
    RULE_annotation = 8
    RULE_eol = 9
    RULE_assignment = 10
    RULE_member = 11
    RULE_value = 12
    RULE_scalar_value = 13
    RULE_concat_expression = 14
    RULE_concat_tail = 15
    RULE_concat_operand = 16
    RULE_string_literal = 17
    RULE_object_literal = 18
    RULE_object_members = 19
    RULE_object_member = 20
    RULE_object_member_separator = 21
    RULE_list_literal = 22
    RULE_elements = 23
    RULE_number_literal = 24
    RULE_null_literal = 25
    RULE_boolean_literal = 26
    RULE_bad_meta_text = 27
    RULE_bad_member = 28

    ruleNames =  [ "yini", "prolog", "terminal_stmt", "stmt", "invalid_section_stmt", 
                   "meta_stmt", "directive", "yini_mode", "annotation", 
                   "eol", "assignment", "member", "value", "scalar_value", 
                   "concat_expression", "concat_tail", "concat_operand", 
                   "string_literal", "object_literal", "object_members", 
                   "object_member", "object_member_separator", "list_literal", 
                   "elements", "number_literal", "null_literal", "boolean_literal", 
                   "bad_meta_text", "bad_member" ]

    EOF = Token.EOF
    SHEBANG=1
    YINI_TOKEN=2
    INCLUDE_TOKEN=3
    DEPRECATED_TOKEN=4
    TERMINAL_TOKEN=5
    SECTION_HEAD=6
    INVALID_SECTION_HEAD=7
    BOOLEAN_FALSE=8
    BOOLEAN_TRUE=9
    NULL=10
    EMPTY_OBJECT=11
    EMPTY_LIST=12
    STRING=13
    TRIPLE_QUOTED_STRING=14
    SINGLE_OR_DOUBLE=15
    R_AND_C_STRING=16
    NUMBER=17
    SS=18
    CARET=19
    GT=20
    LT=21
    EQ=22
    COMMA=23
    COLON=24
    OB=25
    CB=26
    OC=27
    CC=28
    PLUS=29
    DOLLAR=30
    PC=31
    AT=32
    SEMICOLON=33
    NL=34
    WS=35
    BLOCK_COMMENT=36
    FULL_LINE_COMMENT=37
    INLINE_COMMENT=38
    KEY=39
    IDENT_INVALID=40
    REST=41
    META_INVALID=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class YiniContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(YiniParser.EOF, 0)

        def prolog(self):
            return self.getTypedRuleContext(YiniParser.PrologContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.StmtContext)
            else:
                return self.getTypedRuleContext(YiniParser.StmtContext,i)


        def terminal_stmt(self):
            return self.getTypedRuleContext(YiniParser.Terminal_stmtContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_yini

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYini" ):
                return visitor.visitYini(self)
            else:
                return visitor.visitChildren(self)




    def yini(self):

        localctx = YiniParser.YiniContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_yini)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 58
                self.prolog()


            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7164177563612) != 0):
                self.state = 61
                self.stmt()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 67
                self.terminal_stmt()


            self.state = 70
            self.match(YiniParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrologContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHEBANG(self):
            return self.getToken(YiniParser.SHEBANG, 0)

        def eol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.EolContext)
            else:
                return self.getTypedRuleContext(YiniParser.EolContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_prolog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProlog" ):
                return visitor.visitProlog(self)
            else:
                return visitor.visitChildren(self)




    def prolog(self):

        localctx = YiniParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prolog)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(YiniParser.SHEBANG)
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 73
                        self.eol() 
                    self.state = 78
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 79
                        self.eol()

                    else:
                        raise NoViableAltException(self)
                    self.state = 82 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Terminal_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERMINAL_TOKEN(self):
            return self.getToken(YiniParser.TERMINAL_TOKEN, 0)

        def eol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.EolContext)
            else:
                return self.getTypedRuleContext(YiniParser.EolContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_terminal_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_stmt" ):
                return visitor.visitTerminal_stmt(self)
            else:
                return visitor.visitChildren(self)




    def terminal_stmt(self):

        localctx = YiniParser.Terminal_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_terminal_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(YiniParser.TERMINAL_TOKEN)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 87
                self.eol()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def SECTION_HEAD(self):
            return self.getToken(YiniParser.SECTION_HEAD, 0)

        def invalid_section_stmt(self):
            return self.getTypedRuleContext(YiniParser.Invalid_section_stmtContext,0)


        def assignment(self):
            return self.getTypedRuleContext(YiniParser.AssignmentContext,0)


        def meta_stmt(self):
            return self.getTypedRuleContext(YiniParser.Meta_stmtContext,0)


        def bad_member(self):
            return self.getTypedRuleContext(YiniParser.Bad_memberContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = YiniParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.eol()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(YiniParser.SECTION_HEAD)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.invalid_section_stmt()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 96
                self.assignment()
                pass
            elif token in [2, 3, 4, 42]:
                self.enterOuterAlt(localctx, 5)
                self.state = 97
                self.meta_stmt()
                pass
            elif token in [8, 9, 10, 11, 12, 13, 17, 22, 25, 27, 41]:
                self.enterOuterAlt(localctx, 6)
                self.state = 98
                self.bad_member()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Invalid_section_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INVALID_SECTION_HEAD(self):
            return self.getToken(YiniParser.INVALID_SECTION_HEAD, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_invalid_section_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInvalid_section_stmt" ):
                return visitor.visitInvalid_section_stmt(self)
            else:
                return visitor.visitChildren(self)




    def invalid_section_stmt(self):

        localctx = YiniParser.Invalid_section_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_invalid_section_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(YiniParser.INVALID_SECTION_HEAD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meta_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def directive(self):
            return self.getTypedRuleContext(YiniParser.DirectiveContext,0)


        def annotation(self):
            return self.getTypedRuleContext(YiniParser.AnnotationContext,0)


        def bad_meta_text(self):
            return self.getTypedRuleContext(YiniParser.Bad_meta_textContext,0)


        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_meta_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_stmt" ):
                return visitor.visitMeta_stmt(self)
            else:
                return visitor.visitChildren(self)




    def meta_stmt(self):

        localctx = YiniParser.Meta_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_meta_stmt)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.directive()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.annotation()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.bad_meta_text()
                self.state = 106
                self.eol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def YINI_TOKEN(self):
            return self.getToken(YiniParser.YINI_TOKEN, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def yini_mode(self):
            return self.getTypedRuleContext(YiniParser.Yini_modeContext,0)


        def INCLUDE_TOKEN(self):
            return self.getToken(YiniParser.INCLUDE_TOKEN, 0)

        def string_literal(self):
            return self.getTypedRuleContext(YiniParser.String_literalContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = YiniParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(YiniParser.YINI_TOKEN)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 111
                    self.yini_mode()


                self.state = 114
                self.eol()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(YiniParser.INCLUDE_TOKEN)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 116
                    self.string_literal()


                self.state = 119
                self.eol()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Yini_modeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_yini_mode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYini_mode" ):
                return visitor.visitYini_mode(self)
            else:
                return visitor.visitChildren(self)




    def yini_mode(self):

        localctx = YiniParser.Yini_modeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_yini_mode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(YiniParser.KEY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEPRECATED_TOKEN(self):
            return self.getToken(YiniParser.DEPRECATED_TOKEN, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_annotation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotation" ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = YiniParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(YiniParser.DEPRECATED_TOKEN)
            self.state = 125
            self.eol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_eol

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEol" ):
                return visitor.visitEol(self)
            else:
                return visitor.visitChildren(self)




    def eol(self):

        localctx = YiniParser.EolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_eol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 127
                    self.match(YiniParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 130 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(YiniParser.MemberContext,0)


        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = YiniParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.member()
            self.state = 133
            self.eol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def EQ(self):
            return self.getToken(YiniParser.EQ, 0)

        def value(self):
            return self.getTypedRuleContext(YiniParser.ValueContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = YiniParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(YiniParser.KEY)
            self.state = 136
            self.match(YiniParser.EQ)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 167919360) != 0):
                self.state = 137
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concat_expression(self):
            return self.getTypedRuleContext(YiniParser.Concat_expressionContext,0)


        def scalar_value(self):
            return self.getTypedRuleContext(YiniParser.Scalar_valueContext,0)


        def list_literal(self):
            return self.getTypedRuleContext(YiniParser.List_literalContext,0)


        def object_literal(self):
            return self.getTypedRuleContext(YiniParser.Object_literalContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = YiniParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.concat_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.scalar_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.list_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.object_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def null_literal(self):
            return self.getTypedRuleContext(YiniParser.Null_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(YiniParser.String_literalContext,0)


        def number_literal(self):
            return self.getTypedRuleContext(YiniParser.Number_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(YiniParser.Boolean_literalContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_scalar_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_value" ):
                return visitor.visitScalar_value(self)
            else:
                return visitor.visitChildren(self)




    def scalar_value(self):

        localctx = YiniParser.Scalar_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_scalar_value)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.null_literal()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.string_literal()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.number_literal()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.boolean_literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(YiniParser.STRING, 0)

        def concat_tail(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Concat_tailContext)
            else:
                return self.getTypedRuleContext(YiniParser.Concat_tailContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_concat_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_expression" ):
                return visitor.visitConcat_expression(self)
            else:
                return visitor.visitChildren(self)




    def concat_expression(self):

        localctx = YiniParser.Concat_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_concat_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(YiniParser.STRING)
            self.state = 154 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 153
                self.concat_tail()
                self.state = 156 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==29):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(YiniParser.PLUS, 0)

        def concat_operand(self):
            return self.getTypedRuleContext(YiniParser.Concat_operandContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_concat_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_tail" ):
                return visitor.visitConcat_tail(self)
            else:
                return visitor.visitChildren(self)




    def concat_tail(self):

        localctx = YiniParser.Concat_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_concat_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(YiniParser.PLUS)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 159
                self.match(YiniParser.NL)
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 165
            self.concat_operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Concat_operandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(YiniParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(YiniParser.NUMBER, 0)

        def BOOLEAN_TRUE(self):
            return self.getToken(YiniParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(YiniParser.BOOLEAN_FALSE, 0)

        def NULL(self):
            return self.getToken(YiniParser.NULL, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_concat_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_operand" ):
                return visitor.visitConcat_operand(self)
            else:
                return visitor.visitChildren(self)




    def concat_operand(self):

        localctx = YiniParser.Concat_operandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_concat_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 141056) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(YiniParser.STRING, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_string_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)




    def string_literal(self):

        localctx = YiniParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(YiniParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OC(self):
            return self.getToken(YiniParser.OC, 0)

        def CC(self):
            return self.getToken(YiniParser.CC, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def object_members(self):
            return self.getTypedRuleContext(YiniParser.Object_membersContext,0)


        def EMPTY_OBJECT(self):
            return self.getToken(YiniParser.EMPTY_OBJECT, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_object_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_literal" ):
                return visitor.visitObject_literal(self)
            else:
                return visitor.visitChildren(self)




    def object_literal(self):

        localctx = YiniParser.Object_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_object_literal)
        self._la = 0 # Token type
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(YiniParser.OC)
                self.state = 175
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 172
                        self.match(YiniParser.NL) 
                    self.state = 177
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 178
                    self.object_members()


                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 181
                    self.match(YiniParser.NL)
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 187
                self.match(YiniParser.CC)
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 188
                        self.match(YiniParser.NL) 
                    self.state = 193
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.match(YiniParser.EMPTY_OBJECT)
                self.state = 198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 195
                        self.match(YiniParser.NL) 
                    self.state = 200
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_membersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_member(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Object_memberContext)
            else:
                return self.getTypedRuleContext(YiniParser.Object_memberContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.COMMA)
            else:
                return self.getToken(YiniParser.COMMA, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_object_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_members" ):
                return visitor.visitObject_members(self)
            else:
                return visitor.visitChildren(self)




    def object_members(self):

        localctx = YiniParser.Object_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_object_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.object_member()
            self.state = 214
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 204
                    self.match(YiniParser.COMMA)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 205
                        self.match(YiniParser.NL)
                        self.state = 210
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 211
                    self.object_member() 
                self.state = 216
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 217
                self.match(YiniParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def object_member_separator(self):
            return self.getTypedRuleContext(YiniParser.Object_member_separatorContext,0)


        def value(self):
            return self.getTypedRuleContext(YiniParser.ValueContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_object_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_member" ):
                return visitor.visitObject_member(self)
            else:
                return visitor.visitChildren(self)




    def object_member(self):

        localctx = YiniParser.Object_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_object_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(YiniParser.KEY)
            self.state = 221
            self.object_member_separator()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 222
                self.match(YiniParser.NL)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_member_separatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(YiniParser.COLON, 0)

        def EQ(self):
            return self.getToken(YiniParser.EQ, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_object_member_separator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_member_separator" ):
                return visitor.visitObject_member_separator(self)
            else:
                return visitor.visitChildren(self)




    def object_member_separator(self):

        localctx = YiniParser.Object_member_separatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_object_member_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if not(_la==22 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(YiniParser.OB, 0)

        def CB(self):
            return self.getToken(YiniParser.CB, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def elements(self):
            return self.getTypedRuleContext(YiniParser.ElementsContext,0)


        def EMPTY_LIST(self):
            return self.getToken(YiniParser.EMPTY_LIST, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_list_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_literal" ):
                return visitor.visitList_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_literal(self):

        localctx = YiniParser.List_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(YiniParser.OB)
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 233
                        self.match(YiniParser.NL) 
                    self.state = 238
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 167919360) != 0):
                    self.state = 239
                    self.elements()


                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 242
                    self.match(YiniParser.NL)
                    self.state = 247
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 248
                self.match(YiniParser.CB)
                self.state = 252
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 249
                        self.match(YiniParser.NL) 
                    self.state = 254
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(YiniParser.EMPTY_LIST)
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 256
                        self.match(YiniParser.NL) 
                    self.state = 261
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.ValueContext)
            else:
                return self.getTypedRuleContext(YiniParser.ValueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.COMMA)
            else:
                return self.getToken(YiniParser.COMMA, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = YiniParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.value()
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 268
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 265
                        self.match(YiniParser.NL)
                        self.state = 270
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 271
                    self.match(YiniParser.COMMA)
                    self.state = 275
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==34:
                        self.state = 272
                        self.match(YiniParser.NL)
                        self.state = 277
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 278
                    self.value() 
                self.state = 283
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 285
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 284
                self.match(YiniParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YiniParser.NUMBER, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_number_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_literal" ):
                return visitor.visitNumber_literal(self)
            else:
                return visitor.visitChildren(self)




    def number_literal(self):

        localctx = YiniParser.Number_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_number_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(YiniParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Null_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(YiniParser.NULL, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_null_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNull_literal" ):
                return visitor.visitNull_literal(self)
            else:
                return visitor.visitChildren(self)




    def null_literal(self):

        localctx = YiniParser.Null_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(YiniParser.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN_TRUE(self):
            return self.getToken(YiniParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(YiniParser.BOOLEAN_FALSE, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = YiniParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bad_meta_textContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def META_INVALID(self):
            return self.getToken(YiniParser.META_INVALID, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_bad_meta_text

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBad_meta_text" ):
                return visitor.visitBad_meta_text(self)
            else:
                return visitor.visitChildren(self)




    def bad_meta_text(self):

        localctx = YiniParser.Bad_meta_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_bad_meta_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(YiniParser.META_INVALID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bad_memberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(YiniParser.EQ, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.ValueContext)
            else:
                return self.getTypedRuleContext(YiniParser.ValueContext,i)


        def REST(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.REST)
            else:
                return self.getToken(YiniParser.REST, i)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_bad_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBad_member" ):
                return visitor.visitBad_member(self)
            else:
                return visitor.visitChildren(self)




    def bad_member(self):

        localctx = YiniParser.Bad_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_bad_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.state = 295
                self.match(YiniParser.REST)
                pass
            elif token in [8, 9, 10, 11, 12, 13, 17, 25, 27]:
                self.state = 296
                self.value()
                pass
            elif token in [22]:
                pass
            else:
                pass
            self.state = 299
            self.match(YiniParser.EQ)
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 17, 25, 27]:
                self.state = 300
                self.value()
                pass
            elif token in [41]:
                self.state = 301
                self.match(YiniParser.REST)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 304
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





