# PRODIGY_CS_03

# Password Strength Checker Program

This Python program allows users to check the strength of their passwords by analyzing various criteria such as length, the presence of uppercase and lowercase letters, special characters, and numeric characters. It provides immediate feedback on the password strength with a colored message.

## Features
- **Password Length Validation:** Ensures that passwords have at least 8 characters.
- **Regex-Based Validation:** Validates the presence of uppercase letters, lowercase letters, digits, and special characters.
- **Password Strength Feedback:** Provides color-coded feedback on the strength of the password (very weak, weak, moderate, good, or strong).
- **Secure Password Input:** Uses `getpass` to securely input the password without displaying it on the screen.
- **Program Termination:** Allows the user to exit the program by entering '1' at the password prompt.

## How It Works
1. **Password Input:** 
   - The user is prompted to enter a password using the `getpass` module, which hides the input on the screen for security.
   - If the user inputs '1', the program terminates.

2. **Password Strength Validation:**
   - The program checks if the password meets the following criteria:
     - Contains at least 8 characters.
     - Contains at least one uppercase letter.
     - Contains at least one lowercase letter.
     - Contains at least one numeric character.
     - Contains at least one special character (e.g., `!@#$%^&*()`).

3. **Strength Calculation:**
   - Based on the password’s compliance with the above rules, the program calculates a strength score.
   - A score of `5` indicates a strong password, and lower scores indicate progressively weaker passwords.

4. **Color-Coded Feedback:**
   - The program provides immediate feedback on the password's strength using color-coded messages:
     - **Very Weak:** Red background
     - **Weak:** Light red background
     - **Moderate:** Yellow background
     - **Good:** Light yellow background
     - **Strong:** Green background

## Dependencies
- **termcolor:** For displaying colored text output in the terminal.
- **colorama:** Initializes color support on Windows.
- **getpass:** Allows secure password input without echoing the characters.
- **re:** For regular expression-based validation of password content.

## Functions

### `getPassword()`
- Prompts the user to enter a password securely using `getpass`.
- Allows termination of the program if the user enters '1'.

### `validatePasswordLength(password)`
- Checks if the password length is at least 8 characters.
- Returns a score and feedback message.

### `validatePasswordHasRegex(password, regex, message)`
- Validates whether the password contains a pattern based on the provided regex (e.g., uppercase letters, digits).
- Returns a score and feedback message.

### `validatePasswordStrength(password)`
- Validates the strength of the password by checking for length, upper/lowercase letters, special characters, and digits.
- Returns the overall password strength score.

### `determinePasswordStrength(passwordStrength)`
- Provides color-coded feedback based on the password strength score.

## How to Use

1. **Install Dependencies:**
   - Install the required libraries by running:
     ```bash
     pip install termcolor colorama
     ```

2. **Run the Program:**
   - Execute the Python program from the command line:
     ```bash
     python password_strength_checker.py
     ```

3. **Follow the Prompts:**
   - The program will prompt you to enter a password. Based on the entered password, it will give you feedback on its strength.

4. **Exit the Program:**
   - You can exit the program by entering `1` when prompted for the password.

## Example

```
*** Welcome To Password Strength Checker Program ***

If You Want To End The Program Enter 1

Please enter password: 
Password: ********

The Password Should Contain Upper Case Letters.
The Password Should Contain Special Characters.

You Have Entered A Moderate Password!!!

*** Thank You For Using Password Strength Checker Program ***
```

## License
This program is free to use for personal or educational purposes.

---
