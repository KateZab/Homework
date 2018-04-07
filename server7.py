import socket
import datetime, time
# import thread module
from _thread import *
import threading
from decimal import Decimal
 
print_lock = threading.Lock()
 
# thread fuction
def threaded(c):
    while True:
 
        data = c.recv(1024)
        if not data:
            print('Bye')
             
            
            break
 
        
        data = data_to_sent(data.decode("utf-8"))
 
        # send back reversed string to client
        c.send(data.encode())
 
    # connection closed
    c.close()
 
def data_to_sent(data):
    seq_num, resdate = data.split(",")
    now = datetime.datetime.now().timestamp()
    
    time_dff = now - float(resdate)
    return seq_num + "," + str(time_dff)
def Main():
    host = ""
 
   
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to post", port)
 
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
 
    # a forever loop until client wants to exit
    while True:
 
        
        c, addr = s.accept()
 
      
        print('Connected to :', addr[0], ':', addr[1])
 
        
        start_new_thread(threaded, (c,))
    s.close()
 
 
if __name__ == '__main__':
    Main()
