"""
7. Character Processing

chr()
ord()
String isalnum()

https://www.w3schools.com/python/ref_func_chr.asp
https://www.w3schools.com/python/ref_func_ord.asp
https://www.w3schools.com/python/ref_string_isalnum.asp
https://www.w3schools.com/python/python_strings_methods.asp

Mini Project: Password Strength Analyzer

Scenario:
Build a small password analysis tool that checks user input, validates characters, and provides information about password quality.

You have a list of example passwords:

passwords = [
"Hello123",
"Admin!2026",
"abc",
"Secure_Pass99"
]

Use isalnum() to detect whether passwords contain only letters and numbers.
Use ord() to analyze character Unicode values.
Use chr() to generate characters from Unicode values.
"""

passwords: list[str] = ["Hello123", "Admin!2026", "abc", "Secure_Pass99"]


def init_process():
    print("check isalnum: ")
    for item in passwords:
        print(item, item.isalnum())
    print("\n")

    for pwd in passwords:
        print(pwd)
        for char in pwd:
            print(ord(char), sep=",", end=" ")
        print("\n")

    string_int1: tuple = (72, 101, 108, 108, 111, 49, 50, 51)
    string_int2: tuple = (97, 98, 99)

    print("\n")
    for int in string_int1:
        print(chr(int), sep=",", end=" ")
    for int in string_int2:
        print(chr(int), sep=",", end=" ")


def main():
    init_process()


if __name__ == "__main__":
    main()
