# Optional addition:
# add a password strength score
# add is not in dict

import msvcrt


class Password:
    MIN_LENGTH: int = 10
    ALLOWED_SPECIALS_REGEX = r"[!@#$%^&*()_\-+=?]"
    ALLOWED_SPECIALS = "!@#$%^&*()_-+=?"

    def __init__(self):
        self.character_list: list = []
        self.has_min_length: bool = False
        self.has_upper_case_char: bool = False
        self.has_lower_case_char: bool = False
        self.has_number: bool = False
        self.has_special_character: bool = False


def init_password_validation():
    password = Password()
    enter_validation_loop(password)


def enter_validation_loop(password: Password):
    while True:
        if is_password_valid(password):
            output_password_result(password.character_list)
            break

        else:
            set_password_string(password)
            validate_password_length(password)
            validate_is_upper(password)
            validate_is_lower(password)
            validate_has_number(password)
            validate_has_special_character(password)


def validate_has_special_character(password: Password):
    password.has_special_character = any(
        char in password.ALLOWED_SPECIALS for char in password.character_list
    )

    if not password.has_special_character:
        print("no special char")


def validate_has_number(password: Password):
    password.has_number = any(char.isnumeric() for char in password.character_list)
    if not password.has_number:
        print("no number")


def validate_is_lower(password: Password):
    password.has_lower_case_char = any(
        char.islower() for char in password.character_list
    )
    if not password.has_lower_case_char:
        print("no lower case char")


def validate_is_upper(password: Password):
    password.has_upper_case_char = any(
        char.isupper() for char in password.character_list
    )
    if not password.has_upper_case_char:
        print("no upper case char")


def validate_password_length(password: Password):
    if len(password.character_list) >= password.MIN_LENGTH:
        password.has_min_length = True
    else:
        if not password.has_min_length:
            password.has_min_length = False
            print("to short")


def set_password_string(password: Password):
    while True:
        try:
            string: str = msvcrt.getch().decode("ASCII")
            if string == "\x08":  # mapping return
                try:
                    password.character_list.pop()
                    print(password.character_list)
                    break

                except IndexError:
                    print("string list already empty.")
                    continue

            elif string == "\r":
                if is_password_valid(password):
                    break
                else:
                    print("password is invalid")

            elif string == " ":
                print("no space allowed.")
                continue

            elif string == "\x03":
                exit()

            else:
                if not string.isalnum() and string not in password.ALLOWED_SPECIALS:
                    print("not allowed use: !@#$%^&*()_\\-+=?")
                    continue

                else:
                    password.character_list.append(string)
                    print(password.character_list)
                    break

        except UnicodeDecodeError:
            print("dont use Umlaute.")


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
