# two players alternating
# 3 cols 3 rows
# Xs and Os as symbols
# print board after each move
# check condition every move
# endgame on win or board full


# optional:
# add scoring for multiple rounds
# allow new game start without restart
# allow different board sizes
import sps
from colorama import Fore, Style


class Player:
    def __init__(self, name: str):
        self.name = name
        self.player_token: str = ""
        self.player_set_tokens: list = []
        self.is_starting_player: bool = False


class GameData:
    def __init__(self):
        self.starting_player: int = 0
        self.token_first_select: str = "X"
        self.token_second_select: str = "O"
        self.turn_indicator: int = 0
        self.win_conditions: list = [
            (7, 8, 9),
            (4, 5, 6),
            (1, 2, 3),
            (7, 4, 1),
            (8, 5, 2),
            (9, 6, 3),
            (7, 5, 3),
            (9, 5, 1),
        ]

        self.board: dict = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

    LINE_SEPARATOR: str = "---+---+---"


game_data = GameData()
player1 = Player("Player 1")
player2 = Player("Player 2")


def init_game():
    try:
        sps.main()
        game_data.starting_player = sps.game_data.winner

        if game_data.starting_player:
            print_board()
            start_round()

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        exit()


def print_board():
    print(game_data.LINE_SEPARATOR)
    print(
        f" {color_token(game_data.board["7"])} | "
        f"{color_token(game_data.board["8"])} | "
        f"{color_token(game_data.board["9"])}"
    )
    print(game_data.LINE_SEPARATOR)
    print(
        f" {color_token(game_data.board["4"])} | "
        f"{color_token(game_data.board["5"])} | "
        f"{color_token(game_data.board["6"])}"
    )
    print(game_data.LINE_SEPARATOR)
    print(
        f" {color_token(game_data.board["1"])} | "
        f"{color_token(game_data.board["2"])} | "
        f"{color_token(game_data.board["3"])}"
    )
    print(game_data.LINE_SEPARATOR)


# define colors by character
def color_token(token: str) -> str:
    if token == "X":
        return f"{Fore.RED}{token}{Style.RESET_ALL}"
    elif token == "O":
        return f"{Fore.BLUE}{token}{Style.RESET_ALL}"
    else:
        return f"{Fore.LIGHTBLACK_EX}{token}{Style.RESET_ALL}"


def start_round():
    assign_tokens_and_order()

    first_player = player1 if player1.is_starting_player else player2
    second_player = player2 if player1.is_starting_player else player1

    while True:
        player_set_token(first_player)
        check_win_condition()

        player_set_token(second_player)
        check_win_condition()


def assign_tokens_and_order():
    if game_data.starting_player == 1:
        player1.player_token = game_data.token_first_select
        player2.player_token = game_data.token_second_select
        player1.is_starting_player = True

    elif game_data.starting_player == 2:
        player1.player_token = game_data.token_second_select
        player2.player_token = game_data.token_first_select
        player2.is_starting_player = True


def player_set_token(player: Player):
    while True:
        position: str = input(f"{player.name} select your token position: ")
        if game_data.board[position] not in ("X", "O"):
            game_data.board[position] = player.player_token
            player.player_set_tokens.append(position)
            print_board()
            break
        else:
            print("position allready set, choose a different one.")


def check_win_condition():
    print("checking win condition - TBD")


def clear_console():
    # \033[2J → clear the terminal screen
    # \033[H → move cursor to the top-left
    # end="" → don't add another newline
    print("\033[2J\033[H", end="")


def main():
    init_game()


if __name__ == "__main__":
    main()
