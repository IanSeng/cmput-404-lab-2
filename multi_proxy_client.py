
from multiprocessing import Pool

import socket

HOST = '127.0.0.1' 
PORT = 8001        
def connect(connect):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(connect)
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))

def main():
    address = [('127.0.0.1', 8001)]

    with Pool() as p:
        p.map(connect, address*10)
        
if __name__ == "__main__":
    main()