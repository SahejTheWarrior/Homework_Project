from tkinter import *

# Create main window
root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.config(bg="#E6F2FF")

# Functions to calculate interests
def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest
        si = (p * t * r) / 100

        # Compound Interest
        amount = p * ((1 + r / 100) ** t)
        ci = amount - p

        # Display results
        si_result.config(text=f"Simple Interest: {si:.2f}")
        ci_result.config(text=f"Compound Interest: {ci:.2f}")

    except ValueError:
        si_result.config(text="Please enter valid numbers")
        ci_result.config(text="")

# Heading
heading = Label(
    root,
    text="Interest Calculator",
    font=("Arial", 18, "bold"),
    bg="#E6F2FF",
    fg="#003366"
)
heading.pack(pady=15)

# Frame for input fields
frame = Frame(root, bg="#E6F2FF")
frame.pack(pady=10)

# Principal
principal_label = Label(
    frame,
    text="Principal:",
    font=("Arial", 12),
    bg="#E6F2FF"
)
principal_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

principal_entry = Entry(frame, font=("Arial", 12), width=18)
principal_entry.grid(row=0, column=1, padx=10)

# Time
time_label = Label(
    frame,
    text="Time (Years):",
    font=("Arial", 12),
    bg="#E6F2FF"
)
time_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

time_entry = Entry(frame, font=("Arial", 12), width=18)
time_entry.grid(row=1, column=1, padx=10)

# Rate
rate_label = Label(
    frame,
    text="Rate (%):",
    font=("Arial", 12),
    bg="#E6F2FF"
)
rate_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

rate_entry = Entry(frame, font=("Arial", 12), width=18)
rate_entry.grid(row=2, column=1, padx=10)

# Calculate Button
calc_button = Button(
    root,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=calculate_interest
)
calc_button.pack(pady=20)

# Result Labels
si_result = Label(
    root,
    text="Simple Interest: ",
    font=("Arial", 12),
    bg="#E6F2FF",
    fg="#000080"
)
si_result.pack(pady=5)

ci_result = Label(
    root,
    text="Compound Interest: ",
    font=("Arial", 12),
    bg="#E6F2FF",
    fg="#000080"
)
ci_result.pack(pady=5)

# Run the application
root.mainloop()