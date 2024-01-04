# Generated from grammar/lex.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,66,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,54,8,10,11,10,12,10,55,
        1,11,4,11,59,8,11,11,11,12,11,60,1,12,1,12,1,12,1,12,0,0,13,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,0,
        3,2,0,65,90,97,122,3,0,42,42,65,90,97,122,3,0,9,10,13,13,32,32,67,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,
        1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,
        1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,34,1,0,0,0,5,36,
        1,0,0,0,7,38,1,0,0,0,9,40,1,0,0,0,11,42,1,0,0,0,13,44,1,0,0,0,15,
        46,1,0,0,0,17,48,1,0,0,0,19,50,1,0,0,0,21,53,1,0,0,0,23,58,1,0,0,
        0,25,62,1,0,0,0,27,28,5,114,0,0,28,29,5,101,0,0,29,30,5,116,0,0,
        30,31,5,117,0,0,31,32,5,114,0,0,32,33,5,110,0,0,33,2,1,0,0,0,34,
        35,5,59,0,0,35,4,1,0,0,0,36,37,5,40,0,0,37,6,1,0,0,0,38,39,5,41,
        0,0,39,8,1,0,0,0,40,41,5,60,0,0,41,10,1,0,0,0,42,43,5,62,0,0,43,
        12,1,0,0,0,44,45,5,123,0,0,45,14,1,0,0,0,46,47,5,125,0,0,47,16,1,
        0,0,0,48,49,5,44,0,0,49,18,1,0,0,0,50,51,5,61,0,0,51,20,1,0,0,0,
        52,54,7,0,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,
        0,0,0,56,22,1,0,0,0,57,59,7,1,0,0,58,57,1,0,0,0,59,60,1,0,0,0,60,
        58,1,0,0,0,60,61,1,0,0,0,61,24,1,0,0,0,62,63,7,2,0,0,63,64,1,0,0,
        0,64,65,6,12,0,0,65,26,1,0,0,0,3,0,55,60,1,6,0,0
    ]

class lex(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    SEMICOLON = 2
    BRACKET_OR = 3
    BRACKET_CR = 4
    BRACKET_OS = 5
    BRACKET_CS = 6
    BRACKET_OW = 7
    BRACKET_CW = 8
    COMMA = 9
    EQUAL = 10
    IDENTIFIER = 11
    TYPE_IDENTIFIER = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "';'", "'('", "')'", "'<'", "'>'", "'{'", "'}'", 
            "','", "'='" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "SEMICOLON", "BRACKET_OR", "BRACKET_CR", "BRACKET_OS", 
            "BRACKET_CS", "BRACKET_OW", "BRACKET_CW", "COMMA", "EQUAL", 
            "IDENTIFIER", "TYPE_IDENTIFIER", "WS" ]

    ruleNames = [ "RETURN", "SEMICOLON", "BRACKET_OR", "BRACKET_CR", "BRACKET_OS", 
                  "BRACKET_CS", "BRACKET_OW", "BRACKET_CW", "COMMA", "EQUAL", 
                  "IDENTIFIER", "TYPE_IDENTIFIER", "WS" ]

    grammarFileName = "lex.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


