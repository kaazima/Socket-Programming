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
sum=0
for x in range(1,int(number/2)+1):
    if(number%x==0):
        sum+=x
if(number<sum):
    message=received+" is an abundant number"
else:
    message=received+" is not an abundant number"
connection.send(message.encode())
connection.close()
serversocket.close()
