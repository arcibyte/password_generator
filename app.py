import random
import string

def generate_password(password_len, use_special_chars=True):
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation

    password = "".join(random.choice(chars) for _ in range(password_len))
    return password

while True:
    password_len = int(input("How many characters do you want in your password?: "))
    password_count = int(input("How many passwords would you like to generate?: "))
    include_special_chars = input("Do you want to include special characters in the passwords? (yes/no): ").lower() == 'yes'

    save_passwords = input("Do you want to save the passwords to a file? (yes/no): ").lower() == 'yes'

    passwords = []

    for _ in range(password_count):
        password = generate_password(password_len, include_special_chars)
        passwords.append(password)
        print("Here is your password:", password)

    if save_passwords:
        filename = input("Enter the filename to save passwords to: ")
        with open(filename, 'w') as file:
            for password in passwords:
                file.write(password + '\n')

        print(f"Passwords saved to {filename}")
