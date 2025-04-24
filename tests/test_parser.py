"""Parser structure tests (Lecture 2)."""

import pytest
from tinypy.lexer import lexer
from tinypy.parser import parser
from tinypy.ast_nodes import Number, Identifier, BinOp


def parse(src):
    return parser.parse(src, lexer=lexer)


def test_ast_simple_number():
    ast = parse("42")[0]
    assert isinstance(ast, Number) and ast.value == 42


def test_ast_identifier():
    ast = parse("foo")[0]
    assert isinstance(ast, Identifier) and ast.name == "foo"


def test_ast_precedence():
    ast = parse("1+2*3")[0]
    assert isinstance(ast, BinOp) and ast.op == "+"
    assert isinstance(ast.right, BinOp) and ast.right.op == "*"


def test_ast_parentheses():
    ast = parse("(1+2)*3")[0]
    assert isinstance(ast, BinOp) and ast.op == "*"
    assert isinstance(ast.left, BinOp) and ast.left.op == "+"


"""Evaluation tests using interpreter.eval_node."""
import pytest
from tinypy.lexer import lexer
from tinypy.parser import parser
from tinypy.interpreter import eval_node


def eval_expr(expr: str, env=None):
    env = env or {}
    ast = parser.parse(expr, lexer=lexer)[0]
    return eval_node(ast, env)


def test_arithmetic():
    assert eval_expr("1+2") == 3


def test_precedence():
    assert eval_expr("1+2*3") == 7


def test_parentheses():
    assert eval_expr("(1+2)*3") == 9


def test_identifier_env():
    assert eval_expr("x+2", env={"x": 5}) == 7


def test_undefined_variable():
    with pytest.raises(Exception):
        eval_expr("y")
