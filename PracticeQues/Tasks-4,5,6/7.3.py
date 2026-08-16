def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate(a, op, b):

    if op in operations:
        return operations[op](a, b)
    else:
        return "Unknown operator: " + op

print(calculate(10, "+", 3))
print(calculate(10, "-", 3))
print(calculate(10, "*", 3))
print(calculate(10, "/", 3))
print(calculate(10, "%", 3))