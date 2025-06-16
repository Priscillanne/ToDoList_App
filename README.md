# Iteration 2

In this second iteration, the To-Do-List application was significantly upgraded to include 

1. Due date
2. Priority 
3. Category for each task. 

## Key Features Added

The most notable enhancements in this iteration include:

- **Due Date Support**  
  Users can now assign a deadline to each task using the format `yyyy-mm-dd`. This helps in prioritizing time-sensitive activities.

- **Priority Level**  
  Users can set a task's priority to `High`, `Medium`, or `Low`, which helps in focusing on critical items first.

- **Task Category**  
  A new “category” field allows grouping tasks based on purpose (e.g., Work, Personal, School), making task management more contextual.

- **Input Validation**  
  Input validation was added to:
  - Ensure users enter dates in the correct `yyyy-mm-dd` format  
  - Restrict selection of priority to valid levels only (High, Medium, Low)


## Updated Existing Features

All existing core features from Iteration 1 were updated to support the new fields. These include:

1. **Add Task**  
   Now includes due date, priority, and category fields in addition to task name and status.

2. **View All Tasks**  
   Tasks are displayed with full details, making the list more informative and meaningful.

3. **Delete Task**  
   Works with the enhanced data model and removes tasks along with all their attributes.

4. **Update Task Status**  
   Supports tasks with due dates and priorities while preserving user-defined progress labels.

5. **Filter by Status**  
   The filtering functionality continues to work effectively, now showing all fields for each task.

## Enhancements and Design Considerations 
These features were adapted to support and display the new fields. The view functions now provide a richer and more informative output which improves the overall user experience not only that but status filtering also reflects these changes like showing tasks along with their new details when filtered.


## Limitations and Future Scope
No core functionality was removed but features were enhanced to offer more flexibility without sacrificing simplicity. While this version does not support persistent storage or filtering by category or priority, it lays the foundation for future improvement like file saving and advanced search. This iteration moves the app closer to becoming a reliable daily task planner.

## Conclusion 
This iteration significantly improves the application's usefulness as a daily planning tool. By introducing due dates, priorities, and categories, and upgrading all existing features accordingly, the app is now better equipped to serve users' real-world task management needs while still remaining light, accessible, and easy to use.
