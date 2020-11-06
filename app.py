import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

while True:
    password_len = int(input("How many characters do you want in your password?: "))
    password_count = int(input("How many passwords would you like to generate?: "))

    for _ in range(password_count):
        password = "".join(random.choice(chars) for _ in range(password_len))
        print("Here is your password:", password)
