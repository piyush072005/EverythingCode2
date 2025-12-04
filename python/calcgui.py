#GUI Calculator using Tkinter
import tkinter as tk
from calculator import add, subtract, multiply, divide, power, sqrt, log, exp
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

        self.power_button = tk.Button(master, text="**", command=self.power)
        self.power_button.pack()

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
            try:
                result = add(a, b)
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
            else:
                # Format lists/tuples nicely
                if isinstance(result, (list, tuple)):
                    disp = ", ".join(str(x) for x in result)
                else:
                    disp = result
                self.result_label.config(text=f"Result: {disp}")

    def subtract(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            try:
                result = subtract(a, b)
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
            else:
                if isinstance(result, (list, tuple)):
                    disp = ", ".join(str(x) for x in result)
                else:
                    disp = result
                self.result_label.config(text=f"Result: {disp}")

    def multiply(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            try:
                result = multiply(a, b)
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
            else:
                if isinstance(result, (list, tuple)):
                    disp = ", ".join(str(x) for x in result)
                else:
                    disp = result
                self.result_label.config(text=f"Result: {disp}")

    def divide(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            if b == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
            else:
                try:
                    result = divide(a, b)
                except Exception as e:
                    messagebox.showerror("Calculation Error", str(e))
                else:
                    if isinstance(result, (list, tuple)):
                        disp = ", ".join(str(x) for x in result)
                    else:
                        disp = result
                    self.result_label.config(text=f"Result: {disp}")

    def power(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            try:
                result = power(a, b)
            except Exception as e:
                messagebox.showerror("Calculation Error", str(e))
            else:
                if isinstance(result, (list, tuple)):
                    disp = ", ".join(str(x) for x in result)
                else:
                    disp = result
                self.result_label.config(text=f"Result: {disp}")

    def _unary_from_entry1(self, func, name=None):
        # Helper for unary ops using only entry1
        try:
            a = float(self.entry1.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number in the first field.")
            return
        try:
            result = func(a)
        except Exception as e:
            messagebox.showerror("Calculation Error", str(e))
        else:
            if isinstance(result, (list, tuple)):
                disp = ", ".join(str(x) for x in result)
            else:
                disp = result
            label = name or "Result"
            self.result_label.config(text=f"{label}: {disp}")

    def sqrt(self):
        self._unary_from_entry1(sqrt, name="Sqrt")

    def log(self):
        self._unary_from_entry1(log, name="Log")

    def exp(self):
        self._unary_from_entry1(exp, name="Exp")


if __name__ == "__main__":
    try:
        root = tk.Tk()
    except Exception as e:
        print("Unable to start Tkinter GUI:", e)
    else:
        app = CalculatorGUI(root)
        # Bind Enter key to perform addition by default
        root.bind('<Return>', lambda event: app.add())
        root.mainloop()
    
