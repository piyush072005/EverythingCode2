#GUI Calculator using Tkinter
import tkinter as tk
from calculator import add, subtract, multiply, divide
from tkinter import messagebox
class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.label = tk.Label(master, text="Simple Calculator")
        self.label.pack()

        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        self.add_button = tk.Button(master, text="+", command=self.add)
        self.add_button.pack()

        self.subtract_button = tk.Button(master, text="-", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = tk.Button(master, text="*", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(master, text="/", command=self.divide)
        self.divide_button.pack()

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.pack()

    def get_inputs(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None

    def add(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            result = add(a, b)
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            result = subtract(a, b)
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            result = multiply(a, b)
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            if b == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
            else:
                result = divide(a, b)
                self.result_label.config(text=f"Result: {result}")


if __name__ == "__main__":
    try:
        root = tk.Tk()
    except Exception as e:
        print("Unable to start Tkinter GUI:", e)
    else:
        app = CalculatorGUI(root)
        root.mainloop()
    
