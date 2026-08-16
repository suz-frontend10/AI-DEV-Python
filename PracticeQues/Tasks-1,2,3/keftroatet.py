import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6, 7])
k = 3
for i in range(k):
    x = a.pop(0)
    a.append(x)
print(a)