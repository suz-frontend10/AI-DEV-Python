def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact
print(" n |                        n! | digits")
print("----+---------------------------+-------")
for n in range(16):

    fact = factorial(n)
    digits = len(str(fact))
    print(f"{n:3} | {fact:25,} | {digits:6}")