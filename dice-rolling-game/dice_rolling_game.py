import random

# state variable
is_rolling: bool = False


def roll_dice():
    if is_rolling:
        rnd_int1: int = random.randint(1, 6)
        rnd_int2: int = random.randint(1, 6)
        print("print roll :", rnd_int1, rnd_int2)


def set_is_rolling():
    user_select: str = input("y or n:").lower()

    if user_select == "y":
        toggle_rolling_state()
        roll_dice()
        toggle_rolling_state()
        set_is_rolling()
    elif user_select == "n":
        print("exit program.")
        exit()
    else:
        print("invalid input, enter either y or n.")
        set_is_rolling()


def toggle_rolling_state():
    global is_rolling
    is_rolling = not is_rolling


def main():
    set_is_rolling()


if __name__ == "__main__":
    main()
