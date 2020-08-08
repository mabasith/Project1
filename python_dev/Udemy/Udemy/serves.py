from socket import *
from time import ctime
from threading import Thread

class ClientHandler(Thread):

    def __init__(self, client):
        Thread.__init__(self)
        self._client = client
    def run(self):
        self._client.send(bytes(ctime() + " Have a nice day!, ascii"))
        self._client.close()
HOST = 'localhost'
PORT = 15203
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('waiting for connection...')
    client, address = server.accept()
    print('... connected from:', address)
    handler = ClientHandler(client)
    handler.start()