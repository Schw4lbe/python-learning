import random
import math
from textwrap import dedent


class GameData:
    def __init__(self):
        self.user_select: int = 0
        self.user_rounds_won: int = 0
        self.user2_select: int = 0
        self.user2_rounds_won: int = 0
        self.ai_select: int = 0
        self.ai_rounds_won: int = 0
        self.draw_count: int = 0
        self.game_mode: int = 0
        self.win_condition: int = 0
        self.is_multiplayer: bool = False

    # constants
    MODES: dict = {
        1: {"name": "best of 1", "max_turns": 1},
        2: {"name": "best of 3", "max_turns": 3},
        3: {"name": "best of 5", "max_turns": 5},
    }
    OPTIONS: dict = {
        1: {"name": "stone", "icon": "\u26ab"},
        2: {"name": "paper", "icon": "\U0001f4c4"},
        3: {"name": "scissors", "icon": "\u2702\ufe0f"},
    }
    STYLE: dict = {  # ANSI escape codes
        "GREEN": "\033[92m",
        "RED": "\033[91m",
        "RESET": "\033[0m",
    }


game_data = GameData()


def init_game():
    clear_console()
    reset_game_data()

    try:
        set_player_count()
        set_game_mode()
        play_turn()

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        exit()


def set_player_count():
    while True:
        try:
            player_count: str = int(input("select player count (1, 2): "))
            if player_count == 1:
                game_data.is_multiplayer = False
                break
            elif player_count == 2:
                game_data.is_multiplayer = True
                break
            else:
                print("select either 1 or 2.")
                continue
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            exit()
        except:
            print("select either 1 or 2.")
            continue


def set_game_mode():
    print("SELECT GAME MODE: \n(1) best of 1\n(2) best of 3\n(3) best of 5\n")
    game_data.game_mode = get_user_select()
    game_data.win_condition = get_win_condition(
        game_data.MODES[game_data.game_mode]["max_turns"]
    )


def reset_game_data():
    game_data.__init__()


def clear_console():
    # \033[2J → clear the terminal screen
    # \033[H → move cursor to the top-left
    # end="" → don't add another newline
    print("\033[2J\033[H", end="")


def get_win_condition(turns):
    return math.ceil(turns / 2)


def play_turn():
    if check_win_condition():
        end_round()

    if game_data.is_multiplayer:
        print(
            f"SCORE: player1_option {game_data.user_rounds_won} : {game_data.ai_rounds_won} player2_option"
        )
    else:
        print(f"SCORE: YOU {game_data.user_rounds_won} : {game_data.ai_rounds_won} AI")

    print(dedent(f"""
        Best of {game_data.MODES[game_data.game_mode]["max_turns"]}
        New Round, select your option:
        1 = {game_data.OPTIONS[1]["name"]} {game_data.OPTIONS[1]["icon"]}
        2 = {game_data.OPTIONS[2]["name"]} {game_data.OPTIONS[2]["icon"]}
        3 = {game_data.OPTIONS[3]["name"]} {game_data.OPTIONS[3]["icon"]}
    """))
    set_turn_options()


def set_turn_options():
    if game_data.is_multiplayer:
        game_data.user_select = get_user_select()
        game_data.user2_select = get_user_select()
        compare_select(game_data.user_select, game_data.user2_select)
    else:
        game_data.user_select = get_user_select()
        game_data.ai_select = get_ai_select()
        compare_select(game_data.user_select, game_data.ai_select)


def end_round():
    while True:
        user_input: str = input("Do you want to play again? (y/n): ")
        if user_input == "y":
            init_game()
            break
        elif user_input == "n":
            clear_console()
            exit()
        else:
            print("Select either y or n.")
            continue


def check_win_condition():
    final_score_string_single_player: str = (
        f"FINAL SCORE: PLAYER1 ({game_data.user_rounds_won} : {game_data.ai_rounds_won}) AI // DRAWS: {game_data.draw_count}"
    )

    final_score_string_multi_player: str = (
        f"FINAL SCORE: PLAYER1 ({game_data.user_rounds_won} : {game_data.user2_rounds_won}) PLAYER2 // DRAWS: {game_data.draw_count}"
    )

    if game_data.user_rounds_won == game_data.win_condition:
        print(f"{game_data.STYLE["GREEN"]}PLAYER1 WINS !!!{game_data.STYLE["RESET"]}")
        if game_data.is_multiplayer:
            print(final_score_string_multi_player)
        else:
            print(final_score_string_single_player)
        return True

    elif game_data.user2_rounds_won == game_data.win_condition:
        print(f"{game_data.STYLE["GREEN"]}PLAYER2 WINS !!!{game_data.STYLE["RESET"]}")
        print(final_score_string_multi_player)
        return True

    elif game_data.ai_rounds_won == game_data.win_condition:
        print(f"{game_data.STYLE["RED"]}GAME OVER ...{game_data.STYLE["RESET"]}")
        print(final_score_string_single_player)
        return True


def get_user_select():
    while True:
        try:
            user_input = int(input("type 1, 2 or 3 to select: "))
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
    compare_display_string: str = (
        f"{game_data.OPTIONS[player1_option]["icon"]} VS {game_data.OPTIONS[player2_option]["icon"]}\n"
    )

    if player1_option == player2_option:
        game_data.draw_count += 1
        print(f"DRAW, SELECT AGAIN\n{compare_display_string}")
        set_turn_options()

    if game_data.is_multiplayer:
        if get_option_counter(player1_option) == player2_option:
            game_data.user2_rounds_won += 1
            print(f"{game_data.STYLE["GREEN"]}PLAYER2 WON{game_data.STYLE["RESET"]}")
        else:
            game_data.user_rounds_won += 1
            print(f"{game_data.STYLE["GREEN"]}PLAYER1 WON{game_data.STYLE["RESET"]}")

    else:
        if get_option_counter(player1_option) == player2_option:
            game_data.ai_rounds_won += 1
            print(f"{game_data.STYLE["RED"]}ROUND LOST{game_data.STYLE["RESET"]}")
        else:
            game_data.user_rounds_won += 1
            print(f"{game_data.STYLE["GREEN"]}ROUND WON{game_data.STYLE["RESET"]}")

    print(compare_display_string)
    play_turn()


# circular motion
def get_option_counter(current):
    return (current % len(game_data.OPTIONS)) + 1


def main():
    init_game()


if __name__ == "__main__":
    main()
