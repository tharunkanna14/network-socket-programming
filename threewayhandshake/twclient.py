# socket simple writing: server client
 # 
import socket #import socket module
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 # socket.AF_INET : indicates network-based
 # socket.SOCK_STREAM: indicates that it is based on the TCP protocol.
client.connect(("127.0.0.1",8000))
 #connect((server IP, port number)): indicates the connection server
 #-------------- Complete the three-way handshake ---------------------------
client.send("hello".encode("utf-8"))
 #Connect to the server, send (): send to the server, the content must be binary
data=client.recv(1024)
 #recv(1024) The client accepts the content replied by the server
 #-------------- Complete the data transfer above -----------------------------
print(data)
