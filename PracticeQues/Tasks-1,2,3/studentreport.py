def report(name, *marks, **details):
    print("Student :", name)
    print("Section :", details["section"])
    print("Year    :", details["year"])
    print("Marks   :", end=" ")

    for mark in marks:
        print(mark, end=", ")
    print()

    total = sum(marks)
    average = total / len(marks)

    print("Total   :", total)
    print("Average :", average)
    if average >= 40:
        print("Result  : PASS")
    else:
        print("Result  : FAIL")

report("Priya", 85, 92, 78, 90, section="A", year=2)