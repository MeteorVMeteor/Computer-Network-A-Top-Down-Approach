from socket import *
server_ip_address = '127.0.0.1'
server_port = 12333
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((server_ip_address, server_port))
clientSocket.sendall('GET /hellotcp.html HTTP/1.1\r\n'.encode())
clientSocket.send('\r\n'.encode()) 
while True:
    get_message = clientSocket.recv(2048).decode()
    if len(get_message) == 0:
        print('connection closed')
        break
    print(get_message)
clientSocket.close()
