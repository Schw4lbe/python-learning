"""
12. Error Handling & Testing

assert
errno
dir()
eval()

https://www.w3schools.com/python/ref_keyword_assert.asp
https://www.w3schools.com/python/ref_func_dir.asp
https://www.w3schools.com/python/ref_func_eval.asp
https://www.w3schools.com/python/module_errno.asp

Mini Project: Data Import Validation System

Scenario:
Build a small data import system that reads external data, validates input, handles possible failures, and provides meaningful error information. The system should follow Python best practices for reliability and debugging.

Create a data import function that can fail due to invalid input or missing resources.
Use try, except, else, and finally to handle different execution outcomes.
Handle specific exceptions instead of catching all errors blindly.
Use raise to create custom error situations when input does not meet requirements.
Use assert to verify assumptions during development and testing.
Use errno to identify and handle operating system-related errors.
Use dir() to inspect objects and discover available methods and attributes.
Use eval() to evaluate controlled mathematical expressions safely.
Create custom exception classes for specific application errors.
Create validation tests that verify correct behavior and expected failures.

optional:
Extend the system with a logging mechanism that records errors and debugging information.

Real-world use case:
Used in data processing systems, APIs, automation tools, database applications, testing frameworks, and production software where predictable error handling and debugging are essential.
"""


def main():
    print("Hello from 12-error-handling-and-testing!")


if __name__ == "__main__":
    main()
