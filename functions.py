# functions.py

import os
import json

USER_DATA_FILE = "auth/users.json"

def load_users():
    """Load existing users from the JSON file."""
    if not os.path.exists(USER_DATA_FILE):
        return []
    
    try:
        with open(USER_DATA_FILE, "r") as file:
            if os.path.getsize(USER_DATA_FILE) == 0:
                return []
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_users(users):
    """Save the list of users to the JSON file."""
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)



def email_validator(email):
    """Validate the email format."""
    if '@' in email and '.' in email:
        return True
    else:
        return False

def password_validator(password, email, confirm_password):
    """Validate the password."""
    if len(password) < 6:
        return False
    elif password in email:
        return False
    elif password != confirm_password:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isupper() for char in password):
        return False
    else:
        return True

def register():
    """Register a new user."""
    errors = []

    # Inputs
    print("Please enter the following details:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    phone = input("Enter your phone number: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    # Validate email
    if not email_validator(email):
        errors.append("Invalid email: Email must contain '@' and '.'")

    # Validate password
    if not password_validator(password, email, confirm_password):
        errors.append("Invalid password: Password must be at least 6 characters long, contain a digit, an uppercase letter, and match the confirmation.")

    # Check if the email is already registered
    users = load_users()
    if any(user["email"] == email for user in users):
        errors.append("Email is already registered.")

    # Display validation results
    if errors:
        print("\nValidation Errors:")
        for error in errors:
            print(f"• {error}")
        return None  # Registration failed
    else:
        print("\n✅ Registration successful!")
        # Create a new user dictionary
        new_user = {
            "email": email,
            "password": password,  # In a real app, hash the password before saving!
            "phone": phone,
            "name": name,
            "age": age
        }
        # Add the new user to the list and save
        users.append(new_user)
        save_users(users)
        return new_user
print(USER_DATA_FILE)
def login():

    """Login an existing user."""
    print("Please enter the following details:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Load existing users
    users = load_users()

    # Check if the user exists and the password matches
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("\n✅ Login successful! Welcome back.")
            return user  # Return the logged-in user

    # If no match is found
    print("\n❌ Login failed. Invalid email or password.")
    return None