import os

# Define the file to store tasks
TASK_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks


def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")


def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found!")
        return
    print("\nTasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task.startswith("[DONE]") else "✗"
        task_name = task.replace("[DONE]", "").strip()
        print(f"{idx}. {task_name} [{status}]")


def add_task(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"\nTask added: {task}")


def remove_task(task_number):
    """Remove a task by its number."""
    tasks = load_tasks()
    if task_number <= 0 or task_number > len(tasks):
        print("\nInvalid task number!")
        return
    removed_task = tasks.pop(task_number - 1)
    save_tasks(tasks)
    print(f"\nTask removed: {removed_task}")


def mark_task_completed(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if task_number <= 0 or task_number > len(tasks):
        print("\nInvalid task number!")
        return
    tasks[task_number - 1] = f"[DONE] {tasks[task_number - 1]}"
    save_tasks(tasks)
    print(f"\nTask marked as completed: {tasks[task_number - 1]}")


def show_help():
    """Display the help menu."""
    print("""
Command-Line Task Manager:
Usage:
    list               - List all tasks
    add <task>         - Add a new task
    remove <number>    - Remove a task by its number
    complete <number>  - Mark a task as completed
    help               - Show this help message
    """)


def main():
    """Main function to handle command-line input."""
    import sys
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "list":
        list_tasks()
    elif command == "add" and len(sys.argv) > 2:
        task = " ".join(sys.argv[2:])
        add_task(task)
    elif command == "remove" and len(sys.argv) > 2:
        try:
            task_number = int(sys.argv[2])
            remove_task(task_number)
        except ValueError:
            print("\nPlease provide a valid task number.")
    elif command == "complete" and len(sys.argv) > 2:
        try:
            task_number = int(sys.argv[2])
            mark_task_completed(task_number)
        except ValueError:
            print("\nPlease provide a valid task number.")
    else:
        show_help()


if __name__ == "__main__":
    main()
