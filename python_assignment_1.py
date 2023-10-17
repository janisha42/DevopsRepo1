import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase, lowercase, digit, and special character checks using regular expressions
    if not re.search(r'[A-Z]', password) or \
       not re.search(r'[a-z]', password) or \
       not re.search(r'[0-9]', password) or \
       not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    # Password meets all criteria
    return True

# Get user input for password
password = input("Enter your new password: ")

# Check password strength and provide feedback to the user
if check_password_strength(password):
    print("Password is strong and meets all criteria.")
else:
    print("Password is weak. Please ensure it has at least 8 characters, includes uppercase and lowercase letters, a digit, and a special character.")
