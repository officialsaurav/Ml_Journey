"""For a TCP based daytime server
● socket() – Create the Communication Endpoint
○ The server first creates a socket, which is like a telephone or communication endpoint.
○ Without a socket, the server cannot communicate over the network.
● bind() – Assign an Address to the Socket
○ The server assigns its socket to a specific IP address and port number so clients know where to find  it.

● listen() – Wait for Clients
○ The server starts listening for incoming connection requests.
● accept() – Accept a Client Connection
○ When a client requests a connection, the server accepts it.
● Get the Current Time
○ Before sending data, the server reads the system clock.
● send() – Send the Current Time
○ The server sends the current date and time to the client.
● close()- close the connection
○ Once the server has sent the current time, there is nothing more to send, so it closes the
connection."""


import socket
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "0.0.0.0"
PORT = 5000

server.bind((HOST, PORT))
server.listen(1)
print("Server is running...")

while True:
    client_socket, client_address = server.accept()
    time_str = datetime.now().strftime("%A, %d %b %Y %I:%M:%S %p")
    print(f"Connection from {client_address} - Sent: {time_str}")
    
    client_socket.send(time_str.encode())
    client_socket.close()
