import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 25000))
serversocket.listen()
print("Server is listening....")
connection, address = serversocket.accept()
print("Connection has been established")
msg = connection.recv(1024)
received=msg.decode()
number=int(received)
count=0
flag=0
for x in range(1,number+1):
    if(number%2==0):
        count+=1
    if(count>2):
        flag=1
        break
if(flag==0):
    message="Prime"
    connection.send(message.encode())
else:
    message="Composite"
    connection.send(message.encode())
connection.close()
serversocket.close()
