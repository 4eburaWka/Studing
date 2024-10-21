%{
#include "y.tab.h"
%}

%%

"record"                                        { printf("%s → Ключевое слово\n", yytext); return KEYWORD; }
"integer"                                       { printf("%s → Ключевое слово\n", yytext); return KEYWORD; }
"real"                                          { printf("%s → Ключевое слово\n", yytext); return KEYWORD; }
"byte"                                          { printf("%s → Ключевое слово\n", yytext); return KEYWORD; }
"word"                                          { printf("%s → Ключевое слово\n", yytext); return KEYWORD; }
"char"                                          { printf("%s → Ключевое слово\n", yytext); return KEYWORD; }
"string"                                        { printf("%s → Ключевое слово\n", yytext); return KEYWORD; }
"["                                             { printf("%s → Скобка\n", yytext); return OPERATOR; }
"]"                                             { printf("%s → Скобка\n", yytext); return OPERATOR; }
[0-9]*                                          { printf("%s → Число\n", yytext); return NUMBER; }
[a-zA-Z_][a-zA-Z0-9_]*                          { printf("%s → Идентификатор\n", yytext); return IDENTIFIER; }
[=;:,.\[\]]                                     { printf("%s → Оператор\n", yytext); return OPERATOR; }
\{([^}])*\}                                     { printf("%s → Комментарий\n", yytext); return COMMENT;}

%%

int yywrap() {
    return 1;
}
