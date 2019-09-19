# Echo server program
import socket

def save_to_file(client_name,file_name, contents):
    fh = open(client_name+file_name, 'a')
    fh.write(contents+ '\n')
    fh.close()
def convertTuple(tup):
    str =  ''.join(tup)
    return str
HOST = ''
PORT = 50025
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(100)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            save_to_file('client1','.xdb',data.decode("utf-8"))
            save_to_file('client1','.xdb',addr[0])

