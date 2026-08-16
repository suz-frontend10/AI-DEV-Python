def factorial(n, depth=0):
    print("|  " * depth + f"factorial({n}) called")
    if n == 1:
        print("|  " * depth + "BASE CASE -> returning 1")
        return 1
    print("|  " * depth + f"needs {n} * factorial({n-1}) ... waiting")
    answer = factorial(n - 1, depth + 1)
    result = n * answer
    print("|  " * depth + f"got {answer}, so {n} * {answer} = {result}")
    return result
ans = factorial(4)
print("\nFinal answer:", ans)