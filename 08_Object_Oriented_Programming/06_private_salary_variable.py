class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Name-mangled private attribute.

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.__salary = new_salary

employee = Employee(input("Employee name: "), float(input("Salary: ")))
print("Employee:", employee.name)
print("Salary:", employee.get_salary())

new_salary = float(input("Enter revised salary: "))
employee.set_salary(new_salary)
print("Updated salary:", employee.get_salary())
