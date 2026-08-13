"""
11. Platform Module

platform Module

https://www.w3schools.com/python/module_platform.asp

Mini Project: System Information Collector

Scenario:
Build a small diagnostic tool that collects information about the machine and Python environment it is running on.
The tool should create a system report for troubleshooting and compatibility checks.

Use platform.system() to identify the operating system.
Use platform.release() to get the operating system version.
Use platform.version() to retrieve detailed system information.
Use platform.machine() to identify the hardware architecture.
Use platform.processor() to retrieve processor information.
Use platform.architecture() to detect 32-bit or 64-bit environments.
Use platform.python_version() to check the Python runtime version.
Use platform.python_implementation() to identify the Python interpreter.
Use platform.uname() to collect a complete system summary.

Real-world use case:
Used in diagnostic tools, software installers, compatibility checks, bug reports, deployment systems, and applications that need to adapt to different operating environments.
"""

import platform


def init_diagnosis():
    operating_system: str = platform.system()
    operating_system_version: str = platform.release()
    operating_system_build: str = platform.version()
    hardware_vendor: str = platform.machine()
    processor_info: str = platform.processor()
    architecture: tuple = platform.architecture()
    python_runtime_version: str = platform.python_version()
    python_interpreter: str = platform.python_implementation()
    system_summary = platform.uname()

    print(
        operating_system,
        operating_system_version,
        operating_system_build,
        hardware_vendor,
        processor_info,
        architecture,
        python_runtime_version,
        python_interpreter,
        system_summary,
    )


def main():
    init_diagnosis()


if __name__ == "__main__":
    main()
