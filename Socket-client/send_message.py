import threading
import pickle

from type_messages import TypeMessage
from chat_message import ChatMessage


class SendMessage(threading.Thread):

    def __init__(self, socket, user):
        self.socket = socket
        self.user = user
        self.lock = threading.Lock()
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                message = input()
                
                if(message == "EXIT"):
                    chatMessage = ChatMessage(
                        self.user, f"{self.user.name} Saiu", TypeMessage.DISCONNECT)
                    data = pickle.dumps(chatMessage)
                    self.socket.sendall(data)
                    break;    
                
                chatMessage = ChatMessage(self.user, message, TypeMessage.MESSAGE)
                data = pickle.dumps(chatMessage)
                self.socket.sendall(data)
            except EOFError:
                print('Saiu do servidor.')
                quit()
            