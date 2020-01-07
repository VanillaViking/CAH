
import socket

class cli_socket():
    def __init__(self, tcp_ip, tcp_port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((tcp_ip, tcp_port))
    
    def send(self, msg):
        self.s.sendall(msg.encode('utf-8'))

    def recv(self):
        return str(self.s.recv(1024))[2:-1]
    def close(self):
        self.s.close()
