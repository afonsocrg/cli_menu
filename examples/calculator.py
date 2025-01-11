#! /usr/bin/env python3
from cli_menu import command, run_menu

@command("Add Numbers")
def add():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a + b}")
    return True

@command("Subtract Numbers")
def subtract():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a - b}")
    return True

@command("Multiply Numbers")
def multiply():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Result: {a * b}")
    return True

if __name__ == "__main__":
    run_menu(
      prompt="> ",
      order_formatter=lambda order: chr(order + ord('a') - 1) if order > 0 else 'x',
      item_formatter=lambda order, name: f"{order}) {name}",
      # show_menu_on_invalid=True,
      show_menu_on_empty=True,
      # exit_order_last=True,
      # order_start=10,
      exit_name="Quit"
    ) 