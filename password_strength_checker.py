from termcolor import colored
from colorama import init
import getpass
import re

# Initialize colorama for color display on Windows
init()

def getPassword():
    """
    Prompts the user to enter a password securely using getpass.
    Allows termination of the program if the user enters '1'.
    
    Returns:
        str or None: The entered password or None if the user wants to exit.
    """
    print("\nIf You Want To End The Program Enter 1")
    password = getpass.getpass("\nPlease enter password: \n")
    if password == "1":
        return None
    else:
        return password

def validatePasswordLength(password):
    """
    Checks if the password length is at least 8 characters.
    
    Args:
        password (str): The password to validate.

    Returns:
        tuple: (score, message) where score is 1 for valid length, otherwise -4, 
        and message is the feedback to the user.
    """
    if len(password) >= 8:
        return 1, ""
    else:
        return -4, "\nThe Password Should Be 8 or More Characters."

def validatePasswordHasRegex(password, regex, message):
    """
    Validates whether the password contains a pattern based on the provided regex.
    
    Args:
        password (str): The password to validate.
        regex (str): The regular expression to check.
        message (str): The feedback message in case of failure.

    Returns:
        tuple: (score, message) where score is 1 if the regex matches, otherwise 0.
    """
    if re.search(regex, password):
        return 1, ""
    else:
        return 0, f"\nThe Password Should Contain {message}"

def validatePasswordStrength(password):
    """
    Validates the strength of the password by checking multiple conditions 
    such as length, uppercase, lowercase, special characters, and digits.
    
    Args:
        password (str): The password to validate.

    Returns:
        int: The overall password strength score.
    """
    results = ""
    passwordStrength = 0

    # Define regex patterns for validation
    specialRegex = '[!@#$%^&*()_<>|\/{~:}]+'
    lowerRegex = '[a-z]+'
    upperRegex = '[A-Z]+'
    digitRegex = '[\d]+'

    # Validate password length
    strength, result = validatePasswordLength(password)
    passwordStrength += strength
    results += result

    # Validate presence of upper case
    strength, result = validatePasswordHasRegex(password, upperRegex, "Upper Case Letters.")
    passwordStrength += strength
    results += result

    # Validate presence of lower case
    strength, result = validatePasswordHasRegex(password, lowerRegex, "Lower Case Letters.")
    passwordStrength += strength
    results += result

    # Validate presence of special characters
    strength, result = validatePasswordHasRegex(password, specialRegex, "Special Characters.")
    passwordStrength += strength
    results += result

    # Validate presence of digits
    strength, result = validatePasswordHasRegex(password, digitRegex, "Numeric Characters.")
    passwordStrength += strength
    results += result

    print(results)
    return passwordStrength

def determinePasswordStrength(passwordStrength):
    """
    Prints out a colored message based on the strength score of the password.
    
    Args:
        passwordStrength (int): The strength score of the password.
    """
    if passwordStrength <= 1:
        print(colored("\nYou Have Entered A Very Weak Password!!!", "white", "on_red"))
    elif passwordStrength == 2:
        print(colored("\nYou Have Entered A Weak Password!!!", "white", "on_light_red"))
    elif passwordStrength == 3:
        print(colored("\nYou Have Entered A Moderate Password!!!", "white", "on_light_yellow"))
    elif passwordStrength == 4:
        print(colored("\nYou Have Entered A Good Password:):):).", "white", "on_yellow"))
    else:
        print(colored("\nYou Have Entered A Strong Password:):):).", "white", "on_green"))

if __name__ == "__main__":
    print("*** Welcome To Password Strength Checker Program ***")
    
    while True:
        # Get the password from the user
        password = getPassword()

        if password is None:
            break

        # Validate the strength of the entered password
        passwordStrength = validatePasswordStrength(password)

        # Determine the strength and provide feedback
        determinePasswordStrength(passwordStrength)

    print("*** Thank You For Using Password Strength Checker Program ***")
