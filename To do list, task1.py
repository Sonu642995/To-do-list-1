tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("\nEnter new task: ")
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter new task description: ")
                tasks[task_no - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")