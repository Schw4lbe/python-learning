# add tasks
# view tasks
# delete tasks
# mark as complete and move to second list
# create persistant save in json
import uuid


class Task:
    def __init__(self, id: str, description: str, category: str):
        self.id = id
        self.description = description
        self.category = category
        self.is_completed: bool = False


class Manager:
    def __init__(self, task_list: list):
        self.task_list = task_list


data = [
    {
        "id": "1",
        "description": "place text here.",
        "category": "testing",
        "is_completed": False,
    },
    {
        "id": "2",
        "description": "place more text here.",
        "category": "more testing",
        "is_completed": False,
    },
]


def init_task_manager():
    task_data: list = load_tasks()
    task_manager = Manager(task_data)
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
    id: str = str(uuid.uuid1())
    description: str = input("Enter task description: ")
    category: str = input("Enter category: ")
    new_task: Task = Task(id, description, category)
    add_task(task_manager, new_task)


def add_task(task_manager: Manager, new_task: Task):
    task_manager.task_list.append(new_task.__dict__)
    select_option(task_manager)


def display_tasks(task_manager: Manager):
    # TODO: update to hide id and show index instead for task operations
    # consider using a enumeration
    for task in task_manager.task_list:
        print(task)

    select_option(task_manager)


def load_tasks():
    return data


def main():
    init_task_manager()


if __name__ == "__main__":
    main()
