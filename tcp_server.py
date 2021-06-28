import socket

IP - "0.0.0.0"
PORT = 1337

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP,PORT))
server.listen()
server.recv(1024)
server.send(b'Message received')
server.close()
