from tkinter import *
from tkinter import messagebox

tasks = []

# Add Task
def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    due_date = date_entry.get()
    if task == "" or due_date == "":
        messagebox.showwarning("Warning", "Enter task and due date!")
        return

    tasks.append(f"[{priority}] {task} - Due: {due_date}")
    update_list()

    task_entry.delete(0, END)
    date_entry.delete(0, END)

# Update Listbox
def update_list():
    listbox.delete(0, END)

    for task in tasks:
        listbox.insert(END, task)

# Delete Task
def delete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    tasks.pop(selected[0])
    update_list()

# Edit Task
def edit_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    task = task_entry.get()
    priority = priority_var.get()
    due_date = date_entry.get()

    if task == "" or due_date == "":
        messagebox.showwarning("Warning", "Enter task and due date!")
        return

    tasks[selected[0]] = f"[{priority}] {task} - Due: {due_date}"
    update_list()

    task_entry.delete(0, END)
    date_entry.delete(0, END)

# Mark Complete
def complete_task():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task!")
        return

    tasks[selected[0]] = "✔ " + tasks[selected[0]]
    update_list()

# Save Tasks
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

    messagebox.showinfo("Success", "Tasks Saved!")
def select_task(event):
    selected = listbox.curselection()

    if not selected:
        return

    task, priority, due_date = tasks[selected[0]]

    task_entry.delete(0, END)
    task_entry.insert(0, task)

    priority_var.set(priority)

    date_entry.delete(0, END)
    date_entry.insert(0, due_date)
    
# Load Tasks
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

        update_list()

    except FileNotFoundError:
        pass

# GUI
root = Tk()
root.title("To-Do List App")
root.geometry("500x600")

Label(root, text="TO-DO LIST", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Task").pack()
task_entry = Entry(root, width=35)
task_entry.pack(pady=5)

Label(root, text="Priority").pack()

priority_var = StringVar()
priority_var.set("Medium")

OptionMenu(root, priority_var, "High", "Medium", "Low").pack(pady=5)

Label(root, text="Due Date (DD/MM/YYYY)").pack()
date_entry = Entry(root, width=25)
date_entry.pack(pady=5)

Button(root, text="Add Task", width=15, command=add_task).pack(pady=5)
Button(root, text="Edit Task", width=15, command=edit_task).pack(pady=5)
Button(root, text="Delete Task", width=15, command=delete_task).pack(pady=5)
Button(root, text="Mark Complete", width=15, command=complete_task).pack(pady=5)
Button(root, text="Save Tasks", width=15, command=save_tasks).pack(pady=5)


listbox = Listbox(root, width=55, height=15)
listbox.pack(pady=15)

listbox.bind("<<ListboxSelect>>", select_task)

# Load saved tasks when app starts
load_tasks()

root.mainloop()