import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, scrolledtext
import json
import os
from datetime import datetime

NOTES_FILE = "gui_notes.json"

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note-Taking Application")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")
        
        self.notes = self.load_notes()
        self.current_note = None
        
        self.create_widgets()
        self.refresh_note_list()
    
    def create_widgets(self):
        """Create GUI widgets."""
        # Header
        header = tk.Frame(self.root, bg="#2c3e50")
        header.pack(fill=tk.X)
        
        title_label = tk.Label(header, text="My Notes", font=("Arial", 20, "bold"), 
                               fg="white", bg="#2c3e50")
        title_label.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="➕ New Note", command=self.create_note, 
                  bg="#27ae60", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="✏️ Edit", command=self.edit_note, 
                  bg="#f39c12", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="🗑️ Delete", command=self.delete_note, 
                  bg="#e74c3c", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="💾 Export", command=self.export_notes, 
                  bg="#3498db", fg="white", width=12).pack(side=tk.LEFT, padx=5)
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, bg="#f0f0f0")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Notes List (Left)
        list_frame = tk.Frame(content_frame, bg="white", relief=tk.SUNKEN, bd=1)
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10), 
                        ipady=5, ipadx=5)
        
        list_label = tk.Label(list_frame, text="Notes", font=("Arial", 12, "bold"), 
                              bg="white")
        list_label.pack(fill=tk.X, pady=(0, 10))
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.notes_listbox = tk.Listbox(list_frame, font=("Arial", 10), 
                                        yscrollcommand=scrollbar.set, width=25, 
                                        height=20, bg="white")
        self.notes_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.notes_listbox.bind('<<ListboxSelect>>', self.on_note_select)
        scrollbar.config(command=self.notes_listbox.yview)
        
        # Note Display (Right)
        display_frame = tk.Frame(content_frame, bg="white", relief=tk.SUNKEN, bd=1)
        display_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        display_label = tk.Label(display_frame, text="Content", font=("Arial", 12, "bold"), 
                                 bg="white")
        display_label.pack(fill=tk.X, pady=(0, 10), padx=5, pady=5)
        
        self.note_display = scrolledtext.ScrolledText(display_frame, font=("Arial", 10), 
                                                      wrap=tk.WORD, bg="white", 
                                                      state=tk.DISABLED)
        self.note_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Info Frame
        info_frame = tk.Frame(self.root, bg="#ecf0f1", relief=tk.SUNKEN, bd=1)
        info_frame.pack(fill=tk.X, padx=10, pady=(0, 10), ipady=5)
        
        self.info_label = tk.Label(info_frame, text="Select a note to view details", 
                                   font=("Arial", 9), bg="#ecf0f1", fg="#7f8c8d")
        self.info_label.pack(anchor=tk.W)
    
    def load_notes(self):
        """Load notes from JSON file."""
        if os.path.exists(NOTES_FILE):
            try:
                with open(NOTES_FILE, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_notes(self):
        """Save notes to JSON file."""
        with open(NOTES_FILE, "w") as f:
            json.dump(self.notes, f, indent=2)
    
    def refresh_note_list(self):
        """Refresh the notes listbox."""
        self.notes_listbox.delete(0, tk.END)
        for title in self.notes.keys():
            self.notes_listbox.insert(tk.END, title)
    
    def on_note_select(self, event):
        """Handle note selection from listbox."""
        selection = self.notes_listbox.curselection()
        if selection:
            index = selection[0]
            title = self.notes_listbox.get(index)
            self.current_note = title
            self.display_note(title)
    
    def display_note(self, title):
        """Display a note in the display area."""
        if title in self.notes:
            data = self.notes[title]
            self.note_display.config(state=tk.NORMAL)
            self.note_display.delete(1.0, tk.END)
            self.note_display.insert(1.0, data["content"])
            self.note_display.config(state=tk.DISABLED)
            
            self.info_label.config(
                text=f"Created: {data['created']} | Modified: {data['modified']}"
            )
    
    def create_note(self):
        """Create a new note."""
        title = simpledialog.askstring("New Note", "Enter note title:")
        if title is None:
            return
        
        if not title.strip():
            messagebox.showerror("Error", "Title cannot be empty!")
            return
        
        if title in self.notes:
            messagebox.showerror("Error", "Note with this title already exists!")
            return
        
        # Create edit window
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit - {title}")
        edit_window.geometry("600x400")
        
        text_area = scrolledtext.ScrolledText(edit_window, font=("Arial", 11), 
                                              wrap=tk.WORD)
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        def save_new_note():
            content = text_area.get(1.0, tk.END).strip()
            if content:
                self.notes[title] = {
                    "content": content,
                    "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                self.save_notes()
                self.refresh_note_list()
                messagebox.showinfo("Success", f"Note '{title}' created!")
                edit_window.destroy()
            else:
                messagebox.showerror("Error", "Note cannot be empty!")
        
        button_frame = tk.Frame(edit_window)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="Save", command=save_new_note, 
                  bg="#27ae60", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=edit_window.destroy, 
                  bg="#95a5a6", fg="white", width=10).pack(side=tk.LEFT, padx=5)
    
    def edit_note(self):
        """Edit the selected note."""
        if self.current_note is None:
            messagebox.showwarning("Warning", "Please select a note to edit!")
            return
        
        title = self.current_note
        data = self.notes[title]
        
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit - {title}")
        edit_window.geometry("600x400")
        
        text_area = scrolledtext.ScrolledText(edit_window, font=("Arial", 11), 
                                              wrap=tk.WORD)
        text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_area.insert(1.0, data["content"])
        
        def save_edited_note():
            content = text_area.get(1.0, tk.END).strip()
            if content:
                self.notes[title]["content"] = content
                self.notes[title]["modified"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                self.display_note(title)
                messagebox.showinfo("Success", "Note updated!")
                edit_window.destroy()
            else:
                messagebox.showerror("Error", "Note cannot be empty!")
        
        button_frame = tk.Frame(edit_window)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(button_frame, text="Save", command=save_edited_note, 
                  bg="#27ae60", fg="white", width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=edit_window.destroy, 
                  bg="#95a5a6", fg="white", width=10).pack(side=tk.LEFT, padx=5)
    
    def delete_note(self):
        """Delete the selected note."""
        if self.current_note is None:
            messagebox.showwarning("Warning", "Please select a note to delete!")
            return
        
        if messagebox.askyesno("Confirm", 
                               f"Delete '{self.current_note}'?"):
            del self.notes[self.current_note]
            self.save_notes()
            self.current_note = None
            self.refresh_note_list()
            self.note_display.config(state=tk.NORMAL)
            self.note_display.delete(1.0, tk.END)
            self.note_display.config(state=tk.DISABLED)
            self.info_label.config(text="Note deleted. Select another note to view.")
            messagebox.showinfo("Success", "Note deleted!")
    
    def export_notes(self):
        """Export all notes to a text file."""
        if not self.notes:
            messagebox.showwarning("Warning", "No notes to export!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, "w") as f:
                    for title, data in self.notes.items():
                        f.write(f"{'='*60}\n")
                        f.write(f"Title: {title}\n")
                        f.write(f"Created: {data['created']}\n")
                        f.write(f"Modified: {data['modified']}\n")
                        f.write(f"{'='*60}\n")
                        f.write(f"{data['content']}\n\n")
                messagebox.showinfo("Success", "Notes exported successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
