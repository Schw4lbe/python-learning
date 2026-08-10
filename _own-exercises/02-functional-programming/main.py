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
   Create a lambda that formats the first user as "Alice (25)".

2. MAP
   Use map() to create a formatted users list (name: __ age: __ active: __) for the admin dashboard.

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

users: list[tuple] = [
    ("Alice", 25, True),
    ("Bob", 17, False),
    ("Charlie", 32, True),
    ("Diana", 15, True),
]

users_rebuild: list[tuple] = []

names: list[str] = []
ages: list[int] = []
states: list[bool] = []


def init_admin_tool():
    lambda_reformat_example(users[0])
    users_mapped: list = list(map(mapping_function, users))
    for user in users_mapped:
        print(user)

    adults = filter(filter_adults, users)
    print("adult users: ")
    for user in adults:
        print(user)

    destructor_tuples_into_lists(users)
    rebuild_users(names, ages, states)
    contains_active_adult(users)


def contains_active_adult(users: list[tuple]):
    # any needs some sort of iterable and returns a bool
    # when any is used on dict it checks keys first, for values use param.values()
    result: bool = any(user[1] >= 18 and user[2] for user in users)

    if result:
        print("has adult active user.")


def rebuild_users(names: list[str], ages: list[int], states: list[bool]):
    global users_rebuild
    users_rebuild = list(zip(names, ages, states))
    print(users_rebuild)


def destructor_tuples_into_lists(users: list[tuple]):
    for user in users:
        names.append(user[0])
        ages.append(user[1])
        states.append(user[2])

    print(names, ages, states)


def filter_adults(user: tuple):
    if user[1] >= 18:
        return True
    else:
        return False


# LEARNING:
# iterable handed over
# type hint declares single element in iterable
# -> list of tuples -> one element = tuple
# -> hand over string -> one char also type string
# be aware to use propper formatted iterables to have fitting operations inside map function
def mapping_function(user: tuple):
    return f"name: {user[0]}, age: {user[1]}, active: {user[2]}"


def lambda_reformat_example(user: tuple):
    string: str = lambda u: f"{u[0]} ({u[1]})"
    print(string(user))


def main():
    init_admin_tool()


if __name__ == "__main__":
    main()
