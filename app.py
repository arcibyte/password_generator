import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

while True:
    password_len = int(input("How many characters do you want in your password?: "))
    password_count = int(input("How many passwords would you like to generate?: "))
    
    save_passwords = input("Do you want to save the passwords to a file? (yes/no): ").lower() == 'yes'

    passwords = []

    for _ in range(password_count):
        password = "".join(random.choice(chars) for _ in range(password_len))
        passwords.append(password)
        print("Here is your password:", password)

    if save_passwords:
        filename = input("Enter the filename to save passwords to: ")
        with open(filename, 'w') as file:
            for password in passwords:
                file.write(password + '\n')

        print(f"Passwords saved to {filename}")
