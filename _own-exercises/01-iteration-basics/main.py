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

1. ITERATOR
   Use iter() to create a log iterator so the program can inspect logs one at a time.

2. MANUAL INSPECTION
   Use next() when the user chooses "Next log" to display the next available log entry.

3. LOG GENERATOR
   Create a generator with yield that streams the logs one at a time when the user chooses "Show logs".

4. ERROR/WARNING FILTER
   Create a generator that receives the log generator and yields only WARNING and ERROR entries.

5. EVENT COUNTER
   Add a "Statistics" option that consumes the log stream and counts INFO, WARNING, and ERROR entries without storing the logs.

The program should repeatedly show a simple menu:
1 = Next log
2 = Show logs
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


def init_logs_iteration_demo():
    pass


def iteration_loop(iter):
    while True:
        try:
            print(next(iter))
        except:
            break


my_iterator = iter(logs)
iteration_loop(my_iterator)


def main():
    init_logs_iteration_demo()


if __name__ == "__main__":
    main()
