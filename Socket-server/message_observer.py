from chat_message import ChatMessage
from type_messages import TypeMessage
from user import User

class MessageObserver:

    def __init__(self):
        self.message: ChatMessage
        self.users = []     

    def notifyListernersToUserConnect(self, message: ChatMessage):
        self.users.append(message.user)
        self.message = message
        self.__notifyAll()
    
    def notifyListenersToMessage(self, message: ChatMessage):
        self.message = message
        self.__notifyAll()

    def notifyListernersToUserDisconnect(self, message: ChatMessage):
        self.message = message
        self.users = list(filter((lambda element: element.address != message.user.address), self.users))
        self.__notifyAll()

    
    def __notifyAll(self):
        for user in self.users:
            user.sendMessage(self.message)
