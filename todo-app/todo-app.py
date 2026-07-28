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
    try:
        with open("data.json", mode="w", encoding="utf-8") as write_file:
            json.dump(task_manager.task_list, write_file)

    except FileNotFoundError:
        print("data.json not found.")

    init_task_manager()


def init_task_manager():
    task_manager = Manager(get_task_data())
    select_option(task_manager)


def select_option(task_manager: Manager):
    input_options: str = (
        "(1) show tasks\n(2) add task\n(3) check task\n(4) delete task\n(5) end task manager\nSelect: "
    )

    while True:
        user_input: str = input(input_options)
        match user_input:
            case "1":
                display_tasks(task_manager)
            case "2":
                create_new_task(task_manager)
                display_tasks(task_manager)
            case "3":
                print("TBD complete")
            case "4":
                print("TBD delete")
            case "5":
                exit_task_manager()
            case _:
                print("else")


def exit_task_manager():
    # TODO: add all needed steps for clear exit out
    exit()


def create_new_task(task_manager: Manager) -> dict:
    id: str = str(uuid.uuid4())
    description: str = input("Enter task description: ")
    category: str = input("Enter category: ")
    new_task: Task = Task(id, description, category)
    add_task_to_manager(task_manager, new_task.__dict__)


def add_task_to_manager(task_manager: Manager, new_task: dict):
    task_manager.task_list.append(new_task)
    save_to_file(task_manager)


def display_tasks(task_manager: Manager):
    # TODO: update to hide id and show index instead for task operations
    # consider using a enumeration
    for task in task_manager.task_list:
        print(task)

    select_option(task_manager)


def main():
    init_task_manager()


if __name__ == "__main__":
    main()
