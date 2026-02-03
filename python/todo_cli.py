import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks):
    """Add a new task."""
    title = input("\nEnter task: ").strip()
    if not title:
        print("Task cannot be empty!")
        return
    
    priority = input("Priority (High/Medium/Low) [default: Medium]: ").strip() or "Medium"
    due_date = input("Due date (YYYY-MM-DD) [optional]: ").strip() or "None"
    
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(task)
    save_tasks(tasks)
    print(f"✓ Task '{title}' added successfully!")

def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("\nNo tasks found!")
        return
    
    # Separate completed and pending tasks
    pending = [t for t in tasks if not t["completed"]]
    completed = [t for t in tasks if t["completed"]]
    
    if pending:
        print("\n" + "="*80)
        print("PENDING TASKS")
        print("="*80)
        for task in pending:
            status = "○"
            priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}.get(task["priority"], "")
            due = f" | Due: {task['due_date']}" if task["due_date"] != "None" else ""
            print(f"{status} [{task['id']}] {task['title']} {priority_color}{due}")
        print("="*80)
    
    if completed:
        print("\n✓ COMPLETED TASKS")
        print("-"*80)
        for task in completed:
            print(f"✓ [{task['id']}] {task['title']}")
        print("-"*80)

def view_task(tasks):
    """View task details."""
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("\nEnter task ID to view: "))
        for task in tasks:
            if task["id"] == task_id:
                print(f"\n--- Task #{task_id} ---")
                print(f"Title: {task['title']}")
                print(f"Priority: {task['priority']}")
                print(f"Due Date: {task['due_date']}")
                print(f"Status: {'✓ Completed' if task['completed'] else '○ Pending'}")
                print(f"Created: {task['created']}")
                return
        print("Task not found!")
    except ValueError:
        print("Please enter a valid ID!")

def toggle_task(tasks):
    """Mark task as complete/incomplete."""
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("\nEnter task ID to toggle: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                save_tasks(tasks)
                status = "✓ marked as complete" if task["completed"] else "○ marked as pending"
                print(f"Task '{task['title']}' {status}!")
                return
        print("Task not found!")
    except ValueError:
        print("Please enter a valid ID!")

def delete_task(tasks):
    """Delete a task."""
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                title = task["title"]
                confirm = input(f"Delete '{title}'? (y/n): ").lower()
                if confirm == 'y':
                    tasks.pop(i)
                    # Renumber remaining tasks
                    for j, t in enumerate(tasks):
                        t["id"] = j + 1
                    save_tasks(tasks)
                    print(f"✓ Task '{title}' deleted!")
                else:
                    print("Deletion cancelled.")
                return
        print("Task not found!")
    except ValueError:
        print("Please enter a valid ID!")

def clear_completed(tasks):
    """Clear all completed tasks."""
    completed_count = sum(1 for t in tasks if t["completed"])
    if completed_count == 0:
        print("\nNo completed tasks to clear!")
        return
    
    confirm = input(f"Clear {completed_count} completed task(s)? (y/n): ").lower()
    if confirm == 'y':
        tasks[:] = [t for t in tasks if not t["completed"]]
        # Renumber remaining tasks
        for i, t in enumerate(tasks):
            t["id"] = i + 1
        save_tasks(tasks)
        print(f"✓ Cleared {completed_count} completed task(s)!")
    else:
        print("Cancelled.")

def filter_by_priority(tasks):
    """Filter tasks by priority."""
    priority = input("\nFilter by priority (High/Medium/Low): ").strip()
    if priority not in ["High", "Medium", "Low"]:
        print("Invalid priority!")
        return
    
    filtered = [t for t in tasks if t["priority"] == priority and not t["completed"]]
    
    if not filtered:
        print(f"\nNo {priority} priority tasks found!")
        return
    
    print(f"\n{priority.upper()} PRIORITY TASKS")
    print("="*60)
    for task in filtered:
        due = f" | Due: {task['due_date']}" if task["due_date"] != "None" else ""
        print(f"[{task['id']}] {task['title']}{due}")
    print("="*60)

def statistics(tasks):
    """Show task statistics."""
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    
    print("\n" + "="*40)
    print("STATISTICS")
    print("="*40)
    print(f"Total Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    
    if total > 0:
        completion_rate = (completed / total) * 100
        print(f"Completion Rate: {completion_rate:.1f}%")
    
    # Priority breakdown
    high = sum(1 for t in tasks if t["priority"] == "High" and not t["completed"])
    medium = sum(1 for t in tasks if t["priority"] == "Medium" and not t["completed"])
    low = sum(1 for t in tasks if t["priority"] == "Low" and not t["completed"])
    
    print(f"\nPending by Priority:")
    print(f"  High: {high}")
    print(f"  Medium: {medium}")
    print(f"  Low: {low}")
    print("="*40)

def main():
    """Main application loop."""
    print("\n" + "="*50)
    print("WELCOME TO TODO LIST MANAGER")
    print("="*50)
    
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. View Task Details")
        print("4. Toggle Task (Complete/Pending)")
        print("5. Delete Task")
        print("6. Filter by Priority")
        print("7. Clear Completed Tasks")
        print("8. Statistics")
        print("9. Exit")
        
        choice = input("\nChoose an option (1-9): ").strip()
        
        tasks = load_tasks()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            view_task(tasks)
        elif choice == '4':
            toggle_task(tasks)
        elif choice == '5':
            delete_task(tasks)
        elif choice == '6':
            filter_by_priority(tasks)
        elif choice == '7':
            clear_completed(tasks)
        elif choice == '8':
            statistics(tasks)
        elif choice == '9':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
