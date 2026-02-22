test_dict = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}

print("Dictionary:", test_dict)

value = input("Enter the value you want to check the frequency of: ")

if value in test_dict:
    print("Frequency:", test_dict[value])
else:
    print("That value is not in the dictionary.")
