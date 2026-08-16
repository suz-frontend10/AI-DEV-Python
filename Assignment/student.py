class Student:
    """Student Result Management System"""

    # Static Attributes
    college_name = "Aditya Institute of Technology"
    total_students = 0
    PASS_MARK = 35
    MAX_SUBJECTS = 5

    def __init__(self, roll_number, name, branch):
        """Constructor to initialize student details"""

        self.name = name                 # Public
        self._roll_number = roll_number  # Protected
        self._branch = branch            # Protected
        self.__marks = {}                # Private

        Student.total_students += 1

    @property
    def roll_number(self):
        """Returns roll number (Read-only)"""
        return self._roll_number

    @property
    def average(self):
        """Returns average marks"""

        if len(self.__marks) == 0:
            return 0.0

        return sum(self.__marks.values()) / len(self.__marks)

    @property
    def grade(self):
        """Returns grade based on average"""

        avg = self.average

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= Student.PASS_MARK:
            return "C"
        else:
            return "F"

    def add_marks(self, subject, mark):
        """Adds marks for a subject"""

        if not isinstance(mark, (int, float)):
            raise TypeError("Mark must be a number")

        if mark < 0 or mark > 100:
            raise ValueError(f"Mark must be between 0 and 100, got {mark}")

        if len(self.__marks) >= Student.MAX_SUBJECTS:
            raise ValueError("Maximum subjects exceeded")

        self.__marks[subject] = mark

    def get_marks(self):
        """Returns a copy of marks"""

        return dict(self.__marks)

    def has_passed(self):
        """Checks whether student has passed"""

        if len(self.__marks) == 0:
            return False

        for mark in self.__marks.values():
            if mark < Student.PASS_MARK:
                return False

        return True

    def change_branch(self, new_branch):
        """Changes student branch"""

        old_branch = self._branch
        self._branch = new_branch

        return f"{self.name} moved from {old_branch} to {new_branch}"

    @classmethod
    def get_total_students(cls):
        """Returns total students"""

        return cls.total_students

    @staticmethod
    def is_valid_mark(mark):
        """Checks whether mark is valid"""

        return isinstance(mark, (int, float)) and 0 <= mark <= 100

    def __str__(self):
        """Returns student details"""

        return (f"Student[{self._roll_number}] "
                f"{self.name} | "
                f"{self._branch} | "
                f"Avg: {self.average:.2f} | "
                f"Grade: {self.grade}")

def main():
    print(f"{'College':<25}: {Student.college_name}")

    s1 = Student(101, "Pragnya Sree", "CSE")
    s2 = Student(102, "Prakash", "ECE")

    s1.add_marks("Maths", 92)
    s1.add_marks("Physics", 88)
    s1.add_marks("Chemistry", 76)

    s2.add_marks("Maths", 40)
    s2.add_marks("Physics", 35)

    print(f"{'Total students':<25}: {Student.get_total_students()}")

    print(s1)
    print(s2)

    print(f"{'s1 marks':<25}: {s1.get_marks()}")
    print(f"{'s1 passed':<25}: {s1.has_passed()}")
    print(f"{'s2 passed':<25}: {s2.has_passed()}")

    print(f"{'Branch Change':<25}: {s1.change_branch('IT')}")

    print(f"{'is_valid_mark(105)':<25}: {Student.is_valid_mark(105)}")

    try:
        s1.add_marks("English", 150)
    except Exception as e:
        print(f"{'Blocked (mark 150)':<25}: {e}")

    try:
        s1.average = 99
    except Exception as e:
        print(f"{'Blocked (write average)':<25}: {e}")

    try:
        s1.roll_number = 200
    except Exception as e:
        print(f"{'Blocked (write roll)':<25}: {e}")

    print(f"{'protected':<25}: {s1._branch}")
    print(f"{'private':<25}: {s1._Student__marks}")


if __name__ == "__main__":
    main()