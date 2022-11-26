import pickle

class User:
    def __init__(self, userName: str, listen, address):
        self.listen = listen
        self.address = address
        self.name = userName

    def sendMessage(self, chatMessage):
        if(chatMessage.user.address[1] != self.address[1]):
            message = chatMessage.getMessage()
            data = pickle.dumps(message)
            self.listen.sendall(data)
