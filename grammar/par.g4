parser grammar par;

options{tokenVocab=lex;}

program : function* EOF;

function : head BRACKET_OW statement+ BRACKET_CW;

head : type IDENTIFIER type_parameters? BRACKET_OR args BRACKET_CR;

type_parameters : BRACKET_OS type_params BRACKET_CS;
type_params : type | type COMMA type_params;

args : type IDENTIFIER | type IDENTIFIER COMMA args;


statement : return_s | assign_s | init_s;

return_s : RETURN IDENTIFIER SEMICOLON;
assign_s : IDENTIFIER EQUAL IDENTIFIER SEMICOLON;
init_s : type IDENTIFIER SEMICOLON;

type: TYPE_IDENTIFIER | IDENTIFIER;