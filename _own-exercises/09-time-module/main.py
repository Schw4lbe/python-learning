"""
9. Time Module

time Module
datetime Module
date Objects
time Objects
datetime Objects
timedelta
Timestamp Conversion
Time Formatting

https://www.w3schools.com/python/python_datetime.asp
https://www.w3schools.com/python/module_time.asp

Mini Project: Task Execution Tracker

Scenario:
Build a small tool that runs three predefined tasks one after another,
measures their execution time, and produces a readable report.

tasks = [
    ("Backup database", 2),
    ("Process files", 1),
    ("Send report", 3)
]

1. RUN TASKS
   Loop through the tasks and use time.sleep(duration) to simulate each task running.

2. RECORD START
   Use datetime.now() immediately before each task starts to record its start time.

3. MEASURE EXECUTION
   Use time.time() before and after time.sleep() to calculate the actual execution duration.

4. RECORD COMPLETION
   Use datetime.now() immediately after the task finishes to record its completion time.

5. TIMESTAMP CONVERSION
   Convert a completion datetime to a Unix timestamp and convert it back to a datetime.

6. FORMAT & PARSE
   Use strftime() to create a readable completion time, then use strptime() to convert it back.

7. REPORT
   Display each task with its start time, completion time, and execution duration.

Goal:
Run all three tasks sequentially and produce a simple execution report
containing the timing information for each task.
"""

import time
import datetime

tasks: list[tuple] = [("Backup database", 2), ("Process files", 1), ("Send report", 3)]
duration_in_sec: int = 1


def init_task_runner():
    for task in tasks:
        print(datetime.datetime.now())
        print("running task... ", task)
        t_start = time.time()
        time.sleep(duration_in_sec)
        t_end = time.time()
        print("task completed in seconds: ", t_end - t_start)
        print("task finished at: ", datetime.datetime.now())
        # full conversion cycle for testing only
        completion = datetime.datetime.now()
        print(completion)
        timestamp = completion.timestamp()
        print(timestamp)
        converted = datetime.datetime.fromtimestamp(timestamp)
        print(converted)
        x = datetime.datetime(2018, 6, 1)
        print(x.strftime("%B %Y"))


def main():
    init_task_runner()


if __name__ == "__main__":
    main()
