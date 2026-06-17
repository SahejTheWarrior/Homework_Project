from tkinter import *

# Function to check password strength
def check_strength():
    password = entry_password.get()
    length = len(password)

    if length <= 5:
        result_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="light green")
    else:  # length > 12
        result_label.config(text="Very Strong", fg="dark green")


# Create main window
root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

# Optional background color
root.configure(bg="#EAF4FC")

# Heading
heading = Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 16, "bold"),
    bg="#EAF4FC"
)
heading.pack(pady=20)

# Password Entry
Label(
    root,
    text="Enter Password:",
    font=("Arial", 12),
    bg="#EAF4FC"
).pack(pady=10)

entry_password = Entry(root, width=25, show="*", font=("Arial", 12))
entry_password.pack(pady=5)

# Button
check_btn = Button(
    root,
    text="Check Strength",
    command=check_strength,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold")
)
check_btn.pack(pady=20)

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#EAF4FC"
)
result_label.pack(pady=20)

# Run application
root.mainloop()