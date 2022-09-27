from socket import *
host = "0.0.0.0"
server_port = 12333
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind((host, server_port))
cnt = 0
while True:
    message, client_ip= serverSocket.recvfrom(1024)
    print(f'get: {message.decode()}')
    if len(message) > 0:
        cnt += 1
    serverSocket.sendto(f'get {cnt} message'.encode(), client_ip)
    
