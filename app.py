import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKMNLROPQRSTUVWXYZ1234567890"

while True:
    password_len = int(input("How many characters do you want in your password?: "))
    password_count = int(input("How many passwords would you like to generate?: "))

    for _ in range(password_count):
        password = ""
        for _ in range(password_len):
            password_char = random.choice(chars)
            password += password_char

        print("Here is your password: ", password)
