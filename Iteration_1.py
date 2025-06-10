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

        # functions not yet defined, will be added in next steps
        if (choice == 1): 
            pass
        elif (choice == 2):
            pass
        elif (choice == 3):
            pass
        elif (choice == 4):
            pass
        elif (choice == 5):
            pass
        elif(choice == 6):
            print("Thank you")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError as e:
        print("Error: " + str(e))
