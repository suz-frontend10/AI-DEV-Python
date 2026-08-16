class Employee:
    """Employee Management System"""

    # Static Attributes
    company_name = "TechCorp Solutions"
    total_employees = 0
    pf_percentage = 12.0
    MIN_SALARY = 15000
    MAX_SALARY = 500000

    def __init__(self, emp_id, name, department, salary):
        """Constructor to initialize employee details"""

        self.name = name  # Public
        self._emp_id = emp_id
        self._department = department  # Protected
        self.__pan_number = "ABCDE1234F"  # Private

        self.salary = salary

        Employee.total_employees += 1

    @property
    def emp_id(self):
        """Returns employee ID (Read-only)"""
        return self._emp_id

    # Getter
    @property
    def salary(self):
        """Returns employee salary"""
        return self._salary

    # Setter
    @salary.setter
    def salary(self, value):
        """Validates and sets employee salary"""

        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")

        if value < Employee.MIN_SALARY or value > Employee.MAX_SALARY:
            raise ValueError(
                f"Salary must be between {Employee.MIN_SALARY} and {Employee.MAX_SALARY}, got {value}"
            )

        self._salary = value

    def apply_hike(self, percent):
        """Increase salary by a percentage"""

        if percent < 0 or percent > 50:
            raise ValueError("Hike percentage must be between 0 and 50")

        self._salary += self._salary * percent / 100
        return self._salary

    def calculate_pf(self):
        """Calculates Provident Fund"""

        return self._salary * Employee.pf_percentage / 100

    def transfer_department(self, new_dept):
        """Transfers employee to another department"""

        old_dept = self._department
        self._department = new_dept

        return f"{self.name} moved from {old_dept} to {new_dept}"

    @classmethod
    def get_total_employees(cls):
        """Returns total number of employees"""
        return cls.total_employees

    @staticmethod
    def is_valid_salary(amount):
        """Checks whether salary is valid"""

        if not isinstance(amount, (int, float)):
            return False

        return Employee.MIN_SALARY <= amount <= Employee.MAX_SALARY

    def __str__(self):  # string
        """Returns employee details."""

        return (f"Employee[{self._emp_id}] {self.name} | "
                f"{self._department} | Rs.{self._salary:,.2f}")


def main():

    print(f"{'Company':<20}: {Employee.company_name}")
    print(f"{'Employees before':<20}: {Employee.get_total_employees()}")

    e1 = Employee(101, "Pragnya Sree", "Engineering", 60000)
    e2 = Employee(102, "Prakash", "Finance", 75000)

    print(e1)
    print(e2)

    print(f"{'Employees after':<20}: {Employee.get_total_employees()}")

    print(f"{'PF for e1':<20}: {e1.calculate_pf()}")

    print(f"{'After 10% hike':<20}: {e1.apply_hike(10)}")

    print(e1.transfer_department("Data Science"))

    print(f"{'is_valid_salary(9000)':<20}: {Employee.is_valid_salary(9000)}")

    try:
        e1.salary = 5000
    except Exception as e:
        print(f"{'Blocked':<20}: {e}")

    try:
        e1.emp_id = 201
    except Exception as e:
        print(f"{'Blocked':<20}: {e}")

    print(f"{'protected':<20}: {e1._department}")
    print(f"{'private':<20}: {e1._Employee__pan_number}")


if __name__ == "__main__":
    main()