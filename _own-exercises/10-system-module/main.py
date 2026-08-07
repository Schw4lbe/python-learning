"""
10. System Module

sys Module

https://www.w3schools.com/python/module_sys.asp

Mini Project: Command Line Application Framework

Scenario:
Build a small command-line application that interacts with the Python runtime environment, handles user input arguments, and manages application behavior.

Use sys.argv to read command-line arguments.
Use sys.exit() to terminate the program with different exit codes.
Use sys.version to display Python interpreter information.
Use sys.platform to detect the operating system environment.
Use sys.path to inspect and modify module search locations.
Use sys.stdin to read input streams.
Use sys.stdout and sys.stderr to handle normal output and error messages separately.
Use sys.getsizeof() to inspect memory usage of Python objects.
Create a command-line tool that reacts differently based on provided arguments.
Create error handling that returns meaningful exit codes.

optional:
Extend the application into a small CLI utility with multiple commands and custom module loading.

Real-world use case:
Used in command-line tools, automation scripts, development utilities, system administration tools, debugging applications, and software that interacts directly with the Python runtime environment.
"""


def main():
    print("Hello from 10-system-module!")


if __name__ == "__main__":
    main()
