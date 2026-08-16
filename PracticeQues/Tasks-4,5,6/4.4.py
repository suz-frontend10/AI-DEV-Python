import math
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
e = 0
for i in range(20):
    e = e + (1 / factorial(i))
print("Terms used :", 20)
print("Computed e :", e)
print("math.e     :", math.e)
print("Difference :", abs(math.e - e))