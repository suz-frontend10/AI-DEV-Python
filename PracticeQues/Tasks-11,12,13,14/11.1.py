def make_power(power):
    def calculate(num):
        return num**power
    return calculate
square=make_power(2)
cube=make_power(3)
print(square(5))
print(cube(3))
print(make_power(4)(2))