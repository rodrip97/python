def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2 

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operatrions = {
    '+' : add,
    '-' : sub,
    '*' : multiply,
    '/' : divide,
}

num1 = input("What's the first number?:")