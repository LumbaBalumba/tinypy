"""Lexer for TinyPy — implements Lecture 1 subset.
Extend in Lecture 2 (keywords, braces, etc.)
"""

import ply.lex as lex
from .errors import LexerError

reserved = {
    "let": "LET",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "print": "PRINT",
}

tokens = [
    # Identifiers & numbers
    "NUMBER",
    "IDENT",
    # Operators
    "PLUS",
    "MINUS",
    "STAR",
    "SLASH",
    "ASSIGN",
    # Parentheses
    "LPAREN",
    "RPAREN",
    # Braces
    "LBRACE",
    "RBRACE",
] + list(reserved.values())

# --- Single‑character tokens -------------------------------------------------

t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# --- Multi-character tokens --------------------------------------------------

t_WHILE = list(reserved.keys())[3]
t_PRINT = list(reserved.keys())[4]

t_ignore = ' \t'


def t_NUMBER(t):
    r'([0-9]*[\.])?[0-9]+'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t


def t_error(t):
    raise LexerError
    t.lexer.skip(1)


def t_COMMENT(t):
    r'\#.*'
    pass


t_ignore_COMMENT = r'\#.*'

lexer = lex.lex()
