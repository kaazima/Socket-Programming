import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((socket.gethostname(), 25000))
msg = clientsocket.recv(1024)
received=msg.decode()
number=int(received)+100
print(number)
clientsocket.close()
