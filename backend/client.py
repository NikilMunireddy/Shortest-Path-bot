
import socket

TCP_IP = '0.0.0.0'
TCP_PORT = 5008
BUFFER_SIZE = 1024
MESSAGE = "ok"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    se=input('Enter response')
    s.send(se.encode())
    data = s.recv(BUFFER_SIZE).decode()
    print(data)
    if not data or data=='quit':
        s.close()
        break
        
s.close()
