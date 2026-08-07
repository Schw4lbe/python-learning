"""
2. Functional Programming

lambda
map()
filter()
any()
zip()

https://www.w3schools.com/python/python_lambda.asp
https://www.w3schools.com/python/ref_func_map.asp
https://www.w3schools.com/python/ref_func_filter.asp
https://www.w3schools.com/python/ref_func_any.asp
https://www.w3schools.com/python/ref_func_zip.asp

Mini Project: User Data Processing Pipeline

Scenario:
Build a small data processing system that transforms and analyzes user data. The system should clean, combine, filter, and validate information efficiently without manually processing every item.

You have the following user data:
users = [
("Alice", 25, True),
("Bob", 17, False),
("Charlie", 32, True),
("Diana", 15, True)
]

Create a function that formats user information using lambda.
Use map() to transform the user data into a different representation.
Use filter() to select users based on conditions like age or account status.
Use zip() to combine separate data collections like names, ages, and permissions.
Use any() to check whether specific conditions exist in the processed data.

Real-world use case:
Used in data processing, analytics pipelines, API response handling, database transformations, and systems where collections of data need to be transformed or filtered efficiently.
"""


def main():
    print("Hello from 02-functional-programming!")


if __name__ == "__main__":
    main()
