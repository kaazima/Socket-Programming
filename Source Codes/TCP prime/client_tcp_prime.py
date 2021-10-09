import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((socket.gethostname(), 25000))
message="25"
clientsocket.send(message.encode())
msg = clientsocket.recv(1024)
received=msg.decode()
print(received)
clientsocket.close()
