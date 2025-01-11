from pymenu import command, run_menu
import os

@command("List Directory Contents")
def list_directory():
    path = input("Enter directory path (or press Enter for current directory): ").strip()
    path = path or "."
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error: {e}")
    return True

@command("Create New File")
def create_file():
    filename = input("Enter filename: ")
    try:
        with open(filename, 'w') as f:
            content = input("Enter file content (press Enter when done):\n")
            f.write(content)
        print(f"File '{filename}' created successfully!")
    except Exception as e:
        print(f"Error: {e}")
    return True

@command("File Size")
def get_file_size():
    filename = input("Enter filename: ")
    try:
        size = os.path.getsize(filename)
        print(f"Size of '{filename}': {size} bytes")
    except Exception as e:
        print(f"Error: {e}")
    return True

if __name__ == "__main__":
    run_menu() 