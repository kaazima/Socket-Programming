import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((socket.gethostname(),12345))
print("Waiting for client...")
data = sock.recvfrom(1024)	      
print("Received Messages:",data[0].decode()," from",data[1])
