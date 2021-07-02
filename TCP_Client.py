import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host,port))

client.send(b"Hello\r\n")

response = client.recv(1024)

print(response.decode())

client.close()

