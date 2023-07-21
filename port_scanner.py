#!/bin/python3

import socket
import sys
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Please provide argument.")
	print("Example: python3 portscanner.py [ip]")

print("*" * 50)
print("Scanning in progress...")
print("Time started: "+str(datetime.now()))
print("*" * 50)

try:
	for port in range(1,65000):	
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"port {port} is open")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not establish connection. Where's my internet?")
	sys.exit()

# test
#HOST = '127.0.0.1'
#PORT = 

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is a port
#s.connect((HOST,PORT))
