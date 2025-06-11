import datetime

task_list = []

# 1. Add Task Function (adds due date and priority level)
def add_task():
    task_name = input("Enter the task: ")

    # Validate due date format
    while True:
        due_date = input("Enter the due date (YYYY-MM-DD): ")
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Incorrect date format. Please enter as YYYY-MM-DD.")

    # Validate priority input
    while True:
        priority = input("Enter the priority (High/Medium/Low): ").capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("Invalid priority. Please enter High, Medium, or Low.")

    task = {
        "name": task_name,
        "status": "Pending",
        "due_date": due_date,
        "priority": priority
    }
    task_list.append(task)
    print(f'Task "{task["name"]}" has been added with priority {priority} and due date {due_date}.')

# 2. View All Tasks Function
def view_all_task():
    if not task_list:
        raise ValueError("Task list is empty")
    
    print("All Tasks:")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task['name']} - {task['status']} | Due: {task['due_date']} | Priority: {task['priority']}")

# 3. Delete Task Function
def delete_task():
    if not task_list:
        raise ValueError("Task list is empty")

    try:
        delete_index = int(input("Enter the task number to delete: "))
    except:
        raise ValueError("Enter a valid number (e.g., 1, 2, 3...)")

    if delete_index <= 0 or delete_index > len(task_list):
        raise ValueError("That task does not exist")

    deleted_task = task_list.pop(delete_index - 1)
    print(f'Task {delete_index}: "{deleted_task["name"]}" has been deleted.')

# 4. Mark Task as Done Function
def mark_done():
    if not task_list:
        raise ValueError("Task list is empty")
    
    try:
        task_number = int(input("Enter the task number to mark as done (e.g., 1): "))
    except:
        raise ValueError("Invalid input. Please enter a number like 1, 2, 3...")

    if task_number <= 0 or task_number > len(task_list):
        raise ValueError("That task does not exist")

    new_status = input("Enter new status (e.g., Done, In Progress): ")
    task_list[task_number - 1]["status"] = new_status
    print(f'Task {task_number}: "{task_list[task_number - 1]["name"]}" has been marked {new_status}.')

# 5. View Tasks by Status Function
def view_status_task():
    if not task_list:
        raise ValueError("Task list is empty")

    status = input("Enter the status to filter by (e.g., Pending, Done): ")
    matching_tasks = [task for task in task_list if task["status"].lower() == status.lower()]

    if not matching_tasks:
        raise ValueError(f"No tasks with status '{status}'")

    print(f"Tasks with status '{status}':")
    for i, task in enumerate(matching_tasks, start=1):
        print(f"{i}. {task['name']} - {task['status']} | Due: {task['due_date']} | Priority: {task['priority']}")

# Menu and Main Loop
print("To-Do List Menu\n")
print("""
1. Add Task
2. View All Tasks
3. Delete Task
4. Mark Task as Done
5. View Done/Pending Tasks
6. Exit
""")

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
            view_status_task()
        elif choice == 6:
            print("Thank you")
            break
    except ValueError as e:
        print("Error: " + str(e))
