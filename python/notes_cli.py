import os
import json
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    """Load notes from JSON file."""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_notes(notes):
    """Save notes to JSON file."""
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def create_note(notes):
    """Create a new note."""
    title = input("\nEnter note title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return
    
    if title in notes:
        print("Note with this title already exists!")
        return
    
    content = input("Enter note content (press Enter twice to finish):\n")
    lines = [content]
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    notes[title] = {
        "content": "\n".join(lines),
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    save_notes(notes)
    print(f"\n✓ Note '{title}' created successfully!")

def view_note(notes):
    """View a specific note."""
    if not notes:
        print("\nNo notes found!")
        return
    
    print("\nAvailable notes:")
    for i, title in enumerate(notes.keys(), 1):
        print(f"{i}. {title}")
    
    try:
        choice = int(input("\nEnter note number: ")) - 1
        titles = list(notes.keys())
        if 0 <= choice < len(titles):
            title = titles[choice]
            note = notes[title]
            print(f"\n--- {title} ---")
            print(f"Content: {note['content']}")
            print(f"Created: {note['created']}")
            print(f"Modified: {note['modified']}")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")

def list_notes(notes):
    """List all notes."""
    if not notes:
        print("\nNo notes found!")
        return
    
    print("\n" + "="*50)
    print("YOUR NOTES")
    print("="*50)
    for i, (title, data) in enumerate(notes.items(), 1):
        print(f"{i}. {title} (Modified: {data['modified']})")
    print("="*50)

def edit_note(notes):
    """Edit an existing note."""
    if not notes:
        print("\nNo notes found!")
        return
    
    print("\nAvailable notes:")
    for i, title in enumerate(notes.keys(), 1):
        print(f"{i}. {title}")
    
    try:
        choice = int(input("\nEnter note number to edit: ")) - 1
        titles = list(notes.keys())
        if 0 <= choice < len(titles):
            title = titles[choice]
            print(f"\nEditing '{title}':")
            content = input("Enter new content (press Enter twice to finish):\n")
            lines = [content]
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            
            notes[title]["content"] = "\n".join(lines)
            notes[title]["modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print(f"\n✓ Note '{title}' updated successfully!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")

def delete_note(notes):
    """Delete a note."""
    if not notes:
        print("\nNo notes found!")
        return
    
    print("\nAvailable notes:")
    for i, title in enumerate(notes.keys(), 1):
        print(f"{i}. {title}")
    
    try:
        choice = int(input("\nEnter note number to delete: ")) - 1
        titles = list(notes.keys())
        if 0 <= choice < len(titles):
            title = titles[choice]
            confirm = input(f"Are you sure? (y/n): ").lower()
            if confirm == 'y':
                del notes[title]
                save_notes(notes)
                print(f"\n✓ Note '{title}' deleted!")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number!")

def search_notes(notes):
    """Search notes by keyword."""
    keyword = input("\nEnter search keyword: ").lower()
    results = []
    
    for title, data in notes.items():
        if keyword in title.lower() or keyword in data["content"].lower():
            results.append(title)
    
    if results:
        print(f"\nFound {len(results)} note(s):")
        for i, title in enumerate(results, 1):
            print(f"{i}. {title}")
    else:
        print("\nNo notes found matching your search!")

def main():
    """Main application loop."""
    print("\n" + "="*50)
    print("WELCOME TO CLI NOTE-TAKING APP")
    print("="*50)
    
    while True:
        print("\n1. Create Note")
        print("2. View Note")
        print("3. List All Notes")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Search Notes")
        print("7. Exit")
        
        choice = input("\nChoose an option (1-7): ").strip()
        
        notes = load_notes()
        
        if choice == '1':
            create_note(notes)
        elif choice == '2':
            view_note(notes)
        elif choice == '3':
            list_notes(notes)
        elif choice == '4':
            edit_note(notes)
        elif choice == '5':
            delete_note(notes)
        elif choice == '6':
            search_notes(notes)
        elif choice == '7':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
