import array as arr
a = arr.array('i', [1, 4, 7, 9])
b = arr.array('i', [2, 3, 8, 10, 15])
c = arr.array('i')
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i = i + 1
    else:
        c.append(b[j])
        j = j + 1
while i < len(a):
    c.append(a[i])
    i = i + 1
while j < len(b):
    c.append(b[j])
    j = j + 1
print(c)