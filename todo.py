import os
#creating a variable as a TASK_FILE
TASK_FILE = "tasks.txt"

# Load existing tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

#function for saving the task
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# function for displaying tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{tasks}")

#function for adding a new task
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

#function for Removing a task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed task: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu loop
def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
