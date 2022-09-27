import base64
from multiprocessing import connection
from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'
send_mail_LoginID = base64.b64encode(b'GS19875340909@gmail.com').decode() + '\r\n'
send_mail_Password = base64.b64encode(b'***').decode() + '\r\n'
send_mail_add = 'GS19875340909@gmail.com'
recv_mail_add = '***'
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    clientSocket.close()
# Send HELO command and print server response.
heloCommand = 'HELO meteorVmeteor\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    clientSocket.close()
# auth
clientSocket.send('AUTH LOGIN\r\n'.encode())
recv2 = clientSocket.recv(1024).decode()
if recv2[:3] != '334':
    print(f'{recv2} \r\n at auth')
    clientSocket.close()
# LoginID
clientSocket.send(send_mail_LoginID.encode())
recv3 = clientSocket.recv(1024).decode()
if recv3[:3] != '334':
    print('334 reply auth error.\r\nat login')
    clientSocket.close()
# Password
clientSocket.send(send_mail_Password.encode())
recv4 = clientSocket.recv(1024).decode()
if recv4[:3] != '235':
    print(recv4)
    clientSocket.close()
# MAIL FROM
clientSocket.send(f'MAIL FROM: <{send_mail_add}> \r\n'.encode())
recv5 = clientSocket.recv(1024).decode()
if recv5[:3] != '250':
    print(f'{recv5} \r\nat mail from')
    clientSocket.close()
# RCPT TO
clientSocket.send(f'RCPT TO: <{send_mail_add}> \r\n'.encode())
recv6 = clientSocket.recv(1024).decode()
if recv6[:3] != '250':
    print(f'{recv6} \r\nat recp to')
    clientSocket.close()
# Send DATA command and print server response.
clientSocket.send('DATA\r\n'.encode())
recv7 = clientSocket.recv(1024).decode()
if recv7[:3] != '354':
    print(f'{recv7} \r\nat send data request')
    clientSocket.close()
# Send message data.
message = "From: "+'me' +'\r\n'
message += "To: "+'me' +'\r\n'
message += "Subject: " + 'mail by using SMTP!!!' +'\r\n'
message += f'Hello! Another me ^ ^{msg}'
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
recv8 = clientSocket.recv(1024).decode()
if recv8[:3] != '250':
    print(f'{recv8} \r\nat send message data')
    clientSocket.close()
# Send QUIT command and get server response.
clientSocket.send('QUIT\r\n'.encode())
recv9 = clientSocket.recv(1024).decode()
if recv9[:3] != '221':
    print(recv9)
clientSocket.close()