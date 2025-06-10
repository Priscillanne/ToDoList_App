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
            print("Delete Task feature is not implemented yet.")
        elif choice == 4:
            print("Mark Task as Done feature is not implemented yet.")
        elif choice == 5:
            print("View Done/Pending Tasks feature is not implemented yet.")
        elif choice == 6:
            print("Thank you")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError as e:
        print("Error: " + str(e))
