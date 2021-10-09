import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 25000))
message="Hello Server!"
clientsocket.send(message.encode())
clientsocket.close()
