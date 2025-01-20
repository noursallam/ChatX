import socket
import threading
from auth.login import login
from chat.client import ChatClient

HOST = socket.gethostbyname(socket.gethostname())
PORT = 12345
LISTENER = 5
ACTIVE_CONNECTIONS = []

def listen_for_connections(client, username):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                if ChatClient.check_spam(message):
                    send_message_to_all(f"{username} spammed the chat")
                    continue
                final_msg = f"{username} ~ {message}"
                send_message_to_all(final_msg)
            else:
                print(f"The message sent from {username} is empty")
        except:
            print(f"{username} has disconnected")
            ACTIVE_CONNECTIONS.remove((username, client))
            break

def send_message_to_client(client, message):
    client.send(message.encode('utf-8'))

def send_message_to_all(message):
    for user in ACTIVE_CONNECTIONS:
        send_message_to_client(user[1], message)

def client_handler(client):
    while True:
        try:
            username = client.recv(2048).decode('utf-8')
            if username:
                ACTIVE_CONNECTIONS.append((username, client))
                prompt_message = f"SERVER~ {username} has joined the chat"
                send_message_to_all(prompt_message)
                break
            else:
                print("Client username is empty")
        except:
            print("Error receiving username")
            return

    threading.Thread(target=listen_for_connections, args=(client, username)).start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST}:{PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")
        return

    server.listen(LISTENER)
    print("Server is listening for connections...")

    while True:
        client, address = server.accept()
        print(f"Successfully connected to client {address[0]}:{address[1]}")
        threading.Thread(target=client_handler, args=(client,)).start()

if __name__ == '__main__':
    main()