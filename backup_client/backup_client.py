import sys
import os
import socket


def client_service():
    client_host = '0.0.0.0'  # Symbolic name meaning all available interfaces
    client_port = 2380  # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((client_host, client_port))
    s.listen(50)
    while True:
        try:
            conn, addr = s.accept()
            print('Connected by', addr)
            data = conn.recv(1024)
            print("BACKUP STATUS: " + data.decode())
            conn.sendall(b'Done')
            file = open("service.log","w")
            file.write(data.decode())
            file.close()
            conn.close()
        except socket.timeout:
            continue


if __name__ == '__main__':
    client_service()
