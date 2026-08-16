# 12.2 Call Counter

def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Call #{wrapper.count}")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@count_calls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()
print(say_hi.count)