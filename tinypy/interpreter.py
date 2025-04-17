"""Evaluator — skeleton for Lecture 4."""

from __future__ import annotations
from typing import Any, Dict
from .ast_nodes import Number, Identifier, BinOp, Node
from .errors import RuntimeError_


def eval_node(node: Node, env: Dict[str, Any]):
    if isinstance(node, Number):
        return node.value
    if isinstance(node, Identifier):
        if node.name in env:
            return env[node.name]
        raise RuntimeError_(f"Undefined variable '{node.name}'")
    if isinstance(node, BinOp):
        left = eval_node(node.left, env)
        right = eval_node(node.right, env)
        if node.op == "+":
            return left + right
        if node.op == "-":
            return left - right
        if node.op == "*":
            return left * right
        if node.op == "/":
            return left / right
        raise RuntimeError_(f"Unknown operator {node.op}")
    raise RuntimeError_("Unsupported node type")
