# socket simple writing: server client
 #Server 
import socket # import socket module
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 # socket.AF_INET : indicates network-based
 # socket.SOCK_STREAM: indicates that it is based on the TCP protocol.
serv.bind(("127.0.0.1", 8000))
 # bind(ip address, port number---" Yuanzu's form): Bind on that computer as a server
serv.listen(5)
 # listen(n): indicates that 5 links are received at the same time, n: control backlog, ie: semi-link pool;
conn, addr = serv.accept()
 # serv.accept(): indicates that the request information of the client is received.
 # At this point, the server will receive: a tcp link, client ip address, in the form of Yuanzu
 #-------------- Complete the three-way handshake ---------------------------
msg = conn.recv(1024)
 #conn.recv(1024): Accept the content sent by the client from the link, 1024 indicates the size
print("Customer's request information:", msg)
conn.send(msg.upper())
 # After receiving the request information content of the client, send: reply to the client one content, the content is not necessarily msg.upper()
 # 
 #-------------- Complete the data transfer above -----------------------------
conn.close()
 #Close link
serv.close()
 #
