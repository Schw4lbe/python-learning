# takes a string char by char
# define rules use regexes if needed
# rules: length, upper- lowercase char, number, special char
# check for every rule and give advice
# at least once use name mangling for practice

# Optional:
# has at least 9 different chars
# check if not in dictionary

import msvcrt


class Password:
    def __init__(self):
        self.character_list: list = []
        self.has_min_length: bool = False
        self.has_upper_case_char: bool = False
        self.has_lower_case_char: bool = False
        self.has_number: bool = False
        self.has_special_character: bool = False
        self.__MIN_LENGTH: int = 4


def init_password_validation():
    password = Password()
    enter_validation_loop(password)


def enter_validation_loop(password: Password):
    while True:
        if is_password_valid(password):
            # currently end of app when first password is met for dev control
            # TODO: later make password be confirmed via "return"
            output_password_result(password.character_list)
            break

        else:
            set_password_string(password)
            validate_password_length(password)
            validate_is_upper(password)
            validate_is_lower(password)
            validate_has_number(password)

            # check special char

            # in else check each condition in a function
            # therefore state update suggestions


def validate_has_number(password: Password):
    for char in password.character_list:
        if char.isnumeric():
            password.has_number = True
            break

        else:
            password.has_number = False

    else:
        if password.has_number == False:
            print("no number")


def validate_is_lower(password: Password):
    for char in password.character_list:
        if char.islower():
            password.has_lower_case_char = True
            break

        else:
            password.has_lower_case_char = False

    else:
        if password.has_lower_case_char == False:
            print("no lower case char")


def validate_is_upper(password: Password):
    for char in password.character_list:
        if char.isupper():
            password.has_upper_case_char = True
            break

        else:
            password.has_upper_case_char = False

    else:
        if password.has_upper_case_char == False:
            print("no upper case char")


def validate_password_length(password: Password):
    if len(password.character_list) >= password._Password__MIN_LENGTH:
        password.has_min_length = True
    else:
        if not password.has_min_length:
            password.has_min_length = False
            print("to short")


def set_password_string(password: Password):
    # TODO: check for Umlaute and give error message
    while True:
        string: str = msvcrt.getch().decode("ASCII")

        if string == "\x08":  # mapping return
            try:
                password.character_list.pop()
                print(password.character_list)
                break

            except IndexError:
                print("string list already empty.")
                continue

        elif string == "\x03":
            exit()

        else:
            password.character_list.append(string)
            print(password.character_list)
            break


def output_password_result(char_list: list):
    result: str = ""
    for char in char_list:
        result += char

    print("password: ", result)


def is_password_valid(password: Password) -> bool:
    if all(
        (
            password.has_min_length,
            password.has_upper_case_char,
            password.has_lower_case_char,
            password.has_number,
            password.has_special_character,
        )
    ):
        print("Password is valid")
        return True

    else:
        return False


def main():
    init_password_validation()


if __name__ == "__main__":
    main()
