import json
from rich import print


class SessionParams:
    def __init__(self):
        self.difficulty: str
        self.category: str
        self.questions: list
        self.score: int = 0
        self.answered_question_ids: list = []


session_params = SessionParams()


def init_new_game():
    reset_session_params()
    try:
        data = import_game_data()
        set_session_params(data)
    except KeyboardInterrupt:
        print("exit.")


def reset_session_params():
    session_params.__init__()


def set_session_params(data: list):
    difficulties: list = get_difficulties(data)
    session_params.difficulty = select_option(difficulties, "Select difficulty: ")

    categories: list = get_categories(data)
    session_params.category = select_option(categories, "Select category: ")

    get_session_questions(data, session_params.difficulty, session_params.category)


def get_session_questions(data: list, difficulty: str, category: str):
    questions: list = []
    for item in data:
        if item["difficulty"] == difficulty and item["category"] == category:
            questions.append(item)

    session_params.questions = questions
    start_round()


def start_round():
    for item in session_params.questions:
        print(f"\nQUESTION: {item["question"]}\n")
        for answer in item["answers"]:
            print(f"({answer["answer_ID"]}) {answer["answer_content"]}")

        user_input: str = input("Select your answer: ")
        validate_answer(item, user_input)

    end_round()


def end_round():
    print(
        f"You answered {session_params.score} / {len(session_params.answered_question_ids)} questions correct."
    )

    init_new_game()


def validate_answer(item: dict, user_input: str):
    for answer in item["answers"]:
        if answer["is_solution"] == True:
            answer_ID = answer["answer_ID"]
            if user_input == answer_ID:
                print("[green]Correct![/green]")
                session_params.score += 1
                session_params.answered_question_ids.append(item["ID"])
                return True
            else:
                print("[red]Wrong![/red]")
                session_params.answered_question_ids.append(item["ID"])
                return False


def get_difficulties(data: list):
    results: list = []
    existing: set = set()

    for item in data:
        difficulty = item["difficulty"]

        if difficulty in existing:
            continue

        existing.add(difficulty)
        results.append({"id": len(results) + 1, "name": difficulty})

    return results


def get_categories(data: list):
    results: list = []
    existing: set = set()

    for item in data:
        if item["difficulty"] != session_params.difficulty:
            continue

        category = item["category"]

        if category in existing:
            continue

        existing.add(category)
        results.append({"id": len(results) + 1, "name": category})

    return results


def select_option(options: list, prompt: str):
    print("########################################")
    for item in options:
        print(f"({item["id"]}) {item["name"]}")

    user_input: int = int(input(prompt))

    for item in options:
        if user_input == item["id"]:
            return item["name"]


def import_game_data():
    try:
        with open("quiz-data.json", "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print("quiz-data.json file not found.")


# helpers:
def clear_console():
    # \033[2J → clear the terminal screen
    # \033[H → move cursor to the top-left
    # end="" → don't add another newline
    print("\033[2J\033[H", end="")


def main():
    clear_console()
    print("WELCOME")
    init_new_game()


if __name__ == "__main__":
    main()
