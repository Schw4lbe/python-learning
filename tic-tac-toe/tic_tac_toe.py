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
    reset_board()
    try:
        sps.main()
        game_data.starting_player = sps.game_data.winner

        if game_data.starting_player:
            start_round()

    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        exit()


def reset_board():
    game_data.__init__()
    player1.__init__("Player 1")
    player2.__init__("Player 2")


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

    if game_data.starting_player != 0:
        print(f"{player1.name} is using {color_token(player1.player_token)}.")
        print(f"{player2.name} is using {color_token(player2.player_token)}.\n")


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
    print_board()

    first_player = player1 if player1.is_starting_player else player2
    second_player = player2 if player1.is_starting_player else player1

    while True:
        player_set_token(first_player)
        check_win_condition(first_player)

        player_set_token(second_player)
        check_win_condition(second_player)


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
        if int(position) > 9 or int(position) < 1:
            print("choose a valid number.")
            continue

        if game_data.board[position] not in ("X", "O"):
            game_data.turn_indicator += 1
            game_data.board[position] = player.player_token
            player.player_set_tokens.append(int(position))
            clear_console()
            print_board()
            break
        else:
            print("position allready set, choose a different one.")


def check_win_condition(player: Player):
    player_tokens: list = player.player_set_tokens
    for condition in game_data.win_conditions:
        if all(item in player_tokens for item in condition):
            end_round(" WINS", player.name)
            return

    if game_data.turn_indicator >= 9:
        end_round("TIE")


def end_round(msg: str, name: str = ""):
    clear_console()
    print_board()
    print(f"{name}{msg}")
    init_game()


def clear_console():
    # \033[2J → clear the terminal screen
    # \033[H → move cursor to the top-left
    # end="" → don't add another newline
    print("\033[2J\033[H", end="")


def main():
    init_game()


if __name__ == "__main__":
    main()
