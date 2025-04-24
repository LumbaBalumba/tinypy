"""Расширенный набор тестов парсера для Lecture 2.
   Цель — покрыть подавляющее большинство веток правил.
"""

import pytest
from tinypy.lexer import lexer
from tinypy.parser import parser
from tinypy.ast_nodes import Number, Identifier, BinOp
from tinypy.errors import SyntaxError_


def _parse_one(expr: str):
    """Parse expression and return single AST node."""
    return parser.parse(expr, lexer=lexer)[0]


def test_left_associativity_minus():
    ast = _parse_one("10 - 2 - 1")
    assert isinstance(ast, BinOp) and ast.op == "-"
    assert isinstance(ast.left, BinOp) and ast.left.op == "-"


def test_mixed_precedence_chain():
    ast = _parse_one("1 + 2 * 3 / 4 - 5")
    assert isinstance(ast, BinOp) and ast.op == "-"
    assert isinstance(ast.right, Number) and ast.right.value == 5.0
    assert ast.left.op == "+"


def test_parentheses_override():
    ast = _parse_one("(1+2) * (3+4)")
    assert isinstance(ast, BinOp) and ast.op == "*"
    assert isinstance(ast.left, BinOp) and ast.left.op == "+"
    assert isinstance(ast.right, BinOp) and ast.right.op == "+"


def test_multiple_statements_semicolon():
    prog = parser.parse("1+2; 3+4", lexer=lexer)
    assert len(prog) == 2


def test_multiple_statements_newline():
    prog = parser.parse("""1+2
3+4""", lexer=lexer)
    assert len(prog) == 2


def test_unmatched_parenthesis_error():
    with pytest.raises(SyntaxError_):
        parser.parse("1 + (2 * 3", lexer=lexer)


def test_float_and_int():
    node = _parse_one("3.0 + 4")
    assert isinstance(node.left, Number) and node.left.value == 3.0


def test_identifier_mixed():
    ast = _parse_one("a * b + c")
    assert isinstance(ast, BinOp) and ast.op == "+"
    assert isinstance(ast.left, BinOp) and ast.left.op == "*"
    assert isinstance(ast.left.left, Identifier) and ast.left.left.name == "a"
