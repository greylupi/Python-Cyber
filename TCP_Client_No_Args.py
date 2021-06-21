import socket

host = "www.google.com"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host,port))

client.send(b"GET / HTTP/1.1\r\n\r\n")

response = client.recv(1024)

print(response.decode())

client.close()