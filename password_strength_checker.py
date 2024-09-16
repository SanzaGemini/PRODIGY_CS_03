from termcolor import colored
from colorama import init
import getpass
import re

# Initialize colorama
init()

def get_password():
    print("\nIf You Want To End The Program Enter 1")
    password = getpass.getpass("\nPlease enter password: \n")
    if password == "1":
        return None
    else:
        return password

def validate_password_length(password):
    if len(password) >= 8:
        return 1, ""
    else:
        return -4, "\nThe Password Should Be 8 or More Characters."

def validate_password_has_regex(password, regex, message):
    if re.search(regex, password):
        return 1, ""
    else:
        return 0, f"\nThe Password Should Contain {message}"

def validate_password_strength(password):
    results = ""
    password_strength = 0

    # Define regex patterns
    special_regex = '[!@#$%^&*()_<>|\/{~:}]+'
    lower_regex = '[a-z]+'
    upper_regex = '[A-Z]+'
    digit_regex = '[\d]+'

    # Validate password length
    strength, result = validate_password_length(password)
    password_strength += strength
    results += result

    # Validate presence of upper case
    strength, result = validate_password_has_regex(password, upper_regex, "Upper Case Letters.")
    password_strength += strength
    results += result

    # Validate presence of lower case
    strength, result = validate_password_has_regex(password, lower_regex, "Lower Case Letters.")
    password_strength += strength
    results += result

    # Validate presence of special characters
    strength, result = validate_password_has_regex(password, special_regex, "Special Characters.")
    password_strength += strength
    results += result

    # Validate presence of digits
    strength, result = validate_password_has_regex(password, digit_regex, "Numeric Characters.")
    password_strength += strength
    results += result

    print(results)
    return password_strength

def determine_password_strength(password_strength):
    if password_strength <= 1:
        print(colored("\nYou Have Entered A Very Weak Password!!!", "white", "on_red"))
    elif password_strength == 2:
        print(colored("\nYou Have Entered A Weak Password!!!", "white", "on_light_red"))
    elif password_strength == 3:
        print(colored("\nYou Have Entered A Moderate Password!!!", "white", "on_light_yellow"))
    elif password_strength == 4:
        print(colored("\nYou Have Entered A Good Password:):):).", "white", "on_yellow"))
    else:
        print(colored("\nYou Have Entered A Strong Password:):):).", "white", "on_green"))

if __name__ == "__main__":
    print("*** Welcome To Password Strength Checker Program ***")
    while True:
        password = get_password()

        if password is None:
            break

        password_strength = validate_password_strength(password)
        determine_password_strength(password_strength)

    print("*** Thank You For Using Password Strength Checker Program ***")
