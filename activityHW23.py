class Reverse:
    def __init__(self, s=""):
        self.s = s

    def get_reversed(self):
        return self.s[::-1]

# Get input from user
user_input = input("Enter a word: ")
r = Reverse(user_input)
print("Reversed:", r.get_reversed())
