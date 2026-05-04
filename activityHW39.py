import tkinter as tk
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        name = name_entry.get()
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())

        today = date.today()
        dob = date(year, month, day)

        age = today.year - dob.year
        if (today.month, today.day) < (dob.month, dob.day):
            age -= 1

        result_label.config(
            text=f"Hello {name}! You are {age} years old.",
            fg="#2e7d32"
        )
    except:
        result_label.config(
            text="Invalid input! Please check your data.",
            fg="red"
        )

# Main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#e3f2fd")

# Title
title = tk.Label(
    root,
    text="Age Calculator",
    font=("Helvetica", 18, "bold"),
    bg="#e3f2fd",
    fg="#0d47a1"
)
title.pack(pady=15)

# Frame for form
form_frame = tk.Frame(root, bg="#e3f2fd")
form_frame.pack(pady=10)

# Labels & Entries (side by side)
tk.Label(form_frame, text="Name:", bg="#e3f2fd").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(form_frame, width=20)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Day:", bg="#e3f2fd").grid(row=1, column=0, padx=10, pady=5, sticky="e")
day_entry = tk.Entry(form_frame, width=20)
day_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Month:", bg="#e3f2fd").grid(row=2, column=0, padx=10, pady=5, sticky="e")
month_entry = tk.Entry(form_frame, width=20)
month_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Year:", bg="#e3f2fd").grid(row=3, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(form_frame, width=20)
year_entry.grid(row=3, column=1, padx=10, pady=5)

# Button
calc_btn = tk.Button(
    root,
    text="Calculate Age",
    command=calculate_age,
    bg="#1976d2",
    fg="white",
    padx=10,
    pady=5
)
calc_btn.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 12),
    bg="#e3f2fd"
)
result_label.pack(pady=10)

# Run app
root.mainloop()