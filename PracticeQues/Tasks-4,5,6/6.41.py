#fast power
def fast_power(x, n):
    if n == 0:
        return 1
    half = fast_power(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half
print(fast_power(2, 30))