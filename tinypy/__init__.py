import sys as _sys
"""TinyPy package entry point."""

__version__ = "0.1.0"

# Errors re‑export
from .errors import LexerError, SyntaxError_, RuntimeError_  # noqa: F401


def main(argv=None):
    """Execute file or start REPL (implemented in later lectures)."""
    from .repl import repl  # lazy import to avoid circulars until implemented

    repl(argv)


if __name__ == "__main__":

    main(_sys.argv[1:])
