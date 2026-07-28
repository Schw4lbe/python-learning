import random
import math
from textwrap import dedent
from getpass import getpass


class GameData:
    def __init__(self):
        self.user_select: int = 0
        self.user_rounds_won: int = 0
        self.user2_select: int = 0
        self.user2_rounds_won: int = 0
        self.winner: int = 0

    OPTIONS: dict = {
        1: {"name": "stone", "icon": "\u26ab"},
        2: {"name": "paper", "icon": "\U0001f4c4"},
        3: {"name": "scissors", "icon": "\u2702\ufe0f"},
    }


game_data = GameData()


def init_game():
    reset_game_data()

    try:
        play_turn()

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        exit()


def reset_game_data():
    game_data.__init__()


def get_win_condition(turns):
    return math.ceil(turns / 2)


def play_turn():
    check_win_condition()
    if game_data.winner:
        clear_console()
        return game_data.winner

    print(dedent(f"""
        New Round, select your option:
        1 = {game_data.OPTIONS[1]["name"]} {game_data.OPTIONS[1]["icon"]}
        2 = {game_data.OPTIONS[2]["name"]} {game_data.OPTIONS[2]["icon"]}
        3 = {game_data.OPTIONS[3]["name"]} {game_data.OPTIONS[3]["icon"]}
    """))
    set_turn_options()


def clear_console():
    # \033[2J → clear the terminal screen
    # \033[H → move cursor to the top-left
    # end="" → don't add another newline
    print("\033[2J\033[H", end="")


def set_turn_options():
    game_data.user_select = get_user_select("player1")
    game_data.user2_select = get_user_select("player2")
    compare_select(game_data.user_select, game_data.user2_select)


def check_win_condition():
    if game_data.winner:
        return

    if game_data.user_rounds_won == 1:
        print("PLAYER1 STARTS !")
        game_data.winner = 1
        return

    elif game_data.user2_rounds_won == 1:
        print("PLAYER2 STARTS !")
        game_data.winner = 2
        return


def get_user_select(player: str):
    print(f"{player} select: ")
    while True:
        try:
            user_input = int(getpass("type 1, 2 or 3: "))
            if user_input >= 4 or user_input <= 0:
                print("invalid number.")
                continue
            else:
                return user_input

        except (KeyError, ValueError):
            print("no valid value.")


def get_ai_select():
    return random.randint(1, 3)


def compare_select(player1_option, player2_option):
    if player1_option == player2_option:
        print("DRAW, SELECT AGAIN\n")
        set_turn_options()

    elif get_option_counter(player1_option) == player2_option:
        game_data.user2_rounds_won += 1

    else:
        game_data.user_rounds_won += 1

    play_turn()


# circular motion
def get_option_counter(current):
    return (current % len(game_data.OPTIONS)) + 1


def main():
    init_game()
