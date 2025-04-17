"""REPL placeholder — completed in Lecture 6."""

from __future__ import annotations
import sys
from .lexer import lexer
from .parser import parser
from .interpreter import eval_node


def repl(argv=None):
    print("TinyPy REPL (in development). Ctrl+D to exit.")
    env = {}
    try:
        while True:
            line = input(">> ")
            lexer.input(line)
            ast_list = parser.parse(lexer=lexer)
            for ast in ast_list:
                result = eval_node(ast, env)
                if result is not None:
                    print(result)
    except EOFError:
        print()
        sys.exit(0)
