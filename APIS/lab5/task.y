%{

#include <stdio.h>
#include <stdlib.h>

int yylex(void);
void yyerror(const char *s);

%}

%token RECORD IDENTIFIER INTEGER REAL BYTE WORD CHAR STRING
%token SEMICOLON COLON EQUALS LBRACKET RBRACKET NUMBER

%%

program:
    record_declarations
    ;

record_declarations:
    /* пустое */
  | record_declarations record_declaration SEMICOLON { printf("Record declaration found\n"); }
  ;

record_declaration:
    RECORD IDENTIFIER { printf("Record '%s' found\n", $2); }
    '{' field_list '}' 
    ;

field_list:
    field
  | field_list SEMICOLON field
  ;

field:
    type IDENTIFIER { printf("Field of type %s and identifier '%s' found\n", $1, $2); }
  | type IDENTIFIER LBRACKET NUMBER RBRACKET { printf("Array field of type %s and identifier '%s' with length %d found\n", $1, $2, $4); }
  ;

type:
    INTEGER { $$ = "integer"; }
  | REAL    { $$ = "real"; }
  | BYTE    { $$ = "byte"; }
  | WORD    { $$ = "word"; }
  | CHAR    { $$ = "char"; }
  | STRING  { $$ = "string"; }
  ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
    return yyparse();
}
