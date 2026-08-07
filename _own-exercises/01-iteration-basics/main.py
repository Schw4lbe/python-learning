"""
## 1. Iteration Basics

iter()
next()
yield
Generators

https://www.w3schools.com/python/python_iterators.asp
https://www.w3schools.com/python/python_generators.asp

Mini Project: Log File Stream Processor

Scenario:
Build a small monitoring tool that processes server logs one entry at a time instead of loading everything into memory.

You have the following log messages:
logs = [
    "INFO: Server started",
    "WARNING: High memory usage",
    "ERROR: Database connection failed",
    "INFO: User login"
]

Use iter() to convert the log collection into an iterator.
Use next() to manually retrieve log entries from the iterator.
Create a generator using "yield" that provides log entries one by one.
Create a generator that filters specific events like errors or warnings.
Create a processing function that handles any iterator or generator.
Extend the system to count events without storing processed entries.

Real-world use case:
Used in log monitoring, data pipelines, file processing, API data streams, and systems where large amounts of data need to be processed efficiently.
"""


def main():
    print("Hello from 01-iteration-basics!")


if __name__ == "__main__":
    main()
