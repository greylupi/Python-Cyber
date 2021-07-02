import socket

IP = "127.0.0.1"
PORT = 1337

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP,PORT))
server.listen()

while True:
    print('[*] Listening for connections...')
    client, (ip,port) = server.accept()

    client.send(b'You have successfully connected to the TCP server\r\n')

    while True:
        data = client.recv(1024)
        print(f'[*] Received: {data.decode("utf-8")}')
        if len(data) == 0:
            client.close()
            break

server.close()
