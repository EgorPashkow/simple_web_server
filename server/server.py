import threading
from socket import *
from server_thread import connectionThread

class serverThread():
    def __init__(self):
        threading.Thread.__init__(self)
        self.serverPort = 80
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.connectionThreads = []
    def run(self):
        self.serverSocket.bind(('127.0.0.1', self.serverPort))
        self.serverSocket.listen(1)
        while True:
            connectionSocket,addr = self.serverSocket.accept()
            self.connectionThreads.append(connectionThread(connectionSocket))
            self.connectionThreads[-1].daemon = 1
            self.connectionThreads[-1].start()
    def close(self):
        for t in self.connectionThreads:
            try:
                t.connSocket.shutdown(SHUT_RDWR)
                t.connSocket.close()
            except socket.error:
                pass
        self.serverSocket.shutdown(SHUT_RDWR)
        self.serverSocket.close()

server = serverThread()
server.run()
server.close()