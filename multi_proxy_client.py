#!/usr/bin/env python3
from multiprocessing import Pool
import socket

def create_tcp_socket():
    print("creating socket")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Fail to create socket. Error code: {str(msg[0])}, Error message: {msg[1]}')
        sys.exit()

    print('Socket created successfully')
    return s

def connect(connect):
    try: 
        # properties: address, payload and buffersize
        HOST = '127.0.0.1'
        PORT = 8001
        BUFFER_SIZE = 4096

        # create socket, get the ip, and connect 
        s = create_tcp_socket()

        s.connect((HOST, PORT))
        print(f'Socket Connected to {HOST} on io {PORT}')

        s.shutdown(socket.SHUT_WR)

        # continue accepting data until no more left (byte string)
        full_data = b"" 
        while True:

            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data
        print(full_data)
    except Exception as e: 
        print(e)
    finally:
        # always close at the end 
        s.close()

def main():
    address = [('127.0.0.1', 8001)]

    with Pool() as p:
        p.map(connect, address*10)
    

if __name__ == "__main__":
    main()