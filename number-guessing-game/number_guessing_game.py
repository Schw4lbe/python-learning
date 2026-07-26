import random


class GameState:
    rnd_int: int = 0
    user_input: int = 0
    attempts_counter: int = 0
    MAX_ATTEMPTS: int = 10


game_state = GameState()


def init_game():
    try:
        game_state.attempts_counter = 0
        game_state.rnd_int = generate_rnd_int()
        game_state.user_input = get_user_input()
        compare_values(game_state.rnd_int, game_state.user_input)
    except KeyboardInterrupt:
        print("games stopped via STRG + C command.")


def compare_values(rnd_int, user_input):
    game_state.attempts_counter += 1

    # guard end game condition
    if game_state.attempts_counter > game_state.MAX_ATTEMPTS:
        end_round(rnd_int)
        return

    if rnd_int > user_input:
        print("Too low!")

    elif rnd_int < user_input:
        print("Too high!")

    else:
        print(f"Correct! The solution was: {rnd_int}")
        print(f"Total attempts needed: {game_state.attempts_counter}.")
        start_new_round()
        return

    new_user_input: int = get_user_input()
    compare_values(rnd_int, new_user_input)


def generate_rnd_int():
    return random.randint(1, 100)


def get_user_input():
    validated_input = validate_user_input()

    if validated_input < 1 or validated_input > 100:
        print("enter number between 1 and 100.")
        return get_user_input()

    return validated_input


def validate_user_input():
    user_input: str = input("enter a number between 1 and 100: ")

    try:
        return int(user_input)
    except ValueError:
        print("exception, invalid number.")
        return validate_user_input()


def end_round(rnd_int):
    print(f"you failed, the correct answer is: {rnd_int}")
    start_new_round()


def start_new_round():
    while True:
        user_select: str = input("y or n:").lower()

        if user_select == "y":
            print("starting new round.")
            init_game()
            return
        elif user_select == "n":
            print("exit program.")
            exit()
        else:
            print("invalid input, enter either y or n.")
            start_new_round()


def main():
    init_game()


if __name__ == "__main__":
    main()
