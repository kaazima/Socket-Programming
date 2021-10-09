import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg = "Hello Server!"
sock.sendto(msg.encode(),(socket.gethostname(),12345))
