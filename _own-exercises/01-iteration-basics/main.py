"""
## 1. Iteration Basics

iter()
next()
yield
Generators

https://www.w3schools.com/python/python_iterators.asp
https://www.w3schools.com/python/python_generators.asp

PRACTICAL EXERCISE: SERVER LOG MONITOR

logs = [
    "INFO: User logged in",
    "WARNING: Disk space low",
    "INFO: File uploaded",
    "ERROR: Database connection failed",
    "INFO: User logged out",
    "ERROR: Payment service unavailable",
]

1. LOG GENERATOR
   Create a generator with yield that streams the logs one at a time when the user chooses "Show logs".

2. ITERATOR
   Use iter() to create a log iterator so the program can inspect logs one at a time.

3. MANUAL INSPECTION
   Use next() when the user chooses "Next log" to display the next available log entry.

4. ERROR/WARNING FILTER
   Create a function that receives the log generator and yields only WARNING and ERROR entries.

5. EVENT COUNTER
   Add a "Statistics" option that consumes the log stream and counts INFO, WARNING, and ERROR entries without storing the logs.

The program should repeatedly show a simple menu:
1 = Show logs
2 = Next log
3 = Show warnings/errors
4 = Show statistics
5 = Exit

Goal: build one tiny interactive log monitor where every technique has a distinct job.
"""

logs: list[str] = [
    "INFO: User logged in",
    "WARNING: Disk space low",
    "INFO: File uploaded",
    "ERROR: Database connection failed",
    "INFO: User logged out",
    "ERROR: Payment service unavailable",
]


input_string: str = """
1 = Show logs
2 = Next log
3 = Show warnings/errors
4 = Show statistics
5 = Exit
"""


def init_logs_iteration_demo():
    try:
        user_menu_select()
    except KeyboardInterrupt:
        print("exit.")


def user_menu_select():
    user_input: str = input(input_string)
    while True:
        if user_input == "1":
            show_logs()
            break
        elif user_input == "2":
            show_single_log()
            break
        elif user_input == "3":
            show_critical()
            break
        elif user_input == "4":
            create_statistic()
            break
        elif user_input == "5":
            exit()


def create_statistic():
    logs = get_logs()
    info_count: int = 0
    error_count: int = 0
    warning_count: int = 0

    for log in logs:
        if log[0:3] == "INF":
            info_count += 1
        elif log[0:3] == "ERR":
            error_count += 1
        elif log[0:3] == "WAR":
            warning_count += 1

    print(
        f"INFO COUNT: {info_count}\nERROR COUNT: {error_count}\nWARNING COUNT: {warning_count}"
    )

    user_menu_select()


def show_critical():
    logs = get_logs()
    for log in logs:
        if log[0:3] == "INF" or (log[0:3] == "ERR"):
            print(log)
        else:
            continue

    user_menu_select()


def show_single_log():
    my_iterator = iter(logs)  # manually creating iterator object
    iteration_loop(my_iterator)


def iteration_loop(iter):
    print("Press Enter for next log entry or e to exit.")
    while True:
        try:
            user_input: str = input()
            if user_input == "":
                print(next(iter))
                continue
            elif user_input == "e":
                user_menu_select()
                break
            else:
                print("invalid input.")
                continue

        except StopIteration:
            print("NO FURTHER ENTRIES FOUND.")
            user_menu_select()
            break


def show_logs():
    print("\nLOG DISPLAY:")
    for log in get_logs():
        print(log)

    user_menu_select()


def get_logs():
    for log in logs:
        yield log


def main():
    init_logs_iteration_demo()


if __name__ == "__main__":
    main()
