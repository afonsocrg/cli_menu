from pymenu import command, run_menu

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
    run_menu() 