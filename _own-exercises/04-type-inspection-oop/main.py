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
Build a small employee management system using object-oriented programming. The system should handle different employee types while verifying object relationships and sharing common behavior between classes.

Create a base employee class and multiple specialized employee classes.
Use super() to reuse and extend functionality from a parent class.
Use issubclass() to verify class relationships before creating specific workflows.
Use isinstance() to check employee objects and apply different logic depending on their type.
Create a function that receives different employee objects and uses isinstance() to decide how to process each employee type.

optional:
Extend the system with additional employee roles that inherit from existing classes.

Real-world use case:
Used in enterprise software, permission systems, application frameworks, game development, and any system where different object types share common behavior but require specialized functionality.
"""


def main():
    print("Hello from 04-type-inspection-oop!")


if __name__ == "__main__":
    main()
