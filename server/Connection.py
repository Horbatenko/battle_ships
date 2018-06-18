
class Connection:

    def __init__(self, clientSock, clientAddr):
        self.clientSock = clientSock
        self.clientAddr = clientAddr

    def onConnect(self):
        self.clientSock.sendall(self.codeDataToBytes('You was connected to game server'))

    def sendData(self, data, isBytes=True):
        if not isBytes:
            data = self.codeDataToBytes(data)
        self.clientSock.sendall(data)

    def codeDataToBytes(self, data, coding='UTF-8'):
        return bytes(str(data).encode(coding))

    def receiveData(self):
        try:
            data = self.clientSock.recv(1024)
        except Exception as e:
            self.disconnect()
            return None
        else:
            return data



    def disconnect(self):
        self.clientSock.close()