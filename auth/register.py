from functions import load_users, save_users

def email_validator(email):
    return '@' in email and '.' in email

def password_validator(password, email, confirm_password):
    return (len(password) >= 6 and password != email and
            password == confirm_password and any(char.isdigit() for char in password) and
            any(char.isupper() for char in password))

def register():
    errors = []
    print("Please enter the following details:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    phone = input("Enter your phone number: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    if not email_validator(email):
        errors.append("Invalid email: Email must contain '@' and '.'")

    if not password_validator(password, email, confirm_password):
        errors.append("Invalid password: Password must be at least 6 characters long, contain a digit, an uppercase letter, and match the confirmation.")

    users = load_users()
    if any(user["email"] == email for user in users):
        errors.append("Email is already registered.")

    if errors:
        print("\nValidation Errors:")
        for error in errors:
            print(f"• {error}")
        return None

    print("\n✅ Registration successful!")
    new_user = {
        "email": email,
        "password": password,
        "phone": phone,
        "name": name,
        "age": age
    }
    users.append(new_user)
    save_users(users)
    return new_user