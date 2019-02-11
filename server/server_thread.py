import threading
from socket import SHUT_RDWR
from static_handler.request_handler import request_handler
from request import request_file

class connectionThread(threading.Thread):
    def __init__(self, connSocket):
        threading.Thread.__init__(self)
        self.connSocket = connSocket
    def run(self):
        try:
            headers = self.connSocket.recv(1024).decode('utf8').rstrip("\r\n")
            request = request_file(headers)
            handler = request_handler()
            path = request.get_headers("path")
            print(path)
            response = handler.hand(request)
            self.connSocket.send(response)
        finally:
            self.connSocket.shutdown(SHUT_RDWR)
            self.connSocket.close()