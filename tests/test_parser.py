"""Parser structure tests (Lecture 2)."""


from tinypy.lexer import lexer
from tinypy.parser import parser
from tinypy.ast_nodes import Number, Identifier, BinOp


def parse(src):
    return parser.parse(src, lexer=lexer)


def test_ast_simple_number():
    ast = parse("42")
    assert isinstance(ast, Number) and ast.value == 42


def test_ast_identifier():
    ast = parse("foo")
    assert isinstance(ast, Identifier) and ast.name == "foo"


def test_ast_precedence():
    ast = parse("1+2*3")
    assert isinstance(ast, BinOp) and ast.op == "+"
    assert isinstance(ast.right, BinOp) and ast.right.op == "*"


def test_ast_parentheses():
    ast = parse("(1+2)*3")
    assert isinstance(ast, BinOp) and ast.op == "*"
    assert isinstance(ast.left, BinOp) and ast.left.op == "+"
