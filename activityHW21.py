def square_odd_even(start, end):
    even_squares = []
    odd_squares = []

    for num in range(start, end + 1):
        square = num * num
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Even square values:", even_squares)
    print("Odd square values:", odd_squares)


# Taking input from user
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

square_odd_even(start, end)
