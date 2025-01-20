from functions import load_users

def login():
    print("\n--- Login Page ---")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    users = load_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            print("\n✅ Login successful! Welcome back.")
            return user

    print("\n❌ Login failed. Invalid email or password.")
    return None