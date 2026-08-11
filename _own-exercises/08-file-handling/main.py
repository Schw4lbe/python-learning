"""
8. File Handling

File Open
tell()
seek()
with

https://www.w3schools.com/python/python_file_handling.asp
https://www.w3schools.com/python/ref_file_tell.asp
https://www.w3schools.com/python/ref_file_seek.asp
https://www.w3schools.com/python/ref_keyword_with.asp

Mini Project: Server Log Analyzer

Scenario:
Build a small tool that creates a server log, analyzes it, and writes
a separate analysis report.

1. CREATE LOG
   Use open(..., "x") to create server.log and write several INFO,
   WARNING, and ERROR entries; handle the case where it already exists.

logs = [
    "INFO: User logged in",
    "WARNING: Disk space low",
    "ERROR: Database connection failed"
]

2. INSPECT LOG
   Use "r" with readline() to read the first entry and tell() to show
   the current file position.

3. READ & RECHECK
   Use read() to display the log, then seek() back to the beginning
   and use readlines() to retrieve the entries again.

4. SEARCH LOG
   Create a function that searches the entries for a given keyword
   such as "ERROR" or "WARNING" and counts the matches.

5. CREATE REPORT
   Use "w" to create log-result.txt containing the search results.

6. APPEND REPORT
   Use "at" to append a final "Analysis completed" message.

Use with for every file operation.

Goal:
Create one complete file workflow:
create → read → inspect → seek → search → report → append,
while keeping the original log intact after creation.
"""

init_logs: list[str] = [
    "INFO: User logged in",
    "WARNING: Disk space low",
    "ERROR: Database connection failed",
    "ERROR: User connection failed",
]

error_log_results: list[str] = []


def init_logging():
    handle_create_log_file()
    inspect_log_first_line()
    inspect_log()
    create_report()
    finalize_report()


def finalize_report():
    with open("log-result.txt", "at") as f:
        f.write("Analysis completed.")


def create_report():
    search_log("ERROR")
    search_log("WARNING")
    print(error_log_results)

    with open("log-result.txt", "w") as f:
        for result in error_log_results:
            f.write(f"{result[0]} {result[1]}\n")


def search_log(keyword: str):
    with open("log.txt", "r") as f:
        lines_to_list: list[str] = f.readlines()
        for line in lines_to_list:
            if keyword in line:
                print(f"checking for {keyword}: ", line)
                error_log_results.append((f"checking for {keyword}", line))


def inspect_log():
    with open("log.txt", "r") as f:
        print(f.read())
        f.seek(0)
        print("via readlines: ", f.readlines())


def inspect_log_first_line():
    with open("log.txt", "r") as f:
        print(f.readline(), f.tell())


def handle_create_log_file():
    try:
        with open("log.txt", "xt") as f:
            f.write("\n".join(init_logs))

    except FileExistsError:
        print("log file allready created.")


def main():
    init_logging()


if __name__ == "__main__":
    main()
