import customtkinter as ctk
import random

# Set the theme and color palette
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class LoveApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("For You 💖")
        self.geometry("400x300")
        self.resizable(False, False)

        # Center the window on the screen (optional calculation)
        
        # Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Main Question Label
        self.label = ctk.CTkLabel(
            self, 
            text="Do You Love Me?", 
            font=("Roboto Medium", 24),
            text_color=("gray10", "gray90")
        )
        self.label.grid(row=0, column=0, pady=20, sticky="ew")

        # Yes Button
        self.btn_yes = ctk.CTkButton(
            self, 
            text="Yes", 
            command=self.love_confirmed,
            fg_color="#E91E63", # Pinkish
            hover_color="#AD1457",
            font=("Roboto Medium", 16)
        )
        self.btn_yes.grid(row=1, column=0, pady=10)

        # No Button (The tricky one)
        self.btn_no = ctk.CTkButton(
            self, 
            text="No", 
            fg_color="#607D8B",
            hover_color="#455A64",
            font=("Roboto Medium", 16)
        )
        self.btn_no.place(relx=0.5, rely=0.7, anchor="center")
        
        # Bind hover event to move the button
        self.btn_no.bind("<Enter>", self.move_button)
        self.btn_no.bind("<Button-1>", self.move_button) # Just in case they click fast

    def move_button(self, event=None):
        # Move the 'No' button to a random position
        new_x = random.uniform(0.1, 0.9)
        new_y = random.uniform(0.1, 0.9)
        self.btn_no.place(relx=new_x, rely=new_y, anchor="center")

    def love_confirmed(self):
        self.label.configure(text="I Love You Too! 💖", text_color="#E91E63")
        self.btn_yes.configure(text="Forever? 🥺")
        self.btn_no.destroy() # Remove the no button

if __name__ == "__main__":
    app = LoveApp()
    app.mainloop()
