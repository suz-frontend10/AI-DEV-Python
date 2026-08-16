def apply_twice(func, value):
    return func(func(value))
print(apply_twice(lambda x: x + 3, 10))
print(apply_twice(lambda x: x * 2, 5))
print(apply_twice(str.upper, "hi"))