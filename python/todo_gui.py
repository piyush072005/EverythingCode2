import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import json
import os
from datetime import datetime
from tkcalendar import DateEntry

TASKS_FILE = "gui_tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Manager")
        self.root.geometry("900x650")
        self.root.configure(bg="#f0f0f0")
        
        self.tasks = self.load_tasks()
        self.current_task = None
        
        self.create_widgets()
        self.refresh_task_list()
    
    def create_widgets(self):
        """Create GUI widgets."""
        # Header
        header = tk.Frame(self.root, bg="#2c3e50")
        header.pack(fill=tk.X)
        
        title_label = tk.Label(header, text="My Todo List", font=("Arial", 20, "bold"), 
                               fg="white", bg="#2c3e50")
        title_label.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="➕ Add Task", command=self.add_task, 
                  bg="#27ae60", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="✏️ Edit", command=self.edit_task, 
                  bg="#f39c12", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="✓ Complete", command=self.toggle_task, 
                  bg="#3498db", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="🗑️ Delete", command=self.delete_task, 
                  bg="#e74c3c", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="📊 Stats", command=self.show_statistics, 
                  bg="#9b59b6", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        
        # Filter Frame
        filter_frame = tk.Frame(self.root, bg="#ecf0f1")
        filter_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(filter_frame, text="Filter:", font=("Arial", 10), bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        self.filter_var = tk.StringVar(value="All")
        tk.Radiobutton(filter_frame, text="All", variable=self.filter_var, value="All", 
                       command=self.refresh_task_list, bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(filter_frame, text="Pending", variable=self.filter_var, value="Pending", 
                       command=self.refresh_task_list, bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(filter_frame, text="Completed", variable=self.filter_var, value="Completed", 
                       command=self.refresh_task_list, bg="#ecf0f1").pack(side=tk.LEFT, padx=5)
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, bg="#f0f0f0")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tasks List
        list_frame = tk.Frame(content_frame, bg="white", relief=tk.SUNKEN, bd=1)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=(0, 10))
        
        list_label = tk.Label(list_frame, text="Tasks", font=("Arial", 12, "bold"), bg="white")
        list_label.pack(fill=tk.X, pady=(0, 10), padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.task_listbox = tk.Listbox(list_frame, font=("Arial", 10), 
                                       yscrollcommand=scrollbar.set, bg="white", height=20)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.task_listbox.bind('<<ListboxSelect>>', self.on_task_select)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Info Frame
        info_frame = tk.Frame(self.root, bg="#ecf0f1", relief=tk.SUNKEN, bd=1)
        info_frame.pack(fill=tk.X, padx=10, pady=(0, 10), ipady=5)
        
        self.info_label = tk.Label(info_frame, text="Select a task to view details", 
                                   font=("Arial", 9), bg="#ecf0f1", fg="#7f8c8d")
        self.info_label.pack(anchor=tk.W)
    
    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, "r") as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)
    
    def refresh_task_list(self):
        """Refresh the tasks listbox."""
        self.task_listbox.delete(0, tk.END)
        filter_type = self.filter_var.get()
        
        for task in self.tasks:
            if filter_type == "Pending" and task["completed"]:
                continue
            if filter_type == "Completed" and not task["completed"]:
                continue
            
            status = "✓" if task["completed"] else "○"
            priority_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(task["priority"], "")
            display = f"{status} [{task['id']}] {task['title']} {priority_icon}"
            self.task_listbox.insert(tk.END, display)
    
    def on_task_select(self, event):
        """Handle task selection."""
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            # Find the actual task index in the full list
            filter_type = self.filter_var.get()
            count = 0
            for i, task in enumerate(self.tasks):
                if filter_type == "Pending" and task["completed"]:
                    continue
                if filter_type == "Completed" and not task["completed"]:
                    continue
                if count == index:
                    self.current_task = i
                    self.display_task_info(i)
                    return
                count += 1
    
    def display_task_info(self, index):
        """Display task details."""
        task = self.tasks[index]
        status = "✓ Completed" if task["completed"] else "○ Pending"
        info = f"ID: {task['id']} | Status: {status} | Priority: {task['priority']} | Due: {task['due_date']} | Created: {task['created']}"
        self.info_label.config(text=info)
    
    def add_task(self):
        """Add a new task."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add New Task")
        add_window.geometry("500x350")
        
        # Title
        tk.Label(add_window, text="Task Title:", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        title_entry = tk.Entry(add_window, font=("Arial", 10), width=50)
        title_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        # Priority
        tk.Label(add_window, text="Priority:", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        priority_var = tk.StringVar(value="Medium")
        priority_frame = tk.Frame(add_window)
        priority_frame.pack(padx=10, anchor=tk.W)
        for priority in ["High", "Medium", "Low"]:
            tk.Radiobutton(priority_frame, text=priority, variable=priority_var, 
                          value=priority).pack(side=tk.LEFT)
        
        # Due Date
        tk.Label(add_window, text="Due Date:", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        try:
            date_entry = DateEntry(add_window, width=15, font=("Arial", 10))
            date_entry.pack(pady=(0, 10), padx=10, anchor=tk.W)
            has_calendar = True
        except:
            has_calendar = False
            date_entry = tk.Entry(add_window, font=("Arial", 10), width=15)
            date_entry.pack(pady=(0, 10), padx=10, anchor=tk.W)
            date_entry.insert(0, "YYYY-MM-DD")
        
        # Description
        tk.Label(add_window, text="Description (optional):", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        desc_text = scrolledtext.ScrolledText(add_window, font=("Arial", 9), height=5, width=50)
        desc_text.pack(pady=(0, 10), padx=10, fill=tk.BOTH, expand=True)
        
        def save_task():
            title = title_entry.get().strip()
            if not title:
                messagebox.showerror("Error", "Task title cannot be empty!")
                return
            
            due_date = date_entry.get() if has_calendar else date_entry.get()
            description = desc_text.get(1.0, tk.END).strip() or "None"
            
            task = {
                "id": len(self.tasks) + 1,
                "title": title,
                "priority": priority_var.get(),
                "due_date": due_date,
                "description": description,
                "completed": False,
                "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            self.tasks.append(task)
            self.save_tasks()
            self.refresh_task_list()
            messagebox.showinfo("Success", f"Task '{title}' added!")
            add_window.destroy()
        
        button_frame = tk.Frame(add_window)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="Save", command=save_task, 
                  bg="#27ae60", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=add_window.destroy, 
                  bg="#95a5a6", fg="white", width=10).pack(side=tk.LEFT, padx=5)
    
    def edit_task(self):
        """Edit the selected task."""
        if self.current_task is None:
            messagebox.showwarning("Warning", "Please select a task to edit!")
            return
        
        task = self.tasks[self.current_task]
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit Task - {task['title']}")
        edit_window.geometry("500x350")
        
        tk.Label(edit_window, text="Task Title:", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        title_entry = tk.Entry(edit_window, font=("Arial", 10), width=50)
        title_entry.insert(0, task["title"])
        title_entry.pack(pady=(0, 10), padx=10, fill=tk.X)
        
        tk.Label(edit_window, text="Priority:", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        priority_var = tk.StringVar(value=task["priority"])
        priority_frame = tk.Frame(edit_window)
        priority_frame.pack(padx=10, anchor=tk.W)
        for priority in ["High", "Medium", "Low"]:
            tk.Radiobutton(priority_frame, text=priority, variable=priority_var, 
                          value=priority).pack(side=tk.LEFT)
        
        tk.Label(edit_window, text="Due Date:", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        date_entry = tk.Entry(edit_window, font=("Arial", 10), width=15)
        date_entry.insert(0, task["due_date"])
        date_entry.pack(pady=(0, 10), padx=10, anchor=tk.W)
        
        tk.Label(edit_window, text="Description:", font=("Arial", 10, "bold")).pack(pady=(10, 0), padx=10, anchor=tk.W)
        desc_text = scrolledtext.ScrolledText(edit_window, font=("Arial", 9), height=5, width=50)
        desc_text.insert(1.0, task.get("description", ""))
        desc_text.pack(pady=(0, 10), padx=10, fill=tk.BOTH, expand=True)
        
        def save_changes():
            task["title"] = title_entry.get().strip()
            task["priority"] = priority_var.get()
            task["due_date"] = date_entry.get()
            task["description"] = desc_text.get(1.0, tk.END).strip() or "None"
            self.save_tasks()
            self.refresh_task_list()
            messagebox.showinfo("Success", "Task updated!")
            edit_window.destroy()
        
        button_frame = tk.Frame(edit_window)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="Save", command=save_changes, 
                  bg="#27ae60", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=edit_window.destroy, 
                  bg="#95a5a6", fg="white", width=10).pack(side=tk.LEFT, padx=5)
    
    def toggle_task(self):
        """Mark task as complete/incomplete."""
        if self.current_task is None:
            messagebox.showwarning("Warning", "Please select a task!")
            return
        
        task = self.tasks[self.current_task]
        task["completed"] = not task["completed"]
        self.save_tasks()
        self.refresh_task_list()
        status = "✓ marked complete" if task["completed"] else "marked pending"
        messagebox.showinfo("Success", f"Task {status}!")
    
    def delete_task(self):
        """Delete the selected task."""
        if self.current_task is None:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return
        
        task = self.tasks[self.current_task]
        if messagebox.askyesno("Confirm", f"Delete '{task['title']}'?"):
            self.tasks.pop(self.current_task)
            self.save_tasks()
            self.current_task = None
            self.refresh_task_list()
            self.info_label.config(text="Task deleted.")
    
    def show_statistics(self):
        """Show task statistics."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        pending = total - completed
        
        high = sum(1 for t in self.tasks if t["priority"] == "High" and not t["completed"])
        medium = sum(1 for t in self.tasks if t["priority"] == "Medium" and not t["completed"])
        low = sum(1 for t in self.tasks if t["priority"] == "Low" and not t["completed"])
        
        stats_text = f"""
TASK STATISTICS

Total Tasks: {total}
Completed: {completed}
Pending: {pending}

Completion Rate: {(completed/total*100):.1f if total > 0 else 0}%

Pending by Priority:
  High: {high}
  Medium: {medium}
  Low: {low}
"""
        
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Statistics")
        stats_window.geometry("400x300")
        
        text = tk.Text(stats_window, font=("Courier", 11), bg="white")
        text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text.insert(1.0, stats_text)
        text.config(state=tk.DISABLED)
        
        tk.Button(stats_window, text="Close", command=stats_window.destroy, 
                  bg="#95a5a6", fg="white").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
