# Define task list
task_list = []

# 1. Add Task Function
def add_task():
    task = {
        "name": input("Enter the task: "),
        "status": "Pending"
    }
    task_list.append(task)
    print(f'Task "{task["name"]}" has been added.')

# 2. View All Tasks Function
def view_all_task():
    if not task_list:
        raise ValueError("Task list is empty")
    
    print("All Tasks:")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task['name']} - {task['status']}")

# 3. Delete Task Function
def delete_task():
    if not task_list:
        raise ValueError("Task list is empty")

    try:
        delete_index = int(input("Enter the task number to delete: "))
    except:
        raise ValueError("Enter a valid number")

    if delete_index <= 0 or delete_index > len(task_list):
        raise ValueError("That task does not exist")

    deleted_task = task_list.pop(delete_index - 1)
    print(f'Task {delete_index}: "{deleted_task["name"]}" has been deleted.')

# 4. Mark Task as Done Function
def mark_done():
    if not task_list:
        raise ValueError("Task list is empty")
    
    try:
        task_number = int(input("Enter the task number to mark as done: "))
    except:
        raise ValueError("Enter a valid number")

    if task_number <= 0 or task_number > len(task_list):
        raise ValueError("That task does not exist")

    new_status = input("Enter new status (e.g., Done, In Progress): ")
    task_list[task_number - 1]["status"] = new_status
    print(f'Task {task_number}: "{task_list[task_number - 1]["name"]}" has been marked {new_status}.')

# Menu and Main Loop
print("To-Do List Menu")
print()
print(
    "1. Add Task\n"
    "2. View All Tasks\n"
    "3. Delete Task\n"
    "4. Mark Task as Done\n"
    "5. View Done/Pending Tasks\n"
    "6. Exit"
)

while True:
    print()
    try:
        user_input = input("Enter your choice (1-6): ")

        try:
            choice = int(user_input)
        except:
            raise ValueError("Enter a number")

        if choice <= 0 or choice > 6:
            raise ValueError("Choose a number 1-6")

        if choice == 1:
            add_task()
        elif choice == 2:
            view_all_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            mark_done()
        elif choice == 5:
            print("View Done/Pending Tasks feature is not implemented yet.")
        elif choice == 6:
            print("Thank you")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError as e:
        print("Error: " + str(e))
