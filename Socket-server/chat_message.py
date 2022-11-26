from type_messages import TypeMessage
from user import User

class ChatMessage:
    def __init__(self, user: User, message: str, typeMessage: TypeMessage):
        self.user = user
        self.message = message
        self.typeMessage = typeMessage

    def getMessage(self):
        return ChatMessage(User(self.user.name, None, None), self.message, self.typeMessage)