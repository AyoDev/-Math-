import rply

lexer = rply.LexerGenerator()
tokens = {
    'num': '\d+',
    'add': '\+',
    'sub': '\-',
    'equ': '\=',
    'var': '',
    'end': '\;',
    'fac': '\!',
    'mul': '\*',
    'var': '"[a-zA-Z][a-zA-Z0-9]*"',
    'open-paren':'\(',
    'close-paren':'\)',
    'open-brace':'\{',
    'close-brace':'\}'
}

for i in range(len(tokens)):
    lexer.add([*tokens][i], tokens[[*tokens][i]])

lexer.ignore('\s+')
lexer.ignore('\;')
lexer.ignore('\n')

l = lexer.build()

