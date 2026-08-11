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
Build a small tool that runs a few tasks, measures how long they take,
and creates a readable execution report.

tasks = [
    ("Backup database", 2),
    ("Process files", 1),
    ("Send report", 3)
]

1. TASK START
   Use datetime.now() to record when each task starts.

2. MEASURE EXECUTION
   Use time.time() before and after time.sleep() to measure how long
   each simulated task takes.

3. TASK COMPLETION
   Store the completion time as a datetime and use timedelta to
   calculate the duration between start and completion.

4. TIMESTAMP
   Convert a completion datetime to a Unix timestamp and convert it
   back to a datetime.

5. FORMAT REPORT
   Use strftime() to display task completion times in a readable format.

6. PARSE DATE
   Use strptime() to convert one formatted completion time back into
   a datetime object.

7. REPORT
   Display each task with its start time, completion time, and duration.

Goal:
Run all tasks, measure their execution, and produce a simple readable
execution report.

Optional:
Ask the user for a delay and use time.sleep() before starting each task.
"""

import time


def main():
    print("Hello from 09-time-module!")


if __name__ == "__main__":
    main()
