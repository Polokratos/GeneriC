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

IF: 'if';
FOR: 'for';
WHILE: 'while';

INCREMENT : '++';
DECREMENT : '--';

LVALUE : [&]* [a-zA-Z*]+ ('['[a-zA-Z0-9*]+']')?;

CONSTANT : '0' | [1-9][0-9]*;
WS: [\r\t\n ] -> skip;