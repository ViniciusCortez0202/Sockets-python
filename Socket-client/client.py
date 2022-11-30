import socket, pickle

from chat_message import ChatMessage
from user import User
from type_messages import TypeMessage
from send_message import SendMessage

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 5555  # The port used by the server
def start(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        chatMessage = connect()
        data = pickle.dumps(chatMessage)
        s.sendall(data)
        sendMessage = SendMessage(s, chatMessage.user)
        sendMessage.start()
        while True:
            if(not sendMessage.is_alive):            
                break
            data = s.recv(4096)
            chatMessage = pickle.loads(data)
            if chatMessage.typeMessage == TypeMessage.CONNECT:
                print(f"{chatMessage.message}")
            elif chatMessage.typeMessage == TypeMessage.DISCONNECT:
                print(f"{chatMessage.message}")
            elif chatMessage.typeMessage == TypeMessage.MESSAGE:
                print(f"{chatMessage.user.name}: {chatMessage.message}")
            else:
                print(f"FAIL")
def connect():
    userName = input("Insira seu nome: ")
    user = User(userName=userName)
    return ChatMessage(user, f"{userName} Entrou", TypeMessage.CONNECT)

start()