"""Extended lexer tests to reach 16 total cases."""

import pytest
from tinypy.lexer import lexer


def tokenize(src):
    lexer.input(src)
    return list(iter(lexer.token, None))


# ---- existing basic cases covered in test_lexer_basic.py (5 tests) ----

# 6. whitespace robustness


def test_whitespace_and_tabs():
    toks = tokenize("  7   -  3	+2")
    types_vals = [(t.type, t.value) for t in toks]
    assert types_vals == [
        ("NUMBER", 7.0),
        ("MINUS", "-"),
        ("NUMBER", 3.0),
        ("PLUS", "+"),
        ("NUMBER", 2.0),
    ]


# 7. floating numbers support


def test_float_number():
    toks = tokenize("3.14 * 2")
    assert (toks[0].type, toks[0].value) == ("NUMBER", 3.14)
    assert toks[1].type == "STAR"


# 8. newline increments lineno


def test_newline_lineno():
    toks = tokenize(
        """1+2
    3"""
    )
    # last token should be lineno 2
    assert toks[-1].lineno == 2


# 9. comments are skipped


def test_comment_skipped():
    toks = tokenize(
        """1 # comment
        + 2"""
    )
    assert [t.type for t in toks] == ["NUMBER", "PLUS", "NUMBER"]


# 10. identifier containing digits (but not starting with digit)


def test_identifier_with_digits():
    toks = tokenize("foo123 + 1")
    assert (toks[0].type, toks[0].value) == ("IDENT", "foo123")


# 11. reserved word `let` vs `lets`


def test_reserved_vs_ident():
    toks = tokenize("let lets")
    assert [t.type for t in toks][:2] == ["LET", "IDENT"]


# 12. integer literal stored as float


def test_integer_is_float():
    tok = tokenize("42")[0]
    assert isinstance(tok.value, float) and tok.value == 42.0


# 13. order of tokens and operators


def test_operator_sequence():
    types = [t.type for t in tokenize("1/2*3")]
    assert types == ["NUMBER", "SLASH", "NUMBER", "STAR", "NUMBER"]


# 14. multiple lines track lexpos increasing


def test_lexpos_monotonic():
    toks = tokenize("a + 1")
    lexpos_values = [t.lexpos for t in toks]
    assert lexpos_values == sorted(lexpos_values)


# 15. parentheses nesting


def test_nested_parentheses():
    types = [t.type for t in tokenize("((1))")]  # two LPAREN, NUMBER, two RPAREN
    assert types == ["LPAREN", "LPAREN", "NUMBER", "RPAREN", "RPAREN"]


# 16. illegal character still raises error (edge case)


def test_illegal_character_dollar():
    with pytest.raises(Exception):
        tokenize("$1 + 2")
