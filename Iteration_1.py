# Function 1: Add Task
def add_task():
    task = {
        "name" : input("Enter the task: "),
        "status" : "Pending"
    }
    print("Task \"{0}\" has been added.".format(task.get("name")))
    task_list.append(task)

print("To-Do List Menu")
print()

#print to-do list options
print(
    "1. Add Task\n"
    "2. View All Tasks\n"
    "3. Delete Task\n"
    "4. Mark Task as Done\n"
    "5. View Done/Pending Tasks\n"
    "6. Exit"
)

#define array for tasks
task_list = []

#repeat questions until option 6(exit)
while True:
    print()

    try:
        user_input = input("Enter your choice (1-6): ")

        try:
            choice = int(user_input)
        except:
            raise ValueError("Enter a number")

        if (choice <= 0) or (choice > 6):
            raise ValueError("Choose a number 1-6")

        if (choice == 1): 
            add_task()
        elif (choice == 2):
            view_all_task()
        elif (choice == 3):
            delete_task()
        elif (choice == 4):
            mark_done()
        elif (choice == 5):
            view_status_task()
        elif(choice == 6):
            print("Thank you")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError as e:
        print("Error: " + str(e))
