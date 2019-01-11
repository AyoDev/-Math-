import rply

lexer = rply.LexerGenerator()
tokens = {
    'num': '\d+',
    'add': '\+',
    'sub': '\-',
    'equ': '\=',
    'end': '\;',
    'fac': '\!',
    'mul': '\*',
    'open-paren':'\(',
    'close-paren':'\)',
    'open-brace':'\{',
    'close-brace':'\}',
    'newline':';',
    'newline':'\n'
}

for i in range(len(tokens)):
    lexer.add([*tokens][i], tokens[[*tokens][i]])

lexer.ignore('\s+')


l = lexer.build()

