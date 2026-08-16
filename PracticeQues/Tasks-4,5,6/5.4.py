count = 0
def hanoi(n, source, helper, destination):
    global count
    if n == 1:
        count = count + 1
        print("Move disk 1:", source, "->", destination)
        return
    hanoi(n - 1, source, destination, helper)
    count = count + 1
    print("Move disk", n, ":", source, "->", destination)
    hanoi(n - 1, helper, source, destination)
hanoi(3, "A", "B", "C")
print("Total moves:", count)