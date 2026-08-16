def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def nPr(n, r):
    if r > n:
        return "Error: r cannot be greater than n"
    return factorial(n) // factorial(n - r)


def nCr(n, r):
    if r > n:
        return "Error: r cannot be greater than n"
    return factorial(n) // (factorial(r) * factorial(n - r))
print("nPr(5,2) =", nPr(5, 2))
print("nCr(5,2) =", nCr(5, 2))
print("nCr(15,11) =", nCr(15, 11))
print("nCr(52,5) =", nCr(52, 5))
print("nCr(5,7) =", nCr(5, 7))