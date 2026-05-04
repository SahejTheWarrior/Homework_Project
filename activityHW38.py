import tkinter as tk
from datetime import date

# Function to calculate age
def calculate_age():
    try:
        name = entry_name.get()
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        today = date.today()
        birth_date = date(year, month, day)

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(
            text=f"Hello {name}! You are {age} years old.",
            fg="green"
        )
    except:
        result_label.config(
            text="Please enter valid data!",
            fg="red"
        )

# Create main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f0f8ff")

# Title Label
title_label = tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold"), bg="#f0f8ff")
title_label.pack(pady=10)

# Frame for inputs
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=10)

# Name
tk.Label(frame, text="Name:", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Day
tk.Label(frame, text="Day:", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_day = tk.Entry(frame)
entry_day.grid(row=1, column=1, padx=5, pady=5)

# Month
tk.Label(frame, text="Month:", bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_month = tk.Entry(frame)
entry_month.grid(row=2, column=1, padx=5, pady=5)

# Year
tk.Label(frame, text="Year:", bg="#f0f8ff").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_year = tk.Entry(frame)
entry_year.grid(row=3, column=1, padx=5, pady=5)

# Calculate Button
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="#4CAF50", fg="white")
calc_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff")
result_label.pack(pady=10)

# Run the app
root.mainloop()