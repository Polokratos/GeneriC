parser grammar par;

options{tokenVocab=lex;}

program: 
    function* EOF;

function: 
    head body;

head: 
    type function_name type_parameters? arguments;

function_name: 
    LVALUE;

type_parameters:
    BRACKET_OS type_params BRACKET_CS;
type_params: 
    type 
    | type COMMA type_params;

arguments: 
    BRACKET_OR args BRACKET_CR;
args:
    type LVALUE 
    | type LVALUE COMMA args;

body: 
    BRACKET_OW statement* BRACKET_CW;

statement: 
    return_s 
    | init_assign_s
    | assign_s 
    | init_s 
    | if_s 
    | for_s 
    | while_s 
    | function_call_s
    | arithmetic_s;

return_s: 
    RETURN LVALUE SEMICOLON;

assign_s: 
    LVALUE EQUAL LVALUE SEMICOLON
    | LVALUE EQUAL CONSTANT SEMICOLON;

init_s: 
    type LVALUE SEMICOLON;

if_s: 
    IF BRACKET_OR arithmetic_expr BRACKET_CR body;

for_s: 
    FOR BRACKET_OR 
    statement 
    arithmetic_expr SEMICOLON 
    LVALUE (INCREMENT | DECREMENT) 
    BRACKET_CR body;

while_s: 
    WHILE BRACKET_OR arithmetic_expr BRACKET_CR body;

function_call_s: 
    LVALUE type_parameters? BRACKET_OR function_call_args BRACKET_CR SEMICOLON;

function_call_args:
    LVALUE
    | LVALUE COMMA function_call_args;

arithmetic_s :
    LVALUE INCREMENT SEMICOLON
    | LVALUE DECREMENT SEMICOLON;

arithmetic_expr:
    LVALUE
    | LVALUE BRACKET_CS LVALUE
    | LVALUE BRACKET_OS LVALUE
    | LVALUE BRACKET_CS CONSTANT
    | LVALUE BRACKET_OS CONSTANT;

init_assign_s:
    type LVALUE EQUAL LVALUE SEMICOLON
    | type LVALUE EQUAL CONSTANT SEMICOLON
    | type LVALUE EQUAL function_call_s;

type: 
    LVALUE;