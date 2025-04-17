class TinyPyError(Exception):
    """Base class for TinyPy errors."""


class LexerError(TinyPyError):
    pass


class SyntaxError_(TinyPyError):
    pass


class RuntimeError_(TinyPyError):
    pass
