import socket

s = socket.socket()
HOST = 'localhost'
PORT = 15203

s.connect((HOST, PORT))
print (s.recv(1024))
s.close