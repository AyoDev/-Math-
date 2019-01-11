from lexerX import *
from parserX import *

f=open("test.math",'r')
f= f.read()
print(parser.parse(l.lex(f)).eval())

