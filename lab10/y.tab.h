/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    INT = 258,
    CHAR = 259,
    STRING = 260,
    READ = 261,
    WRITE = 262,
    IF = 263,
    ELSE = 264,
    WHILE = 265,
    IDENTIFIER = 266,
    INTEGER = 267,
    CONSTSTRING = 268,
    CONSTCHAR = 269,
    OPEN_CURLY_BRACKET = 270,
    CLOSED_CURLY_BRACKET = 271,
    OPEN_SQUARE_BRACKET = 272,
    CLOSED_SQUARE_BRACKET = 273,
    OPEN_ROUND_BRACKET = 274,
    CLOSED_ROUND_BRACKET = 275,
    SEMICOLON = 276,
    ASSIGN = 277,
    PLUS = 278,
    MINUS = 279,
    MULT = 280,
    DIV = 281,
    LTE = 282,
    GTE = 283,
    EQUAL = 284,
    NOT_EQUAL = 285,
    LT = 286,
    GT = 287
  };
#endif
/* Tokens.  */
#define INT 258
#define CHAR 259
#define STRING 260
#define READ 261
#define WRITE 262
#define IF 263
#define ELSE 264
#define WHILE 265
#define IDENTIFIER 266
#define INTEGER 267
#define CONSTSTRING 268
#define CONSTCHAR 269
#define OPEN_CURLY_BRACKET 270
#define CLOSED_CURLY_BRACKET 271
#define OPEN_SQUARE_BRACKET 272
#define CLOSED_SQUARE_BRACKET 273
#define OPEN_ROUND_BRACKET 274
#define CLOSED_ROUND_BRACKET 275
#define SEMICOLON 276
#define ASSIGN 277
#define PLUS 278
#define MINUS 279
#define MULT 280
#define DIV 281
#define LTE 282
#define GTE 283
#define EQUAL 284
#define NOT_EQUAL 285
#define LT 286
#define GT 287

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
