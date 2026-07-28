import uuid
import json


class Task:
    def __init__(self, id: str, description: str, category: str):
        self.id = id
        self.description = description
        self.category = category
        self.is_completed: bool = False


class Manager:
    def __init__(self, task_list: list):
        self.task_list = task_list


def get_task_data() -> list:
    try:
        with open("data.json", mode="r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        return data

    except FileNotFoundError:
        print("data.json not found.")


def save_to_file(task_manager: Manager):
    clear_console()
    try:
        with open("data.json", mode="w", encoding="utf-8") as write_file:
            json.dump(task_manager.task_list, write_file)
        print("SAVED SUCCESSFULLY!")

    except FileNotFoundError:
        print("data.json not found.")

    init_task_manager()


def init_task_manager():
    clear_console()
    task_manager = Manager(get_task_data())
    display_tasks(task_manager)
    select_option(task_manager)


def select_option(task_manager: Manager):
    input_options: str = (
        "\n(1) add task\n(2) toggle task done\n(3) delete task\n(4) end task manager\nSelect: "
    )

    while True:
        user_input: str = input(input_options)
        match user_input:
            case "1":
                create_new_task(task_manager)
            case "2":
                toggle_task_done(task_manager)
            case "3":
                delete_task(task_manager)
            case "4":
                exit_task_manager()
            case _:
                print("please select one option.")


def delete_task(task_manager: Manager):
    while True:
        max_index: int = len(task_manager.task_list) - 1
        user_input: str = input("select task to toggle: ")
        if check_abort_operation(user_input):
            return

        if int(user_input) <= 0 or int(user_input) > max_index:
            print("select a valid number.")
            continue

        else:
            del task_manager.task_list[user_input - 1]
            save_to_file(task_manager)
            break


def toggle_task_done(task_manager: Manager):
    while True:
        max_index: int = len(task_manager.task_list) - 1
        user_input: str = input("select task to toggle: ")
        if check_abort_operation(user_input):
            return

        if int(user_input) <= 0 or int(user_input) > max_index:
            print("select a valid number.")
            continue

        else:
            task_manager.task_list[user_input - 1]["is_completed"] = (
                not task_manager.task_list[user_input - 1]["is_completed"]
            )
            save_to_file(task_manager)
            break


def create_new_task(task_manager: Manager):
    id: str = str(uuid.uuid4())

    description: str = input("Enter task description: ")
    if check_abort_operation(description):
        return

    category: str = input("Enter category: ")
    if check_abort_operation(category):
        return

    new_task: Task = Task(id, description, category)
    add_task_to_manager(task_manager, new_task.__dict__)


def exit_task_manager():
    while True:
        user_confirm: str = input("quit? (y/n): ")
        if user_confirm == "y":
            clear_console()
            exit()
        elif user_confirm == "n":
            break
        else:
            print("select y or n.")
            continue


def add_task_to_manager(task_manager: Manager, new_task: dict):
    task_manager.task_list.append(new_task)
    save_to_file(task_manager)


def display_tasks(task_manager: Manager):
    for index, task in enumerate(task_manager.task_list):
        print(f"({index}) {task}")


def clear_console():
    # \033[2J → clear the terminal screen
    # \033[H → move cursor to the top-left
    # end="" → don't add another newline
    print("\033[2J\033[H", end="")


def check_abort_operation(input: str) -> bool:
    if input == "!a":
        return True


def main():
    init_task_manager()


if __name__ == "__main__":
    main()
