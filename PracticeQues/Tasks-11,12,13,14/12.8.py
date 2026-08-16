# 12.8 Cache the Fibonacci

import time
from functools import wraps, lru_cache

# 1. WITHOUT CACHE

def fib_without_cache(n):
    if n <= 1:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)


start = time.perf_counter()
result = fib_without_cache(35)
end = time.perf_counter()

print("Without cache:")
print("fib(35) =", result)
print(f"Time = {end - start:.4f} seconds")

# 2. OUR OWN @cache DECORATOR

def cache(func):
    memory = {}

    @wraps(func)
    def wrapper(*args):
        if args in memory:
            return memory[args]
        result = func(*args)
        memory[args] = result
        return result
    return wrapper

@cache
def fib_with_cache(n):
    if n <= 1:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)

start = time.perf_counter()
result = fib_with_cache(35)
end = time.perf_counter()

print("\nWith our @cache:")
print("fib(35) =", result)
print(f"Time = {end - start:.4f} seconds")

print("fib(100) =", fib_with_cache(100))

# 3. USING functools.lru_cache

@lru_cache(maxsize=None)
def fib_lru(n):
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)

start = time.perf_counter()
result = fib_lru(35)
end = time.perf_counter()

print("\nWith @lru_cache:")
print("fib(35) =", result)
print(f"Time = {end - start:.4f} seconds")

print("fib(100) =", fib_lru(100))