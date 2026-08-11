"""
5. Math Module

math Module

https://www.w3schools.com/python/module_math.asp

Mini Project: Geometry & Statistics Calculator

Scenario:
Build a small calculator tool that performs common mathematical operations for a construction and analytics application.

You need to support calculations for distances, areas, rounding, and numerical analysis.
Use math.sqrt() to calculate distances and square roots.
Use math.pow() to perform exponent calculations.
Use math.ceil() and math.floor() to handle different rounding requirements.
Use math.pi for calculations involving circles.
Use math.sin(), math.cos(), and math.tan() for angle-based calculations.
Use math.factorial() for calculating combinations and mathematical sequences.
Use math.fabs() to calculate absolute floating-point differences.
Use math.gcd() to calculate the greatest common divisor.
Use math.isclose() to compare floating-point values safely.
Create a calculator function that receives different mathematical operations and returns the calculated result.

Real-world use case:
Used in engineering software, simulations, game development, scientific applications, financial calculations, data analysis, and systems requiring reliable mathematical operations.
"""

import math


def init_calculator():
    try:
        user_menu_select()
    except KeyboardInterrupt:
        print("exit.")


def user_menu_select():
    print("""
0 - sqrt
1 - pow
2 - ceil / floor
3 - pi
4 - sin cos tan
5 - factorial
6 - fabs
7 - gcd (greatest common divisor)
8 - isclose
""")
    user_input: str = input("select calculation: ")

    match user_input:
        case "0":
            print(math.sqrt(float(input("sqrt of: "))))

        case "1":
            num1: float = float(input("num1: "))
            num2: float = float(input("num2: "))
            print(math.pow(num1, num2))

        case "2":
            mode: str = input("ceil (c) or floor (f)?: ")
            if mode == "c":
                print(math.ceil(float(input("enter number: "))))
            elif mode == "f":
                print(math.floor(float(input("enter number: "))))

        case "3":
            print(float(input("circle diameter: ")) * math.pi)

        case "4":
            mode: str = input("sin(s), cos(c), tan(t): ")
            if mode == "s":
                print(math.sin(float(input("sin of: "))))
            elif mode == "c":
                print(math.cos(float(input("cos of: "))))
            elif mode == "t":
                print(math.tan(float(input("tan of: "))))

        case "5":
            print(math.factorial(int(input("enter int: "))))

        case "6":
            print(math.fabs(float(input("enter negative number: "))))

        case "7":
            int1: int = int(input("enter int1: "))
            int2: int = int(input("enter int2: "))
            print(math.gcd(int1, int2))

        case "8":
            number1: float = float(input("enter number1: "))
            number2: float = float(input("enter number2: "))
            max: float = float(input("enter tollerance: "))
            print(math.isclose(number1, number2, rel_tol=max))

    user_menu_select()


def main():
    init_calculator()


if __name__ == "__main__":
    main()
