"""Lexer for TinyPy — implements Lecture 1 subset.
Extend in Lecture 2 (keywords, braces, etc.)
"""

import ply.lex as lex
from .errors import LexerError

reserved = {
    "let": "LET",
    # future: "if": "IF", "else": "ELSE", "while": "WHILE", "print": "PRINT",
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
    "LBRACE",
    "RBRACE",
    # Multiple symbols
    "EQUALITY",
    "NOTEQUAL",
    "LESSTHAN",
    "GREATERTHAN",
    "LESSEQUAL",
    "GREATEREQUAL"
] + list(reserved.values())

# --- Single‑character tokens -------------------------------------------------

t_LET = r'let'
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALITY = r'=='
t_NOTEQUAL = r'!='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='


# --- Multi-character tokens --------------------------------------------------

# Your code here

def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_lbrace(t):
    r'\{'
    t.type = '{'
    return t

def t_rbrace(t):
    r'\}'
    t.type = '}'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

def t_error(t):
    raise LexerError(f"Invalid token '{t.value}' at line {t.lineno}")

t_ignore = ' \t'
t_ignore_COMMENT = r'\#.*'

lexer = lex.lex()
