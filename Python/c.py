# Echo client program
import socket
import os
import psutil
HOST = '127.0.0.1'    # The remote host
PORT = 50025              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(psutil.cpu_count())
    qq = str(psutil.cpu_count())
    men = str(psutil.virtual_memory())
    s.sendall(b'The CPU core that your server have is:'+qq.encode("utf-8")+men.encode("utf-8"))
    #s.sendall(qq.encode("utf-8"))
    data = s.recv(1024)
