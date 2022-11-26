import threading
import socket
from message_observer import MessageObserver

from socket_listen_messages import SocketMessage


class SocketListen(threading.Thread):

    def __init__(self, socket: socket.socket, observerMessage: MessageObserver):
        self.socket = socket
        self.lock = threading.Lock()
        self.observerMessage = observerMessage   
        threading.Thread.__init__(self)

    def run(self):
        while True:           
            try:
                listen, address = self.socket.accept()
                self.lock
                socketMessage = SocketMessage(listen, address, self.observerMessage)
                socketMessage.start()
            except BaseException as e:
                print(e)            
