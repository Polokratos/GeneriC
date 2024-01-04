lexer grammar lex;

RETURN : 'return';
SEMICOLON : ';';

BRACKET_OR : '(';
BRACKET_CR : ')';
BRACKET_OS: '<';
BRACKET_CS: '>';
BRACKET_OW: '{';
BRACKET_CW: '}';

COMMA: ',';
EQUAL: '=';

IDENTIFIER : [a-zA-Z]+;
TYPE_IDENTIFIER : [a-zA-Z*]+;
WS: [\r\t\n ] -> skip;