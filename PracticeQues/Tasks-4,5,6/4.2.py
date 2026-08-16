def trailing_zeros(n):
    count = 0
    while n > 0:
        n = n // 5
        count = count + n
    return count
print(trailing_zeros(10))
print(trailing_zeros(25))
print(trailing_zeros(100))
print(trailing_zeros(1000))