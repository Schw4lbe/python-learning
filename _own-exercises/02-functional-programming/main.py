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

Mini Project: Admin User Management Pipeline

Scenario:
You are building a small admin tool for a website.
The tool receives user data from different sources and prepares it
for an admin dashboard.

users = [
    ("Alice", 25, True),
    ("Bob", 17, False),
    ("Charlie", 32, True),
    ("Diana", 15, True)
]

1. LAMBDA
   Create a lambda that formats one user as "Alice (25)".

2. MAP
   Use map() to create the formatted user list for the admin dashboard.

3. FILTER
   Use filter() to find users who are adults AND have an active account.

4. ZIP
   Split the original data into names, ages, and account statuses,
   then use zip() to rebuild the user records.

5. ANY
   Use any() to check whether the system contains at least one
   active adult user.

Goal:
Build a small data pipeline that takes raw user data, reconstructs
it when needed, transforms it for display, filters it for an admin
operation, and checks whether a relevant user exists..
"""


def main():
    print("Hello from 02-functional-programming!")


if __name__ == "__main__":
    main()
