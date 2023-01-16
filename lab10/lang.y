%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define YYDEBUG 1

int yylex();
void yyerror();

%}

%token INT CHAR STRING READ WRITE IF ELSE WHILE IDENTIFIER INTEGER CONSTSTRING CONSTCHAR
%token OPEN_CURLY_BRACKET CLOSED_CURLY_BRACKET OPEN_SQUARE_BRACKET CLOSED_SQUARE_BRACKET OPEN_ROUND_BRACKET CLOSED_ROUND_BRACKET
%token SEMICOLON ASSIGN PLUS MINUS MULT DIV LTE GTE EQUAL NOT_EQUAL LT GT

%%

program: OPEN_CURLY_BRACKET decllist stmtlist CLOSED_CURLY_BRACKET;
decllist: declaration | declaration decllist;
declaration: type IDENTIFIER SEMICOLON;
type: typesimple | typearray;
typesimple: INT | CHAR | STRING;
typearray: typesimple OPEN_SQUARE_BRACKET INTEGER CLOSED_SQUARE_BRACKET | typesimple OPEN_SQUARE_BRACKET IDENTIFIER CLOSED_SQUARE_BRACKET;
stmtlist: stmt | stmt stmtlist;
stmt: simplestmt | structstmt;
simplestmt: assignstmt SEMICOLON | iostmt SEMICOLON;
assignstmt: IDENTIFIER ASSIGN expression | arrayaccess ASSIGN expression;
arrayaccess: IDENTIFIER OPEN_SQUARE_BRACKET IDENTIFIER CLOSED_SQUARE_BRACKET | IDENTIFIER OPEN_SQUARE_BRACKET INT CLOSED_SQUARE_BRACKET;
expression: term PLUS expression | term MINUS expression | term;
term: factor MULT term | factor DIV term | factor;
factor: OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | IDENTIFIER | INTEGER | arrayaccess;
iostmt: READ OPEN_ROUND_BRACKET IDENTIFIER CLOSED_ROUND_BRACKET | READ OPEN_ROUND_BRACKET arrayaccess CLOSED_ROUND_BRACKET | WRITE OPEN_ROUND_BRACKET IDENTIFIER CLOSED_ROUND_BRACKET | WRITE OPEN_ROUND_BRACKET INT CLOSED_ROUND_BRACKET | WRITE OPEN_ROUND_BRACKET CONSTSTRING CLOSED_ROUND_BRACKET | WRITE OPEN_ROUND_BRACKET CONSTCHAR CLOSED_ROUND_BRACKET | WRITE OPEN_ROUND_BRACKET arrayaccess CLOSED_ROUND_BRACKET;
structstmt: ifstmt | whilestmt;
ifstmt: IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET | IF OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET ELSE OPEN_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET;
whilestmt: WHILE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET OPEN_CURLY_BRACKET stmtlist CLOSED_CURLY_BRACKET;
condition: expression relation expression;
relation: LTE | GTE | EQUAL | NOT_EQUAL | LT | GT;

%%

void yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

int main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}
