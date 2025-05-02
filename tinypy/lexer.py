"""Lexer for TinyPy — implements Lecture 1 subset.
Extend in Lecture 2 (keywords, braces, etc.)
"""

import ply.lex as lex
from errors import LexerError

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
] + list(reserved.values())

# --- Single‑character tokens -------------------------------------------------

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_STAR   = r'\*'
t_SLASH  = r'/'
t_ASSIGN = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'

# --- Multi-character tokens --------------------------------------------------

# Your code here
def t_NUMBER(t):
    r'-?\d+\[.,]\d+?'
    t.value = float(t.value)
    return t

def t_IDENT(t):
    r'[a-zA-Z][a-zA-Z]*'
    t.type = reserved.get(t.value, 'IDENT')
    return t

def t_error(t):
    raise LexerError(f"Invalid token '{t.value}' at line {t.lineno}")

lexer = lex.lex()
