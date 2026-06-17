from tkinter import *
import random

# Function to play the game
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    computer_label.config(text=f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="blue")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You Win!", fg="green")

    else:
        result_label.config(text="Computer Wins!", fg="red")


# Create main window
root = Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#E6F2FF")

# Heading
heading = Label(
    root,
    text="Rock Paper Scissors Game",
    font=("Arial", 16, "bold"),
    bg="#E6F2FF"
)
heading.pack(pady=20)

# Instruction Label
instruction = Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12),
    bg="#E6F2FF"
)
instruction.pack(pady=10)

# Buttons Frame
button_frame = Frame(root, bg="#E6F2FF")
button_frame.pack(pady=20)

# Choice Buttons
rock_btn = Button(
    button_frame,
    text="Rock",
    width=10,
    command=lambda: play("Rock"),
    bg="#FF9999"
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = Button(
    button_frame,
    text="Paper",
    width=10,
    command=lambda: play("Paper"),
    bg="#FFFF99"
)
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = Button(
    button_frame,
    text="Scissors",
    width=10,
    command=lambda: play("Scissors"),
    bg="#99FF99"
)
scissors_btn.grid(row=0, column=2, padx=5)

# Computer Choice Label
computer_label = Label(
    root,
    text="Computer chose: ",
    font=("Arial", 12),
    bg="#E6F2FF"
)
computer_label.pack(pady=15)

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#E6F2FF"
)
result_label.pack(pady=20)

# Run the application
root.mainloop()