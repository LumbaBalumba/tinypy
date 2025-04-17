# TinyPy

Educational interpreter written in Python 3.11 during a six‑lecture high‑school course.

```bash
python -m tinypy examples/hello.tny   # run file (to be implemented)
python -m tinypy                      # REPL (to be implemented)
```

- **Lecture 1** — lexer (`tinypy/lexer.py`)
- **Lecture 2** — PLY lexer polish
- **Lecture 3** — parser + AST (`tinypy/parser.py`, `tinypy/ast_nodes.py`)
- **Lecture 4** — evaluator (`tinypy/interpreter.py`)
- **Lecture 5** — language features (if/while/functions)
- **Lecture 6** — REPL and error handling

## Developer setup

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
pytest -q            # run unit‑tests
flake8               # style + spell‑check (codespell)
```

CI runs the same commands via GitHub Actions (see `.github/workflows/ci.yml`).
