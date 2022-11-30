import threading
import pickle

from chat_message import ChatMessage
from message_observer import MessageObserver
from type_messages import TypeMessage


class SocketMessage(threading.Thread):

    def __init__(self, listen, address, observerMessage: MessageObserver):
        self.listen = listen
        self.address = address
        self.lock = threading.Lock()
        messageObserver = observerMessage
        self.action = {
            TypeMessage.CONNECT: lambda chatMessage: messageObserver.notifyListernersToUserConnect(chatMessage),
            TypeMessage.MESSAGE: lambda chatMessage: messageObserver.notifyListenersToMessage(chatMessage),
            TypeMessage.DISCONNECT: lambda chatMessage: messageObserver.notifyListernersToUserDisconnect(
                chatMessage)
        }
        self.observerMessage = observerMessage
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                data = self.listen.recv(4096) 
                self.lock
                chatMessage = pickle.loads(data) 
                chatMessage.user.address = self.address
                chatMessage.user.listen = self.listen
                self.action[chatMessage.typeMessage](chatMessage)
            except ConnectionResetError:   
                if(chatMessage.typeMessage == TypeMessage.DISCONNECT):
                    self.listen.close()            
                    break