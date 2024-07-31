# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter task to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# Function to remove a task from the list
def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

# Function to view all tasks in the list
def view_tasks():
    if tasks:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("You have no tasks.")

# Main program loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
