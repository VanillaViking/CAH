
import socket

class cli_socket():
    def __init__(self, tcp_ip, tcp_port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((tcp_ip, tcp_port))
        self.messages = []
    
    def send(self, msg):
        while True:
            self.s.sendall(msg.encode('utf-8'))
            if str(self.s.recv(1))[2:-1] == "0":
                return 0

    def recv(self, buf=1024):
        while True:
        data = str(self.s.recv(buf))[2:-1]
        if data[-1] == "|":
            self.send("0")
            self.messages = data.split("|")
            break
        else:
            self.send("1")


    def close(self):
        self.s.close()
