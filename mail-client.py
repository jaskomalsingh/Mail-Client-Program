from socket import *
import ssl
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver mailserver = #Fill in start #Fill in end
mailserver = ('smtp.gmail.com', 465) #gmail server

# Create socket called clientSocket and establish a TCP connection with mailserver

# Fill in start

clientSocket = ssl.wrap_socket(socket(AF_INET,SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23) #create socket with SSL
clientSocket.connect(mailserver) #socket tries to connect to gmail server

# Fill in end

recv = clientSocket.recv(1024).decode()
print("msg from server: " + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response. heloCommand = 'HELO Alice\r\n' clientSocket.send(heloCommand.encode())
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print("msg from server: " + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.

#Authorization
clientSocket.send('AUTH LOGIN\r\n'.encode()) 
response1 = clientSocket.recv(2048) 
#Hardcode email and password
email_username = base64.b64encode('networkingece4436uwo@gmail.com'.encode())
email_password = base64.b64encode('xsjw nrot fjjh hwga'.encode())

clientSocket.send(email_username + '\r\n'.encode())  
clientSocket.send(email_password + '\r\n'.encode())

print("login message: " + clientSocket.recv(1024).decode() + " end of login message\n")
# Fill in start

clientSocket.send("MAIL FROM: <networkingece4436uwo@gmail.com>\r\n".encode())    
recv2 = clientSocket.recv(1024).decode()    
print("msg from MAIL FROM command: " + recv2)


# Fill in end

# Send RCPT TO command and print server response.

# Fill in start
recipient_email = input("Who is the recipient of this email: ") #ask user to input who the recipient of the email
RCPTTO = 'RCPT TO: <'+recipient_email+'>\r\n' #SMTP command.
clientSocket.send(RCPTTO.encode()) 
recv3 = clientSocket.recv(1024).decode()    
print("RCPT TO msg: " + recv3)

# Fill in end


# Send DATA command and print server response.

# Fill in start
clientSocket.send('DATA\r\n'.encode()) 
print("DATA response: " + clientSocket.recv(1024).decode())#print the response
# Fill in end

# Send message data.

# Fill in start
message = "Subject: This is the subject line.\r\n"+msg 
clientSocket.send(message.encode()) 
# Fill in end

# Fill in start
clientSocket.send(endmsg.encode()) 
# Fill in end

# Send QUIT command and get server response.

# Fill in start
clientSocket.send('QUIT\r\n'.encode())
print('quit message: ' + clientSocket.recv(1024).decode())
clientSocket.close()

# Fill in end