import sys
import socket
ip='127.0.0.1'
port=10086
s=socket.socket()
s.connect((ip,port))
while 1:
    cmd=input("command：").strip()
    s.send(cmd.encode())
    if cmd=='exit':
        break
    result=s.recv(8192).decode()
    print(result)
s.close()
