def factorial(n):
    if type(n) != int:
        raise TypeError("Expected an integer, got " + type(n).__name__)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact
print(factorial(5))
print(factorial(0))
try:
    print(factorial(-3))
except Exception as e:
    print(type(e).__name__ + ":", e)
try:
    print(factorial(2.5))
except Exception as e:
    print(type(e).__name__ + ":", e)
try:
    print(factorial("five"))
except Exception as e:
    print(type(e).__name__ + ":", e)