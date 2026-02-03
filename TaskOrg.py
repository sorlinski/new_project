import os

def load_tasks(filename):
    """Loads tasks from a file into a list."""
    tasks = []
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                # Remove whitespace and empty lines
                tasks = [line.strip() for line in file if line.strip()]
    except (FileNotFoundError, IOError) as e:
        print(f"Error loading file: {e}")
    return tasks

def save_tasks(filename, tasks):
    """Saves the current list of tasks to a file."""
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except PermissionError:
        print("Error: Could not save tasks. The file might be locked.")

def add_task(tasks):
    """Adds a new task to the list."""
    new_task = input("Enter the task description: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"Added: {new_task}")
    else:
        print("Task cannot be empty!")

def view_tasks(tasks):
    """Displays all current tasks."""
    if not tasks:
        print("\nYour task list is currently empty.")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(tasks):
    """Removes a task by its list number."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        # List index is task_num - 1
        removed = tasks.pop(task_num - 1)
        print(f"Removed task: {removed}")
    except (ValueError, IndexError):
        print("Invalid choice! Please enter a valid number from the list.")

def main():
    filename = "task_list.txt"
    tasks = load_tasks(filename)
    
    while True:
        print("\n--- Task Manager ---")
        print("1. View Tasks\n2. Add Task\n3. Remove Task\n4. Save & Exit")
        choice = input("Select an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid selection, please try again.")

if __name__ == "__main__":
    main()