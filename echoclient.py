import socket
UDP_IP_ADDRESS="127.0.0.1"
UDP_PORT_NO=6600
Message="Hello,Server"
bytesToSend=str.encode(Message)
clientSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend,(UDP_IP_ADDRESS,UDP_PORT_NO))				
data=clientSock.recvfrom(1024)
print (data)
