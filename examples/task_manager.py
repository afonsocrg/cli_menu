from pymenu import command, run_menu

tasks = []

@command("Add Task")
def add_task():
    task = input("Enter task description: ")
    tasks.append(task)
    print(f"Task added: {task}")
    return True

@command("List Tasks")
def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    return True

@command("Clear Tasks")
def clear_tasks():
    tasks.clear()
    print("All tasks cleared!")
    return True

if __name__ == "__main__":
    run_menu() 