#import socket module 
from socket import * 
import sys # In order to terminate the program 
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a server socket 
#Fill in start 
host = "localhost"
port = 12333
serverSocket.bind((host, port))
serverSocket.listen(1)
#Fill in end 
while True: 
 #Establish the connection 
    print('Ready to serve...') 
    #Fill in start
    connectionSocket, addr = serverSocket.accept() # accept() return a new socekt and addr
    #Fill in end
    try: 
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        print(str(message))
        f = open(filename[1:], "r")  
        outputdata = f.readlines()#Fill in start #Fill in end   
        #Send one HTTP header line into socket 
        #Fill in start 
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('\r\n'.encode()) 
        #Fill in end  
        #Send the content of the requested file to the client  
        for i in range(0, len(outputdata)):  
            connectionSocket.send(outputdata[i].encode())  
        connectionSocket.send('\r\n'.encode()) 
        connectionSocket.close() 
    except IOError: 
        #Send response message for file not found 
        #Fill in start 
        connectionSocket.send('HTTP/1.1 404 not found\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        #Fill in end 
        #Close client socket 
        #Fill in start 
        connectionSocket.send(f'File:{message.split()[1]} Not Exist'.encode())
        #Fill in end  
serverSocket.close() 
sys.exit()#Terminate the program after sending the corresponding data  
