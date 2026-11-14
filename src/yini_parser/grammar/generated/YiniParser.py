# Generated from ./grammar/v1.0.0-rc.6x/YiniParser.g4 by ANTLR 4.13.2
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
        4,1,41,340,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,3,0,74,8,0,1,0,5,0,77,8,0,10,0,12,0,
        80,9,0,1,0,3,0,83,8,0,1,0,1,0,1,1,1,1,5,1,89,8,1,10,1,12,1,92,9,
        1,1,1,4,1,95,8,1,11,1,12,1,96,3,1,99,8,1,1,2,1,2,5,2,103,8,2,10,
        2,12,2,106,9,2,1,3,1,3,3,3,110,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,120,8,4,1,5,1,5,3,5,124,8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,
        8,1,8,3,8,135,8,8,1,9,1,9,1,9,3,9,140,8,9,1,9,3,9,143,8,9,1,10,1,
        10,3,10,147,8,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,13,4,13,157,
        8,13,11,13,12,13,158,1,14,1,14,3,14,163,8,14,1,15,1,15,1,15,1,16,
        1,16,1,17,1,17,1,17,3,17,173,8,17,1,18,1,18,1,18,1,18,3,18,179,8,
        18,1,19,1,19,1,19,1,19,3,19,185,8,19,1,20,1,20,4,20,189,8,20,11,
        20,12,20,190,1,21,1,21,5,21,195,8,21,10,21,12,21,198,9,21,1,21,1,
        21,1,22,1,22,1,22,1,22,1,22,3,22,207,8,22,1,23,1,23,1,24,1,24,5,
        24,213,8,24,10,24,12,24,216,9,24,1,24,3,24,219,8,24,1,24,5,24,222,
        8,24,10,24,12,24,225,9,24,1,24,1,24,3,24,229,8,24,1,25,1,25,5,25,
        233,8,25,10,25,12,25,236,9,25,1,25,1,25,5,25,240,8,25,10,25,12,25,
        243,9,25,1,25,5,25,246,8,25,10,25,12,25,249,9,25,1,25,5,25,252,8,
        25,10,25,12,25,255,9,25,1,25,3,25,258,8,25,1,26,1,26,1,26,1,26,1,
        27,1,27,1,28,1,28,5,28,268,8,28,10,28,12,28,271,9,28,1,28,3,28,274,
        8,28,1,28,5,28,277,8,28,10,28,12,28,280,9,28,1,28,1,28,3,28,284,
        8,28,1,29,1,29,5,29,288,8,29,10,29,12,29,291,9,29,1,29,1,29,5,29,
        295,8,29,10,29,12,29,298,9,29,1,29,5,29,301,8,29,10,29,12,29,304,
        9,29,1,29,5,29,307,8,29,10,29,12,29,310,9,29,1,29,3,29,313,8,29,
        1,30,1,30,1,31,3,31,318,8,31,1,31,1,31,1,32,1,32,1,33,1,33,1,34,
        1,34,1,35,1,35,3,35,330,8,35,1,35,1,35,1,35,3,35,335,8,35,1,35,3,
        35,338,8,35,1,35,0,0,36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,
        5,2,0,8,10,38,38,2,0,19,19,21,21,2,0,32,32,35,36,1,0,26,27,1,0,8,
        9,362,0,73,1,0,0,0,2,98,1,0,0,0,4,100,1,0,0,0,6,109,1,0,0,0,8,119,
        1,0,0,0,10,121,1,0,0,0,12,125,1,0,0,0,14,127,1,0,0,0,16,134,1,0,
        0,0,18,142,1,0,0,0,20,144,1,0,0,0,22,150,1,0,0,0,24,152,1,0,0,0,
        26,156,1,0,0,0,28,162,1,0,0,0,30,164,1,0,0,0,32,167,1,0,0,0,34,169,
        1,0,0,0,36,178,1,0,0,0,38,184,1,0,0,0,40,186,1,0,0,0,42,192,1,0,
        0,0,44,206,1,0,0,0,46,208,1,0,0,0,48,228,1,0,0,0,50,230,1,0,0,0,
        52,259,1,0,0,0,54,263,1,0,0,0,56,283,1,0,0,0,58,285,1,0,0,0,60,314,
        1,0,0,0,62,317,1,0,0,0,64,321,1,0,0,0,66,323,1,0,0,0,68,325,1,0,
        0,0,70,329,1,0,0,0,72,74,3,2,1,0,73,72,1,0,0,0,73,74,1,0,0,0,74,
        78,1,0,0,0,75,77,3,8,4,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,
        0,78,79,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,81,83,3,4,2,0,82,81,
        1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,5,0,0,1,85,1,1,0,0,0,86,
        90,5,1,0,0,87,89,3,26,13,0,88,87,1,0,0,0,89,92,1,0,0,0,90,88,1,0,
        0,0,90,91,1,0,0,0,91,99,1,0,0,0,92,90,1,0,0,0,93,95,3,26,13,0,94,
        93,1,0,0,0,95,96,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,
        0,98,86,1,0,0,0,98,94,1,0,0,0,99,3,1,0,0,0,100,104,5,5,0,0,101,103,
        3,6,3,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,
        1,0,0,0,105,5,1,0,0,0,106,104,1,0,0,0,107,110,3,26,13,0,108,110,
        3,10,5,0,109,107,1,0,0,0,109,108,1,0,0,0,110,7,1,0,0,0,111,120,3,
        26,13,0,112,120,3,10,5,0,113,120,3,12,6,0,114,120,5,6,0,0,115,120,
        3,14,7,0,116,120,3,30,15,0,117,120,3,16,8,0,118,120,3,70,35,0,119,
        111,1,0,0,0,119,112,1,0,0,0,119,113,1,0,0,0,119,114,1,0,0,0,119,
        115,1,0,0,0,119,116,1,0,0,0,119,117,1,0,0,0,119,118,1,0,0,0,120,
        9,1,0,0,0,121,123,5,36,0,0,122,124,3,26,13,0,123,122,1,0,0,0,123,
        124,1,0,0,0,124,11,1,0,0,0,125,126,5,35,0,0,126,13,1,0,0,0,127,128,
        5,7,0,0,128,15,1,0,0,0,129,135,3,18,9,0,130,135,3,24,12,0,131,132,
        3,68,34,0,132,133,3,28,14,0,133,135,1,0,0,0,134,129,1,0,0,0,134,
        130,1,0,0,0,134,131,1,0,0,0,135,17,1,0,0,0,136,143,3,20,10,0,137,
        139,5,3,0,0,138,140,3,46,23,0,139,138,1,0,0,0,139,140,1,0,0,0,140,
        141,1,0,0,0,141,143,3,28,14,0,142,136,1,0,0,0,142,137,1,0,0,0,143,
        19,1,0,0,0,144,146,5,2,0,0,145,147,3,22,11,0,146,145,1,0,0,0,146,
        147,1,0,0,0,147,148,1,0,0,0,148,149,3,28,14,0,149,21,1,0,0,0,150,
        151,5,38,0,0,151,23,1,0,0,0,152,153,5,4,0,0,153,154,3,28,14,0,154,
        25,1,0,0,0,155,157,5,32,0,0,156,155,1,0,0,0,157,158,1,0,0,0,158,
        156,1,0,0,0,158,159,1,0,0,0,159,27,1,0,0,0,160,163,3,26,13,0,161,
        163,5,0,0,1,162,160,1,0,0,0,162,161,1,0,0,0,163,29,1,0,0,0,164,165,
        3,34,17,0,165,166,3,28,14,0,166,31,1,0,0,0,167,168,7,0,0,0,168,33,
        1,0,0,0,169,170,3,32,16,0,170,172,5,19,0,0,171,173,3,36,18,0,172,
        171,1,0,0,0,172,173,1,0,0,0,173,35,1,0,0,0,174,179,3,40,20,0,175,
        179,3,38,19,0,176,179,3,56,28,0,177,179,3,48,24,0,178,174,1,0,0,
        0,178,175,1,0,0,0,178,176,1,0,0,0,178,177,1,0,0,0,179,37,1,0,0,0,
        180,185,3,64,32,0,181,185,3,46,23,0,182,185,3,62,31,0,183,185,3,
        66,33,0,184,180,1,0,0,0,184,181,1,0,0,0,184,182,1,0,0,0,184,183,
        1,0,0,0,185,39,1,0,0,0,186,188,5,13,0,0,187,189,3,42,21,0,188,187,
        1,0,0,0,189,190,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,41,1,
        0,0,0,192,196,5,26,0,0,193,195,3,60,30,0,194,193,1,0,0,0,195,198,
        1,0,0,0,196,194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,196,
        1,0,0,0,199,200,3,44,22,0,200,43,1,0,0,0,201,207,5,13,0,0,202,207,
        3,62,31,0,203,207,5,9,0,0,204,207,5,8,0,0,205,207,5,10,0,0,206,201,
        1,0,0,0,206,202,1,0,0,0,206,203,1,0,0,0,206,204,1,0,0,0,206,205,
        1,0,0,0,207,45,1,0,0,0,208,209,5,13,0,0,209,47,1,0,0,0,210,214,5,
        24,0,0,211,213,3,60,30,0,212,211,1,0,0,0,213,216,1,0,0,0,214,212,
        1,0,0,0,214,215,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,217,219,
        3,50,25,0,218,217,1,0,0,0,218,219,1,0,0,0,219,223,1,0,0,0,220,222,
        3,60,30,0,221,220,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,0,223,224,
        1,0,0,0,224,226,1,0,0,0,225,223,1,0,0,0,226,229,5,25,0,0,227,229,
        5,11,0,0,228,210,1,0,0,0,228,227,1,0,0,0,229,49,1,0,0,0,230,247,
        3,52,26,0,231,233,3,60,30,0,232,231,1,0,0,0,233,236,1,0,0,0,234,
        232,1,0,0,0,234,235,1,0,0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,
        241,5,20,0,0,238,240,3,60,30,0,239,238,1,0,0,0,240,243,1,0,0,0,241,
        239,1,0,0,0,241,242,1,0,0,0,242,244,1,0,0,0,243,241,1,0,0,0,244,
        246,3,52,26,0,245,234,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,
        248,1,0,0,0,248,257,1,0,0,0,249,247,1,0,0,0,250,252,3,60,30,0,251,
        250,1,0,0,0,252,255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,
        256,1,0,0,0,255,253,1,0,0,0,256,258,5,20,0,0,257,253,1,0,0,0,257,
        258,1,0,0,0,258,51,1,0,0,0,259,260,3,32,16,0,260,261,3,54,27,0,261,
        262,3,36,18,0,262,53,1,0,0,0,263,264,7,1,0,0,264,55,1,0,0,0,265,
        269,5,22,0,0,266,268,3,60,30,0,267,266,1,0,0,0,268,271,1,0,0,0,269,
        267,1,0,0,0,269,270,1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,272,
        274,3,58,29,0,273,272,1,0,0,0,273,274,1,0,0,0,274,278,1,0,0,0,275,
        277,3,60,30,0,276,275,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,
        279,1,0,0,0,279,281,1,0,0,0,280,278,1,0,0,0,281,284,5,23,0,0,282,
        284,5,12,0,0,283,265,1,0,0,0,283,282,1,0,0,0,284,57,1,0,0,0,285,
        302,3,36,18,0,286,288,3,60,30,0,287,286,1,0,0,0,288,291,1,0,0,0,
        289,287,1,0,0,0,289,290,1,0,0,0,290,292,1,0,0,0,291,289,1,0,0,0,
        292,296,5,20,0,0,293,295,3,60,30,0,294,293,1,0,0,0,295,298,1,0,0,
        0,296,294,1,0,0,0,296,297,1,0,0,0,297,299,1,0,0,0,298,296,1,0,0,
        0,299,301,3,36,18,0,300,289,1,0,0,0,301,304,1,0,0,0,302,300,1,0,
        0,0,302,303,1,0,0,0,303,312,1,0,0,0,304,302,1,0,0,0,305,307,3,60,
        30,0,306,305,1,0,0,0,307,310,1,0,0,0,308,306,1,0,0,0,308,309,1,0,
        0,0,309,311,1,0,0,0,310,308,1,0,0,0,311,313,5,20,0,0,312,308,1,0,
        0,0,312,313,1,0,0,0,313,59,1,0,0,0,314,315,7,2,0,0,315,61,1,0,0,
        0,316,318,7,3,0,0,317,316,1,0,0,0,317,318,1,0,0,0,318,319,1,0,0,
        0,319,320,5,14,0,0,320,63,1,0,0,0,321,322,5,10,0,0,322,65,1,0,0,
        0,323,324,7,4,0,0,324,67,1,0,0,0,325,326,5,41,0,0,326,69,1,0,0,0,
        327,330,5,40,0,0,328,330,3,36,18,0,329,327,1,0,0,0,329,328,1,0,0,
        0,329,330,1,0,0,0,330,331,1,0,0,0,331,334,5,19,0,0,332,335,3,36,
        18,0,333,335,5,40,0,0,334,332,1,0,0,0,334,333,1,0,0,0,335,337,1,
        0,0,0,336,338,3,26,13,0,337,336,1,0,0,0,337,338,1,0,0,0,338,71,1,
        0,0,0,44,73,78,82,90,96,98,104,109,119,123,134,139,142,146,158,162,
        172,178,184,190,196,206,214,218,223,228,234,241,247,253,257,269,
        273,278,283,289,296,302,308,312,317,329,334,337
    ]

class YiniParser ( Parser ):

    grammarFileName = "YiniParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'{}'", "'[]'", 
                     "<INVALID>", "<INVALID>", "'^'", "'\\u00A7'", "'>'", 
                     "'<'", "'='", "','", "':'", "'['", "']'", "'{'", "'}'", 
                     "'+'", "'-'", "'$'", "'%'", "'@'", "';'" ]

    symbolicNames = [ "<INVALID>", "SHEBANG", "YINI_TOKEN", "INCLUDE_TOKEN", 
                      "DEPRECATED_TOKEN", "TERMINAL_TOKEN", "SECTION_HEAD", 
                      "INVALID_SECTION_HEAD", "BOOLEAN_FALSE", "BOOLEAN_TRUE", 
                      "NULL", "EMPTY_OBJECT", "EMPTY_LIST", "STRING", "NUMBER", 
                      "CARET", "SS", "GT", "LT", "EQ", "COMMA", "COLON", 
                      "OB", "CB", "OC", "CC", "PLUS", "MINUS", "DOLLAR", 
                      "PC", "AT", "SEMICOLON", "NL", "WS", "BLOCK_COMMENT", 
                      "DISABLED_LINE", "FULL_LINE_COMMENT", "INLINE_COMMENT", 
                      "KEY", "IDENT_INVALID", "REST", "META_INVALID" ]

    RULE_yini = 0
    RULE_prolog = 1
    RULE_terminal_stmt = 2
    RULE_terminal_trivia = 3
    RULE_stmt = 4
    RULE_full_line_comment_stmt = 5
    RULE_disabled_line_stmt = 6
    RULE_invalid_section_stmt = 7
    RULE_meta_stmt = 8
    RULE_directive = 9
    RULE_yini_directive = 10
    RULE_yini_mode_declaration = 11
    RULE_annotation = 12
    RULE_eol = 13
    RULE_line_end = 14
    RULE_assignment = 15
    RULE_identifier = 16
    RULE_member = 17
    RULE_value = 18
    RULE_scalar_value = 19
    RULE_concat_expression = 20
    RULE_concat_tail = 21
    RULE_concat_operand = 22
    RULE_string_literal = 23
    RULE_object_literal = 24
    RULE_object_members = 25
    RULE_object_member = 26
    RULE_object_member_separator = 27
    RULE_list_literal = 28
    RULE_elements = 29
    RULE_multiline_trivia = 30
    RULE_number_literal = 31
    RULE_null_literal = 32
    RULE_boolean_literal = 33
    RULE_bad_meta_text = 34
    RULE_bad_member = 35

    ruleNames =  [ "yini", "prolog", "terminal_stmt", "terminal_trivia", 
                   "stmt", "full_line_comment_stmt", "disabled_line_stmt", 
                   "invalid_section_stmt", "meta_stmt", "directive", "yini_directive", 
                   "yini_mode_declaration", "annotation", "eol", "line_end", 
                   "assignment", "identifier", "member", "value", "scalar_value", 
                   "concat_expression", "concat_tail", "concat_operand", 
                   "string_literal", "object_literal", "object_members", 
                   "object_member", "object_member_separator", "list_literal", 
                   "elements", "multiline_trivia", "number_literal", "null_literal", 
                   "boolean_literal", "bad_meta_text", "bad_member" ]

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
    NUMBER=14
    CARET=15
    SS=16
    GT=17
    LT=18
    EQ=19
    COMMA=20
    COLON=21
    OB=22
    CB=23
    OC=24
    CC=25
    PLUS=26
    MINUS=27
    DOLLAR=28
    PC=29
    AT=30
    SEMICOLON=31
    NL=32
    WS=33
    BLOCK_COMMENT=34
    DISABLED_LINE=35
    FULL_LINE_COMMENT=36
    INLINE_COMMENT=37
    KEY=38
    IDENT_INVALID=39
    REST=40
    META_INVALID=41

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
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 72
                self.prolog()


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3681009827804) != 0):
                self.state = 75
                self.stmt()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 81
                self.terminal_stmt()


            self.state = 84
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
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(YiniParser.SHEBANG)
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 87
                        self.eol() 
                    self.state = 92
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 93
                        self.eol()

                    else:
                        raise NoViableAltException(self)
                    self.state = 96 
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

        def terminal_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Terminal_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Terminal_triviaContext,i)


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
            self.state = 100
            self.match(YiniParser.TERMINAL_TOKEN)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==36:
                self.state = 101
                self.terminal_trivia()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Terminal_triviaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def full_line_comment_stmt(self):
            return self.getTypedRuleContext(YiniParser.Full_line_comment_stmtContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_terminal_trivia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_trivia" ):
                return visitor.visitTerminal_trivia(self)
            else:
                return visitor.visitChildren(self)




    def terminal_trivia(self):

        localctx = YiniParser.Terminal_triviaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_terminal_trivia)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.eol()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.full_line_comment_stmt()
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def full_line_comment_stmt(self):
            return self.getTypedRuleContext(YiniParser.Full_line_comment_stmtContext,0)


        def disabled_line_stmt(self):
            return self.getTypedRuleContext(YiniParser.Disabled_line_stmtContext,0)


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
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.eol()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.full_line_comment_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.disabled_line_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 114
                self.match(YiniParser.SECTION_HEAD)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 115
                self.invalid_section_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 116
                self.assignment()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 117
                self.meta_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 118
                self.bad_member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Full_line_comment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FULL_LINE_COMMENT(self):
            return self.getToken(YiniParser.FULL_LINE_COMMENT, 0)

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_full_line_comment_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFull_line_comment_stmt" ):
                return visitor.visitFull_line_comment_stmt(self)
            else:
                return visitor.visitChildren(self)




    def full_line_comment_stmt(self):

        localctx = YiniParser.Full_line_comment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_full_line_comment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(YiniParser.FULL_LINE_COMMENT)
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 122
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Disabled_line_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISABLED_LINE(self):
            return self.getToken(YiniParser.DISABLED_LINE, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_disabled_line_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisabled_line_stmt" ):
                return visitor.visitDisabled_line_stmt(self)
            else:
                return visitor.visitChildren(self)




    def disabled_line_stmt(self):

        localctx = YiniParser.Disabled_line_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_disabled_line_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(YiniParser.DISABLED_LINE)
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
        self.enterRule(localctx, 14, self.RULE_invalid_section_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
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


        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_meta_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_stmt" ):
                return visitor.visitMeta_stmt(self)
            else:
                return visitor.visitChildren(self)




    def meta_stmt(self):

        localctx = YiniParser.Meta_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_meta_stmt)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.directive()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.annotation()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.bad_meta_text()
                self.state = 132
                self.line_end()
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

        def yini_directive(self):
            return self.getTypedRuleContext(YiniParser.Yini_directiveContext,0)


        def INCLUDE_TOKEN(self):
            return self.getToken(YiniParser.INCLUDE_TOKEN, 0)

        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


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
        self.enterRule(localctx, 18, self.RULE_directive)
        self._la = 0 # Token type
        try:
            self.state = 142
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.yini_directive()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(YiniParser.INCLUDE_TOKEN)
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 138
                    self.string_literal()


                self.state = 141
                self.line_end()
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


    class Yini_directiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def YINI_TOKEN(self):
            return self.getToken(YiniParser.YINI_TOKEN, 0)

        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


        def yini_mode_declaration(self):
            return self.getTypedRuleContext(YiniParser.Yini_mode_declarationContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_yini_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYini_directive" ):
                return visitor.visitYini_directive(self)
            else:
                return visitor.visitChildren(self)




    def yini_directive(self):

        localctx = YiniParser.Yini_directiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_yini_directive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(YiniParser.YINI_TOKEN)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 145
                self.yini_mode_declaration()


            self.state = 148
            self.line_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Yini_mode_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_yini_mode_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitYini_mode_declaration" ):
                return visitor.visitYini_mode_declaration(self)
            else:
                return visitor.visitChildren(self)




    def yini_mode_declaration(self):

        localctx = YiniParser.Yini_mode_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_yini_mode_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
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

        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_annotation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnnotation" ):
                return visitor.visitAnnotation(self)
            else:
                return visitor.visitChildren(self)




    def annotation(self):

        localctx = YiniParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_annotation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(YiniParser.DEPRECATED_TOKEN)
            self.state = 153
            self.line_end()
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
        self.enterRule(localctx, 26, self.RULE_eol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 155
                    self.match(YiniParser.NL)

                else:
                    raise NoViableAltException(self)
                self.state = 158 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eol(self):
            return self.getTypedRuleContext(YiniParser.EolContext,0)


        def EOF(self):
            return self.getToken(YiniParser.EOF, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_line_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_end" ):
                return visitor.visitLine_end(self)
            else:
                return visitor.visitChildren(self)




    def line_end(self):

        localctx = YiniParser.Line_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_line_end)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.eol()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(YiniParser.EOF)
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(YiniParser.MemberContext,0)


        def line_end(self):
            return self.getTypedRuleContext(YiniParser.Line_endContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = YiniParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.member()
            self.state = 165
            self.line_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY(self):
            return self.getToken(YiniParser.KEY, 0)

        def BOOLEAN_TRUE(self):
            return self.getToken(YiniParser.BOOLEAN_TRUE, 0)

        def BOOLEAN_FALSE(self):
            return self.getToken(YiniParser.BOOLEAN_FALSE, 0)

        def NULL(self):
            return self.getToken(YiniParser.NULL, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = YiniParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 274877908736) != 0)):
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


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(YiniParser.IdentifierContext,0)


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
        self.enterRule(localctx, 34, self.RULE_member)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.identifier()
            self.state = 170
            self.match(YiniParser.EQ)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 222330624) != 0):
                self.state = 171
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
        self.enterRule(localctx, 36, self.RULE_value)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.concat_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.scalar_value()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.list_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 177
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
        self.enterRule(localctx, 38, self.RULE_scalar_value)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.null_literal()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.string_literal()
                pass
            elif token in [14, 26, 27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.number_literal()
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
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
        self.enterRule(localctx, 40, self.RULE_concat_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(YiniParser.STRING)
            self.state = 188 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 187
                    self.concat_tail()

                else:
                    raise NoViableAltException(self)
                self.state = 190 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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


        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_concat_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcat_tail" ):
                return visitor.visitConcat_tail(self)
            else:
                return visitor.visitChildren(self)




    def concat_tail(self):

        localctx = YiniParser.Concat_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_concat_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(YiniParser.PLUS)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                self.state = 193
                self.multiline_trivia()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
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

        def number_literal(self):
            return self.getTypedRuleContext(YiniParser.Number_literalContext,0)


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
        self.enterRule(localctx, 44, self.RULE_concat_operand)
        try:
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(YiniParser.STRING)
                pass
            elif token in [14, 26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.number_literal()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(YiniParser.BOOLEAN_TRUE)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(YiniParser.BOOLEAN_FALSE)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.match(YiniParser.NULL)
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
        self.enterRule(localctx, 46, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


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
        self.enterRule(localctx, 48, self.RULE_object_literal)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(YiniParser.OC)
                self.state = 214
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 211
                        self.multiline_trivia() 
                    self.state = 216
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 274877908736) != 0):
                    self.state = 217
                    self.object_members()


                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                    self.state = 220
                    self.multiline_trivia()
                    self.state = 225
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 226
                self.match(YiniParser.CC)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(YiniParser.EMPTY_OBJECT)
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_object_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_members" ):
                return visitor.visitObject_members(self)
            else:
                return visitor.visitChildren(self)




    def object_members(self):

        localctx = YiniParser.Object_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_object_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.object_member()
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 234
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                        self.state = 231
                        self.multiline_trivia()
                        self.state = 236
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 237
                    self.match(YiniParser.COMMA)
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                        self.state = 238
                        self.multiline_trivia()
                        self.state = 243
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 244
                    self.object_member() 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                    self.state = 250
                    self.multiline_trivia()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
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

        def identifier(self):
            return self.getTypedRuleContext(YiniParser.IdentifierContext,0)


        def object_member_separator(self):
            return self.getTypedRuleContext(YiniParser.Object_member_separatorContext,0)


        def value(self):
            return self.getTypedRuleContext(YiniParser.ValueContext,0)


        def getRuleIndex(self):
            return YiniParser.RULE_object_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_member" ):
                return visitor.visitObject_member(self)
            else:
                return visitor.visitChildren(self)




    def object_member(self):

        localctx = YiniParser.Object_memberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_object_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.identifier()
            self.state = 260
            self.object_member_separator()
            self.state = 261
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
        self.enterRule(localctx, 54, self.RULE_object_member_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not(_la==19 or _la==21):
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


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
        self.enterRule(localctx, 56, self.RULE_list_literal)
        self._la = 0 # Token type
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(YiniParser.OB)
                self.state = 269
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 266
                        self.multiline_trivia() 
                    self.state = 271
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 222330624) != 0):
                    self.state = 272
                    self.elements()


                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                    self.state = 275
                    self.multiline_trivia()
                    self.state = 280
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 281
                self.match(YiniParser.CB)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(YiniParser.EMPTY_LIST)
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

        def multiline_trivia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(YiniParser.Multiline_triviaContext)
            else:
                return self.getTypedRuleContext(YiniParser.Multiline_triviaContext,i)


        def getRuleIndex(self):
            return YiniParser.RULE_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElements" ):
                return visitor.visitElements(self)
            else:
                return visitor.visitChildren(self)




    def elements(self):

        localctx = YiniParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.value()
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 289
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                        self.state = 286
                        self.multiline_trivia()
                        self.state = 291
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 292
                    self.match(YiniParser.COMMA)
                    self.state = 296
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                        self.state = 293
                        self.multiline_trivia()
                        self.state = 298
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 299
                    self.value() 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0):
                    self.state = 305
                    self.multiline_trivia()
                    self.state = 310
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 311
                self.match(YiniParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiline_triviaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(YiniParser.NL, 0)

        def DISABLED_LINE(self):
            return self.getToken(YiniParser.DISABLED_LINE, 0)

        def FULL_LINE_COMMENT(self):
            return self.getToken(YiniParser.FULL_LINE_COMMENT, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_multiline_trivia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiline_trivia" ):
                return visitor.visitMultiline_trivia(self)
            else:
                return visitor.visitChildren(self)




    def multiline_trivia(self):

        localctx = YiniParser.Multiline_triviaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_multiline_trivia)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 107374182400) != 0)):
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


    class Number_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(YiniParser.NUMBER, 0)

        def PLUS(self):
            return self.getToken(YiniParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(YiniParser.MINUS, 0)

        def getRuleIndex(self):
            return YiniParser.RULE_number_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_literal" ):
                return visitor.visitNumber_literal(self)
            else:
                return visitor.visitChildren(self)




    def number_literal(self):

        localctx = YiniParser.Number_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_number_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26 or _la==27:
                self.state = 316
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 319
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
        self.enterRule(localctx, 64, self.RULE_null_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
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
        self.enterRule(localctx, 66, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
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
        self.enterRule(localctx, 68, self.RULE_bad_meta_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
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
        self.enterRule(localctx, 70, self.RULE_bad_member)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.state = 327
                self.match(YiniParser.REST)
                pass
            elif token in [8, 9, 10, 11, 12, 13, 14, 22, 24, 26, 27]:
                self.state = 328
                self.value()
                pass
            elif token in [19]:
                pass
            else:
                pass
            self.state = 331
            self.match(YiniParser.EQ)
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 11, 12, 13, 14, 22, 24, 26, 27]:
                self.state = 332
                self.value()
                pass
            elif token in [40]:
                self.state = 333
                self.match(YiniParser.REST)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 336
                self.eol()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





