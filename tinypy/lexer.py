import ply.lex as lex


reserved = {
   'if' : 'IF',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'let': 'LET',
   'true': 'TRUE',
   'false': 'FALSE',
   'print': 'PRINT'
}

rules = [
    (r"[><=]{1, 2}", 'OPERATOR')
    (r"\d+", "NUMBER"), (r"\d.\d+", "FLOAT"),
    (r"[A-Za-z_][A-Za-z0-9_]*", "IDENT"),
    (r"\+", "PLUS"), (r"-", "MINUS"),
    (r"\*", "TIMES"), (r"/", "SLASH"),
    (r"\(", "LPAREN"), (r"\)", "RPAREN"),
    (r"//", "DIVIDE"), (r"# [0-9A-Za-z\s]*`", "COMMENT")
    ]# comm:  # {typing...} `tokens = list(reserved.values()) + dict(rules.values)

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d.\d+'
    t.value = float(t.value)
    return t

def t_OPERATOR(t):
    r'[><=]{1, 2}'
    if t.value == '==':

    elif t.value == '>=':

    elif t.value == '<=':

    elif t.value == '<>':
        raise SyntaxError('Внимание: недопустимая последовательность символов.')


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()