import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class QRCodeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.qr_image = None
        self.qr_photo = None
        
        # Title
        title_label = tk.Label(
            root, 
            text="QR Code Generator", 
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title_label.pack(pady=20)
        
        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f0f0")
        input_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(
            input_frame, 
            text="Enter Text or URL:", 
            font=("Arial", 12),
            bg="#f0f0f0"
        ).pack(anchor="w")
        
        self.text_input = tk.Text(
            input_frame, 
            height=4, 
            font=("Arial", 11),
            wrap="word",
            relief="solid",
            borderwidth=1
        )
        self.text_input.pack(fill="x", pady=5)
        
        # Options Frame
        options_frame = tk.Frame(root, bg="#f0f0f0")
        options_frame.pack(pady=10, padx=20, fill="x")
        
        # Size option
        size_frame = tk.Frame(options_frame, bg="#f0f0f0")
        size_frame.pack(side="left", padx=10)
        
        tk.Label(
            size_frame, 
            text="Size:", 
            font=("Arial", 10),
            bg="#f0f0f0"
        ).pack(side="left")
        
        self.size_var = tk.StringVar(value="10")
        size_spinbox = tk.Spinbox(
            size_frame,
            from_=1,
            to=40,
            textvariable=self.size_var,
            width=5,
            font=("Arial", 10)
        )
        size_spinbox.pack(side="left", padx=5)
        
        # Border option
        border_frame = tk.Frame(options_frame, bg="#f0f0f0")
        border_frame.pack(side="left", padx=10)
        
        tk.Label(
            border_frame, 
            text="Border:", 
            font=("Arial", 10),
            bg="#f0f0f0"
        ).pack(side="left")
        
        self.border_var = tk.StringVar(value="4")
        border_spinbox = tk.Spinbox(
            border_frame,
            from_=0,
            to=10,
            textvariable=self.border_var,
            width=5,
            font=("Arial", 10)
        )
        border_spinbox.pack(side="left", padx=5)
        
        # Error correction level
        error_frame = tk.Frame(options_frame, bg="#f0f0f0")
        error_frame.pack(side="left", padx=10)
        
        tk.Label(
            error_frame, 
            text="Error Correction:", 
            font=("Arial", 10),
            bg="#f0f0f0"
        ).pack(side="left")
        
        self.error_var = tk.StringVar(value="M")
        error_menu = tk.OptionMenu(
            error_frame,
            self.error_var,
            "L", "M", "Q", "H"
        )
        error_menu.config(width=3, font=("Arial", 10))
        error_menu.pack(side="left", padx=5)
        
        # Buttons Frame
        button_frame = tk.Frame(root, bg="#f0f0f0")
        button_frame.pack(pady=15)
        
        generate_btn = tk.Button(
            button_frame,
            text="Generate QR Code",
            command=self.generate_qr,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            relief="raised",
            cursor="hand2"
        )
        generate_btn.pack(side="left", padx=10)
        
        save_btn = tk.Button(
            button_frame,
            text="Save QR Code",
            command=self.save_qr,
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=10,
            relief="raised",
            cursor="hand2"
        )
        save_btn.pack(side="left", padx=10)
        
        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_all,
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            relief="raised",
            cursor="hand2"
        )
        clear_btn.pack(side="left", padx=10)
        
        # QR Code Display Frame
        display_frame = tk.Frame(root, bg="white", relief="solid", borderwidth=2)
        display_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        self.qr_label = tk.Label(
            display_frame,
            text="QR Code will appear here",
            font=("Arial", 12),
            bg="white",
            fg="#999"
        )
        self.qr_label.pack(expand=True)
        
        # Info label
        self.info_label = tk.Label(
            root,
            text="Error Correction: L=7%, M=15%, Q=25%, H=30%",
            font=("Arial", 9),
            bg="#f0f0f0",
            fg="#666"
        )
        self.info_label.pack(pady=5)
    
    def generate_qr(self):
        """Generate QR code from input text"""
        data = self.text_input.get("1.0", "end-1c").strip()
        
        if not data:
            messagebox.showwarning("Warning", "Please enter text or URL to generate QR code!")
            return
        
        try:
            # Get parameters
            box_size = int(self.size_var.get())
            border = int(self.border_var.get())
            error_correction = self.error_var.get()
            
            # Map error correction level
            error_map = {
                'L': qrcode.constants.ERROR_CORRECT_L,
                'M': qrcode.constants.ERROR_CORRECT_M,
                'Q': qrcode.constants.ERROR_CORRECT_Q,
                'H': qrcode.constants.ERROR_CORRECT_H
            }
            
            # Create QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=error_map.get(error_correction, qrcode.constants.ERROR_CORRECT_M),
                box_size=box_size,
                border=border,
            )
            
            qr.add_data(data)
            qr.make(fit=True)
            
            # Generate image
            self.qr_image = qr.make_image(fill_color="black", back_color="white")
            
            # Display in GUI
            self.display_qr()
            
            messagebox.showinfo("Success", "QR Code generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate QR code:\n{str(e)}")
    
    def display_qr(self):
        """Display QR code in the GUI"""
        if self.qr_image:
            # Resize for display
            display_size = (350, 350)
            img_copy = self.qr_image.copy()
            img_copy.thumbnail(display_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            self.qr_photo = ImageTk.PhotoImage(img_copy)
            
            # Update label
            self.qr_label.configure(image=self.qr_photo, text="")
            self.qr_label.image = self.qr_photo
    
    def save_qr(self):
        """Save QR code to file"""
        if not self.qr_image:
            messagebox.showwarning("Warning", "Please generate a QR code first!")
            return
        
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("All files", "*.*")
                ]
            )
            
            if file_path:
                self.qr_image.save(file_path)
                messagebox.showinfo("Success", f"QR code saved successfully!\n{file_path}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save QR code:\n{str(e)}")
    
    def clear_all(self):
        """Clear all inputs and display"""
        self.text_input.delete("1.0", "end")
        self.size_var.set("10")
        self.border_var.set("4")
        self.error_var.set("M")
        self.qr_image = None
        self.qr_photo = None
        self.qr_label.configure(image="", text="QR Code will appear here")

def main():
    root = tk.Tk()
    app = QRCodeGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
