# Generated from ./grammar/v1.0.0-rc.5x/YiniParser.g4 by ANTLR 4.13.2
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
        4,1,44,290,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,3,0,50,8,0,1,0,5,0,53,8,0,
        10,0,12,0,56,9,0,1,0,3,0,59,8,0,1,0,1,0,1,1,1,1,5,1,65,8,1,10,1,
        12,1,68,9,1,1,1,4,1,71,8,1,11,1,12,1,72,3,1,75,8,1,1,2,1,2,5,2,79,
        8,2,10,2,12,2,82,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,90,8,3,1,4,1,4,
        1,5,1,5,1,5,1,5,1,5,3,5,99,8,5,1,6,1,6,1,6,1,6,3,6,105,8,6,1,6,3,
        6,108,8,6,1,7,1,7,1,7,1,8,4,8,114,8,8,11,8,12,8,115,1,9,1,9,1,9,
        1,10,1,10,1,10,3,10,124,8,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,
        132,8,11,1,12,1,12,5,12,136,8,12,10,12,12,12,139,9,12,1,12,3,12,
        142,8,12,1,12,5,12,145,8,12,10,12,12,12,148,9,12,1,12,1,12,5,12,
        152,8,12,10,12,12,12,155,9,12,1,12,1,12,5,12,159,8,12,10,12,12,12,
        162,9,12,3,12,164,8,12,1,13,1,13,1,13,5,13,169,8,13,10,13,12,13,
        172,9,13,1,13,5,13,175,8,13,10,13,12,13,178,9,13,1,13,3,13,181,8,
        13,1,14,1,14,1,14,5,14,186,8,14,10,14,12,14,189,9,14,1,14,1,14,1,
        15,1,15,5,15,195,8,15,10,15,12,15,198,9,15,1,15,3,15,201,8,15,1,
        15,5,15,204,8,15,10,15,12,15,207,9,15,1,15,1,15,5,15,211,8,15,10,
        15,12,15,214,9,15,1,15,1,15,5,15,218,8,15,10,15,12,15,221,9,15,3,
        15,223,8,15,1,16,1,16,5,16,227,8,16,10,16,12,16,230,9,16,1,16,1,
        16,5,16,234,8,16,10,16,12,16,237,9,16,1,16,5,16,240,8,16,10,16,12,
        16,243,9,16,1,16,3,16,246,8,16,1,17,1,17,1,18,1,18,1,19,1,19,5,19,
        254,8,19,10,19,12,19,257,9,19,1,20,5,20,260,8,20,10,20,12,20,263,
        9,20,1,20,1,20,5,20,267,8,20,10,20,12,20,270,9,20,1,20,1,20,1,21,
        1,21,1,22,1,22,1,23,1,23,3,23,280,8,23,1,23,1,23,1,23,3,23,285,8,
        23,1,23,3,23,288,8,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,0,1,1,0,8,9,315,0,49,1,0,0,0,
        2,74,1,0,0,0,4,76,1,0,0,0,6,89,1,0,0,0,8,91,1,0,0,0,10,98,1,0,0,
        0,12,107,1,0,0,0,14,109,1,0,0,0,16,113,1,0,0,0,18,117,1,0,0,0,20,
        120,1,0,0,0,22,131,1,0,0,0,24,163,1,0,0,0,26,165,1,0,0,0,28,182,
        1,0,0,0,30,222,1,0,0,0,32,224,1,0,0,0,34,247,1,0,0,0,36,249,1,0,
        0,0,38,251,1,0,0,0,40,261,1,0,0,0,42,273,1,0,0,0,44,275,1,0,0,0,
        46,279,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,49,50,1,0,0,0,50,54,1,
        0,0,0,51,53,3,6,3,0,52,51,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,
        55,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,57,59,3,4,2,0,58,57,1,0,0,
        0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,0,0,1,61,1,1,0,0,0,62,66,5,
        1,0,0,63,65,3,16,8,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,
        67,1,0,0,0,67,75,1,0,0,0,68,66,1,0,0,0,69,71,3,16,8,0,70,69,1,0,
        0,0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,62,
        1,0,0,0,74,70,1,0,0,0,75,3,1,0,0,0,76,80,5,5,0,0,77,79,3,16,8,0,
        78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,5,1,0,
        0,0,82,80,1,0,0,0,83,90,3,16,8,0,84,90,5,6,0,0,85,90,3,8,4,0,86,
        90,3,18,9,0,87,90,3,10,5,0,88,90,3,46,23,0,89,83,1,0,0,0,89,84,1,
        0,0,0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,1,0,0,0,90,
        7,1,0,0,0,91,92,5,7,0,0,92,9,1,0,0,0,93,99,3,12,6,0,94,99,3,14,7,
        0,95,96,3,44,22,0,96,97,3,16,8,0,97,99,1,0,0,0,98,93,1,0,0,0,98,
        94,1,0,0,0,98,95,1,0,0,0,99,11,1,0,0,0,100,101,5,2,0,0,101,108,3,
        16,8,0,102,104,5,3,0,0,103,105,3,38,19,0,104,103,1,0,0,0,104,105,
        1,0,0,0,105,106,1,0,0,0,106,108,3,16,8,0,107,100,1,0,0,0,107,102,
        1,0,0,0,108,13,1,0,0,0,109,110,5,4,0,0,110,111,3,16,8,0,111,15,1,
        0,0,0,112,114,5,36,0,0,113,112,1,0,0,0,114,115,1,0,0,0,115,113,1,
        0,0,0,115,116,1,0,0,0,116,17,1,0,0,0,117,118,3,20,10,0,118,119,3,
        16,8,0,119,19,1,0,0,0,120,121,5,41,0,0,121,123,5,23,0,0,122,124,
        3,22,11,0,123,122,1,0,0,0,123,124,1,0,0,0,124,21,1,0,0,0,125,132,
        3,36,18,0,126,132,3,38,19,0,127,132,3,34,17,0,128,132,3,42,21,0,
        129,132,3,30,15,0,130,132,3,24,12,0,131,125,1,0,0,0,131,126,1,0,
        0,0,131,127,1,0,0,0,131,128,1,0,0,0,131,129,1,0,0,0,131,130,1,0,
        0,0,132,23,1,0,0,0,133,137,5,29,0,0,134,136,5,36,0,0,135,134,1,0,
        0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,138,1,0,0,0,138,141,1,0,
        0,0,139,137,1,0,0,0,140,142,3,26,13,0,141,140,1,0,0,0,141,142,1,
        0,0,0,142,146,1,0,0,0,143,145,5,36,0,0,144,143,1,0,0,0,145,148,1,
        0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,
        0,0,0,149,153,5,30,0,0,150,152,5,36,0,0,151,150,1,0,0,0,152,155,
        1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,164,1,0,0,0,155,153,
        1,0,0,0,156,160,5,11,0,0,157,159,5,36,0,0,158,157,1,0,0,0,159,162,
        1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,164,1,0,0,0,162,160,
        1,0,0,0,163,133,1,0,0,0,163,156,1,0,0,0,164,25,1,0,0,0,165,176,3,
        28,14,0,166,170,5,25,0,0,167,169,5,36,0,0,168,167,1,0,0,0,169,172,
        1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,173,1,0,0,0,172,170,
        1,0,0,0,173,175,3,28,14,0,174,166,1,0,0,0,175,178,1,0,0,0,176,174,
        1,0,0,0,176,177,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,179,181,
        5,25,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,27,1,0,0,0,182,183,
        5,41,0,0,183,187,5,26,0,0,184,186,5,36,0,0,185,184,1,0,0,0,186,189,
        1,0,0,0,187,185,1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,
        1,0,0,0,190,191,3,22,11,0,191,29,1,0,0,0,192,196,5,27,0,0,193,195,
        5,36,0,0,194,193,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,196,197,
        1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,199,201,3,32,16,0,200,199,
        1,0,0,0,200,201,1,0,0,0,201,205,1,0,0,0,202,204,5,36,0,0,203,202,
        1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,
        1,0,0,0,207,205,1,0,0,0,208,212,5,28,0,0,209,211,5,36,0,0,210,209,
        1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,1,0,0,0,213,223,
        1,0,0,0,214,212,1,0,0,0,215,219,5,12,0,0,216,218,5,36,0,0,217,216,
        1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,223,
        1,0,0,0,221,219,1,0,0,0,222,192,1,0,0,0,222,215,1,0,0,0,223,31,1,
        0,0,0,224,241,3,22,11,0,225,227,5,36,0,0,226,225,1,0,0,0,227,230,
        1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,228,
        1,0,0,0,231,235,5,25,0,0,232,234,5,36,0,0,233,232,1,0,0,0,234,237,
        1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,238,1,0,0,0,237,235,
        1,0,0,0,238,240,3,22,11,0,239,228,1,0,0,0,240,243,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,244,246,
        5,25,0,0,245,244,1,0,0,0,245,246,1,0,0,0,246,33,1,0,0,0,247,248,
        5,18,0,0,248,35,1,0,0,0,249,250,5,10,0,0,250,37,1,0,0,0,251,255,
        5,13,0,0,252,254,3,40,20,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,
        1,0,0,0,255,256,1,0,0,0,256,39,1,0,0,0,257,255,1,0,0,0,258,260,5,
        36,0,0,259,258,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,
        0,0,0,262,264,1,0,0,0,263,261,1,0,0,0,264,268,5,31,0,0,265,267,5,
        36,0,0,266,265,1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,269,1,
        0,0,0,269,271,1,0,0,0,270,268,1,0,0,0,271,272,5,13,0,0,272,41,1,
        0,0,0,273,274,7,0,0,0,274,43,1,0,0,0,275,276,5,44,0,0,276,45,1,0,
        0,0,277,280,5,43,0,0,278,280,3,22,11,0,279,277,1,0,0,0,279,278,1,
        0,0,0,279,280,1,0,0,0,280,281,1,0,0,0,281,284,5,23,0,0,282,285,3,
        22,11,0,283,285,5,43,0,0,284,282,1,0,0,0,284,283,1,0,0,0,285,287,
        1,0,0,0,286,288,3,16,8,0,287,286,1,0,0,0,287,288,1,0,0,0,288,47,
        1,0,0,0,40,49,54,58,66,72,74,80,89,98,104,107,115,123,131,137,141,
        146,153,160,163,170,176,180,187,196,200,205,212,219,222,228,235,
        241,245,255,261,268,279,284,287
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
                     "<INVALID>", "<INVALID>", "'\\u00A7'", "'^'", "'>'", 
                     "'<'", "'='", "'#'", "','", "':'", "'['", "']'", "'{'", 
                     "'}'", "'+'", "'$'", "'%'", "'@'", "';'" ]

    symbolicNames = [ "<INVALID>", "SHEBANG", "YINI_TOKEN", "INCLUDE_TOKEN", 
                      "DEPRECATED_TOKEN", "TERMINAL_TOKEN", "SECTION_HEAD", 
                      "INVALID_SECTION_HEAD", "BOOLEAN_FALSE", "BOOLEAN_TRUE", 
                      "NULL", "EMPTY_OBJECT", "EMPTY_LIST", "STRING", "TRIPLE_QUOTED_STRING", 
                      "SINGLE_OR_DOUBLE", "R_AND_C_STRING", "HYPER_STRING", 
                      "NUMBER", "SS", "CARET", "GT", "LT", "EQ", "HASH", 
                      "COMMA", "COLON", "OB", "CB", "OC", "CC", "PLUS", 
                      "DOLLAR", "PC", "AT", "SEMICOLON", "NL", "WS", "BLOCK_COMMENT", 
                      "FULL_LINE_COMMENT", "INLINE_COMMENT", "KEY", "IDENT_INVALID", 
                      "REST", "META_INVALID" ]

    RULE_yini = 0
    RULE_prolog = 1
    RULE_terminal_stmt = 2
    RULE_stmt = 3
    RULE_invalid_section_stmt = 4
    RULE_meta_stmt = 5
    RULE_directive = 6
    RULE_annotation = 7
    RULE_eol = 8
    RULE_assignment = 9
    RULE_member = 10
    RULE_value = 11
    RULE_object_literal = 12
    RULE_object_members = 13
    RULE_object_member = 14
    RULE_list_literal = 15
    RULE_elements = 16
    RULE_number_literal = 17
    RULE_null_literal = 18
    RULE_string_literal = 19
    RULE_string_concat = 20
    RULE_boolean_literal = 21
    RULE_bad_meta_text = 22
    RULE_bad_member = 23

    ruleNames =  [ "yini", "prolog", "terminal_stmt", "stmt", "invalid_section_stmt", 
                   "meta_stmt", "directive", "annotation", "eol", "assignment", 
                   "member", "value", "object_literal", "object_members", 
                   "object_member", "list_literal", "elements", "number_literal", 
                   "null_literal", "string_literal", "string_concat", "boolean_literal", 
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
    HYPER_STRING=17
    NUMBER=18
    SS=19
    CARET=20
    GT=21
    LT=22
    EQ=23
    HASH=24
    COMMA=25
    COLON=26
    OB=27
    CB=28
    OC=29
    CC=30
    PLUS=31
    DOLLAR=32
    PC=33
    AT=34
    SEMICOLON=35
    NL=36
    WS=37
    BLOCK_COMMENT=38
    FULL_LINE_COMMENT=39
    INLINE_COMMENT=40
    KEY=41
    IDENT_INVALID=42
    REST=43
    META_INVALID=44

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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 48
                self.prolog()


            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 28656701554652) != 0):
                self.state = 51
                self.stmt()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 57
                self.terminal_stmt()


            self.state = 60
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(YiniParser.SHEBANG)
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 63
                        self.eol() 
                    self.state = 68
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 69
                        self.eol()

                    else:
                        raise NoViableAltException(self)
                    self.state = 72 
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
            self.state = 76
            self.match(YiniParser.TERMINAL_TOKEN)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 77
                self.eol()
                self.state = 82
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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.eol()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.match(YiniParser.SECTION_HEAD)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.invalid_section_stmt()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.assignment()
                pass
            elif token in [2, 3, 4, 44]:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
                self.meta_stmt()
                pass
            elif token in [8, 9, 10, 11, 12, 13, 18, 23, 27, 29, 43]:
                self.enterOuterAlt(localctx, 6)
                self.state = 88
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
            self.state = 91
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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.directive()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.annotation()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 3)
                self.state = 95
                self.bad_meta_text()
                self.state = 96
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
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.match(YiniParser.YINI_TOKEN)
                self.state = 101
                self.eol()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.match(YiniParser.INCLUDE_TOKEN)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 103
                    self.string_literal()


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
        self.enterRule(localctx, 14, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(YiniParser.DEPRECATED_TOKEN)
            self.state = 110
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
        self.enterRule(localctx, 16, self.RULE_eol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 112
                    self.match(YiniParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 115 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.member()
            self.state = 118
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
        self.enterRule(localctx, 20, self.RULE_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(YiniParser.KEY)
            self.state = 121
            self.match(YiniParser.EQ)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 671366912) != 0):
                self.state = 122
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

        def null_literal(self):
            return self.getTypedRuleContext(YiniParser.Null_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(YiniParser.String_literalContext,0)


        def number_literal(self):
            return self.getTypedRuleContext(YiniParser.Number_literalContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(YiniParser.Boolean_literalContext,0)


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
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.null_literal()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.string_literal()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.number_literal()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.boolean_literal()
                pass
            elif token in [12, 27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.list_literal()
                pass
            elif token in [11, 29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.object_literal()
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
        self.enterRule(localctx, 24, self.RULE_object_literal)
        self._la = 0 # Token type
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(YiniParser.OC)
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 134
                        self.match(YiniParser.NL) 
                    self.state = 139
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==41:
                    self.state = 140
                    self.object_members()


                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 143
                    self.match(YiniParser.NL)
                    self.state = 148
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 149
                self.match(YiniParser.CC)
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 150
                        self.match(YiniParser.NL) 
                    self.state = 155
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.match(YiniParser.EMPTY_OBJECT)
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 157
                        self.match(YiniParser.NL) 
                    self.state = 162
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_object_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.object_member()
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 166
                    self.match(YiniParser.COMMA)
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 167
                        self.match(YiniParser.NL)
                        self.state = 172
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 173
                    self.object_member() 
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 179
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

        def COLON(self):
            return self.getToken(YiniParser.COLON, 0)

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
        self.enterRule(localctx, 28, self.RULE_object_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(YiniParser.KEY)
            self.state = 183
            self.match(YiniParser.COLON)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 184
                self.match(YiniParser.NL)
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 190
            self.value()
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
        self.enterRule(localctx, 30, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(YiniParser.OB)
                self.state = 196
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 193
                        self.match(YiniParser.NL) 
                    self.state = 198
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 671366912) != 0):
                    self.state = 199
                    self.elements()


                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 202
                    self.match(YiniParser.NL)
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 208
                self.match(YiniParser.CB)
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 209
                        self.match(YiniParser.NL) 
                    self.state = 214
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(YiniParser.EMPTY_LIST)
                self.state = 219
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 216
                        self.match(YiniParser.NL) 
                    self.state = 221
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.value()
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 225
                        self.match(YiniParser.NL)
                        self.state = 230
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 231
                    self.match(YiniParser.COMMA)
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 232
                        self.match(YiniParser.NL)
                        self.state = 237
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 238
                    self.value() 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 244
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
        self.enterRule(localctx, 34, self.RULE_number_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
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
        self.enterRule(localctx, 36, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(YiniParser.NULL)
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

        def string_concat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.String_concatContext)
            else:
                return self.getTypedRuleContext(YiniParser.String_concatContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_string_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)




    def string_literal(self):

        localctx = YiniParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(YiniParser.STRING)
            self.state = 255
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 252
                    self.string_concat() 
                self.state = 257
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_concatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(YiniParser.PLUS, 0)

        def STRING(self):
            return self.getToken(YiniParser.STRING, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(YiniParser.NL)
            else:
                return self.getToken(YiniParser.NL, i)

        def getRuleIndex(self):
            return YiniParser.RULE_string_concat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_concat" ):
                return visitor.visitString_concat(self)
            else:
                return visitor.visitChildren(self)




    def string_concat(self):

        localctx = YiniParser.String_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_string_concat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 258
                self.match(YiniParser.NL)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self.match(YiniParser.PLUS)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 265
                self.match(YiniParser.NL)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self.match(YiniParser.STRING)
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
        self.enterRule(localctx, 42, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
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
        self.enterRule(localctx, 44, self.RULE_bad_meta_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
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
        self.enterRule(localctx, 46, self.RULE_bad_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.state = 277
                self.match(YiniParser.REST)
                pass
            elif token in [8, 9, 10, 11, 12, 13, 18, 27, 29]:
                self.state = 278
                self.value()
                pass
            elif token in [23]:
                pass
            else:
                pass
            self.state = 281
            self.match(YiniParser.EQ)
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 18, 27, 29]:
                self.state = 282
                self.value()
                pass
            elif token in [43]:
                self.state = 283
                self.match(YiniParser.REST)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 286
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





