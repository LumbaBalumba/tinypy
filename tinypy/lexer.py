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
] + list(reserved.values())

# --- Single‑character tokens -------------------------------------------------

# Your code here

# --- Multi-character tokens --------------------------------------------------

# Your code here

lexer = lex.lex()
