
from message_observer import MessageObserver
from socket_listen import SocketListen
from socket_server import SocketServer

def main(): 
    try:
        socketServer = SocketServer('127.0.0.1', 5555)
        socket = socketServer.createSocket()
        observerMessage = MessageObserver()
        socketListen = SocketListen(socket, observerMessage)
        socketListen.start()
    except Exception as e:
        print(e)


main()