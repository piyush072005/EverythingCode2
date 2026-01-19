from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import os

class MemeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Meme Generator")
        self.root.geometry("900x750")
        self.root.configure(bg="#2c3e50")
        
        self.original_image = None
        self.meme_image = None
        self.display_photo = None
        self.image_path = None
        
        # Default text settings
        self.text_color = "#FFFFFF"
        self.outline_color = "#000000"
        
        # Header
        header = tk.Label(
            root,
            text="🎨 MEME GENERATOR 🎨",
            font=("Arial", 26, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        header.pack(pady=15)
        
        # Main container
        main_frame = tk.Frame(root, bg="#2c3e50")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Left panel - Controls
        control_panel = tk.Frame(main_frame, bg="#34495e", relief="raised", borderwidth=2)
        control_panel.pack(side="left", fill="y", padx=(0, 10))
        
        # File selection
        file_frame = tk.LabelFrame(
            control_panel,
            text="Image",
            font=("Arial", 11, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        file_frame.pack(padx=10, pady=10, fill="x")
        
        tk.Button(
            file_frame,
            text="📁 Load Image",
            command=self.load_image,
            font=("Arial", 11),
            bg="#3498db",
            fg="white",
            padx=15,
            pady=8,
            cursor="hand2",
            relief="raised"
        ).pack(fill="x")
        
        # Top text
        top_frame = tk.LabelFrame(
            control_panel,
            text="Top Text",
            font=("Arial", 11, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        top_frame.pack(padx=10, pady=10, fill="x")
        
        self.top_text = tk.Text(
            top_frame,
            height=2,
            font=("Arial", 10),
            wrap="word",
            relief="solid",
            borderwidth=1
        )
        self.top_text.pack(fill="x")
        
        # Bottom text
        bottom_frame = tk.LabelFrame(
            control_panel,
            text="Bottom Text",
            font=("Arial", 11, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        bottom_frame.pack(padx=10, pady=10, fill="x")
        
        self.bottom_text = tk.Text(
            bottom_frame,
            height=2,
            font=("Arial", 10),
            wrap="word",
            relief="solid",
            borderwidth=1
        )
        self.bottom_text.pack(fill="x")
        
        # Font size
        size_frame = tk.LabelFrame(
            control_panel,
            text="Font Size",
            font=("Arial", 11, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        size_frame.pack(padx=10, pady=10, fill="x")
        
        self.font_size = tk.IntVar(value=60)
        tk.Scale(
            size_frame,
            from_=20,
            to=150,
            variable=self.font_size,
            orient="horizontal",
            bg="#34495e",
            fg="#ecf0f1",
            highlightbackground="#34495e",
            troughcolor="#2c3e50",
            activebackground="#3498db"
        ).pack(fill="x")
        
        # Colors
        color_frame = tk.LabelFrame(
            control_panel,
            text="Colors",
            font=("Arial", 11, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        color_frame.pack(padx=10, pady=10, fill="x")
        
        tk.Button(
            color_frame,
            text="🎨 Text Color",
            command=self.choose_text_color,
            font=("Arial", 10),
            bg="#9b59b6",
            fg="white",
            padx=10,
            pady=5,
            cursor="hand2"
        ).pack(fill="x", pady=2)
        
        tk.Button(
            color_frame,
            text="🖌️ Outline Color",
            command=self.choose_outline_color,
            font=("Arial", 10),
            bg="#8e44ad",
            fg="white",
            padx=10,
            pady=5,
            cursor="hand2"
        ).pack(fill="x", pady=2)
        
        # Action buttons
        action_frame = tk.Frame(control_panel, bg="#34495e")
        action_frame.pack(padx=10, pady=15, fill="x")
        
        tk.Button(
            action_frame,
            text="✨ Generate Meme",
            command=self.generate_meme,
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            padx=15,
            pady=10,
            cursor="hand2",
            relief="raised"
        ).pack(fill="x", pady=5)
        
        tk.Button(
            action_frame,
            text="💾 Save Meme",
            command=self.save_meme,
            font=("Arial", 12, "bold"),
            bg="#e67e22",
            fg="white",
            padx=15,
            pady=10,
            cursor="hand2",
            relief="raised"
        ).pack(fill="x", pady=5)
        
        tk.Button(
            action_frame,
            text="🔄 Reset",
            command=self.reset,
            font=("Arial", 11),
            bg="#e74c3c",
            fg="white",
            padx=15,
            pady=8,
            cursor="hand2",
            relief="raised"
        ).pack(fill="x", pady=5)
        
        # Right panel - Image display
        display_frame = tk.Frame(main_frame, bg="#34495e", relief="raised", borderwidth=2)
        display_frame.pack(side="right", fill="both", expand=True)
        
        self.canvas = tk.Canvas(
            display_frame,
            bg="#2c3e50",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Initial message
        self.canvas.create_text(
            300, 300,
            text="Load an image to start creating memes!",
            font=("Arial", 14),
            fill="#95a5a6",
            tags="placeholder"
        )
        
    def load_image(self):
        """Load an image file"""
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.gif *.bmp"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.image_path = file_path
                self.original_image = Image.open(file_path)
                
                # Convert to RGB if necessary
                if self.original_image.mode in ('RGBA', 'LA', 'P'):
                    # Create white background
                    background = Image.new('RGB', self.original_image.size, (255, 255, 255))
                    if self.original_image.mode == 'P':
                        self.original_image = self.original_image.convert('RGBA')
                    background.paste(self.original_image, mask=self.original_image.split()[-1] if self.original_image.mode in ('RGBA', 'LA') else None)
                    self.original_image = background
                elif self.original_image.mode != 'RGB':
                    self.original_image = self.original_image.convert('RGB')
                
                self.display_image(self.original_image)
                messagebox.showinfo("Success", "Image loaded successfully!")
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image:\n{str(e)}")
    
    def display_image(self, img):
        """Display image on canvas"""
        # Clear canvas
        self.canvas.delete("all")
        
        # Get canvas size
        self.canvas.update()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Resize image to fit canvas while maintaining aspect ratio
        img_copy = img.copy()
        img_copy.thumbnail((canvas_width - 20, canvas_height - 20), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        self.display_photo = ImageTk.PhotoImage(img_copy)
        
        # Center image on canvas
        x = (canvas_width - img_copy.width) // 2
        y = (canvas_height - img_copy.height) // 2
        
        self.canvas.create_image(x, y, image=self.display_photo, anchor="nw")
    
    def choose_text_color(self):
        """Choose text color"""
        color = colorchooser.askcolor(title="Choose Text Color", initialcolor=self.text_color)
        if color[1]:
            self.text_color = color[1]
    
    def choose_outline_color(self):
        """Choose outline color"""
        color = colorchooser.askcolor(title="Choose Outline Color", initialcolor=self.outline_color)
        if color[1]:
            self.outline_color = color[1]
    
    def draw_text_with_outline(self, draw, text, position, font, text_color, outline_color, outline_width=3):
        """Draw text with outline for better visibility"""
        x, y = position
        
        # Draw outline
        for adj_x in range(-outline_width, outline_width + 1):
            for adj_y in range(-outline_width, outline_width + 1):
                draw.text((x + adj_x, y + adj_y), text, font=font, fill=outline_color)
        
        # Draw main text
        draw.text(position, text, font=font, fill=text_color)
    
    def generate_meme(self):
        """Generate meme with text"""
        if not self.original_image:
            messagebox.showwarning("Warning", "Please load an image first!")
            return
        
        top_text_content = self.top_text.get("1.0", "end-1c").strip().upper()
        bottom_text_content = self.bottom_text.get("1.0", "end-1c").strip().upper()
        
        if not top_text_content and not bottom_text_content:
            messagebox.showwarning("Warning", "Please enter at least one text!")
            return
        
        try:
            # Create a copy of the original image
            self.meme_image = self.original_image.copy()
            draw = ImageDraw.Draw(self.meme_image)
            
            # Get image dimensions
            img_width, img_height = self.meme_image.size
            
            # Load font
            font_size = int(self.font_size.get() * (img_width / 500))  # Scale font based on image width
            
            try:
                # Try to use Impact font (classic meme font)
                font = ImageFont.truetype("impact.ttf", font_size)
            except:
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
            
            # Draw top text
            if top_text_content:
                # Get text bounding box
                bbox = draw.textbbox((0, 0), top_text_content, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                
                # Center text horizontally, place near top
                x = (img_width - text_width) / 2
                y = img_height * 0.05
                
                self.draw_text_with_outline(
                    draw, 
                    top_text_content, 
                    (x, y), 
                    font, 
                    self.text_color, 
                    self.outline_color,
                    outline_width=max(2, font_size // 20)
                )
            
            # Draw bottom text
            if bottom_text_content:
                bbox = draw.textbbox((0, 0), bottom_text_content, font=font)
                text_width = bbox[2] - bbox[0]
                text_height = bbox[3] - bbox[1]
                
                # Center text horizontally, place near bottom
                x = (img_width - text_width) / 2
                y = img_height * 0.88 - text_height
                
                self.draw_text_with_outline(
                    draw, 
                    bottom_text_content, 
                    (x, y), 
                    font, 
                    self.text_color, 
                    self.outline_color,
                    outline_width=max(2, font_size // 20)
                )
            
            # Display the meme
            self.display_image(self.meme_image)
            messagebox.showinfo("Success", "Meme generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate meme:\n{str(e)}")
    
    def save_meme(self):
        """Save the generated meme"""
        if not self.meme_image:
            messagebox.showwarning("Warning", "Please generate a meme first!")
            return
        
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[
                    ("PNG files", "*.png"),
                    ("JPEG files", "*.jpg"),
                    ("All files", "*.*")
                ],
                initialfile="meme.png"
            )
            
            if file_path:
                self.meme_image.save(file_path)
                messagebox.showinfo("Success", f"Meme saved successfully!\n{file_path}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save meme:\n{str(e)}")
    
    def reset(self):
        """Reset everything"""
        self.top_text.delete("1.0", "end")
        self.bottom_text.delete("1.0", "end")
        self.font_size.set(60)
        self.text_color = "#FFFFFF"
        self.outline_color = "#000000"
        
        if self.original_image:
            self.display_image(self.original_image)
            self.meme_image = None
        else:
            self.canvas.delete("all")
            self.canvas.create_text(
                300, 300,
                text="Load an image to start creating memes!",
                font=("Arial", 14),
                fill="#95a5a6",
                tags="placeholder"
            )

def main():
    root = tk.Tk()
    app = MemeGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
