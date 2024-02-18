tasks = []

print("\nTodo List Menu:")

while True:
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. View Tasks")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_task = input("\nEnter the task: ")
        tasks.append(new_task)
        print("Task added successfully!\n")
    elif choice == 2:
        if not tasks:
            print("No tasks to mark as done.\n")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_number = int(input("Enter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                print(f"Task '{tasks[task_number - 1]}' marked as done.\n")
                del tasks[task_number - 1]
            else:
                print("Invalid task number.\n")
    elif choice == 3:
        if not tasks:
            print("No tasks to display.\n")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            print()
    elif choice == 4:
        print("Exiting Todo List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.\n")
