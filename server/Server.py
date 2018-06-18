from socket import socket, AF_INET, SOCK_STREAM
from .Connection import Connection
import threading
import random


class Server:

    def __init__(self, host, port, connectionsLimit=2):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.host = host
        self.port = port
        self.connectionsLimit = connectionsLimit
        self.connections = []

    def run(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.alertMessage('Server started..')
        self.listenToConnections()

    def listenToConnections(self):
        startGameFlag = threading.Event()
        startGameFlag.clear()
        while True:
            clientSock, clientAddr = self.socket.accept()
            connection = Connection(clientSock, clientAddr)
            connection.onConnect()
            self.alertMessage('{} was connected'.format(clientAddr))
            thread = threading.Thread(target=self.clientThreadFunc, args=(connection, startGameFlag))
            thread.start()

            self.connections.append(connection)
            self.connectionsLimit -= 1

            if not self.connectionsLimit:
                startGameFlag.set()
                break

        self.choiseFirstPlayer()
        self.alertMessage('Game begin')

    def clientThreadFunc(self, connection, startGameFlag):

        connection.sendData('Wait for oponent', isBytes=False)

        startGameFlag.wait()

        while True:
            data = connection.receiveData()
            if data:
                self.alertMessage('{} - from: {}'.format(data, connection.clientAddr))
                for conn in self.connections:
                    if conn != connection:
                        conn.sendData(data)
            else:
                self.alertMessage('Disconnected by: {}'.format(connection.clientAddr))
                break

    def choiseFirstPlayer(self):
        first = random.choice(self.connections)
        first.sendData('turn', isBytes=False)
        for p in self.connections:
            if p != first:
                p.sendData('wait', isBytes=False)

    def alertMessage(self, data):
        print(str(data))