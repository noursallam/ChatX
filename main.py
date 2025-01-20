import keyboard
from auth.register import register
from auth.login import login
from chat.client import ChatClient
import socket

def main():
    print("Welcome to ChatX!")
    print("Press 'Ctrl + R' to register or 'Ctrl + L' to login.")

    keyboard.add_hotkey('ctrl+r', register_user)
    keyboard.add_hotkey('ctrl+l', login_user)

    keyboard.wait('esc')

def register_user():
    print("\n--- Registration Page ---")
    user = register()
    if user:
        print("✅ Registration successful! Redirecting to the chat...")
        start_chat(user['name'])

def login_user():
    print("\n--- Login Page ---")
    user = login()
    if user:
        print("✅ Login successful! Redirecting to the chat...")
        start_chat(user['name'])

def start_chat(username):
    print(f"\n--- Chat Page ---")
    print(f"Welcome, {username}! Press 'Ctrl + Q' to logout.")

    chat_client = ChatClient(socket.gethostbyname(socket.gethostname()), 12345)
    chat_client.send_messages(username)

    keyboard.add_hotkey('ctrl+q', logout, args=(username,))

def logout(username):
    print(f"\n{username} has logged out. Returning to the login page...")
    login_user()

if __name__ == "__main__":
    main()