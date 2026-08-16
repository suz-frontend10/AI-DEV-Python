def once(func):
    result = None
    called = False
    def wrapper():
        nonlocal result, called
        if not called:
            result = func()
            called = True
        return result
    return wrapper
def expensive_setup():
    print("Running setup...")
    return "DONE"
setup = once(expensive_setup)
print(setup())
print(setup())
print(setup())