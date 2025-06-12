import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os
import datetime

# Global list to store tasks
task_list = []
FILENAME = "tasks.json"  # File to store tasks persistently

# Load tasks from the JSON file
def load_tasks():
    global task_list
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            task_list.clear()
            task_list.extend(json.load(f))

# Save current task list to the JSON file
def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(task_list, f, indent=2)

# Check if the due date is in valid format
def validate_due_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Check if priority entered is valid (High, Medium, or Low)
def validate_priority(priority_str):
    return priority_str.capitalize() in ["High", "Medium", "Low"]

# Refresh the display area to show current tasks
def refresh_task_display():
    for widget in task_frame.winfo_children():
        widget.destroy()  # Clear old task widgets

    if not task_list:
        tk.Label(task_frame, text="No tasks added.", fg="gray").pack()
        return

    for i, task in enumerate(task_list, start=1):
        display = (
            f"{i}. {task['name']}\n"
            f"   • Status: {task['status']}\n"
            f"   • Due: {task.get('due_date', 'N/A')}\n"
            f"   • Priority: {task.get('priority', 'N/A')}\n"
            f"   • Category: {task.get('category', 'N/A')}"
        )
        label = tk.Label(task_frame, text=display, anchor="w", justify="left", padx=10, pady=5, bg="white", relief="groove")
        label.pack(fill="x", padx=5, pady=4)

# Add a new task using dialog inputs
def add_task():
    task_name = simpledialog.askstring("Add Task", "Enter the task:")
    if not task_name:
        return

    # Ask for due date and validate format
    while True:
        task_due = simpledialog.askstring("Due Date", "Enter due date (YYYY-MM-DD):")
        if task_due is None:
            return
        if validate_due_date(task_due):
            break
        else:
            messagebox.showerror("Invalid Input", "Incorrect date format. Please enter as YYYY-MM-DD.")

    # Ask for priority and validate input
    while True:
        task_priority = simpledialog.askstring("Priority", "Enter priority (High/Medium/Low):")
        if task_priority is None:
            return
        if validate_priority(task_priority):
            task_priority = task_priority.capitalize()
            break
        else:
            messagebox.showerror("Invalid Input", "Priority must be High, Medium, or Low.")

    # Ask for category (optional)
    task_category = simpledialog.askstring("Category", "Enter category (e.g., School, Work, Personal):")
    if task_category is None:
        task_category = "Uncategorized"

    # Create task dictionary and add to list
    task = {
        "name": task_name,
        "status": "Pending",
        "due_date": task_due,
        "priority": task_priority,
        "category": task_category
    }
    task_list.append(task)
    save_tasks()
    refresh_task_display()

# Delete a task by its number
def delete_task():
    if not task_list:
        messagebox.showerror("Error", "List is empty.")
        return

    task_number = simpledialog.askinteger("Delete Task", "Enter task number to delete:")
    if task_number is None:
        return

    if 1 <= task_number <= len(task_list):
        deleted = task_list.pop(task_number - 1)
        save_tasks()
        messagebox.showinfo("Deleted", f'Task {task_number}: "{deleted["name"]}" has been deleted.')
        refresh_task_display()
    else:
        messagebox.showerror("Error", "That task does not exist.")

# Mark a task as done by its number
def mark_task_done():
    if not task_list:
        messagebox.showerror("Error", "List is empty.")
        return

    task_number = simpledialog.askinteger("Mark Task as Done", "Enter task number to mark as done:")
    if task_number is None:
        return

    if 1 <= task_number <= len(task_list):
        task_list[task_number - 1]["status"] = "Done"
        save_tasks()
        messagebox.showinfo("Updated", f'Task {task_number} marked as Done.')
        refresh_task_display()
    else:
        messagebox.showerror("Error", "That task does not exist.")

# View tasks filtered by status (e.g., Done or Pending)
def view_by_status():
    if not task_list:
        messagebox.showerror("Error", "List is empty.")
        return

    status_filter = simpledialog.askstring("Filter Tasks", "Enter status to filter by (e.g., Done, Pending):")
    if status_filter:
        matching = [
            f"{i+1}. {t['name']} [{t['status']}]" 
            for i, t in enumerate(task_list) if t['status'].lower() == status_filter.lower()
        ]
        if matching:
            messagebox.showinfo(f"{status_filter} Tasks", "\n".join(matching))
        else:
            messagebox.showinfo("No Tasks", f"No tasks with status '{status_filter}'.")

# ---------------- GUI Setup ----------------

root = tk.Tk()
root.title("To-Do List App")
root.geometry("420x450")
root.configure(bg="#f0f0f0")

main_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True)

# Title
tk.Label(main_frame, text="To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0").pack()

# Buttons for core functions
button_frame = tk.Frame(main_frame, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", width=15, command=add_task).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Delete Task", width=15, command=delete_task).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Mark as Done", width=15, command=mark_task_done).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="View by Status", width=15, command=view_by_status).grid(row=1, column=1, padx=5, pady=5)

# Task display container with scrollbar
task_display_container = tk.Frame(main_frame, bd=2, relief="sunken")
task_display_container.pack(fill="both", expand=True)

canvas = tk.Canvas(task_display_container, bg="#ffffff")
scrollbar = ttk.Scrollbar(task_display_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#ffffff")

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Frame where tasks will appear
task_frame = scrollable_frame

# Exit button
tk.Button(main_frame, text="Exit", command=root.quit).pack(pady=10)

# Load existing tasks and start GUI
load_tasks()
refresh_task_display()

root.mainloop()
