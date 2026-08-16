from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Expected after all fixes:")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(add(3, 5))
print(add.__name__)
print(add.__doc__)