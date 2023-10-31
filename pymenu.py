from functools import wraps


def exit():
    print("Exiting...")
    return False


commands = {"Exit": exit}


def command(name):
    """
    This decorator registers the decorated function as a command.
    If name is specified, it will be used as the command name,
    otherwise the function name will be used.
    """

    def decorator(f):
        @wraps(f)
        def wrapper():
            return f()

        # key = f.__name__ if name is None else name
        key = name
        commands[key] = wrapper
        return wrapper

    return decorator


def print_menu():
    menu_items = {}
    for i, name in list(enumerate(commands.keys(), start=1)):
        print(f"{i}. {name}")
        menu_items[str(i)] = commands[name]
    return menu_items


def menu():
    mapping = print_menu()
    choice = ""
    while choice.strip() == "":
        choice = input("Enter choice: ")

    try:
        return mapping[choice]()
    except KeyError:
        print("Invalid choice. Try again.")


def run_menu():
    # Put the exit command at the end
    exit_command = commands.pop("Exit")
    commands["Exit"] = exit_command
    while menu() != False:
        pass