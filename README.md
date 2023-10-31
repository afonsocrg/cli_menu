# PyMenu - CLI Menu Creation Made Easy

PyMenu is a Python library that simplifies the creation of CLI menus and interactive command-line interfaces. It allows you to define commands, prompt the user for input, and execute the chosen command effortlessly. Whether you are building a simple command-line tool or a more complex interactive application, PyMenu can streamline the process and enhance user experience.

## Installation

You can install PyMenu using pip:

```bash
pip install pymenu
```

## Usage
Creating CLI Menus

To get started with PyMenu, first import the library and create commands using the @command decorator. Each decorated function defines a command:

```python
from pymenu import command, run_menu

@command("Do something")
def do_something():
    print("You chose to do something!")

@command("Do another thing")
def do_another_thing():
    print("You chose to do another thing!")

if __name__ == "__main__":
    run_menu()

```

## Running the pyMenu
When you run the script, PyMenu will display the registered commands and prompt the user for input. The user can select a command by entering the corresponding number, and PyMenu will execute the associated function:

```bash
$ python example.py
1. Do something
2. Do another thing
Enter command number: 1
You chose to do something!
```

With PyMenu, you can easily create interactive CLI applications, manage user input, and execute commands, making your command-line tools more user-friendly.

## Contributing

Contributions to PyMenu are welcome! If you find issues or have suggestions for improvements, please open an issue or submit a pull request.