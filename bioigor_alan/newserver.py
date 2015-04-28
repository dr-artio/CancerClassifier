

import socket
from tar import *


TIMEOUT = 2
HOST = '0.0.0.0'              
PORT = 8080             

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)


i = 0

while 1:
    conn, addr = s.accept()
    conn.settimeout(TIMEOUT)
    filename = "biofiles/file_%s.tar" % i
    f = open(filename, "wb")
    i += 1
    while 1:
        try:
            data = conn.recv(1024)
            f.write(data)
        except socket.timeout:
            f.close()
            break

        if not data:
            print 'Connection lost. Listening for a new controller.' 
            break
    outcome = process(filename)
    conn.send(outcome)

conn.close()
