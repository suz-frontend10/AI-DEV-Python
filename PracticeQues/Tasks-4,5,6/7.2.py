def compose(f, g):

    def new_function(x):
        return f(g(x))
    return new_function

add_one = lambda x: x + 1
double = lambda x: x * 2
f = compose(add_one, double)
print(f(5))
g = compose(double, add_one)
print(g(5))