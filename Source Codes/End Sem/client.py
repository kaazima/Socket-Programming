import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((socket.gethostname(), 25000))
message=input("Please enter a positive number -> ")
clientsocket.send(message.encode())
msg = clientsocket.recv(1024)
rcv=msg.decode()
print(rcv)
clientsocket.close()
