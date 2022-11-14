import pickle


class User:
    def __init__(self, userName: str, listen, address):
        self.listen = listen
        self.address = address
        self.name = userName
     
     
    def sendMessage(self, chatMessage):
        if(chatMessage.user.address[1] != self.address[1]):
            chatMessage.user.listen = None
            data = pickle.dumps(chatMessage)
            self.listen.send(data)