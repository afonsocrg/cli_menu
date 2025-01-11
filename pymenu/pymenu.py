from functools import wraps
from typing import Callable

commands = {}

def command(name: str) -> Callable[[Callable], Callable]:
    """
    This decorator registers the decorated function as a command.
    If name is specified, it will be used as the command name,
    otherwise the function name will be used.
    """

    def decorator(f):
        @wraps(f)
        def wrapper():
            return f()

        key = name
        commands[key] = wrapper
        return wrapper

    return decorator

def _exit():
    raise SystemExit

def print_menu() -> dict:
    menu_items = {}
    for i, name in list(enumerate(commands.keys(), start=1)):
        print(f"{i}. {name}")
        menu_items[str(i)] = commands[name]
    
    # Add exit command
    print("0. Exit")
    menu_items["0"] = _exit

    return menu_items


def menu(prompt: str = "Enter choice: "):
    mapping = print_menu()
    choice = ""
    while choice.strip() == "":
        choice = input(prompt)

    try:
        return mapping[choice]()
    except KeyError:
        print("Invalid choice. Try again.")


def run_menu(**kwargs):
    try:
        while True:
            menu(**kwargs)
    except SystemExit:
        print("Exiting...")
