 
grade = lambda marks: (
    "A" if marks >= 90 else
    "B" if marks >= 75 else
    "C" if marks >= 60 else
    "D" if marks >= 40 else
    "F"
)

print(grade(95))
print(grade(82))
print(grade(65))
print(grade(45))
print(grade(20))