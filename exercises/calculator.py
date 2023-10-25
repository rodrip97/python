def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2 

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operations = {
    '+' : add,
    '-' : sub,
    '*' : multiply,
    '/' : divide,
}

num1 = float(input("What's the first number?: "))
operation = input('Please select the operation you would like to perform: + , - , / , *: ')
num2 = float(input("What's the second number?: "))

if operation in operations:
    result = operations[operation](num1, num2)
    print('Your result is:', result)
else:
    print('Invalid operation. Please enter +, -, *, or /')
