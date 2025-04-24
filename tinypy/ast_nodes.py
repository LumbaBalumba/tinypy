"""AST node classes (placeholders until Lecture 2)."""

from __future__ import annotations
from dataclasses import dataclass


class Node:
    pass


@dataclass
class Number(Node):
    value: float


@dataclass
class Identifier(Node):
    name: str


@dataclass
class BinOp(Node):
    op: str
    left: Node
    right: Node
