def make_averager():
    total = 0
    count = 0
    def average(number):
        nonlocal total, count
        total += number
        count += 1
        return total / count
    return average
avg = make_averager()
print(avg(10))
print(avg(20))
print(avg(30))
print(avg(40))