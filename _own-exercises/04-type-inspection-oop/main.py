"""
4. Type Inspection & OOP

isinstance()
issubclass()
super()

https://www.w3schools.com/python/ref_func_isinstance.asp
https://www.w3schools.com/python/ref_func_issubclass.asp
https://www.w3schools.com/python/ref_func_super.asp

Mini Project: Employee Management System

Scenario:
Build a small HR system that manages different employee roles.

employees = [
    Developer("Alice"),
    Manager("Bob"),
    Designer("Charlie")
]

1. INHERITANCE
   Create Employee as the base class and Developer, Manager, and Designer as specialized classes.

2. SUPER()
   Use super() to reuse Employee initialization.

3. ISSUBCLASS()
   Use issubclass() to verify that a role class inherits from Employee before adding it to the system.

4. ISINSTANCE()
   Create one processing function that receives any employee and handles it according to its role and produce role-specific output.

Goal:
Build one simple HR workflow where inheritance provides shared behavior and isinstance() determines how each employee is handled.
"""


class Employee:
    def __init__(self, name: str):
        self.name = name


class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)


class Manager:
    def __init__(self, name):
        # super().__init__(name)
        self.name = name


class Designer(Employee):
    def __init__(self, name):
        super().__init__(name)


def init_circle():
    employees: list = create_instances(
        [Developer("Alice"), Manager("Bob"), Designer("Charlie")]
    )
    handle_employees(employees)


def handle_employees(employees: list):
    for employee in employees:
        if type(employee).__name__ == "Developer" and isinstance(employee, Developer):
            print(f"{employee.name} is a Developer")
        elif type(employee).__name__ == "Designer" and isinstance(employee, Designer):
            print(f"{employee.name} is a Designer")
        elif type(employee).__name__ == "Manager" and isinstance(employee, Manager):
            print(f"{employee.name} is a Manager")


def create_instances(creation_list: list):
    print("CHECK INSTANCIATION:")
    for item in creation_list:
        if issubclass(type(item), Employee):
            print(type(item).__name__)
        else:
            print(f"{type(item).__name__} (is non Employee subclass.)")
    print("\n")

    return creation_list


def main():
    init_circle()


if __name__ == "__main__":
    main()
