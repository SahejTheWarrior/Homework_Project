try:
    bill = float(input("Enter total bill amount: "))
    paid = float(input("Enter amount paid: "))

    if paid < bill:
        print("Insufficient amount paid.")
    else:
        change = paid - bill
        print(f"Change to return: ${change:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
