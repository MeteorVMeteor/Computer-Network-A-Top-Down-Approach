from logging.config import listen
from socket import *
import sys
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(('0.0.0.0', 2345))
tcpSerSock.listen(5)
# Fill in end.
while 1:
    # Strat receiving data from the client
    # print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    # print('Received a connection from:', addr)
    # Fill in start.
    message = tcpCliSock.recv(4096).decode()
    # print(message)
    # Fill in end.
    # Extract the filename from the given message
    # for http
    allpath = message.split()[1].partition("//")[2]
    # for https
    # allpath = message.split()[1].partition(':')[0]
    # print(f'allpath: {allpath}')
    filename = allpath.replace('/','_')
    # print(f'filename: {filename}')
    fileExist = False
    filetouse = "D:/Download/CS/SocketLab/SocketLab5/cache/" + filename
    # print(f'filetouse: {filetouse}')
    try:
        # Check wether the file exist in the cache
        f = open(filetouse, "r")
        outputdata = f.read()
        fileExist = True
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())
        # Fill in start.
        tcpCliSock.send(outputdata.encode())
        f.close()
        # Fill in end.
        print('Read from cache')
        # Error handling for file not found in cache
    except IOError:
        if fileExist == False: 
            # Create a socket on the proxyserver
            # Fill in start. 
            c = socket(AF_INET, SOCK_STREAM)
            # Fill in end.
            hostn = allpath.partition('/')[0]
            # print(f"hostn: {hostn}")
            try:
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, 80))
                c.send(message.encode())
                # Fill in end.
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket
                cachemessage = c.recv(4096).decode()
                tcpCliSock.send(cachemessage.encode())
                # Fill in start.
                tmpFile = open(filetouse,"w")
                tmpFile.write(cachemessage.replace('\r\n', '\r'))
                tmpFile.close()
                print('Read from server')
                # Fill in end.
            except:
                print("Illegal request")
            c.close()
        else:
            # HTTP response message for file not found
            # Fill in start.
            tcpCliSock.send("HTTP/1.0 404 Not Found\r\n".encode())
            tcpCliSock.send("\r\n".encode())
            tcpCliSock.send(f"{filename} not existed".encode())
            # Fill in end.
    # Close the client and the server sockets
    tcpCliSock.close()
# Fill in start.
tcpSerSock.close()
# Fill in end.
