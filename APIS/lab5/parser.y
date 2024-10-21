%{
#include <stdio.h>
#include <stdlib.h>
%}

%token KEYWORD
%token IDENTIFIER
%token OPERATOR
%token NUMBER
%token COMMENT
%%


description_list: 
  description_list description 
  {

  }
  | description
  {

  };
  
description:
  OPERATOR
  {

  }
  | KEYWORD
  {

  }
  | IDENTIFIER
  {

  }
  | NUMBER
  {

  }
  | COMMENT
  {

  }
%%

int main(void) {
  printf("Введите описание записей:\n");
  yyparse();
  return 0;
}

int yyerror(char *s) {
    fprintf(stderr, "Ошибка: %s\n", s);
    return 0;
}
