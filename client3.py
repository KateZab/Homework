# Echo client program
import socket
import sys
import datetime, time

HOST = ''    # The remote host
PORT = 8080              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_INET, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except:
        s = None
        continue
    try:
        s.connect(sa)
    except:
        s.close()
        s = None
        continue
    break
if s is None:
    print ('could not open socket')
    sys.exit(1)
count = 0
while(count < 100000):

    now = datetime.datetime.now().timestamp()
    strint = str(count) + "," + str(now)
    s.send(strint.encode())
    data = s.recv(1024)
    
    print ('Received', data.decode("utf-8"))
    count = count +1
    
s.close()

