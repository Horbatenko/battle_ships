from socket import socket, AF_INET, SOCK_STREAM

class Connection:

    def __init__(self, host, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.host = host
        self.port = port

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
        except ConnectionRefusedError as e:
            print('Server error: {}'.format(e.strerror))
            exit(1)

    def sendData(self, data, isBytes=True):
        if not isBytes:
            data = self.codeDataToBytes(data)
        self.socket.sendall(data)

    def codeDataToBytes(self, data, coding='UTF-8'):
        return bytes(str(data).encode(coding))

    def receiveData(self):
        try:
            data = self.socket.recv(1024)
        except Exception as e:
            self.disconnect()
            return None
        else:
            return data

    def disconnect(self):
        self.socket.close()