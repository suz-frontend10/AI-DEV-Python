def make_stack():
    stack = []
    def push(item):
        stack.append(item)
        print("Pushed", item, ". Size:", len(stack))
    def pop():
        if len(stack) == 0:
            print("Stack is empty")
        else:
            item = stack.pop()
            print("Popped", item, ". Size:", len(stack))
    def size():
        print(len(stack))
    return push, pop, size
push, pop, size = make_stack()
push(10)
push(20)
push(30)
pop()
pop()
size()
pop()
pop()