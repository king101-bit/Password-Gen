import secrets
import string
import requests
import hashlib

def generate_password(length=16, require_special_chars=True, require_digits=True):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''

    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))

        if (not require_special_chars or any(char in string.punctuation for char in password)) and \
                (not require_digits or sum(char in string.digits for char in password) >= 3):
            break

    return password

def is_password_pwned(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    response_lines = response.text.splitlines()
    for line in response_lines:
        if line.startswith(suffix):
            return True
    return False

def main_menu():
    print("===== Password Generator =====")
    print("1. Generate a new password")
    print("2. Specify the number of characters")
    print("3. Check if a password is pwned")
    print("4. Exit")
    print("==============================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        length = int(input("Enter the desired password length (4-20): "))
        password = generate_password(length=length)
        print(f"Generated password: {password}")
    elif choice == "2":
        num_chars = int(input("Enter the number of characters for the password: "))
        password = generate_password(length=num_chars)
        print(f"Generated password: {password}")
    elif choice == "3":
        password = input("Enter the password to check: ")
        if is_password_pwned(password):
            print("This password has been pwned. Please choose a different one.")
        else:
            print("This password has not been pwned. You can use it.")
    elif choice == "4":
        return
    else:
        print("Invalid choice. Please try again.")

    print()
    main_menu()

# Start the program
main_menu()
