import random
import string
import sys
import pyperclip

def password_generator():
    while True:
        user_input = ask_for_user_input()
        validate_user_input(user_input)

def ask_for_user_input():
    user_input = input("Enter desired password length and press enter (leave blank for default length of 50) ('q' to quit)\n")
    return user_input

def validate_user_input(user_input):
    if user_input == "q" or user_input == "quit":
            exit_pw_generator()
    elif user_input == "":
        print_password(generate_password())
    else:
        try:
            print_password(generate_password(int(user_input)))
        except ValueError:
            password = generate_password()
            print(f"Invalid value, a password with 50 characters was generated and copied to clipboard instead:{password}\n")

def generate_password(length = 50):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    pyperclip.copy(password)
    return password

def print_password(password):
    print(f"Password generated and copied to clipboard: {password}\n")

def exit_pw_generator():
    print("Exiting password generator")
    sys.exit() 

if __name__ == "__main__":
    password_generator()

