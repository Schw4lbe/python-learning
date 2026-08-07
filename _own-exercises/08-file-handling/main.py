"""
8. File Handling

File Open
tell()
seek()
with

https://www.w3schools.com/python/python_file_handling.asp
https://www.w3schools.com/python/ref_file_tell.asp
https://www.w3schools.com/python/ref_file_seek.asp
https://www.w3schools.com/python/python_with.asp

Mini Project: Log File Analyzer

Scenario:
Build a small log analysis tool that reads, searches, and processes application log files. The system should handle files safely and efficiently.

You have a log file containing different application events.
Use open() to read and write files.
Use with to safely manage file resources.
Use different file modes (r, w, a) to handle different operations.
Use read(), readline(), and readlines() to retrieve file content.
Use tell() to track the current position inside a file.
Use seek() to move to a specific position and reread parts of the file.
Create a function that searches the log file for specific keywords like errors or warnings.
Create a report file containing the analysis results.

optional:
Extend the system to process large log files line by line instead of loading the entire file into memory.

Real-world use case:
Used in log monitoring, data processing, configuration management, reporting systems, backups, and applications that need to store or analyze persistent data.
"""


def main():
    print("Hello from 08-file-handling!")


if __name__ == "__main__":
    main()
