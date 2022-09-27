from socket import *
import time
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverIP = '127.0.0.1'
serverPort = 12345
for i in range(1,11):
    try:
        clientSocket.settimeout(2.0)
        sendtime = time.time()
        clientSocket.sendto("ping".encode(), (serverIP, serverPort))
        message = clientSocket.recv(1024).decode()
        recvtime = time.time()
        print(f"get: {message}")
        print(f"Ping {i} {round(recvtime - sendtime, 3)}")
    except TimeoutError:
        print('Request timed out')

