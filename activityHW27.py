import random
import string

def generate_password(length):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password_list = random.sample(chars, length)
    random.shuffle(password_list)
    return "".join(password_list)

length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
