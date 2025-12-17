try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    else:
        if age % 2 == 0:
            print("Age is even.")
        else:
            print("Age is odd.")

except ValueError:
    print("Invalid input! Please enter an integer value only.")
