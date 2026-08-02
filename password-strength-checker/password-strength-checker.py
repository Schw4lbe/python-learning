# takes a string char by char
# define rules use regexes if needed
# rules: length, upper- lowercase char, number, special char
# check for every rule and give advice
# at least once use name mangling for practice

# Optional:
# check if not in dictionary

import msvcrt


class Password:
    def __init__(self):
        self.has_min_length: bool = False
        self.has_upper_case_char: bool = False
        self.has_lower_case_char: bool = False
        self.has_number: bool = False
        self.has_special_character: bool = False
        self.__MIN_LENGTH: int = 10


def init_password_validation():
    password = Password()

    password_character_list: list = []
    while True:
        if len(password_character_list) < password._Password__MIN_LENGTH:
            string: str = msvcrt.getch().decode("ASCII")

            if string == "\x08":
                try:
                    password_character_list.pop()
                    print(password_character_list)
                    continue
                except IndexError:
                    print("string list already empty.")
                    continue

            elif string == "\r" or string == " ":
                print("no return or space allowed.")
                continue

            elif string == "\x03":
                exit()

            else:
                password_character_list.append(string)
                print(password_character_list)
                continue

        else:
            output_password_result(password_character_list)
            break


def output_password_result(char_list: list):
    result: str = ""
    for char in char_list:
        result += char

    print("password: ", result)


def main():
    init_password_validation()


if __name__ == "__main__":
    main()
