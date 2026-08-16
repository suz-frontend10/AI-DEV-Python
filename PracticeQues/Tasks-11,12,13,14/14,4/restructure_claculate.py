# 1. Imports
# No imports required

# 2. Constants
DEFAULT_OPERATOR = "+"

# 3. Functions
def calculator(a, b, op=DEFAULT_OPERATOR):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b
    else:
        return f"Error: unknown operator '{op}'"

# 4. Main function
def main():
    print("calculator(10, 5)      ->", calculator(10, 5))
    print('calculator(10, 5, "-") ->', calculator(10, 5, "-"))
    print('calculator(10, 5, "*") ->', calculator(10, 5, "*"))
    print('calculator(10, 0, "/") ->', calculator(10, 0, "/"))
    print('calculator(10, 5, "%") ->', calculator(10, 5, "%"))

# 5. Main guard
if __name__ == "__main__":
    main()

# Explanation:
# main() keeps the program organized by separating execution logic from reusable functions.
# It also makes the code easier to test, reuse, and import into other Python files.