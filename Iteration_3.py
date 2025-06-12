import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

# Global task list
task_list = []

# Function to refresh the task display
def refresh_task_display():
    for widget in task_frame.winfo_children():
        widget.destroy()

    if not task_list:
        tk.Label(task_frame, text="No tasks added.", fg="gray").pack()
        return

    for i, task in enumerate(task_list, start=1):
        display = f"{i}. {task['name']} - {task['status']}"
        label = tk.Label(task_frame, text=display, anchor="w", justify="left", padx=10, pady=5, bg="white", relief="groove")
        label.pack(fill="x", padx=5, pady=4)

# Add a new task
def add_task():
    task_name = simpledialog.askstring("Add Task", "Enter the task:")
    if not task_name:
        return
    task = {"name": task_name, "status": "Pending"}
    task_list.append(task)
    refresh_task_display()

# Delete a task
def delete_task():
    if not task_list:
        messagebox.showerror("Error", "List is empty.")
        return

    task_number = simpledialog.askinteger("Delete Task", "Enter task number to delete:")
    if task_number is None:
        return

    if 1 <= task_number <= len(task_list):
        deleted = task_list.pop(task_number - 1)
        messagebox.showinfo("Deleted", f'Task {task_number}: "{deleted["name"]}" has been deleted.')
        refresh_task_display()
    else:
        messagebox.showerror("Error", "That task does not exist.")

# Mark a task as done
def mark_task_done():
    if not task_list:
        messagebox.showerror("Error", "List is empty.")
        return

    task_number = simpledialog.askinteger("Mark Task as Done", "Enter task number to mark as done:")
    if task_number is None:
        return

    if 1 <= task_number <= len(task_list):
        task_list[task_number - 1]["status"] = "Done"
        messagebox.showinfo("Updated", f'Task {task_number} marked as Done.')
        refresh_task_display()
    else:
        messagebox.showerror("Error", "That task does not exist.")

# View tasks filtered by status
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

# GUI setup
root = tk.Tk()
root.title("To-Do List App - Iteration 1")
root.geometry("420x450")
root.configure(bg="#f0f0f0")

# Main layout frame
main_frame = tk.Frame(root, padx=10, pady=10, bg="#f0f0f0")
main_frame.pack(fill="both", expand=True)

# App Title
tk.Label(main_frame, text="To-Do List", font=("Arial", 18, "bold"), bg="#f0f0f0").pack()

# Buttons layout
button_frame = tk.Frame(main_frame, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Task", width=15, command=add_task).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Delete Task", width=15, command=delete_task).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Mark as Done", width=15, command=mark_task_done).grid(row=1, column=0, padx=5, pady=5)
tk.Button(button_frame, text="View by Status", width=15, command=view_by_status).grid(row=1, column=1, padx=5, pady=5)

# Scrollable task display area
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

task_frame = scrollable_frame  # Alias

# Exit Button
tk.Button(main_frame, text="Exit", command=root.quit).pack(pady=10)

# Initial task display
refresh_task_display()

root.mainloop()
