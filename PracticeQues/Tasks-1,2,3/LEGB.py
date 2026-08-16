x = "I am global"
def outer():
    x = "I am enclosing"
    
    def inner():
        x = "I am local"
        print("Local     :", x)
        print("Enclosing :", "I am enclosing")
        print("Global    :", "I am global")
        print("Built-in  :", len("hello"))
    inner()

outer()