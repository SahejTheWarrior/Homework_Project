from tkinter import *

root = Tk()

root.title("Length Converter App")

root.geometry("400x400")

root.configure(bg="#E6F2FF")

heading = Label(
    root,
    text="Length Converter",
    font=("Arial", 18, "bold"),
    bg="#E6F2FF",
    fg="#003366"
)
heading.pack(pady=20)

# Entry box for input
entry = Entry(
    root,
    font=("Arial", 14),
    width=20,
    bg="white",
    fg="black"
)
entry.pack(pady=10)

label = Label(
    root,
    text="Enter length in meters:",
    font=("Arial", 12),
    bg="#E6F2FF",
    fg="#000000"
)
label.pack()

def convert():
    meters = float(entry.get())
    centimeters = meters * 100
    result_label.config(text=f"{centimeters} cm")

convert_btn = Button(
    root,
    text="Convert",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=convert
)
convert_btn.pack(pady=15)

result_label = Label(
    root,
    text="Result will appear here",
    font=("Arial", 14),
    bg="#E6F2FF",
    fg="#CC0000"
)
result_label.pack(pady=20)

root.mainloop()
