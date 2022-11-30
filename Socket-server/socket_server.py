from asyncio.windows_events import NULL
import socket

class SocketServer:
    def __init__(self, host, port): 
        self.host = host
        self.port = port

    def createSocket(self) -> socket.socket:
        try: 
            newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            newSocket.bind((self.host, self.port))
            newSocket.listen()            
            return newSocket
        except socket.error as msg:
            raise msg
            
