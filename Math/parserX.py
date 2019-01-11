import rply
from Math import *


parser = rply.ParserGenerator(['num',
    'add',
    'sub',
    #'equ',
    #'end',
    'fac',
    'mul',
    'div',
    'open-paren',
    'close-paren'
    #'open-braces',
    #'close-brace'
    ],

    precedence=[
        ('left', ['add', 'sub']),
        ('left', ['mul', 'div'])
    ]
)

@parser.production('expression : num')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))

@parser.production('expression : open-paren expression close-paren')
def expression_parens(p):
    return p[1]

@parser.production('expression : expression fac')
def symbol(p):
    left = p[0]
    if p[1].gettokentype() == 'fac':
        return Factorial(left)

@parser.production('expression : expression add expression')
@parser.production('expression : expression sub expression')
@parser.production('expression : expression mul expression')
@parser.production('expression : expression div expression')
def operators(p):
    left = p[0]
    right = p[2] or None
    if p[1].gettokentype() == 'add':
        return Add(left, right)
    elif p[1].gettokentype() == 'sub':
        return Sub(left, right)
    elif p[1].gettokentype() == 'mul':
        return Mul(left, right)
    elif p[1].gettokentype() == 'div':
        return Div(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')

parser = parser.build()