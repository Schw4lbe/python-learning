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
   Use super() to reuse Employee initialization and add role-specific data.

3. ISSUBCLASS()
   Use issubclass() to verify that a role class inherits from Employee before adding it to the system.

4. ISINSTANCE()
   Create one processing function that receives any employee and handles it according to its role.

5. WORKFLOW
   Pass all employees through the same function and produce role-specific output.

Goal:
Build one simple HR workflow where inheritance provides shared behavior and isinstance() determines how each employee is handled.
"""


def main():
    print("Hello from 04-type-inspection-oop!")


if __name__ == "__main__":
    main()
