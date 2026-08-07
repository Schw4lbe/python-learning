"""
13. Decorators

Decorators
@dataclass
@property
@classmethod
@staticmethod

https://www.w3schools.com/python/python_decorators.asp

Mini Project: Employee Management System with Data Validation

Scenario:
Build an employee management system using classes where decorators improve code structure, reduce boilerplate, and control access to object data.

Create an employee class that stores information like name, role, salary, and employee ID.
Use @dataclass to simplify class creation and automatically generate common methods.
Use @property to create controlled access to class attributes.
Use a property setter to validate values before updating object data.
Use @classmethod to create alternative object creation methods.
Use @staticmethod to create helper functions that belong to the class but do not require object data.
Create methods that demonstrate how decorators can extend or modify class behavior.
Compare a normal class implementation with a decorator-based implementation.

optional:
Create a reusable decorator that logs when methods are called.

Real-world use case:
Used in application models, data structures, APIs, frameworks, validation systems, and professional Python codebases where classes need clean interfaces and controlled behavior.
"""


def main():
    print("Hello from 13-decorators!")


if __name__ == "__main__":
    main()
