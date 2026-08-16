import math
is_even = lambda x: x % 2 == 0
is_leap = lambda year: (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
reverse = lambda s: s[::-1]
bigger = lambda a, b: a if a > b else b
area_circle = lambda r: math.pi * r * r
print(is_even(10))
print(is_leap(2024))
print(is_leap(1900))
print(reverse("python"))
print(bigger(10, 20))
print(area_circle(7))