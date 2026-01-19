import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfReader, PdfWriter
import os

class PDFToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger & Splitter")
        self.root.geometry("800x650")
        self.root.configure(bg="#ecf0f1")
        
        self.pdf_files = []
        
        # Header
        header = tk.Label(
            root,
            text="📄 PDF Merger & Splitter 📄",
            font=("Arial", 24, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        header.pack(pady=20)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Create tabs
        self.merge_tab = tk.Frame(self.notebook, bg="#ecf0f1")
        self.split_tab = tk.Frame(self.notebook, bg="#ecf0f1")
        
        self.notebook.add(self.merge_tab, text="  Merge PDFs  ")
        self.notebook.add(self.split_tab, text="  Split PDF  ")
        
        # Setup tabs
        self.setup_merge_tab()
        self.setup_split_tab()
        
    def setup_merge_tab(self):
        """Setup the merge tab interface"""
        # Instructions
        tk.Label(
            self.merge_tab,
            text="Select multiple PDF files to merge into one",
            font=("Arial", 12),
            bg="#ecf0f1",
            fg="#34495e"
        ).pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.merge_tab, bg="#ecf0f1")
        button_frame.pack(pady=10)
        
        tk.Button(
            button_frame,
            text="➕ Add PDF Files",
            command=self.add_pdf_files,
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            relief="raised"
        ).pack(side="left", padx=5)
        
        tk.Button(
            button_frame,
            text="🗑️ Clear All",
            command=self.clear_files,
            font=("Arial", 11, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2",
            relief="raised"
        ).pack(side="left", padx=5)
        
        # List frame with scrollbar
        list_frame = tk.Frame(self.merge_tab, bg="#ecf0f1")
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        tk.Label(
            list_frame,
            text="Selected Files (in merge order):",
            font=("Arial", 10, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        ).pack(anchor="w")
        
        # Scrollbar and listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.file_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 10),
            yscrollcommand=scrollbar.set,
            selectmode=tk.SINGLE,
            bg="white",
            relief="solid",
            borderwidth=1
        )
        self.file_listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Move buttons
        move_frame = tk.Frame(self.merge_tab, bg="#ecf0f1")
        move_frame.pack(pady=5)
        
        tk.Button(
            move_frame,
            text="⬆️ Move Up",
            command=self.move_up,
            font=("Arial", 9),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        tk.Button(
            move_frame,
            text="⬇️ Move Down",
            command=self.move_down,
            font=("Arial", 9),
            bg="#95a5a6",
            fg="white",
            padx=15,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        tk.Button(
            move_frame,
            text="❌ Remove",
            command=self.remove_file,
            font=("Arial", 9),
            bg="#e67e22",
            fg="white",
            padx=15,
            pady=5,
            cursor="hand2"
        ).pack(side="left", padx=5)
        
        # Merge button
        tk.Button(
            self.merge_tab,
            text="🔗 Merge PDFs",
            command=self.merge_pdfs,
            font=("Arial", 13, "bold"),
            bg="#27ae60",
            fg="white",
            padx=30,
            pady=12,
            cursor="hand2",
            relief="raised"
        ).pack(pady=15)
        
    def setup_split_tab(self):
        """Setup the split tab interface"""
        # Instructions
        tk.Label(
            self.split_tab,
            text="Select a PDF file to split into multiple files",
            font=("Arial", 12),
            bg="#ecf0f1",
            fg="#34495e"
        ).pack(pady=10)
        
        # File selection
        file_frame = tk.Frame(self.split_tab, bg="#ecf0f1")
        file_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Button(
            file_frame,
            text="📂 Select PDF File",
            command=self.select_pdf_to_split,
            font=("Arial", 11, "bold"),
            bg="#3498db",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack()
        
        self.split_file_label = tk.Label(
            file_frame,
            text="No file selected",
            font=("Arial", 10),
            bg="#ecf0f1",
            fg="#7f8c8d",
            wraplength=600
        )
        self.split_file_label.pack(pady=5)
        
        self.page_count_label = tk.Label(
            file_frame,
            text="",
            font=("Arial", 10, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        self.page_count_label.pack()
        
        # Split options
        options_frame = tk.LabelFrame(
            self.split_tab,
            text="Split Options",
            font=("Arial", 11, "bold"),
            bg="#ecf0f1",
            fg="#2c3e50",
            padx=20,
            pady=15
        )
        options_frame.pack(pady=20, padx=20, fill="x")
        
        self.split_mode = tk.StringVar(value="all")
        
        tk.Radiobutton(
            options_frame,
            text="Split into individual pages (one page per file)",
            variable=self.split_mode,
            value="all",
            font=("Arial", 10),
            bg="#ecf0f1",
            activebackground="#ecf0f1",
            command=self.toggle_range_input
        ).pack(anchor="w", pady=5)
        
        tk.Radiobutton(
            options_frame,
            text="Split by page range",
            variable=self.split_mode,
            value="range",
            font=("Arial", 10),
            bg="#ecf0f1",
            activebackground="#ecf0f1",
            command=self.toggle_range_input
        ).pack(anchor="w", pady=5)
        
        # Range input frame
        self.range_frame = tk.Frame(options_frame, bg="#ecf0f1")
        self.range_frame.pack(fill="x", pady=10)
        
        tk.Label(
            self.range_frame,
            text="Page range (e.g., 1-5, 7, 10-15):",
            font=("Arial", 10),
            bg="#ecf0f1"
        ).pack(side="left", padx=(20, 5))
        
        self.range_entry = tk.Entry(
            self.range_frame,
            font=("Arial", 10),
            width=30,
            state="disabled",
            relief="solid",
            borderwidth=1
        )
        self.range_entry.pack(side="left")
        
        # Split button
        tk.Button(
            self.split_tab,
            text="✂️ Split PDF",
            command=self.split_pdf,
            font=("Arial", 13, "bold"),
            bg="#9b59b6",
            fg="white",
            padx=30,
            pady=12,
            cursor="hand2",
            relief="raised"
        ).pack(pady=15)
        
        # Initialize range input state
        self.toggle_range_input()
        
    def add_pdf_files(self):
        """Add PDF files to merge list"""
        files = filedialog.askopenfilenames(
            title="Select PDF Files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if files:
            for file in files:
                if file not in self.pdf_files:
                    self.pdf_files.append(file)
                    self.file_listbox.insert(tk.END, os.path.basename(file))
    
    def clear_files(self):
        """Clear all files from list"""
        self.pdf_files.clear()
        self.file_listbox.delete(0, tk.END)
    
    def remove_file(self):
        """Remove selected file from list"""
        selection = self.file_listbox.curselection()
        if selection:
            index = selection[0]
            self.file_listbox.delete(index)
            self.pdf_files.pop(index)
    
    def move_up(self):
        """Move selected file up in list"""
        selection = self.file_listbox.curselection()
        if selection and selection[0] > 0:
            index = selection[0]
            # Swap in list
            self.pdf_files[index], self.pdf_files[index-1] = self.pdf_files[index-1], self.pdf_files[index]
            # Swap in listbox
            item = self.file_listbox.get(index)
            self.file_listbox.delete(index)
            self.file_listbox.insert(index-1, item)
            self.file_listbox.selection_set(index-1)
    
    def move_down(self):
        """Move selected file down in list"""
        selection = self.file_listbox.curselection()
        if selection and selection[0] < len(self.pdf_files) - 1:
            index = selection[0]
            # Swap in list
            self.pdf_files[index], self.pdf_files[index+1] = self.pdf_files[index+1], self.pdf_files[index]
            # Swap in listbox
            item = self.file_listbox.get(index)
            self.file_listbox.delete(index)
            self.file_listbox.insert(index+1, item)
            self.file_listbox.selection_set(index+1)
    
    def merge_pdfs(self):
        """Merge all selected PDFs into one"""
        if len(self.pdf_files) < 2:
            messagebox.showwarning("Warning", "Please select at least 2 PDF files to merge!")
            return
        
        output_path = filedialog.asksaveasfilename(
            title="Save Merged PDF As",
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            initialfile="merged.pdf"
        )
        
        if not output_path:
            return
        
        try:
            pdf_writer = PdfWriter()
            
            # Add all pages from all PDFs
            for pdf_file in self.pdf_files:
                pdf_reader = PdfReader(pdf_file)
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)
            
            # Write merged PDF
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
            
            messagebox.showinfo(
                "Success", 
                f"Successfully merged {len(self.pdf_files)} PDFs!\n\nSaved to:\n{output_path}"
            )
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{str(e)}")
    
    def select_pdf_to_split(self):
        """Select PDF file to split"""
        file_path = filedialog.askopenfilename(
            title="Select PDF File to Split",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                self.split_file_path = file_path
                pdf_reader = PdfReader(file_path)
                page_count = len(pdf_reader.pages)
                
                self.split_file_label.config(
                    text=f"Selected: {os.path.basename(file_path)}",
                    fg="#2c3e50"
                )
                self.page_count_label.config(text=f"Total Pages: {page_count}")
                self.split_page_count = page_count
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read PDF:\n{str(e)}")
                self.split_file_path = None
    
    def toggle_range_input(self):
        """Enable/disable range input based on split mode"""
        if self.split_mode.get() == "range":
            self.range_entry.config(state="normal")
        else:
            self.range_entry.config(state="disabled")
    
    def parse_page_range(self, range_str, max_pages):
        """Parse page range string and return list of page numbers"""
        pages = set()
        
        for part in range_str.split(','):
            part = part.strip()
            if '-' in part:
                start, end = part.split('-')
                start = int(start.strip())
                end = int(end.strip())
                if start < 1 or end > max_pages or start > end:
                    raise ValueError(f"Invalid range: {part}")
                pages.update(range(start, end + 1))
            else:
                page = int(part.strip())
                if page < 1 or page > max_pages:
                    raise ValueError(f"Invalid page: {page}")
                pages.add(page)
        
        return sorted(pages)
    
    def split_pdf(self):
        """Split PDF based on selected mode"""
        if not hasattr(self, 'split_file_path') or not self.split_file_path:
            messagebox.showwarning("Warning", "Please select a PDF file to split!")
            return
        
        output_dir = filedialog.askdirectory(title="Select Output Folder")
        if not output_dir:
            return
        
        try:
            pdf_reader = PdfReader(self.split_file_path)
            base_name = os.path.splitext(os.path.basename(self.split_file_path))[0]
            
            if self.split_mode.get() == "all":
                # Split into individual pages
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer = PdfWriter()
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                    
                    output_path = os.path.join(output_dir, f"{base_name}_page_{page_num + 1}.pdf")
                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
                
                messagebox.showinfo(
                    "Success",
                    f"Successfully split PDF into {len(pdf_reader.pages)} files!\n\nSaved to:\n{output_dir}"
                )
                
            else:
                # Split by range
                range_str = self.range_entry.get().strip()
                if not range_str:
                    messagebox.showwarning("Warning", "Please enter a page range!")
                    return
                
                try:
                    pages = self.parse_page_range(range_str, len(pdf_reader.pages))
                    
                    pdf_writer = PdfWriter()
                    for page_num in pages:
                        pdf_writer.add_page(pdf_reader.pages[page_num - 1])  # Convert to 0-indexed
                    
                    output_path = os.path.join(output_dir, f"{base_name}_pages_{range_str.replace(',', '_').replace('-', 'to')}.pdf")
                    with open(output_path, 'wb') as output_file:
                        pdf_writer.write(output_file)
                    
                    messagebox.showinfo(
                        "Success",
                        f"Successfully extracted {len(pages)} pages!\n\nSaved to:\n{output_path}"
                    )
                    
                except ValueError as e:
                    messagebox.showerror("Error", f"Invalid page range:\n{str(e)}")
                    return
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to split PDF:\n{str(e)}")

def main():
    root = tk.Tk()
    app = PDFToolkit(root)
    root.mainloop()

if __name__ == "__main__":
    main()
