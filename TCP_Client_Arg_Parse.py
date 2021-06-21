import socket
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host", help="enter a domain or IP address")
parser.add_argument("port", help="enter a port number")
args = parser.parse_args()


host = sys.argv[1]
port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host,port))

client.send(b"GET / HTTP/1.1\r\n\r\n")

response = client.recv(1024)

print(response.decode())

client.close()
