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


def print_menu(
    order_formatter: Callable[[int], str] = str,
    display_formatter: Callable[[str, str], str] = lambda order, name: f"{order}. {name}"
) -> dict:
    # This is the mapping of the symbol that the user will input to the command that will be executed
    menu_items = {}

    # Starting from 1 because 0 is reserved for the exit command
    for i, name in list(enumerate(commands.keys(), start=1)):
        order = order_formatter(i)
        print(display_formatter(order, name))
        menu_items[order] = commands[name]
    
    # Add exit command (always using "0")
    order = order_formatter(0)
    print(display_formatter(order, "Exit"))
    menu_items[order] = _exit

    return menu_items


def menu(prompt: str = "Enter choice: ", **kwargs):
    mapping = print_menu(**kwargs)
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
