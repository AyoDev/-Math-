
class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class Variable():
    def __init__(self, name, value, tag=''):
        self.name = name
        self.tag = tag
    
    def Tag(self):
        return self.tag

    def Name(self):
        return self.name

    def eval(self):
        return self.value

class Symbol():
    def __init__(self, left):
        self.left = left

class Operator():
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(Operator):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(Operator):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Mul(Operator):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Div(Operator):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Factorial(Symbol):
    def factorial(self,n):
        num = 1
        while n >= 1:
            num = num * n
            n = n - 1
        return num
    def eval(self):
        return self.factorial(self.left.eval())
