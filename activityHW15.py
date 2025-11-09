# Program to store and print birthdays of Raj's friends

friends_birthdays = {
    "Aman": "12 March",
    "Riya": "5 July",
    "Karan": "22 October",
    "Meena": "14 January",
    "Sahil": "30 November"
}

print("Raj's friends' birthdays:")
for name, birthday in friends_birthdays.items():
    print(f"{name}: {birthday}")
