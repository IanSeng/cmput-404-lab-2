# !/usr/bin/env python3
import socket, sys, time

def create_tcp_socket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        sys.exit()

    return s


def get_remote_ip(host):
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        sys.exit()
    return remote_ip
        

def send_data(serversocket, payload):
    try: 
        serversocket.sendall(payload.encode())
    except socket.error:
        sys,exit()

def main():
    try: 
        # properties: address, payload and buffersize
        host = "www.google.com"
        port = 80 
        payload = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" %host
        buffer_size = 4096

        # create socket, get the ip, and connect 
        s = create_tcp_socket()

        remote_ip = get_remote_ip(host)

        s.connect((remote_ip, port))
        print(f'Socket Connected to {host} on io {remote_ip}')

        # send data and shutdown 
        send_data(s, payload)
        s.shutdown(socket.SHUT_WR)
        
        # continue accepting data until no more left (byte string)
        full_data = b"" 
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
        # print(full_data)
    except Exception as e: 

        print(e)
    finally:
        # always close at the end 
        s.close()

    # Establish scoket server 
    SERVER_HOST = ""
    SERVER_PORT = 8001
    BUFFER_SIZE = 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        #bind socket to address
        s.bind((SERVER_HOST, SERVER_PORT))
        #set to listening mode
        s.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = s.accept()
            print("Connected by", addr)
            
            #recieve data, wait a bit, then send it back
            full_data = conn.recv(BUFFER_SIZE)
            print(full_data)
            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

    

if __name__ == "__main__":
    main()