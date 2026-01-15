import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar App")
        self.root.geometry("400x450")
        self.root.resizable(False, False)
        
        # Get current date
        today = datetime.now()
        self.current_year = today.year
        self.current_month = today.month
        self.today_day = today.day
        
        # Selected date for display
        self.selected_year = self.current_year
        self.selected_month = self.current_month
        
        # Create UI elements
        self.create_widgets()
        self.update_calendar()
    
    def create_widgets(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg="#2c3e50")
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Previous month button
        self.prev_btn = tk.Button(
            header_frame, 
            text="<", 
            command=self.prev_month,
            bg="#34495e",
            fg="white",
            font=("Arial", 12, "bold"),
            width=3
        )
        self.prev_btn.pack(side=tk.LEFT, padx=5)
        
        # Month and year display
        self.month_year_label = tk.Label(
            header_frame,
            text="",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 16, "bold")
        )
        self.month_year_label.pack(side=tk.LEFT, expand=True)
        
        # Next month button
        self.next_btn = tk.Button(
            header_frame,
            text=">",
            command=self.next_month,
            bg="#34495e",
            fg="white",
            font=("Arial", 12, "bold"),
            width=3
        )
        self.next_btn.pack(side=tk.RIGHT, padx=5)
        
        # Calendar frame
        self.calendar_frame = tk.Frame(self.root, bg="white")
        self.calendar_frame.pack(padx=10, pady=10)
        
        # Day headers
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            label = tk.Label(
                self.calendar_frame,
                text=day,
                bg="#3498db",
                fg="white",
                font=("Arial", 10, "bold"),
                width=5,
                height=2
            )
            label.grid(row=0, column=i, padx=1, pady=1)
        
        # Create day labels (6 rows for weeks)
        self.day_labels = []
        for week in range(6):
            week_labels = []
            for day in range(7):
                label = tk.Label(
                    self.calendar_frame,
                    text="",
                    bg="white",
                    font=("Arial", 10),
                    width=5,
                    height=2,
                    relief=tk.RIDGE,
                    borderwidth=1
                )
                label.grid(row=week + 1, column=day, padx=1, pady=1)
                week_labels.append(label)
            self.day_labels.append(week_labels)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg="white")
        button_frame.pack(pady=10)
        
        # Today button
        today_btn = tk.Button(
            button_frame,
            text="Today",
            command=self.goto_today,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            width=10
        )
        today_btn.pack(side=tk.LEFT, padx=5)
        
        # Year selection
        year_frame = tk.Frame(button_frame, bg="white")
        year_frame.pack(side=tk.LEFT, padx=10)
        
        tk.Label(year_frame, text="Year:", bg="white", font=("Arial", 10)).pack(side=tk.LEFT, padx=2)
        
        self.year_spinbox = tk.Spinbox(
            year_frame,
            from_=1900,
            to=2100,
            width=6,
            font=("Arial", 10),
            command=self.change_year
        )
        self.year_spinbox.pack(side=tk.LEFT)
        self.year_spinbox.delete(0, tk.END)
        self.year_spinbox.insert(0, self.selected_year)
    
    def update_calendar(self):
        # Update month and year label
        month_name = calendar.month_name[self.selected_month]
        self.month_year_label.config(text=f"{month_name} {self.selected_year}")
        
        # Update year spinbox
        self.year_spinbox.delete(0, tk.END)
        self.year_spinbox.insert(0, self.selected_year)
        
        # Get calendar for the selected month
        cal = calendar.monthcalendar(self.selected_year, self.selected_month)
        
        # Clear all day labels
        for week in self.day_labels:
            for day_label in week:
                day_label.config(text="", bg="white", fg="black")
        
        # Fill in the days
        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    label = self.day_labels[week_num][day_num]
                    label.config(text=str(day))
                    
                    # Highlight today
                    if (day == self.today_day and 
                        self.selected_month == self.current_month and 
                        self.selected_year == self.current_year):
                        label.config(bg="#e74c3c", fg="white", font=("Arial", 10, "bold"))
                    else:
                        label.config(bg="white", fg="black", font=("Arial", 10))
    
    def prev_month(self):
        self.selected_month -= 1
        if self.selected_month < 1:
            self.selected_month = 12
            self.selected_year -= 1
        self.update_calendar()
    
    def next_month(self):
        self.selected_month += 1
        if self.selected_month > 12:
            self.selected_month = 1
            self.selected_year += 1
        self.update_calendar()
    
    def goto_today(self):
        self.selected_year = self.current_year
        self.selected_month = self.current_month
        self.update_calendar()
    
    def change_year(self):
        try:
            self.selected_year = int(self.year_spinbox.get())
            self.update_calendar()
        except ValueError:
            pass


def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
