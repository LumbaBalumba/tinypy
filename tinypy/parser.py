"""PLY parser."""

from __future__ import annotations
import ply.yacc as yacc
from .ast_nodes import Number, Identifier, BinOp
from .errors import SyntaxError_
from .lexer import tokens


precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "STAR", "SLASH"),
)


def p_expr_multipleops(p):
    """expr : expr SEMI expr"""
    p[0] = [p[1], p[3]]


def p_expr_number(p):
    """expr : NUMBER"""
    p[0] = Number(p[1])


def p_expr_identifier(p):
    """expr : IDENT"""
    p[0] = Identifier(p[1])


def p_expr_binop(p):
    """expr : expr PLUS expr
    | expr MINUS expr
    | expr STAR expr
    | expr SLASH expr"""
    p[0] = BinOp(p[2], p[1], p[3])


def p_expr_group(p):
    """expr : LPAREN expr RPAREN"""
    p[0] = p[2]


def p_error(p):
    raise SyntaxError_("Syntax error")


parser = yacc.yacc()
