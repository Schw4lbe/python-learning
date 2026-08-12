"""
10. System Module

sys Module

https://www.w3schools.com/python/module_sys.asp

Mini Project: Python System Info CLI

Scenario:
Build a small command-line tool that lets a developer inspect their
current Python environment.

1. ARGUMENTS
   Use sys.argv to choose one of the diagnostic commands: info, input,
   memory, or modules.

2. SYSTEM INFO
   For "info", display the Python version using sys.version and the
   operating system using sys.platform.

3. USER INPUT
   For "input", use sys.stdin to let the developer enter a project name,
   then display the entered project name.

4. OUTPUT
   Use sys.stdout for normal diagnostic results and sys.stderr for
   invalid commands or errors.

5. MEMORY
   For "memory", use sys.getsizeof() to show the memory size of the
   project name entered by the user.

6. EXIT CODES
   Use sys.exit(0) when a command succeeds and sys.exit(1) when the
   command is invalid or an error occurs.

7. MODULE PATH
   For "modules", display sys.path and temporarily add a "plugins"
   directory to the module search path.

Goal:
Run the program from the terminal, choose one of the three commands,
and receive the corresponding information. Invalid commands should
produce an error and a non-zero exit code.
"""

import sys


def init_cmd_tool():
    handle_console_arguments()


def handle_console_arguments():
    try:
        command = sys.argv[1]
        if command == "info":
            display_system_info()
        elif command == "input":
            input_project_data(command)
        elif command == "memory":
            input_project_data(command)
        elif command == "modules":
            print("Before:")
            print(sys.path)

            # path to module packages added manually
            # having another place to search for packages and modules
            sys.path.append("./plugins")

            print("After:")
            print(sys.path)

        else:
            sys.stderr.write("Unknown command!")

    except IndexError:
        print("missing argument.")
        sys.exit(1)


def input_project_data(command: str):
    byte_size: int = 0
    for line in sys.stdin:
        line = line.strip()
        if command == "memory":
            byte_size += sys.getsizeof(line)

        if line == "q":
            if command == "memory":
                print("Input size in bytes: ", byte_size)
            break

        print("Received:", line)
        sys.exit(0)


def display_system_info():
    sys.stdout.write("providing system info:\n  ")
    print("sys version: ", sys.version)
    print("sys platform: ", sys.platform)
    sys.exit(0)


def main():
    init_cmd_tool()


if __name__ == "__main__":
    main()
