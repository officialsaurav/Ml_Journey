import socket
from datetime import datetime

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("0.0.0.0",5000))
while True:
    message,client_address= server.recvfrom(1024)
    time=datetime.now().strftime("%A , %d  %B  %Y %I %L %S %p")
    server.sendto(time.encode(), client_address )