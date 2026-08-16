count = 0
def counter():
    global count
    count = count + 1
    return count
print(counter())
print(counter())
print(counter())