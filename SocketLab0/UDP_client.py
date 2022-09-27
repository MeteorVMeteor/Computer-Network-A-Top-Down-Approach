from socket import *
server_ip_address = '127.0.0.1'
server_port = 12333
serverSocket = socket(AF_INET, SOCK_DGRAM) 
message = "hello!"
serverSocket.sendto(message.encode(), (server_ip_address, server_port))
recv_message , server_ip = serverSocket.recvfrom(1024)
print(recv_message.decode())
serverSocket.close()