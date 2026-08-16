def calculator(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Error: cannot divide by zero"
    else:
        return "Error: unknown operator '" + op + "'"
print(calculator(10, 5))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 0, "/"))
print(calculator(10, 5, "%"))