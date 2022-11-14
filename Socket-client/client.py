import socket, pickle

from chat_message import ChatMessage
from user import User
from type_messages import TypeMessage

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5555  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    user = User("vinicius")
    chatMessage = ChatMessage(user, "vinicius Entrou", TypeMessage.CONNECT)
    data = pickle.dumps(chatMessage)
    s.sendall(data)
    while True:
        data = s.recv(1024)
        chatMessage = pickle.loads(data)
        print(f"Received {chatMessage.user.name!r}")