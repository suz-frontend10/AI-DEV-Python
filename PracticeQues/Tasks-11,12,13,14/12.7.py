# 12.7 Stacking Order

def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"
print(text())        

@italic
@bold
def text2():
    return "Hello"
print(text2())