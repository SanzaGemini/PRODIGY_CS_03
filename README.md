# PRODIGY_CS_03

# Password Strength Checker

This is a Python program that checks the strength of a password by validating various criteria such as length, presence of upper and lower case letters, special characters, and numeric digits. It provides feedback on the password's strength and offers suggestions for improvement.

## Features

- **Password Strength Validation**: 
  - Ensures the password contains at least 8 characters.
  - Checks for at least one upper-case letter, one lower-case letter, one special character, and one digit.
- **Password Feedback**: 
  - Displays color-coded feedback on the strength of the password:
    - Very Weak
    - Weak
    - Moderate
    - Good
    - Strong
- **Secure Input**: 
  - Password is securely entered using the `getpass` module, ensuring the password is hidden as the user types.

## Requirements

- Python 3.x
- Libraries:
  - `colorama`: For colorful terminal output.
  - `termcolor`: For additional color formatting.
  - `getpass`: For secure password input.
  - `re`: For regex-based password validation.

### Install Dependencies

You can install the required Python packages using `pip`:

```bash
pip install colorama termcolor
```

## How to Use

1. **Run the Program**:
   To start the program, simply run the Python script:

   ```bash
   python password_strength_checker.py
   ```

2. **Enter a Password**:
   - The program will prompt you to enter a password. As you type, the input will be hidden for security purposes.
   - After entering the password, the program will check its strength.

3. **Review Feedback**:
   - Based on the password strength, feedback will be displayed in color:
     - **Red** for very weak passwords.
     - **Light Red** for weak passwords.
     - **Yellow** for moderate passwords.
     - **Light Yellow** for good passwords.
     - **Green** for strong passwords.

4. **End the Program**:
   - If you wish to exit the program, enter `1` when prompted to input a password.

## Example

```bash
*** Welcome To Password Strength Checker Program ***

If You Want To End The Program Enter 1

Please enter password: 
```

After entering the password, you will see feedback like:

```
The Password Should Contain Upper Case Letters.
The Password Should Contain Special Characters.

You Have Entered A Weak Password!!!
```

Or:

```
You Have Entered A Strong Password:):):).
```

## Code Structure

- `get_password()`: Handles password input securely using `getpass`.
- `validate_password_length()`: Validates if the password is at least 8 characters long.
- `validate_password_has_regex()`: Checks if the password contains specific patterns (upper-case, lower-case, special characters, digits).
- `validate_password_strength()`: Orchestrates the validation process and calculates password strength.
- `determine_password_strength()`: Provides color-coded feedback based on the calculated password strength.

## License

This project is open-source and available for educational use.

---
