# Iteration 3

In this third iteration, the To-Do-List application transitioned from a **console-based interface** to a fully functional **Graphical User Interface (GUI)** using **Tkinter**.  
This marks a significant **usability improvement**, making the app more **user-friendly** and **visually accessible**.


## GUI Task Operations
**All major task operations such as:**
- Adding
- Deleting
- Updating
- Filtering tasks - are now done through interactive dialog boxes and buttons, replacing terminal inputs.

## Task Attributes Retained
**Each task retains the previous attributes for consistency:**
- Name
- Status
- Due date
- Priority
- Category - for consistency, and tasks are displayed with clear formatting inside a scrollable window.

Tasks are displayed with **clear formatting** inside a **scrollable window**, improving readability and usability.

 ## Persistent Storage (Major Enhancement)

One of the most impactful additions in this iteration is persistent storage using JSON.
**Tasks are now:**
- Saved to a file (tasks.json)
- Automatically loaded when the application starts

This solves the biggest limitation of previous versions, where all data was lost once the app was closed.

## Additional Improvements

This iteration also introduces:

1) **Input validation** for:
  - Date format  
  - Priority level  

2) **Information message boxes** for:
  - Errors  
  - Confirmations  

3) A **smooth task display refresh mechanism** that updates the UI **instantly** after every change.

4) These features were implemented to align with **standard GUI expectations** while ensuring the app remains **lightweight** and **easy to use**.

5) A **deliberate design choice** was made to use `simpledialog` for inputs to maintain a **clean and straightforward interface**.

## Limitations & Future Work

While this version is highly improved, a few limitations remain:

- The app currently supports filtering by status only

**Future iterations could explore the following enhancements:**

- Advanced filtering (by category or due date)  
- Editing tasks  
- Color-coded task indicators

## Conclusion
In summary, iteration 3 successfully modernized the app interface, while strengthening its functionality with data persistence.
