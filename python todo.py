tasks = []

def show_menu():
    print("\nSimple To-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!")
    else:
        print("Invalid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Invalid choice, try again.")
