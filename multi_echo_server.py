#!/usr/bin/env python3
import socket 
import time
from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def helper_echo(add, conn):
    full_data = conn.recv(BUFFER_SIZE)
    time.sleep(0.5)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_WR)
    conn.close()
    
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2)

        while True:
            conn, addr = s.accept()
            p = Process(target=helper_echo, args=(addr, conn))
            p.daemon = True
            p.start()
            print("Started proess ", p)
    

if __name__ == "__main__":
    main()
