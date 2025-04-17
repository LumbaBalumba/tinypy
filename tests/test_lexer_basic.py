"""Basic lexer tests for Lecture 1 subset.
Run with `pytest -q`. All should pass after students implement lexer rules.
"""

import pytest
from tinypy.errors import LexerError
from tinypy.lexer import lexer, tokens as _tokens


def tokenize(src: str):
    lexer.input(src)
    return [(tok.type, tok.value) for tok in iter(lexer.token, None)]


def test_tokens_list_contains_expected():
    expected = {
        "NUMBER",
        "IDENT",
        "PLUS",
        "MINUS",
        "STAR",
        "SLASH",
        "LPAREN",
        "RPAREN",
        "LET",
    }
    assert expected.issubset(set(_tokens))


def test_simple_expression():
    src = "1+2"
    assert tokenize(src) == [("NUMBER", 1.0), ("PLUS", "+"), ("NUMBER", 2.0)]


def test_parenthesized():
    src = "(3 - 4)"
    assert tokenize(src) == [
        ("LPAREN", "("),
        ("NUMBER", 3.0),
        ("MINUS", "-"),
        ("NUMBER", 4.0),
        ("RPAREN", ")"),
    ]


def test_identifier_and_keyword():
    src = "let var = 5 # comment"
    tokens = tokenize(src)
    types = [t[0] for t in tokens]
    assert types[0] == "LET"  # keyword recognised
    assert types[1] == "IDENT"
    assert tokens[-1] == ("NUMBER", 5.0)


def test_illegal_character():
    with pytest.raises(LexerError):
        tokenize("$")
