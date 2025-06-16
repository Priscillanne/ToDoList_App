# **Iteration 1: report**

The first iteration of the To-Do-List application is a basic command-line interface which was developed using python, in the application allows users to: 

1. Add tasks
2. View all tasks
3. Delete tasks 
4. Mark tasks as done 
5. Filter tasks based on their status

Each task is stored as a dictionary containing two fields whose name and status are set to “pending” upon creation. The menu-driven interface guides the user through each operation which ensures a smooth interaction experience. 

## Key feature 

**Key feature implemented in this iteration is :** 
* The ability to mark a task with any custom status such as “done” or “in progress” instead of limiting it to just “Done”. This provides users with greater flexibility in tracking their task progress.
* Users can view tasks filtered by specific statuses, which enhance task management clarity. 
* Proper error handling has been incorporated across all features, ensuring that invalid inputs and edge cases like an empty task list or incorrect task numbers are handled gracefully, preventing the application from crashing.

## Enhancement 
While the feature set aligns well with standard to-do-list functionality, a few enhancements were deliberately made. 

**For example,** 
* The ability to input custom status names (instead of hardcoding “done”) makes the system more realistic and adaptable. 
* All user inputs are validated with appropriate error messages to improve the overall robustness of the system.

## Limitations 
This iteration sets a solid foundation for future development, although the application functions effectively in its current form, 
* It lacks persistence data storage when all tasks are lost when the program exits. This will be addressed in the next iteration.

## Conclusion
Overall this iteration successfully delivers a fully functional, text based task manager with clean modular code and a focus on user experience.
