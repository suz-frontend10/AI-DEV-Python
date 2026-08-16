funcs = []
for i in range(3):
    funcs.append(lambda: i * 10)

print([f() for f in funcs])
# Bug Explanation:
# The lambda does not store the value of i immediately.
# It remembers the variable i itself.
# After the loop ends, i becomes 2.
# So every lambda uses i = 2, giving [20, 20, 20].

#fixed code
funcs = []

for i in range(3):
    funcs.append(lambda i=i: i * 10)

print([f() for f in funcs])