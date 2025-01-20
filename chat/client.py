import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(message)
                else:
                    break
            except:
                print("Disconnected from the server")
                self.client_socket.close()
                break

    def send_messages(self, username):
        self.client_socket.send(username.encode('utf-8'))
        threading.Thread(target=self.receive_messages).start()

        while True:
            message = input()
            if message.lower() == 'exit':
                break
            elif self.check_spam(message):
                print("You are not allowed to send this message")
                continue
            self.client_socket.send(message.encode('utf-8'))

        self.client_socket.close()

    @staticmethod
    def check_spam(message):
        xwords = ['alsisi', 'egypt', 'syria', 'suria', 'hack', 'hate', 'مصر', 'israel']
        return any(word in message.lower() for word in xwords)