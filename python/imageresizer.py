from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

class ImageResizerCompressor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer & Compressor")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f5f5f5")
        
        self.original_image = None
        self.processed_image = None
        self.display_photo = None
        self.image_path = None
        self.batch_files = []
        
        # Header
        header = tk.Label(
            root,
            text="🖼️ Image Resizer & Compressor 🖼️",
            font=("Arial", 24, "bold"),
            bg="#f5f5f5",
            fg="#2c3e50"
        )
        header.pack(pady=15)
        
        # Main container
        main_frame = tk.Frame(root, bg="#f5f5f5")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Left panel - Controls
        control_panel = tk.Frame(main_frame, bg="#ffffff", relief="raised", borderwidth=2)
        control_panel.pack(side="left", fill="y", padx=(0, 10))
        
        # Mode selection
        mode_frame = tk.LabelFrame(
            control_panel,
            text="Mode",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        mode_frame.pack(padx=10, pady=10, fill="x")
        
        self.mode_var = tk.StringVar(value="single")
        
        tk.Radiobutton(
            mode_frame,
            text="Single Image",
            variable=self.mode_var,
            value="single",
            font=("Arial", 10),
            bg="#ffffff",
            command=self.toggle_mode
        ).pack(anchor="w")
        
        tk.Radiobutton(
            mode_frame,
            text="Batch Processing",
            variable=self.mode_var,
            value="batch",
            font=("Arial", 10),
            bg="#ffffff",
            command=self.toggle_mode
        ).pack(anchor="w")
        
        # File selection
        file_frame = tk.LabelFrame(
            control_panel,
            text="File Selection",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        file_frame.pack(padx=10, pady=10, fill="x")
        
        self.load_btn = tk.Button(
            file_frame,
            text="📁 Load Image",
            command=self.load_image,
            font=("Arial", 10),
            bg="#3498db",
            fg="white",
            padx=15,
            pady=8,
            cursor="hand2"
        )
        self.load_btn.pack(fill="x", pady=2)
        
        self.batch_btn = tk.Button(
            file_frame,
            text="📂 Load Multiple",
            command=self.load_batch,
            font=("Arial", 10),
            bg="#9b59b6",
            fg="white",
            padx=15,
            pady=8,
            cursor="hand2",
            state="disabled"
        )
        self.batch_btn.pack(fill="x", pady=2)
        
        self.file_label = tk.Label(
            file_frame,
            text="No file loaded",
            font=("Arial", 9),
            bg="#ffffff",
            fg="#7f8c8d",
            wraplength=250
        )
        self.file_label.pack(pady=5)
        
        # Resize options
        resize_frame = tk.LabelFrame(
            control_panel,
            text="Resize Options",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        resize_frame.pack(padx=10, pady=10, fill="x")
        
        self.resize_mode = tk.StringVar(value="percentage")
        
        tk.Radiobutton(
            resize_frame,
            text="By Percentage",
            variable=self.resize_mode,
            value="percentage",
            font=("Arial", 9),
            bg="#ffffff",
            command=self.toggle_resize_inputs
        ).pack(anchor="w")
        
        # Percentage input
        self.percentage_frame = tk.Frame(resize_frame, bg="#ffffff")
        self.percentage_frame.pack(fill="x", pady=5)
        
        tk.Label(
            self.percentage_frame,
            text="Scale:",
            font=("Arial", 9),
            bg="#ffffff"
        ).pack(side="left")
        
        self.percentage_var = tk.IntVar(value=100)
        self.percentage_scale = tk.Scale(
            self.percentage_frame,
            from_=10,
            to=200,
            variable=self.percentage_var,
            orient="horizontal",
            bg="#ffffff",
            length=150
        )
        self.percentage_scale.pack(side="left", padx=5)
        
        self.percentage_label = tk.Label(
            self.percentage_frame,
            text="100%",
            font=("Arial", 9, "bold"),
            bg="#ffffff",
            width=5
        )
        self.percentage_label.pack(side="left")
        
        self.percentage_var.trace('w', self.update_percentage_label)
        
        tk.Radiobutton(
            resize_frame,
            text="Custom Dimensions",
            variable=self.resize_mode,
            value="custom",
            font=("Arial", 9),
            bg="#ffffff",
            command=self.toggle_resize_inputs
        ).pack(anchor="w", pady=(10, 0))
        
        # Custom dimensions
        self.custom_frame = tk.Frame(resize_frame, bg="#ffffff")
        self.custom_frame.pack(fill="x", pady=5)
        
        dim_row1 = tk.Frame(self.custom_frame, bg="#ffffff")
        dim_row1.pack(fill="x")
        
        tk.Label(
            dim_row1,
            text="Width:",
            font=("Arial", 9),
            bg="#ffffff",
            width=8
        ).pack(side="left")
        
        self.width_var = tk.StringVar()
        tk.Entry(
            dim_row1,
            textvariable=self.width_var,
            font=("Arial", 9),
            width=10,
            state="disabled"
        ).pack(side="left", padx=5)
        
        tk.Label(
            dim_row1,
            text="px",
            font=("Arial", 9),
            bg="#ffffff"
        ).pack(side="left")
        
        dim_row2 = tk.Frame(self.custom_frame, bg="#ffffff")
        dim_row2.pack(fill="x", pady=5)
        
        tk.Label(
            dim_row2,
            text="Height:",
            font=("Arial", 9),
            bg="#ffffff",
            width=8
        ).pack(side="left")
        
        self.height_var = tk.StringVar()
        tk.Entry(
            dim_row2,
            textvariable=self.height_var,
            font=("Arial", 9),
            width=10,
            state="disabled"
        ).pack(side="left", padx=5)
        
        tk.Label(
            dim_row2,
            text="px",
            font=("Arial", 9),
            bg="#ffffff"
        ).pack(side="left")
        
        self.maintain_aspect = tk.BooleanVar(value=True)
        tk.Checkbutton(
            resize_frame,
            text="Maintain aspect ratio",
            variable=self.maintain_aspect,
            font=("Arial", 9),
            bg="#ffffff",
            state="disabled"
        ).pack(anchor="w")
        
        # Compression options
        compress_frame = tk.LabelFrame(
            control_panel,
            text="Compression",
            font=("Arial", 11, "bold"),
            bg="#ffffff",
            padx=10,
            pady=10
        )
        compress_frame.pack(padx=10, pady=10, fill="x")
        
        quality_frame = tk.Frame(compress_frame, bg="#ffffff")
        quality_frame.pack(fill="x")
        
        tk.Label(
            quality_frame,
            text="Quality:",
            font=("Arial", 9),
            bg="#ffffff"
        ).pack(side="left")
        
        self.quality_var = tk.IntVar(value=90)
        tk.Scale(
            quality_frame,
            from_=10,
            to=100,
            variable=self.quality_var,
            orient="horizontal",
            bg="#ffffff",
            length=120
        ).pack(side="left", padx=5)
        
        self.quality_label = tk.Label(
            quality_frame,
            text="90%",
            font=("Arial", 9, "bold"),
            bg="#ffffff",
            width=5
        )
        self.quality_label.pack(side="left")
        
        self.quality_var.trace('w', self.update_quality_label)
        
        # Format selection
        format_frame = tk.Frame(compress_frame, bg="#ffffff")
        format_frame.pack(fill="x", pady=5)
        
        tk.Label(
            format_frame,
            text="Format:",
            font=("Arial", 9),
            bg="#ffffff"
        ).pack(side="left")
        
        self.format_var = tk.StringVar(value="JPEG")
        format_menu = ttk.Combobox(
            format_frame,
            textvariable=self.format_var,
            values=["JPEG", "PNG", "WebP"],
            font=("Arial", 9),
            width=10,
            state="readonly"
        )
        format_menu.pack(side="left", padx=5)
        
        # Action buttons
        action_frame = tk.Frame(control_panel, bg="#ffffff")
        action_frame.pack(padx=10, pady=15, fill="x")
        
        tk.Button(
            action_frame,
            text="⚡ Process",
            command=self.process_image,
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(fill="x", pady=3)
        
        tk.Button(
            action_frame,
            text="💾 Save",
            command=self.save_image,
            font=("Arial", 11, "bold"),
            bg="#e67e22",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(fill="x", pady=3)
        
        tk.Button(
            action_frame,
            text="🔄 Reset",
            command=self.reset,
            font=("Arial", 10),
            bg="#e74c3c",
            fg="white",
            padx=20,
            pady=8,
            cursor="hand2"
        ).pack(fill="x", pady=3)
        
        # Right panel - Image display
        display_panel = tk.Frame(main_frame, bg="#ffffff", relief="raised", borderwidth=2)
        display_panel.pack(side="right", fill="both", expand=True)
        
        # Display header
        display_header = tk.Frame(display_panel, bg="#34495e")
        display_header.pack(fill="x")
        
        tk.Label(
            display_header,
            text="Image Preview",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="white",
            pady=10
        ).pack()
        
        # Canvas for image
        self.canvas = tk.Canvas(
            display_panel,
            bg="#ecf0f1",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Info label
        self.info_label = tk.Label(
            display_panel,
            text="No image loaded",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#7f8c8d"
        )
        self.info_label.pack(pady=10)
        
        # Initial placeholder
        self.canvas.create_text(
            350, 300,
            text="Load an image to start",
            font=("Arial", 14),
            fill="#95a5a6",
            tags="placeholder"
        )
        
    def toggle_mode(self):
        """Toggle between single and batch mode"""
        if self.mode_var.get() == "batch":
            self.batch_btn.config(state="normal")
            self.load_btn.config(state="disabled")
        else:
            self.batch_btn.config(state="disabled")
            self.load_btn.config(state="normal")
    
    def toggle_resize_inputs(self):
        """Enable/disable resize input fields"""
        if self.resize_mode.get() == "percentage":
            self.percentage_scale.config(state="normal")
            for widget in self.custom_frame.winfo_children():
                for child in widget.winfo_children():
                    if isinstance(child, tk.Entry):
                        child.config(state="disabled")
        else:
            self.percentage_scale.config(state="disabled")
            for widget in self.custom_frame.winfo_children():
                for child in widget.winfo_children():
                    if isinstance(child, tk.Entry):
                        child.config(state="normal")
    
    def update_percentage_label(self, *args):
        """Update percentage label"""
        self.percentage_label.config(text=f"{self.percentage_var.get()}%")
    
    def update_quality_label(self, *args):
        """Update quality label"""
        self.quality_label.config(text=f"{self.quality_var.get()}%")
    
    def load_image(self):
        """Load a single image"""
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.image_path = file_path
                self.original_image = Image.open(file_path)
                self.processed_image = None
                
                # Update file label
                self.file_label.config(
                    text=f"{os.path.basename(file_path)}\n{self.original_image.width}x{self.original_image.height}",
                    fg="#2c3e50"
                )
                
                # Set default custom dimensions
                self.width_var.set(str(self.original_image.width))
                self.height_var.set(str(self.original_image.height))
                
                # Display image
                self.display_image(self.original_image, "Original")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")
    
    def load_batch(self):
        """Load multiple images for batch processing"""
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.webp"),
                ("All files", "*.*")
            ]
        )
        
        if files:
            self.batch_files = list(files)
            self.file_label.config(
                text=f"{len(files)} images selected",
                fg="#2c3e50"
            )
    
    def display_image(self, img, status=""):
        """Display image on canvas"""
        self.canvas.delete("all")
        
        # Get canvas size
        self.canvas.update()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Resize for display
        img_copy = img.copy()
        img_copy.thumbnail((canvas_width - 40, canvas_height - 40), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        self.display_photo = ImageTk.PhotoImage(img_copy)
        
        # Center on canvas
        x = (canvas_width - img_copy.width) // 2
        y = (canvas_height - img_copy.height) // 2
        
        self.canvas.create_image(x, y, image=self.display_photo, anchor="nw")
        
        # Update info
        if status:
            self.info_label.config(
                text=f"{status} | Size: {img.width}x{img.height} | Format: {img.format or 'N/A'}",
                fg="#2c3e50"
            )
    
    def process_image(self):
        """Process the image based on settings"""
        if self.mode_var.get() == "single":
            if not self.original_image:
                messagebox.showwarning("Warning", "Please load an image first!")
                return
            
            try:
                img = self.original_image.copy()
                
                # Resize
                if self.resize_mode.get() == "percentage":
                    scale = self.percentage_var.get() / 100
                    new_width = int(img.width * scale)
                    new_height = int(img.height * scale)
                else:
                    new_width = int(self.width_var.get())
                    new_height = int(self.height_var.get())
                    
                    if self.maintain_aspect.get():
                        # Calculate aspect ratio
                        aspect = img.width / img.height
                        if new_width / new_height > aspect:
                            new_width = int(new_height * aspect)
                        else:
                            new_height = int(new_width / aspect)
                
                # Apply resize
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Convert format if needed
                if self.format_var.get() == "JPEG" and img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = background
                
                self.processed_image = img
                self.display_image(img, "Processed")
                
                messagebox.showinfo("Success", "Image processed successfully!")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to process image:\n{str(e)}")
        
        else:
            # Batch processing
            if not self.batch_files:
                messagebox.showwarning("Warning", "Please load images first!")
                return
            
            output_dir = filedialog.askdirectory(title="Select Output Folder")
            if not output_dir:
                return
            
            try:
                success_count = 0
                
                for file_path in self.batch_files:
                    try:
                        img = Image.open(file_path)
                        
                        # Resize
                        if self.resize_mode.get() == "percentage":
                            scale = self.percentage_var.get() / 100
                            new_width = int(img.width * scale)
                            new_height = int(img.height * scale)
                        else:
                            new_width = int(self.width_var.get())
                            new_height = int(self.height_var.get())
                            
                            if self.maintain_aspect.get():
                                aspect = img.width / img.height
                                if new_width / new_height > aspect:
                                    new_width = int(new_height * aspect)
                                else:
                                    new_height = int(new_width / aspect)
                        
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        
                        # Convert format if needed
                        if self.format_var.get() == "JPEG" and img.mode in ('RGBA', 'LA', 'P'):
                            background = Image.new('RGB', img.size, (255, 255, 255))
                            if img.mode == 'P':
                                img = img.convert('RGBA')
                            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                            img = background
                        
                        # Save
                        base_name = os.path.splitext(os.path.basename(file_path))[0]
                        ext = self.format_var.get().lower()
                        if ext == "jpeg":
                            ext = "jpg"
                        output_path = os.path.join(output_dir, f"{base_name}_processed.{ext}")
                        
                        save_kwargs = {'quality': self.quality_var.get()} if self.format_var.get() in ['JPEG', 'WebP'] else {}
                        img.save(output_path, format=self.format_var.get(), **save_kwargs)
                        
                        success_count += 1
                        
                    except Exception as e:
                        print(f"Failed to process {file_path}: {e}")
                        continue
                
                messagebox.showinfo(
                    "Success",
                    f"Processed {success_count}/{len(self.batch_files)} images!\n\nSaved to:\n{output_dir}"
                )
                
            except Exception as e:
                messagebox.showerror("Error", f"Batch processing failed:\n{str(e)}")
    
    def save_image(self):
        """Save the processed image"""
        if not self.processed_image:
            messagebox.showwarning("Warning", "Please process an image first!")
            return
        
        ext = self.format_var.get().lower()
        if ext == "jpeg":
            ext = "jpg"
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=f".{ext}",
            filetypes=[
                (f"{self.format_var.get()} files", f"*.{ext}"),
                ("All files", "*.*")
            ],
            initialfile=f"processed.{ext}"
        )
        
        if file_path:
            try:
                save_kwargs = {'quality': self.quality_var.get()} if self.format_var.get() in ['JPEG', 'WebP'] else {}
                self.processed_image.save(file_path, format=self.format_var.get(), **save_kwargs)
                
                # Show file size info
                original_size = os.path.getsize(self.image_path) / 1024  # KB
                new_size = os.path.getsize(file_path) / 1024  # KB
                reduction = ((original_size - new_size) / original_size) * 100
                
                messagebox.showinfo(
                    "Success",
                    f"Image saved successfully!\n\n"
                    f"Original: {original_size:.1f} KB\n"
                    f"New: {new_size:.1f} KB\n"
                    f"Reduction: {reduction:.1f}%"
                )
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save image:\n{str(e)}")
    
    def reset(self):
        """Reset everything"""
        self.original_image = None
        self.processed_image = None
        self.image_path = None
        self.batch_files = []
        
        self.file_label.config(text="No file loaded", fg="#7f8c8d")
        self.info_label.config(text="No image loaded", fg="#7f8c8d")
        
        self.percentage_var.set(100)
        self.quality_var.set(90)
        self.width_var.set("")
        self.height_var.set("")
        
        self.canvas.delete("all")
        self.canvas.create_text(
            350, 300,
            text="Load an image to start",
            font=("Arial", 14),
            fill="#95a5a6",
            tags="placeholder"
        )

def main():
    root = tk.Tk()
    app = ImageResizerCompressor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
