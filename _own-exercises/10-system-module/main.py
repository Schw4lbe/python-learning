"""
10. System Module

sys Module

https://www.w3schools.com/python/module_sys.asp

Mini Project: Python System Info CLI

Scenario:
Build a small command-line tool that reports information about the
Python environment and accepts commands from the terminal.

1. ARGUMENTS
   Use sys.argv to determine which command the user requested.

2. SYSTEM INFO
   Use sys.version and sys.platform to display Python and OS information.

3. USER INPUT
   Use sys.stdin to read additional input when required.

4. OUTPUT
   Use sys.stdout for normal output and sys.stderr for error messages.

5. MEMORY
   Use sys.getsizeof() to display the memory size of a Python object.

6. EXIT CODES
   Use sys.exit() with different codes for successful execution and errors.

7. MODULE PATH
   Display sys.path and temporarily add a custom path to it.

Goal:
Create one small CLI application where the requested command determines
what information is displayed and invalid commands produce an error with
an appropriate exit code.
"""


def main():
    print("Hello from 10-system-module!")


if __name__ == "__main__":
    main()
