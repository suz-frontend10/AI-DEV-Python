x = 10
def f():
    print(x)
    x = 20
f()
#Prediction: Error - UnboundLocalError
#Explanation: x is treated as local because it is assigned inside f(), but it is used before assignment.

x = 5
def f(x):
    x = 10
f(x)
print(x)
# Prediction: 5
# Explanation: The x inside f() is local, so changing it does not change the global x.

x = "global"
def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()
outer()
# Prediction: enclosing
# Explanation: inner() finds x in its enclosing function outer().

if True:
    z = 99
print(z)
# Prediction: 99
# Explanation: An if block does not create a new scope, so z is available outside it.